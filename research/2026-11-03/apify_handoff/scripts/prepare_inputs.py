"""Regenerate proposed USER-RUN inputs; never executes actors or reads credentials."""
import json, pathlib, csv
base=pathlib.Path(__file__).resolve().parents[1]
queries={
 'historical_premium_value':'pepsodent (sensitive OR whitening OR herbal OR "mineral expert" OR "complete care") (mahal OR murah OR promo OR "beli lagi" OR "sama aja")',
 'historical_household':'(odol OR "pasta gigi") (ortu OR "orang tua" OR dibeliin OR mama OR keluarga OR kos)',
 'historical_sensory':'(pepsodent OR sensodyne OR enzim) (bersih OR segar OR busa OR pedas OR kesat OR rasa OR ngilu)',
 'historical_switching':'(pepsodent OR sensodyne OR enzim) ("balik ke" OR "ganti odol" OR "beli lagi" OR "repeat order" OR "sebelumnya pakai")',
 'current_comparison':'(pepsodent OR sensodyne OR enzim) ("sensitive" OR whitening OR "ultra white") (mahal OR promo OR bersih OR segar OR "beli lagi")',
}
manifest=[]
for name,q in queries.items():
 for stage,limit in [('pilot',40),('main',300)]:
  current=name.startswith('current')
  x={'mode':'search','twitterContent':q,'maxItems':limit,'queryType':'Latest','since':'2026-07-01' if current else '2022-01-01','until':'2026-11-04' if current else '2026-07-01','tweetTypes':{'excludeRetweets':True},'outputVariant':'rich','fieldStyle':'snake_case','alwaysSaveRunRecords':True}
  fn=f'xquik_{name}_{stage}.json';(base/'inputs'/fn).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
  manifest.append({'filename':fn,'actor':'xquik/x-tweet-scraper','stage':stage,'ready_status':'schema_validated_not_execution_tested','target_scope':name,'max_data_rows':limit,'free_result_fees_usd':round(limit*.00015,5),'separate_platform_cost':'yes; measure pilot','suggested_max_total_charge_usd':.25 if stage=='pilot' else .75,'suggested_timeout_seconds':300 if stage=='pilot' else 600,'historical':not current})
u='https://shopee.co.id/Pepsodent-Sensitiv-Expert-Complete-Care-100g-i.1647008809.41674486015'
for stage,limit in [('pilot',20),('main',200)]:
 x={'startUrls':[u],'country':'ID','maxReviews':limit,'minRating':1,'maxRating':5,'onlyWithComment':True,'onlyWithMedia':False,'includeShopSummary':True}
 fn=f'scrapewise_shopee_complete_care_{stage}.json';(base/'inputs'/fn).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
 manifest.append({'filename':fn,'actor':'scrapewise/shopee-reviews-scraper','stage':stage,'ready_status':'schema_validated_not_execution_tested; low priority','target_scope':'one independent Bekasi listing; not official brand store','max_data_rows':limit,'free_result_fees_usd':round(limit*.003,5),'separate_platform_cost':'API does not flag user-paid platform; verify console; actor-start extra .005 per GB min1','suggested_max_total_charge_usd':.15 if stage=='pilot' else .80,'suggested_timeout_seconds':300,'historical':False})
(base/'input_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with (base/'input_manifest.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(manifest[0]));w.writeheader();w.writerows(manifest)
# Validate exact supplied actor fields and JSON types against the archived full schemas.
import jsonschema
validation=[]
for m in manifest:
 n='xquik' if m['actor'].startswith('xquik') else 'scrapewise';s=json.loads((base/'schemas'/f'{n}_input_schema.json').read_text());x=json.loads((base/'inputs'/m['filename']).read_text())
 unknown=sorted(set(x)-set(s.get('properties',{})))
 assert not unknown,unknown
 jsonschema.Draft7Validator(s).validate(x)
 validation.append({'file':m['filename'],'schema':f'schemas/{n}_input_schema.json','result':'valid','actor_executed':False})
(base/'validation_report.json').write_text(json.dumps(validation,indent=2)+'\n')
print(f'Generated and schema-validated {len(manifest)} proposed input JSONs; no actors executed.')
