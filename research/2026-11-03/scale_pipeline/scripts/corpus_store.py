#!/usr/bin/env python3
"""Streaming, append-only provenance store for collected public research records.
No network or actor execution. Python standard library only.
"""
import argparse,csv,datetime,hashlib,json,sqlite3,sys,pathlib,re,gzip
BASE=pathlib.Path(__file__).resolve().parents[1]
SCHEMA='''
PRAGMA journal_mode=DELETE;
PRAGMA synchronous=FULL;
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS sources(source_version_id TEXT PRIMARY KEY,path TEXT NOT NULL,sha256 TEXT NOT NULL,bytes INTEGER NOT NULL,ingested_at TEXT NOT NULL,completed INTEGER NOT NULL DEFAULT 0,rows_read INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS records(record_key TEXT PRIMARY KEY,platform TEXT NOT NULL,source_record_id TEXT,record_type TEXT NOT NULL,source_url TEXT,text_original TEXT,title_original TEXT,content_date TEXT,date_raw TEXT,collected_at TEXT,incentive_status TEXT NOT NULL,scope TEXT NOT NULL,relevance_status TEXT NOT NULL,product_name TEXT,product_scope TEXT,relevance_basis TEXT,parent_post_id TEXT,self_reported_age TEXT,age_verified INTEGER NOT NULL DEFAULT 0,premium_to_basic_verified INTEGER NOT NULL DEFAULT 0,text_fingerprint TEXT,identity_basis TEXT NOT NULL,first_source_version_id TEXT NOT NULL REFERENCES sources(source_version_id),first_locator INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS observations(observation_id TEXT PRIMARY KEY,record_key TEXT NOT NULL REFERENCES records(record_key),source_version_id TEXT NOT NULL REFERENCES sources(source_version_id),locator INTEGER NOT NULL,payload_sha256 TEXT NOT NULL,payload_json TEXT NOT NULL,conflicts_with_first INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS obs_record ON observations(record_key);
CREATE INDEX IF NOT EXISTS rec_text_hash ON records(text_fingerprint);
CREATE TABLE IF NOT EXISTS exclusions(source_version_id TEXT,locator INTEGER,reason TEXT NOT NULL,payload_json TEXT NOT NULL,PRIMARY KEY(source_version_id,locator));
CREATE TABLE IF NOT EXISTS ingestion_errors(source_version_id TEXT,locator INTEGER,error TEXT NOT NULL);
'''
FIELDS=['record_key','platform','source_record_id','record_type','source_url','text_original','title_original','content_date','date_raw','collected_at','incentive_status','scope','relevance_status','product_name','product_scope','relevance_basis','parent_post_id','self_reported_age','age_verified','premium_to_basic_verified','text_fingerprint','identity_basis','first_source_version_id','first_locator']
class ExpectedExclusion(Exception):pass
def sha(x):return hashlib.sha256(x).hexdigest()
def utcnow():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def pick(r,*names):
 for n in names:
  v=r.get(n)
  if v is not None and v!='':return v
 return None
def string(v):
 if v is None:return None
 return v if isinstance(v,str) else json.dumps(v,ensure_ascii=False,sort_keys=True)
def explicit_true(v):
 return int(v is True or (isinstance(v,str) and v.casefold()=='true'))
