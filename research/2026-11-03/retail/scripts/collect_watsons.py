#!/usr/bin/env python3
"""Public Watsons SSR catalogue capture, no authentication/paid service.
No branch/postcode chosen; catalogue stock is not checkout/shelf availability.
"""
import urllib.request,urllib.parse,json,re,time,csv,hashlib
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'raw'; RAW.mkdir(exist_ok=True)
BRANDS={'pepsodent':'Pepsodent','sensodyne':'SENSODYNE','closeup':'CLOSE-UP','colgate':'COLGATE','enzim':'ENZIM'}
def fetch(task):
 key,brand,page=task
 u=f'https://www.watsons.co.id/id/all-brands/list/{brand}/{key if key != "closeup" else "close-up"}?page={page}'
 if key=='enzim':u=f'https://www.watsons.co.id/id/search?text=enzim&page={page}'
 sid=f'WAT-{key.upper()}-P{page}'
 at=datetime.now(timezone.utc).isoformat()
 p=RAW/f'{sid}.html'
 log={'source_id':sid,'url':u,'retrieved_at':at,'file':str(p.relative_to(ROOT)),'request_method':'public_HTTP_GET','location_selected':False}
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (research catalogue audit)'}),timeout=35)
  b=r.read();p.write_bytes(b);s=b.decode('utf-8','replace');log.update(status=r.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),final_url=r.url)
  m=re.search(r'<script id="wtcid-state" type="application/json">(.*?)</script>',s,re.S)
  if not m:log['outcome']='no_state';return log,[]
  state=json.loads(m.group(1));res=state['cx-state']['product']['search']['results'];log['pagination']=res.get('pagination');log['outcome']='state_parsed'
  (RAW/f'{sid}.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
  rows=[]
  for i,x in enumerate(res.get('products',[])):
   name=x.get('name','');size=x.get('elabVariantProductContentSizeUnits',[])
   g=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:g\b|gr\b|gram\b)',name,re.I)
   if not g and size:g=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:g\b|gr\b|gram\b)',size[0],re.I)
   grams=float(g.group(1).replace(',','.')) if g else None
   cats=[z.get('name') for z in x.get('categoryNameLevels',[])]
   rows.append({'observation_id':f'{sid}-{i+1:03d}','source_id':sid,'url':'https://www.watsons.co.id/id'+x.get('url',''),'catalogue_url':u,'retrieved_at':at,'evidence_level':'live_public_SSR_JSON','record_locator':f'cx-state.product.search.results.products[{i}]','raw_file':str(p.relative_to(ROOT)),'state_file':f'raw/{sid}.json','product_code':x.get('code'),'ean':x.get('ean'),'brand':x.get('masterBrand',{}).get('name'),'product_name':name,'category_path':'/'.join(cats),'is_toothpaste':'Pasta Gigi' in cats,'grams_single_named_unit':grams,'content_size_raw':size,'price_idr':x.get('price',{}).get('value'),'reference_price_idr':x.get('strikeThroughPrice'),'original_price_idr':x.get('elabOldPrice',{}).get('value'),'markdown_price_idr':x.get('elabMarkDownPrice',{}).get('value'),'promo_tag':x.get('promotionFirstTag'),'promo_start_raw':x.get('promotionFirstTagStartDate'),'promo_end_raw':x.get('promotionFirstTagEndDate'),'promotion_title':x.get('topPromotion',{}).get('title'),'catalogue_stock_flag':x.get('stock',{}).get('stockLevelStatus'),'purchasable_flag':x.get('purchasable'),'is_stock_loaded':x.get('isStockLoaded'),'seller':'Watsons Indonesia','country':'Indonesia','location_verified':False,'availability_status':'catalogue_flag_only_no_location_checkout','notes':'No Jakarta branch or delivery postcode selected. SSR may expose different prices from indexed page. Price/stock flags are not verified transactional offers. Do not use named unit grams for multi-buy effective price without validating pack count.'})
  return log,rows
 except Exception as e:log.update(outcome='failed',error=type(e).__name__+': '+str(e));return log,[]
if __name__=='__main__':
 logs=[];allrows=[]
 tasks=[(k,b,p) for k,b in BRANDS.items() for p in range(2)]
 with ThreadPoolExecutor(max_workers=5) as ex:
  for f in as_completed([ex.submit(fetch,t) for t in tasks]):
   log,rows=f.result();logs.append(log);allrows+=rows;print(log['source_id'],log['outcome'],len(rows),flush=True)
 allrows.sort(key=lambda x:x['observation_id']);logs.sort(key=lambda x:x['source_id'])
 for name,data in [('watsons_products_all.json',allrows),('collection_log.json',logs),('source_register.json',logs)]: (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 rows=[r for r in allrows if r['is_toothpaste']]
 (ROOT/'retail_observations.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
 if rows:
  with (ROOT/'retail_observations.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows([{k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows])
 print('ALL',len(allrows),'TOOTHPASTE',len(rows),'UNIQUE_TOOTHPASTE_CODES',len({r['product_code'] for r in rows}))
