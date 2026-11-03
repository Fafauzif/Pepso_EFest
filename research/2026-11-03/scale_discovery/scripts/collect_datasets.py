from pathlib import Path
import urllib.request,json,datetime,hashlib,csv,re,io,concurrent.futures
B=Path(__file__).resolve().parents[1];logs=[]
def get(url,path,limit=50_000_000):
 now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read(limit)
  (B/path).write_bytes(b);logs.append(dict(url=url,raw_file=path,status='success',retrieved_at_utc=now,bytes=len(b),sha256=hashlib.sha256(b).hexdigest()));return b
 except Exception as e:logs.append(dict(url=url,status='failed',error=str(e),retrieved_at_utc=now));return None
selected=[];inventory=[]
for did in ['74xrbd4vxy','574v66hf2v']:
 url=f'https://data.mendeley.com/public-api/datasets/{did}/files?folder_id=root&version=1'
 b=get(url,f'raw/mendeley_{did}_files.json')
 if not b:continue
 files=json.loads(b);print(did,[(x.get('filename'),x.get('size'),x.get('content_details',{})) for x in files],flush=True)
 for f in files:
  name=f.get('filename','')
  if not name.endswith('.csv') or name.startswith('Processed'):continue
  u=f.get('content_details',{}).get('download_url');fn='raw/'+did+'_'+re.sub(r'[^A-Za-z0-9_.-]+','_',name)
  if not u:continue
  data=get(u,fn)
  if not data:continue
  rows=list(csv.DictReader(io.StringIO(data.decode('utf-8-sig','replace')))); print(did,'downloaded',len(rows),'columns',list(rows[0]) if rows else [],flush=True)
  hits=[]
  for i,r in enumerate(rows,2):
   # Product-name first if present. Text-only matches remain unverified leads.
   pname=r.get('Product Name') or r.get('product_name') or r.get('productName') or ''
   blob=pname if pname else ' '.join(str(v) for v in r.values())
   if re.search(r'(?i)pepsodent|sensodyne|pasta\s*gigi|toothpaste|\bodol\b|\bclose\s*up\b|ciptadent|\bsystema\b|colgate|darlie|enzim|enzym|oral.?b|parodontax',blob):
    hit={'dataset_id':did,'dataset_url':f'https://data.mendeley.com/datasets/{did}/1','license':'CC BY 4.0 per primary landing page','raw_file':fn,'csv_line':i,'product_name_field':pname,'relevance_status':'product_name_match' if pname else 'text_match_requires_manual_relevance_review','original_record':r};hits.append(hit)
  inventory.append(dict(dataset_id=did,url=f'https://data.mendeley.com/datasets/{did}/1',downloaded_rows=len(rows),matched_rows=len(hits),columns=list(rows[0]) if rows else [],raw_file=fn,license='CC BY 4.0',original_filename=name))
  selected.extend(hits)
(B/'clean/dataset_toothpaste_candidates.json').write_text(json.dumps(selected,indent=2,ensure_ascii=False));(B/'dataset_inventory.json').write_text(json.dumps(inventory,indent=2));(B/'dataset_collection_log.json').write_text(json.dumps(logs,indent=2));print('inventory',inventory)
