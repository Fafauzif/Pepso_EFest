#!/usr/bin/env python3
"""Resumable public Watsons review-history collection discovered in public frontend.
No login, account sessions, paid API, actor or challenge bypass. Stop global HTTP429/403.
Raw response retained; clean table excludes reviewer aliases/media URLs.
"""
import urllib.request,urllib.parse,urllib.error,json,csv,re,hashlib,datetime,time,threading,argparse
from collections import Counter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
R=Path(__file__).resolve().parents[1];RESEARCH=R.parent
for d in ['raw/watsons','clean/by_product','logs']:(R/d).mkdir(parents=True,exist_ok=True)
STOP=threading.Event();LOCK=threading.Lock()
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def collect(t):
 product,args=t;code=product['product_code'].replace('BP_','');name=product['product_name'];rows=[];logs=[];seen=set();reason=''
 prior_path=R/'logs'/f'{code}.json';prior_logs=json.loads(prior_path.read_text()).get('sources',[]) if prior_path.exists() else [];prior_by_id={z['source_id']:z for z in prior_logs}
 for page in range(args.max_pages):
  if STOP.is_set():reason='global_stop_on_access_limit';break
  q=dict(fields='ASIA_CUSTOMER_REVIEW',currentPage=page,pageSize=args.page_size,sort='date:desc',needsTotal='true',lang='id',curr='IDR')
  u=f'https://api.watsons.co.id/api/v2/wtcid/products/{code}/paginatedReviews?'+urllib.parse.urlencode(q)
  f=R/'raw/watsons'/f'{code}_p{page}_s{args.page_size}.json';sid=f'WATREV-{code}-P{page}-S{args.page_size}';at=now();log=dict(source_id=sid,url=u,retrieved_at_utc=at,product_code=code,product_name=name,page_requested=page,page_size_requested=args.page_size)
  try:
   if f.exists():
    b=f.read_bytes();log['cache_reused']=True;log['cache_read_at_utc']=at
    if sid in prior_by_id:at=prior_by_id[sid]['retrieved_at_utc'];log['retrieved_at_utc']=at
   else:
    with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (public catalogue review research)'}),timeout=30) as resp:b=resp.read(10*1024*1024);log['status']=resp.status
    f.write_bytes(b);time.sleep(.45)
   d=json.loads(b);rr=d.get('reviews',[]);pg=d.get('pagination',{});log.update(outcome='success',raw_file=str(f.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),pagination=pg,rows=len(rr));logs.append(log)
   fresh=0
   for i,v in enumerate(rr):
    rid=str(v.get('id') or hashlib.sha256((code+str(v)).encode()).hexdigest());uniqueid='WATREV-'+rid
    if uniqueid in seen:continue
    seen.add(uniqueid);fresh+=1;date=v.get('date');iso=None
    if date:
     try:iso=datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S%z').astimezone(datetime.timezone.utc).isoformat()
     except ValueError:pass
    rows.append(dict(record_id=uniqueid,source_id=sid,platform='Watsons Indonesia',source_url=u,product_url=product['url'],product_code=code,product_name=name,brand=product['brand'],review_id=rid,review_text=v.get('comment'),rating=v.get('rating'),published_raw=date,published_at_utc=iso,within_case_period=bool(iso and '2022-01-01'<=iso[:10]<='2026-06-30'),retrieved_at_utc=at,raw_file=str(f.relative_to(R)),raw_locator=f'reviews[{i}]',approval_status=v.get('approvalStatus'),incentive_status='not_established',age_verified=False,premium_to_basic_verified=False,selection_caveat='Public approved retailer reviews, date-desc pagination; product/variant histories can overlap. No verified age, switching, usage or organic/unincentivized status.',country_evidence='Indonesian Watsons site; reviewer residence not verified'))
   if not rr:reason='no_more_reviews';break
   if fresh==0:reason='repeated_page_no_new_ids';break
   if not pg.get('hasNext',False):reason='reported_history_complete';break
  except urllib.error.HTTPError as e:
   log.update(outcome='http_error',status=e.code,error=str(e));logs.append(log)
   if e.code in [429,403]:STOP.set()
   reason='HTTP_'+str(e.code);break
  except Exception as e:log.update(outcome='failed',error=repr(e));logs.append(log);reason='error_no_blind_retry';break
 else:reason='max_page_cap'
 summary=dict(product_code=code,product_name=name,unique_review_ids=len(rows),stop_reason=reason,reported_total=next((l['pagination'].get('totalCount') for l in logs if l.get('pagination')),None),complete=(reason=='reported_history_complete'))
 (R/'clean/by_product'/f'{code}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(R/'logs'/f'{code}.json').write_text(json.dumps(dict(summary=summary,sources=logs),ensure_ascii=False,indent=2))
 with LOCK:print(json.dumps(summary,ensure_ascii=False),flush=True)
 return summary

def merge():
 allrows=[];logs=[];summaries=[]
 for p in sorted((R/'clean/by_product').glob('*.json')):allrows+=json.loads(p.read_text())
 for p in sorted((R/'logs').glob('*.json')):
  z=json.loads(p.read_text());logs+=z['sources'];summaries.append(z['summary'])
 unique={};contexts={};conflicts=[]
 for row in allrows:
  k=row['record_id'];ctx=dict(source_id=row['source_id'],product_code=row['product_code'],raw_file=row['raw_file'],raw_locator=row['raw_locator'])
  contexts.setdefault(k,[]).append(ctx)
  if k not in unique:unique[k]=row
  elif unique[k]['review_text']!=row['review_text'] or unique[k]['rating']!=row['rating']:conflicts.append(dict(record_id=k,first_source_id=unique[k]['source_id'],other_source_id=row['source_id']))
 rows=list(unique.values())
 for row in rows:
  row['capture_contexts']=contexts[row['record_id']];row['capture_context_count']=len(contexts[row['record_id']]);row['product_scope']='adjacent_whitening_serum' if re.search('serum',row['product_name'],re.I) else 'toothpaste';row['text_status']='written_review' if str(row.get('review_text') or '').strip() else 'rating_only_or_blank';row['time_scope_status']='unknown' if not row.get('published_at_utc') else ('within_case_period' if row['within_case_period'] else ('pre_case_period' if row['published_at_utc'][:10]<'2022-01-01' else 'post_case_period'));row['reviewer_residence_verified']=False;row['reviewer_language_verified']=False;row['syndication_status']='not_established';row['verified_buyer_status']='not_exposed_by_captured_endpoint'
 (R/'clean/reviews.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
 if rows:
  with (R/'clean/reviews.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows([{k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()} for row in rows])
 (R/'source_register.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2));(R/'product_coverage.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2));(R/'clean/duplicate_id_conflicts.json').write_text(json.dumps(conflicts,ensure_ascii=False,indent=2))
 summary=dict(product_contexts=len(summaries),reported_complete_product_histories=sum(x['complete'] for x in summaries),raw_review_observations=len(allrows),unique_review_ids=len(rows),nonempty_review_text=sum(bool(str(x.get('review_text') or '').strip()) for x in rows),within_case_period=sum(x['within_case_period'] for x in rows),duplicate_review_id_observations=len(allrows)-len(rows),conflicting_ids=len(conflicts),http429_or403=sum(x.get('status') in [429,403] for x in logs),source_pages=len(logs),successful_source_pages=sum(x['outcome']=='success' for x in logs),paid_spend_usd=0,apify_runs=0)
 summary.update(rating_counts=dict(Counter(str(x['rating']) for x in rows)),written_review_records=sum(x['text_status']=='written_review' for x in rows),rating_only_or_blank_records=sum(x['text_status']=='rating_only_or_blank' for x in rows),within_case_written_review_records=sum(x['within_case_period'] and x['text_status']=='written_review' for x in rows),time_scope_counts=dict(Counter(x['time_scope_status'] for x in rows)),product_scope_counts=dict(Counter(x['product_scope'] for x in rows)),incentive_counts=dict(Counter(x['incentive_status'] for x in rows)),verified_residence_count=0,verified_18_30_switcher_count=0,country_scope='Indonesian Watsons endpoint only; no reviewer residence/country or language field exposed',syndication_scope='No syndication/origin field exposed; no duplicate IDs across captured SKU histories; cross-platform authorship or syndication not established',all_records_manually_read=False)
 texts=Counter(re.sub(r'\s+',' ',str(x.get('review_text') or '')).strip().casefold() for x in rows if str(x.get('review_text') or '').strip());summary['exact_normalized_text_duplicate_groups']=sum(v>1 for v in texts.values());summary['written_review_records_in_duplicate_text_groups']=sum(v for v in texts.values() if v>1);summary['excess_exact_text_records']=sum(v-1 for v in texts.values() if v>1)
 (R/'quality_report.json').write_text(json.dumps(summary,indent=2));print('MERGED',json.dumps(summary),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--page-size',type=int,default=500);p.add_argument('--max-pages',type=int,default=25);p.add_argument('--workers',type=int,default=3);p.add_argument('--merge-only',action='store_true');a=p.parse_args()
 if not a.merge_only:
  products=json.loads((RESEARCH/'retail/retail_observations.json').read_text());products=[x for x in products if x['seller']=='Watsons Indonesia' and not x['named_children_product']]
  # Prioritize Pepsodent before cross-brand comparison; unique cataloguecodes only.
  products=sorted({x['product_code']:x for x in products}.values(),key=lambda x:(x['brand']!='Pepsodent',x['product_code']))
  with ThreadPoolExecutor(a.workers) as ex:
   for f in as_completed([ex.submit(collect,(x,a)) for x in products]):f.result()
 merge()