def normalize(r,path):
 rid=pick(r,'canonical_identity','canonical_identity_hash','record_id','review_id','reviewId','comment_id','commentId','id')
 platform=string(pick(r,'platform','source_platform'))
 if not platform:
  ident=str(rid or '').upper();url=str(pick(r,'source_url','review_url','url') or '').lower();p=path.lower()
  platform='tryandreview' if ident.startswith('TAR-') or 'tryandreview' in p or 'tryandreview' in url else 'oresa' if 'oresa' in p or 'oresa' in url or ident.startswith('ORESA') else 'reddit' if 'reddit' in p or 'reddit' in url else 'lazada' if 'lazada' in p or 'lazada' in url else 'unknown'
 platform_raw=platform
 platform_key=platform.casefold().replace(' ','')
 platform='tryandreview' if 'tryandreview' in platform_key else 'oresa' if 'oresa' in platform_key else 'watsons' if 'watsons' in platform_key else 'lazada' if 'lazada' in platform_key else 'reddit' if 'reddit' in platform_key else 'amazon_external_context' if 'amazon' in platform_key else platform.casefold()
 if platform=='amazon_external_context' and rid is not None:
  match=re.fullmatch(r'AMZ-(?:HPC|HH)-([0-9a-f]{24})',str(rid))
  if match:rid='AMZ-'+match.group(1)  # Collector confirmed same exact user/product/time/text hash across categories.
 text=string(pick(r,'text_original','review_text','text','content','comment','body'))
 url=string(pick(r,'source_url','review_url','url','permalink'))
 date=string(pick(r,'created_at','published_date','content_date','review_date','date_iso','published_at','published_at_utc'))
 rawdate=string(pick(r,'published_raw','date_raw','date','created_utc','usage_date_raw'))
 collected=string(pick(r,'retrieved_at_utc','collected_at','retrieved_at','collection_timestamp'))
 scope=string(pick(r,'scope','time_scope'))
 scope={'case_window_2022_H1_2026':'case_historical','after_case_H1_2026':'current_context'}.get(scope,scope)
 # Only parse actual ISO content dates. Relative strings never become inferred dates.
 if not scope and date:
  try:
   dt=datetime.datetime.fromisoformat(date.replace('Z','+00:00')).date()
   scope='case_historical' if datetime.date(2022,1,1)<=dt<=datetime.date(2026,6,30) else 'current_context' if dt>datetime.date(2026,6,30) else 'outside_case'
  except ValueError:pass
 scope=scope or 'unknown_date'
 rt=string(pick(r,'record_type')) or ('review' if platform in ('lazada','oresa','tryandreview','watsons','amazon_external_context') else 'comment' if platform=='reddit' else 'unknown')
 identity_basis='supplied_record_id' if rid is not None else 'source_url_text_date_hash'
 key=platform+':'+str(rid) if rid is not None else platform+':sha256:'+sha(json.dumps([url,text,date,rawdate,rt],ensure_ascii=False,separators=(',',':')).encode())
 # Exact normalized text hash flags possible copied text; it never merges records.
 fp=sha(re.sub(r'\s+',' ',text).strip().casefold().encode()) if text and text.strip() else None
 return dict(zip(FIELDS,[key,platform,string(rid),rt,url,text,string(pick(r,'title_original','review_title','title')),date,rawdate,collected,string(pick(r,'incentive_status')) or 'unknown',scope,string(pick(r,'relevance_status')) or ('title_matched_candidate_not_individually_verified' if platform=='amazon_external_context' else 'source_selected_not_individually_verified'),string(pick(r,'product_name','product_title')),string(pick(r,'product_scope')),string(pick(r,'relevance_basis')),string(pick(r,'parent_post_id','post_id')),string(pick(r,'self_reported_age')),explicit_true(r.get('age_verified')),explicit_true(r.get('premium_to_basic_verified')),fp,identity_basis,None,None]))
def iter_rows(path):
 suffix=path.suffix.lower()
 compressed_jsonl=path.name.lower().endswith(('.jsonl.gz','.ndjson.gz'))
 if suffix in ('.jsonl','.ndjson') or compressed_jsonl:
  opener=gzip.open if compressed_jsonl else open
  with opener(path,'rt',encoding='utf-8-sig') as f:
   for n,line in enumerate(f,1):
    if line.strip():yield n,json.loads(line)
 elif suffix=='.csv':
  with path.open(encoding='utf-8-sig',newline='') as f:
   for n,row in enumerate(csv.DictReader(f),1):yield n,row
 elif suffix=='.json':
  # Array JSON is necessarily memory-loaded; convert very large files to JSONL upstream.
  value=json.loads(path.read_text(encoding='utf-8-sig'))
  if isinstance(value,dict):
   for k in ('records','reviews','comments','data','results','items'):
    if isinstance(value.get(k),list):value=value[k];break
  if not isinstance(value,list):raise ValueError('Expected JSON array or known list wrapper; logs/metadata must not be ingested as consumer records')
  for n,row in enumerate(value,1):yield n,row
 else:raise ValueError('Supported inputs: CSV, JSON array, JSONL/NDJSON, JSONL.GZ')
def dbopen(path):
 path.parent.mkdir(parents=True,exist_ok=True);db=sqlite3.connect(path);db.executescript(SCHEMA);return db
