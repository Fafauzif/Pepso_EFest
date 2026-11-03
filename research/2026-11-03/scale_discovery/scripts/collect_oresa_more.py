from pathlib import Path
import urllib.request,json,hashlib,datetime,concurrent.futures,csv,time
B=Path(__file__).resolve().parents[1]
campaigns=[('1017','Pepsodent Gum Expert','https://oresa.id/produk-sampel/166/1017/pepsodent-gum-expert'),('998','Pepsodent Siwak & Habbatussauda','https://www.oresa.id/produk-sampel/147/998/pepsodent-siwak-habbatussauda'),('1061','Pepsodent Pro.Care','https://oresa.id/produk-ulasan/214/1061/pepsodent-procare')]
def fetch(x):
 pid,name,curl,page=x;u=f'https://oresa.id/produk-ulasan/detail-data/{pid}?page={page}&rating=&order=&per_page=100';p=B/'raw'/f'oresa_{pid}_p{page}.json';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','X-Requested-With':'XMLHttpRequest'}),timeout=20) as f:b=f.read()
  p.write_bytes(b);d=json.loads(b);log={'source_id':f'ORESA-{pid}-p{page}','url':u,'status':'success','retrieved_at_utc':now,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'raw_file':str(p.relative_to(B)),'rows':len(d['data']),'total':d.get('total'),'last_page':d.get('last_page')}; rows=[]
  for i,v in enumerate(d['data']):
   rows.append({'record_id':'ORESA-'+str(v['product_review_id']),'corpus':'oresa_incentivized_reviews','source_id':log['source_id'],'source_url':u,'campaign_url':curl,'product_name':name,'review_text':v.get('review_description_more') or v.get('review_description'),'review_title':v.get('review_title'),'rating':v.get('rating'),'published_raw':v.get('created_at'),'sampling_method':v.get('sampling_method'),'incentive_status':'sampling_campaign_context_terms_check','is_transaction_displayed':v.get('is_transaction'),'age_verified':False,'premium_to_basic_verified':False,'retrieved_at_utc':now,'raw_file':str(p.relative_to(B)),'raw_locator':f'data[{i}]','selection_caveat':'Campaign/sampling review, not organic sentiment or repeat evidence; no inferred age/payer/behavior'})
  return log,rows
 except Exception as e:return {'source_id':f'ORESA-{pid}-p{page}','url':u,'status':'failed','error':str(e),'retrieved_at_utc':now},[]
logs=[];rows=[];rest=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for c,(log,part) in zip(campaigns,ex.map(fetch,[(*c,1) for c in campaigns])):
  logs.append(log);rows+=part
  for page in range(2,min(int(log.get('last_page') or 1),60)+1):rest.append((*c,page))
print('First pages',[(x['source_id'],x.get('total'),x.get('last_page')) for x in logs],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for log,part in ex.map(fetch,rest):logs.append(log);rows+=part
out=list({r['record_id']:r for r in rows}.values())
(B/'clean/oresa_new_reviews.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
if out:
 with (B/'clean/oresa_new_reviews.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
(B/'oresa_collection_log.json').write_text(json.dumps(logs,indent=2));print('Retrieved',len(rows),'Unique',len(out),'perproduct',[(c[1],sum(r['product_name']==c[1] for r in out)) for c in campaigns])
