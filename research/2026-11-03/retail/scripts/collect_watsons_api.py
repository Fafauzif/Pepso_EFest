#!/usr/bin/env python3
"""Fetch public Watsons catalogue search endpoint after successful pilot.
The endpoint exposes catalogue information; no store/checkout selected.
"""
import urllib.request,urllib.parse,json,hashlib,csv,re
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
ROOT=Path(__file__).resolve().parents[1]
brands={'pepsodent':'Pepsodent','sensodyne':'SENSODYNE','closeup':'CLOSE-UP','colgate':'COLGATE','enzim':'ENZIM'}
def get(t):
 key,brand=t;sid='WATAPI-'+key.upper();q=':bestSeller:productBrandCode:'+brand
 if key=='enzim':q='enzim:bestSeller'
 u='https://api.watsons.co.id/api/v2/wtcid/products/search?'+urllib.parse.urlencode(dict(query=q,pageSize=100,currentPage=0,lang='id',curr='IDR',fields='FULL'))
 at=datetime.now(timezone.utc).isoformat();log={'source_id':sid,'url':u,'retrieved_at':at,'evidence_level':'live_public_catalogue_API','location_selected':False}
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (public catalogue research)'}),timeout=30);b=r.read();raw=ROOT/'raw'/f'{sid}.json';raw.write_bytes(b);x=json.loads(b);log.update(status=r.status,raw_file=str(raw.relative_to(ROOT)),sha256=hashlib.sha256(b).hexdigest(),pagination=x.get('pagination'),outcome='parsed')
  rows=[]
  for i,p in enumerate(x.get('products',[])):
   name=p.get('name','');cats='/'.join(c.get('name','') for c in p.get('categoryNameLevels',[]));is_toothpaste=('Pasta Gigi' in cats or bool(re.search('toothpaste|pasta gigi',name,re.I))) and not bool(re.search('sikat gigi|toothbrush|sikat lidah|serum',name,re.I))
   g=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:g\b|gr\b|gram\b)',name,re.I);grams=float(g.group(1).replace(',','.')) if g else None
   rows.append(dict(observation_id=f'{sid}-{i+1:03}',source_id=sid,url='https://www.watsons.co.id/id'+p.get('url',''),catalogue_url=u,retrieved_at=at,evidence_level='live_public_catalogue_API',record_locator=f'products[{i}]',raw_file=str(raw.relative_to(ROOT)),product_code=p.get('code'),ean=p.get('ean'),brand=p.get('masterBrand',{}).get('name'),product_name=name,category_path=cats,is_toothpaste=is_toothpaste,grams_single_named_unit=grams,content_size_raw=p.get('elabVariantProductContentSizeUnits'),price_idr=p.get('price',{}).get('value'),reference_price_idr=p.get('strikeThroughPrice'),original_price_idr=p.get('elabOldPrice',{}).get('value'),markdown_price_idr=p.get('elabMarkDownPrice',{}).get('value'),promo_tag=p.get('promotionFirstTag'),promo_start_raw=p.get('promotionFirstTagStartDate'),promo_end_raw=p.get('promotionFirstTagEndDate'),promotion_title=p.get('topPromotion',{}).get('title'),catalogue_stock_flag=p.get('stock',{}).get('stockLevelStatus'),purchasable_flag=p.get('purchasable'),is_stock_loaded=p.get('isStockLoaded'),seller='Watsons Indonesia',country='Indonesia',location_verified=False,availability_status='catalogue_flag_only_no_location_checkout',notes='Public catalogue API. No branch or delivery postcode selected; stock flags not confirmed transactional or shelf availability. Named-unit grams not necessarily total bundle grams.'))
  return log,rows
 except Exception as e:log.update(outcome='failed',error=repr(e));return log,[]
logs=[];rows=[]
for l,r in ThreadPoolExecutor(5).map(get,brands.items()):logs.append(l);rows+=r;print(l['source_id'],l['outcome'],len(r),flush=True)
(ROOT/'watsons_api_all_products.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(ROOT/'watsons_api_collection_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
tp=[r for r in rows if r['is_toothpaste']];(ROOT/'watsons_api_adjacent.json').write_text(json.dumps([r for r in rows if r['brand']=='COLGATE' and re.search('serum',r['product_name'],re.I)],ensure_ascii=False,indent=2));(ROOT/'watsons_api_toothpaste.json').write_text(json.dumps(tp,ensure_ascii=False,indent=2));print('All',len(rows),'Toothpaste',len(tp),'unique',len({r['product_code'] for r in tp}))
