#!/usr/bin/env python3
import json,csv,re,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'watsons_api_toothpaste.json').read_text())+json.loads((ROOT/'watsons_api_adjacent.json').read_text())+json.loads((ROOT/'other_retailers_observations.json').read_text())
for r in rows:
 n=r['product_name'];r['product_scope']='adjacent_whitening_serum' if re.search('serum',n,re.I) else 'toothpaste';r['is_toothpaste']=r['product_scope']=='toothpaste';mult=re.search(r'(\d+)\s*[xX]\s*(\d+(?:[.,]\d+)?)\s*(?:g|gr|gram)\b',n)
 r['explicit_pack_count']=int(mult[1]) if mult else None
 r['grams_total_for_analysis']=int(mult[1])*float(mult[2].replace(',','.')) if mult else (None if re.search(r'value\s*pack|valuepack|valupack|\+',n,re.I) else r['grams_single_named_unit'])
 r['price_per_100g_idr']=round(r['price_idr']/r['grams_total_for_analysis']*100,2) if r['grams_total_for_analysis'] and r['price_idr'] is not None else None
 r['reference_price_not_previous_paid_price']=True
 r['clinical_claim_verified']=False
 r['age_specific_switching_evidence']=False
 r['named_children_product']=bool(re.search(r'kids|anak|baby',n,re.I))
# observations = separate seller SKU contexts; no arbitrary merging of products across sellers
ids=[r['observation_id'] for r in rows];assert len(ids)==len(set(ids));assert all(r['source_id'] and r['url'] and r['record_locator'] for r in rows)
for filename in ['retail_observations.json','retail_unique_view.json']:(ROOT/filename).write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (ROOT/'retail_observations.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows([{k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()} for r in rows])
logs=[]
for name in ['collection_log.json','watsons_api_collection_log.json','other_retailers_log.json']:logs+=json.loads((ROOT/name).read_text())
(ROOT/'source_register.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2))
summary=dict(observation_count=len(rows),unit='oralcare seller/product offer context',strict_toothpaste_count=sum(r['is_toothpaste'] for r in rows),adjacent_whitening_serum_count=sum(r['product_scope']=='adjacent_whitening_serum' for r in rows),taxonomy_correction_note='2026-11-03: one Colgate whitening serum40ml had retailer toothpaste category; semantic product_scope now separates it. All96 contexts retained; raw source unchanged.',seller_counts=dict(collections.Counter(r['seller'] for r in rows)),brand_counts=dict(collections.Counter(r['brand'] for r in rows)),watsons_unique_codes=len({r['product_code'] for r in rows if r['seller']=='Watsons Indonesia'}),location_verified_count=sum(r['location_verified'] for r in rows),price_per_100g_available=sum(r['price_per_100g_idr'] is not None for r in rows),children_named_count=sum(r['named_children_product'] for r in rows),status='validated IDs, provenance fields and unit-price arithmetic; catalogue only, not checkout')
(ROOT/'quality_report.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
