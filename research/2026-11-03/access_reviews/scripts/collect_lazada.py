#!/usr/bin/env python3
"""Collect publicly rendered Lazada ID review SSR payloads. No login, paid actor or private API.
Discovery is purposive indexed search; result is not representative or complete review history.
"""
import concurrent.futures,csv,datetime,hashlib,json,re,time,urllib.request
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def parse(s):
 marker='window.__FIRST_SCREEN_DATA='
 d=json.JSONDecoder().raw_decode(s.split(marker,1)[1])[0]
 for v in d.get('data',{}).values():
  if isinstance(v,dict) and 'reviewPage' in v:return v['reviewPage']
 raise ValueError('No reviewPage')
def collect(item):
 u='https://www.lazada.co.id/product-reviews/?item_id='+item
 started=now(); p=BASE/'raw'/('lazada_'+item+'.html')
 try:
  if not p.exists():
   req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (compatible; research collection)'})
   with urllib.request.urlopen(req,timeout=18) as r:b=r.read(10*1024*1024)
   p.write_bytes(b)
  b=p.read_bytes();d=parse(b.decode('utf-8'));(BASE/'raw'/('lazada_'+item+'_payload.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
  prod=(d.get('products') or [{}])[0]
  if not any(w in str(prod.get('productName','')).lower() for w in ['pasta gigi','toothpaste','pepsodent','sensodyne','closeup','close up']):
   return {'source_id':'LZD-'+item,'url':u,'status':'excluded_irrelevant','product_name':prod.get('productName'),'raw_file':str(p.relative_to(BASE))},[],{}
  records=[]
  for i,v in enumerate((d.get('reviewZone') or {}).get('reviews',[])):
   ts=v.get('reviewTime');date=datetime.datetime.fromtimestamp(ts/1000,datetime.timezone.utc).isoformat() if ts else None
   records.append({'record_id':'LZD-'+str(v.get('reviewId') or item+'-'+str(i)), 'source_id':'LZD-'+item,'platform':'Lazada Indonesia','source_url':u,'product_id':item,'product_name':prod.get('productName'),'seller':prod.get('shop',{}).get('shopName'),'review_id':str(v.get('reviewId')),'review_text':v.get('reviewContent'),'rating':v.get('rating'),'displayed_badge':v.get('badge'),'published_at_utc':date,'within_case_period':bool(date and '2022-01-01'<=date[:10]<='2026-06-30'),'retrieved_at_utc':started,'raw_file':str(p.relative_to(BASE)),'raw_locator':'window.__FIRST_SCREEN_DATA.data.*.reviewPage.reviewZone.reviews['+str(i)+']','age_verified':False,'premium_to_basic_verified':False,'country_evidence':'lazada.co.id and hngLanguage ID site; reviewer residence not verified','selection_caveat':'SEO-page-selected reviews; no complete pagination; templated phrases may be present'})
  return {'source_id':'LZD-'+item,'url':u,'retrieved_at_utc':started,'status':'success','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'raw_file':str(p.relative_to(BASE)),'records':len(records),'displayed_rating_count':(d.get('reviewZone') or {}).get('ratingCnt'),'product_name':prod.get('productName')},records,prod
 except Exception as e:return {'source_id':'LZD-'+item,'url':u,'retrieved_at_utc':started,'status':'failed','error':type(e).__name__+': '+str(e)},[],{}
def main():
 ids={'8721394818'}
 for p in (BASE/'raw').glob('discovery_lazada*.json'):
  ids.update(re.findall(r'product-reviews/\?item_id=(\d+)',p.read_text()))
 seed=BASE/'raw'/'additional_lazada_ids.json'
 if seed.exists():ids.update(json.loads(seed.read_text()))
 rows=[];logs=[];products=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for log,rr,prod in pool.map(collect,sorted(ids)):
   logs.append(log);rows.extend(rr)
   if prod:products.append({'source_id':log['source_id'],'source_url':log['url'],**prod})
 dedup={r['record_id']:r for r in rows}
 (BASE/'clean'/'lazada_reviews.json').write_text(json.dumps(list(dedup.values()),ensure_ascii=False,indent=2))
 if dedup:
  with (BASE/'clean'/'lazada_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(next(iter(dedup.values())).keys()));w.writeheader();w.writerows(dedup.values())
 (BASE/'clean'/'lazada_products.json').write_text(json.dumps(products,ensure_ascii=False,indent=2))
 (BASE/'collection_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
 print(json.dumps({'attempted':len(ids),'successful':sum(l['status']=='success' for l in logs),'raw_records':len(rows),'unique_review_ids':len(dedup),'within_case_period':sum(r['within_case_period'] for r in dedup.values())}))
if __name__=='__main__':main()