def ingest(db,paths,max_records,commit_every):
 outcome=[];used=0
 for p in paths:
  p=p.resolve();bhash=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(1024*1024),b''):bhash.update(b)
  h=bhash.hexdigest();sid=sha((str(p)+'\0'+h).encode());before=db.execute('SELECT completed,rows_read FROM sources WHERE source_version_id=?',(sid,)).fetchone()
  if before and before[0]:outcome.append({'path':str(p),'status':'already_complete','rows_read':before[1]});continue
  checkpoint=before[1] if before else 0
  db.execute('INSERT OR IGNORE INTO sources(source_version_id,path,sha256,bytes,ingested_at)VALUES(?,?,?,?,?)',(sid,str(p),h,p.stat().st_size,utcnow()));db.commit()
  n=checkpoint;read=0;errors=0;excluded=0;complete=True
  for loc,row in iter_rows(p):
   if loc<=checkpoint:continue
   if used>=max_records:complete=False;break
   try:
    if not isinstance(row,dict):raise ValueError('Row is not an object')
    norm=normalize(row,str(p));
    if not norm['text_original'] or not norm['text_original'].strip():raise ExpectedExclusion('missing_or_empty_text')
    if norm['text_original'].strip() in ('[deleted]','[removed]'):raise ExpectedExclusion('removed_or_deleted_marker')
    payload=json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':'));ph=sha(payload.encode());oid=sha((sid+':'+str(loc)).encode());key=norm['record_key']
    first=db.execute('SELECT payload_sha256 FROM observations WHERE record_key=? ORDER BY rowid LIMIT 1',(key,)).fetchone();conflict=int(bool(first and first[0]!=ph))
    norm['first_source_version_id']=sid;norm['first_locator']=loc
    db.execute('INSERT OR IGNORE INTO records('+','.join(FIELDS)+')VALUES('+','.join('?'for _ in FIELDS)+')',[norm[k]for k in FIELDS])
    db.execute('INSERT OR IGNORE INTO observations VALUES(?,?,?,?,?,?,?)',(oid,key,sid,loc,ph,payload,conflict));read+=1
   except ExpectedExclusion as e:
    db.execute('INSERT OR IGNORE INTO exclusions VALUES(?,?,?,?)',(sid,loc,str(e),json.dumps(row,ensure_ascii=False,sort_keys=True)));excluded+=1
   except (ValueError,TypeError) as e:
    db.execute('INSERT INTO ingestion_errors VALUES(?,?,?)',(sid,loc,str(e)));errors+=1
   n=loc;used+=1
   if (read+errors+excluded)%commit_every==0:db.execute('UPDATE sources SET rows_read=? WHERE source_version_id=?',(n,sid));db.commit()
  db.execute('UPDATE sources SET rows_read=?,completed=? WHERE source_version_id=?',(n,int(complete),sid));db.commit();outcome.append({'path':str(p),'status':'complete' if complete else 'checkpointed_at_cap','new_observations':read,'excluded_nontext_rows':excluded,'error_rows':errors,'last_locator':n})
  if used>=max_records:break
 return outcome
def stats(db,dbpath):
 count=lambda sql:db.execute(sql).fetchone()[0]
 n=count('SELECT COUNT(*) FROM records');obs=count('SELECT COUNT(*) FROM observations')
 rawbytes=count('SELECT COALESCE(SUM(length(CAST(payload_json AS BLOB))),0) FROM observations');textbytes=count('SELECT COALESCE(SUM(length(CAST(text_original AS BLOB))),0) FROM records')
 db.commit()
 totalbytes=sum(p.stat().st_size for p in [dbpath,pathlib.Path(str(dbpath)+'-wal')]if p.exists())
 groups={}
 for col in ['platform','scope','incentive_status','record_type','relevance_status','product_scope']:groups[col]=dict(db.execute(f'SELECT {col},COUNT(*) FROM records GROUP BY {col}'))
 # Validation denominators are operational counts; no prevalence in the consumer population.
 return {'unique_platform_records':n,'source_observations':obs,'repeated_identity_observations':obs-n,'observations_with_payload_difference':count('SELECT COUNT(*) FROM observations WHERE conflicts_with_first=1'),'possible_copied_text_groups':count('SELECT COUNT(*) FROM(SELECT text_fingerprint FROM records WHERE text_fingerprint IS NOT NULL GROUP BY text_fingerprint HAVING COUNT(*)>1)'),'source_versions':count('SELECT COUNT(*) FROM sources'),'excluded_missing_text_rows':count("SELECT COUNT(*) FROM exclusions WHERE reason='missing_or_empty_text'"),'excluded_removed_text_rows':count("SELECT COUNT(*) FROM exclusions WHERE reason='removed_or_deleted_marker'"),'ingestion_errors':count('SELECT COUNT(*) FROM ingestion_errors'),'raw_payload_utf8_bytes':rawbytes,'text_utf8_bytes':textbytes,'sqlite_file_bytes_including_checkpointed_wal':totalbytes,'breakdowns':groups,'million_record_storage_projection':{'basis':'Linear extrapolation from this exact collected database; not a collection-rate or available-record estimate','records':1000000,'sqlite_bytes':round(totalbytes/n*1000000) if n else None,'raw_payload_bytes':round(rawbytes/obs*1000000) if obs else None,'text_bytes':round(textbytes/n*1000000) if n else None,'excludes':'raw HTML/media, independent backups and export copies; SQLite/index mix may change at scale'},'throughput_or_completion_forecast':None}
