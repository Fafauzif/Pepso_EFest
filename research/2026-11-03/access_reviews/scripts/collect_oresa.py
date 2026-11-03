#!/usr/bin/env python3
"""Public ORESA campaign reviews, marked incentivized; no consumer prevalence inference."""
import concurrent.futures,csv,datetime,hashlib,json,urllib.request
from pathlib import Path
B=Path(__file__).resolve().parents[1]
def fetch(page):
 u=f'https://oresa.id/produk-ulasan/detail-data/1053?page={page}&rating=&order=&per_page=100'
 now=datetime.datetime.now(datetime.timezone.utc).isoformat();p=B/'raw'/f'oresa_ultrawhite_p{page}.json'
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'}),timeout=18) as r:b=r.read()
  p.write_bytes(b);d=json.loads(b)
  log={'url':u,'status':'success','page':page,'retrieved_at_utc':now,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'raw_file':str(p.relative_to(B)),'rows':len(d['data']),'total':d.get('total'),'last_page':d.get('last_page')}
  rows=[]
  for i,v in enumerate(d['data']):
   rows.append({'record_id':'ORESA-'+str(v['product_review_id']),'source_id':'ORESA-1053-p'+str(page),'source_url':u,'campaign_url':'https://oresa.id/produk-sampel/206/1053/pepsodent-ultra-white','product_name':'Pepsodent Ultra White','review_text':v.get('review_description_more') or v.get('review_description'),'review_title':v.get('review_title'),'rating':v.get('rating'),'published_raw':v.get('created_at'),'sampling_method':v.get('sampling_method'),'incentive_status':'campaign_cashback_and_review_tasks_explicit','is_transaction_displayed':v.get('is_transaction'),'age_verified':False,'premium_to_basic_verified':False,'retrieved_at_utc':now,'raw_file':str(p.relative_to(B)),'raw_locator':'data['+str(i)+']','selection_caveat':'incentivized campaign; campaign/compliance language; not organic sentiment or repeat evidence'})
  return log,rows
 except Exception as e:return {'url':u,'page':page,'status':'failed','error':str(e)},[]
logs=[];rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for l,r in pool.map(fetch,[1,2,3]):logs.append(l);rows.extend(r)
dedup={r['record_id']:r for r in rows};out=list(dedup.values())
(B/'clean'/'oresa_incentivized_reviews.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
if out:
 with (B/'clean'/'oresa_incentivized_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
(B/'oresa_collection_log.json').write_text(json.dumps(logs,indent=2))
print({'retrieved':len(rows),'unique':len(out),'logs':logs})
