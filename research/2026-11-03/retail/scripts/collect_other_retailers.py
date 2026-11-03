#!/usr/bin/env python3
import urllib.request,json,hashlib,re,html
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
slugs=['pasta-gigi-enzim-mild-124gram','pasta-gigi-enzim-mixdent-93-gram','pasta-gigi-enzim-40-plus','pasta-gigi-enzim-40-plus-63gram']
def go(slug):
 u='https://apotekhiro.com/products/'+slug+'.json';sid='HIRO-'+slug.upper();at=datetime.now(timezone.utc).isoformat();log=dict(source_id=sid,url=u,retrieved_at=at)
 try:
  r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25);b=r.read();f=ROOT/'raw'/f'{sid}.json';f.write_bytes(b);p=json.loads(b)['product'];log.update(status=r.status,raw_file=str(f.relative_to(ROOT)),sha256=hashlib.sha256(b).hexdigest(),outcome='parsed');rows=[]
  for i,v in enumerate(p['variants']):
   g=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:gram|gr|g)\b',p['title'],re.I)
   rows.append(dict(observation_id=f'{sid}-{i+1:03}',source_id=sid,url='https://apotekhiro.com/products/'+slug,catalogue_url=u,retrieved_at=at,evidence_level='live_public_product_JSON',record_locator=f'product.variants[{i}]',raw_file=str(f.relative_to(ROOT)),product_code=str(v['id']),ean=v.get('barcode'),brand='Enzim',product_name=p['title'],category_path='toothpaste_by_name',is_toothpaste=True,grams_single_named_unit=float(g.group(1).replace(',','.')) if g else None,content_size_raw=None,price_idr=float(v['price']),reference_price_idr=float(v['compare_at_price']) if v.get('compare_at_price') else None,original_price_idr=None,markdown_price_idr=None,promo_tag=None,promo_start_raw=None,promo_end_raw=None,promotion_title=None,catalogue_stock_flag=None,purchasable_flag=None,is_stock_loaded=None,seller='Apotek Hiro',country='Indonesia',location_verified=False,availability_status='catalogue_only_no_location_checkout',notes='Shopify product JSON. Product creation/update dates are catalogue metadata, not historical transaction dates or shelf checks.'))
  return log,rows
 except Exception as e:log.update(outcome='failed',error=repr(e));return log,[]
logs=[];rows=[]
for l,r in ThreadPoolExecutor(4).map(go,slugs):logs.append(l);rows+=r;print(l['source_id'],l['outcome'],len(r),flush=True)
# Parse already captured Hypermart page 1; no store chosen. Preserve old page prices with uncertainty.
f=ROOT/'raw/channelprobe-3.body';s=f.read_text();probe=json.loads((ROOT/'raw/channelprobe-log.json').read_text())[3];sid='HYPERMART-ORALCARE-P1';logs.append(dict(source_id=sid,url=probe['url'],retrieved_at=probe['retrieved_at'],raw_file=str(f.relative_to(ROOT)),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),outcome='parsed',notes='Catalogue HTML page1 only; no selected branch or proof prices recently updated.'))
pattern=r'<a href="(/hypermart/product/[^"]+)">\s*<h5>(.*?)</h5>\s*<p>(.*?)</p>'
for i,m in enumerate(re.finditer(pattern,s,re.S)):
 name=html.unescape(re.sub('<[^>]+>','',m[2])).strip();pt=html.unescape(re.sub('<[^>]+>',' ',m[3]));prices=re.findall(r'Rp\s*([\d.,]+)',pt);price=float(prices[-1].replace('.','').replace(',','.')) if prices else None
 if not re.search(r'pasta gigi|tooth paste|toothpaste',name,re.I) or re.search(r'tooth brush|sikat gigi',name,re.I):continue
 g=re.search(r'(\d+(?:[.,]\d+)?)\s*(?:gram|gr|g)\b',name,re.I)
 brand=next((x for x in ['PEPSODENT','SENSODYNE','ENZIM','COLGATE','CLOSE UP','CLOSEUP','CIPTADENT','FORMULA','DARLIE'] if x in name.upper()),None)
 rows.append(dict(observation_id=f'{sid}-{i+1:03}',source_id=sid,url='https://shop.hypermart.co.id'+m[1],catalogue_url=probe['url'],retrieved_at=probe['retrieved_at'],evidence_level='live_public_catalogue_HTML',record_locator=f'HTML product-card ordinal {i+1}',raw_file=str(f.relative_to(ROOT)),product_code=m[1].rsplit('-',1)[-1],ean=None,brand=brand,product_name=name,category_path='oralcare page1',is_toothpaste=True,grams_single_named_unit=float(g.group(1).replace(',','.')) if g else None,content_size_raw=None,price_idr=price,reference_price_idr=None,original_price_idr=None,markdown_price_idr=None,promo_tag=None,promo_start_raw=None,promo_end_raw=None,promotion_title=None,catalogue_stock_flag=None,purchasable_flag=None,is_stock_loaded=None,seller='Hypermart online catalogue',country='Indonesia',location_verified=False,availability_status='catalogue_only_no_location_checkout',notes='Captured live public catalogue; underlying price-update date unknown. No branch or stock/checkout verification. Page1 of13 oralcare pages; collection incomplete.'))
(ROOT/'other_retailers_observations.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(ROOT/'other_retailers_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2));print('TOTAL',len(rows))