def export(db,out):
 out.mkdir(parents=True,exist_ok=True);cur=db.execute('SELECT '+','.join(FIELDS)+' FROM records ORDER BY record_key');n=0
 with gzip.open(out/'records.jsonl.gz','wt',encoding='utf-8') as j,gzip.open(out/'records.csv.gz','wt',encoding='utf-8',newline='') as c:
  w=csv.DictWriter(c,fieldnames=FIELDS);w.writeheader()
  for vals in cur:
   r=dict(zip(FIELDS,vals));w.writerow(r);j.write(json.dumps(r,ensure_ascii=False)+'\n');n+=1
 with (out/'source_versions.json').open('w') as f:
  cur=db.execute('SELECT * FROM sources');names=[x[0]for x in cur.description];json.dump([dict(zip(names,x))for x in cur],f,indent=2)
 with gzip.open(out/'observations.jsonl.gz','wt',encoding='utf-8') as f:
  cur=db.execute('SELECT observation_id,record_key,source_version_id,locator,payload_sha256,payload_json,conflicts_with_first FROM observations ORDER BY source_version_id,locator')
  names=['observation_id','record_key','source_version_id','locator','payload_sha256','payload_json','payload_differs_from_first']
  for vals in cur:
   row=dict(zip(names,vals));row['payload']=json.loads(row.pop('payload_json'));f.write(json.dumps(row,ensure_ascii=False)+'\n')
 with gzip.open(out/'excluded_nontext_rows.jsonl.gz','wt',encoding='utf-8') as f:
  for sid,loc,reason,payload in db.execute('SELECT source_version_id,locator,reason,payload_json FROM exclusions ORDER BY source_version_id,locator'):
   f.write(json.dumps({'source_version_id':sid,'locator':loc,'reason':reason,'payload':json.loads(payload)},ensure_ascii=False)+'\n')
 with (out/'conflicting_observations.jsonl').open('w',encoding='utf-8') as f:
  cur=db.execute('SELECT record_key,source_version_id,locator,payload_sha256,payload_json FROM observations WHERE conflicts_with_first=1')
  for vals in cur:f.write(json.dumps(dict(zip(['record_key','source_version_id','locator','payload_sha256','payload_json'],vals)),ensure_ascii=False)+'\n')
 return n
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--db',type=pathlib.Path,default=BASE/'work/corpus.sqlite');sub=ap.add_subparsers(dest='command',required=True)
 ip=sub.add_parser('ingest');ip.add_argument('files',type=pathlib.Path,nargs='+');ip.add_argument('--max-records',type=int,default=100000);ip.add_argument('--commit-every',type=int,default=1000)
 ep=sub.add_parser('export');ep.add_argument('--out',type=pathlib.Path,default=BASE/'clean/export')
 sub.add_parser('stats');args=ap.parse_args();db=dbopen(args.db)
 if args.command=='ingest':
  if args.max_records<1 or args.commit_every<1:ap.error('Caps must be positive')
  print(json.dumps(ingest(db,args.files,args.max_records,args.commit_every),indent=2))
 if args.command=='export':print(json.dumps({'exported':export(db,args.out),'out':str(args.out)}))
 report=stats(db,args.db);(BASE/'clean/collection_stats.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));db.close()
if __name__=='__main__':main()
