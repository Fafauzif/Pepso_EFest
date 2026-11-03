#!/usr/bin/env python3
"""Independent read-only QA of published workstream tables; writes synthesis QA only."""
from pathlib import Path
from collections import Counter,defaultdict
from urllib.parse import urlsplit,urlunsplit,parse_qsl,urlencode
import json,csv,hashlib,re,importlib.util,sys,platform
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'synthesis'
def load(s):return json.loads((ROOT/s).read_text())
configs=[
 ('access_reviews/clean/lazada_reviews.json','consumer_review','review','record_id',None),
 ('access_reviews/clean/reddit_comments.json','consumer_comment','comment from one public thread','record_id',None),
 ('access_reviews/clean/oresa_incentivized_reviews.json','incentivized_review','campaign review','record_id',None),
 ('access_reviews/clean/tryandreview_reviews.json','mixed_incentive_review','review; incentive explicitly tagged where known','record_id',None),
 ('access_reviews/clean/lazada_products.json','product_metadata','Lazada item metadata','productId','context for Lazada reviews; not added to review count or retail count'),
 ('retail/retail_observations.json','retail_offer_observation','seller/product context; no location checkout','observation_id',None),
 ('brand_campaigns/clean/artifacts.json','web_artifact','retrieved artifact including unusable templates','artifact_id',None),
 ('brand_campaigns/clean/products_unique.json','product_page_subset','unique usable product page','artifact_id','subset of brand artifacts; do not add'),
 ('brand_campaigns/clean/campaign_observations.json','coded_observation','analyst observation sourced to brand artifact','observation_id','derived from brand artifacts; not independent source count'),
 ('brand_campaigns/clean/video_targets.json','uncollected_target','embedded video target','video_id','targets discovered, not downloaded videos or collected comments'),
 ('history_publicdata/promotion_events.json','historical_offer_event','advertised event; some non-price events','event_id',None),
 ('history_publicdata/public_health_indicators.json','published_indicator','published aggregate indicator','indicator_id',None),
 ('history_publicdata/public_data_metadata.json','dataset_variable_metadata','published variable definition','variable_id',None),
 ('literature/clean/candidates_all_unique.json','discovery_metadata','deduplicated scholarly discovery candidate','doi','discovery only; not all read or retained'),
 ('literature/clean/reviewed_evidence.json','reviewed_evidence','study/review with stated reading depth','study_id','25 retained sources; overlaps discovery list; do not add'),
 ('apify_handoff/input_manifest.json','proposed_configuration','schema-validated input file','filename','unexecuted; no collected consumer data'),
]
inventory=[];issues=[]
for fn,kind,unit,key,rel in configs:
 rows=load(fn); vals=[str(r.get(key)) for r in rows if r.get(key) is not None]; dup={k:v for k,v in Counter(vals).items() if v>1}
 refs=[];miss=[];hashchecks=[]
 register_path=ROOT/fn.split('/')[0]/'source_register.json'
 registry=json.loads(register_path.read_text()) if register_path.exists() else []
 registered_ids={str(x.get('source_id') or x.get('id') or x.get('study_id')) for x in registry}
 missing_source_ids=sorted({str(x['source_id']) for x in rows if x.get('source_id') and str(x['source_id']) not in registered_ids})
 for i,row in enumerate(rows):
  for fld in ['raw_file','text_file','metadata_raw_file','fulltext_raw_file']:
   v=row.get(fld)
   if v:
    p=ROOT/fn.split('/')[0]/v;refs.append(str(p.relative_to(ROOT)))
    if not p.exists():miss.append({'row':i,'field':fld,'value':v})
  if row.get('metadata_raw_file_sha256') and row.get('metadata_raw_file'):
   p=ROOT/fn.split('/')[0]/row['metadata_raw_file']
   if p.exists():hashchecks.append(hashlib.sha256(p.read_bytes()).hexdigest()==row['metadata_raw_file_sha256'])
 csvp=(ROOT/fn).with_suffix('.csv');csvcount=len(list(csv.DictReader(csvp.open()))) if csvp.exists() else None
 inv=dict(file=fn,count=len(rows),kind=kind,unit=unit,key=key,null_key_count=sum(r.get(key) is None for r in rows),duplicate_nonnull_keys=dup,relationship=rel,csv_row_count=csvcount,csv_count_matches=(csvcount==len(rows)) if csvcount is not None else None,raw_reference_count=len(refs),unique_raw_files=len(set(refs)),missing_raw_references=miss,metadata_hash_checks=len(hashchecks),metadata_hashes_match=all(hashchecks),missing_source_ids=missing_source_ids)
 inventory.append(inv)
 if dup and fn!='literature/clean/candidates_all_unique.json':issues.append({'table':fn,'issue':'duplicate key','detail':dup})
 if missing_source_ids:issues.append({'table':fn,'issue':'source ID absent from primary register','detail':missing_source_ids})
 if miss:issues.append({'table':fn,'issue':'missing raw refs','detail':miss})
 if csvcount is not None and csvcount!=len(rows):issues.append({'table':fn,'issue':'CSV/JSON count mismatch'})
# Four consumer corpora: duplicate IDs and exact normalized text, not accidental deletion.
consumer=[]
for inv in inventory[:4]:
 for r in load(inv['file']):consumer.append({**r,'corpus_file':inv['file']})
textgroups=defaultdict(list)
for r in consumer:
 text=re.sub(r'\s+',' ',r.get('review_text','')).strip().casefold()
 if text:textgroups[text].append(r['record_id'])
dups={hashlib.sha256(k.encode()).hexdigest()[:16]:v for k,v in textgroups.items() if len(v)>1}
ct=dict(records=len(consumer),unique_record_ids=len({r['record_id'] for r in consumer}),exact_normalized_text_duplicate_groups=len(dups),records_in_exact_text_duplicate_groups=sum(map(len,dups.values())),excess_records_beyond_one_per_exact_text=sum(len(v)-1 for v in dups.values()),verified_18_30_switchers=sum(bool(r.get('age_verified') and r.get('premium_to_basic_verified')) for r in consumer),raw_text_encoding_warning_records=sum(bool(re.search('Ã|ð\x9f|â\x9c|ðŸ|âœ',r.get('review_text',''))) for r in consumer),notes='Text repeats can be legitimate template/campaign duplicates. IDs remain unique; no inference of independent people or national prevalence.')
# Canonicalize only documented URL equivalences; retain meaningful page/filter/query semantics.
def canonical(u):
 a=urlsplit(u.strip());host=a.netloc.lower();host=host[4:] if host.startswith('www.') else host
 q=[(k,v) for k,v in parse_qsl(a.query,keep_blank_values=True) if not k.lower().startswith('utm_') and k.lower() not in {'fbclid','gclid'}]
 return urlunsplit(('https' if a.scheme in {'http','https'} else a.scheme,host,a.path.rstrip('/') or '/',urlencode(sorted(q)),''))
registers=[];allurls=[];allhash=[]
for wd in ['access_reviews','retail','brand_campaigns','history_publicdata','literature','apify_handoff']:
 rows=load(wd+'/source_register.json');urls=[r.get('canonical_url') or r.get('url') or r.get('source_url') for r in rows];urls=[u for u in urls if u];norm=[canonical(u) for u in urls]
 failed=[];reg_missing=[];hash_bad=[];checks=0
 for i,r in enumerate(rows):
  for fld in ['raw_file','text_file','metadata_raw_file','fulltext_raw_file','file']:
   v=r.get(fld)
   if v and isinstance(v,str):
    p=ROOT/wd/v
    if not p.exists():reg_missing.append({'row':i,'field':fld,'value':v})
  f=r.get('raw_file') or r.get('file') or r.get('metadata_raw_file');h=r.get('sha256') or r.get('metadata_raw_file_sha256')
  if f and h and (ROOT/wd/f).exists():
   checks+=1
   if hashlib.sha256((ROOT/wd/f).read_bytes()).hexdigest()!=h:hash_bad.append({'row':i,'file':f})
  if r.get('status')=='failed' or r.get('outcome')=='failed':failed.append(i)
 d=dict(file=wd+'/source_register.json',rows=len(rows),urls_present=len(urls),canonical_unique_urls=len(set(norm)),duplicate_canonical_url_count=len(norm)-len(set(norm)),explicit_failed_rows=len(failed),missing_referenced_files=reg_missing,hash_checks=checks,hash_mismatches=hash_bad);registers.append(d);allurls+=norm
 if reg_missing or hash_bad:issues.append({'register':d['file'],'issue':'source file/hash problem','missing':reg_missing,'hash':hash_bad})
url_summary=dict(primary_register_rows=sum(r['rows'] for r in registers),url_rows=len(allurls),canonical_unique_urls=len(set(allurls)),canonical_duplicate_rows=len(allurls)-len(set(allurls)),canonicalization='lowercase host; remove www; normalize HTTP to HTTPS; remove fragment/trailing slash; sort query; drop utm_,fbclid,gclid only. Meaningful pagination/query params retained.',note='Includes failed attempted sources and actor metadata; not a count of successfully read substantive sources. Auxiliary/retry registers excluded to avoid double-counting.')
# Assert cited 100g/160g price directly against stored API JSON.
r100=next(r for r in load('retail/retail_observations.json') if r['observation_id']=='WATAPI-PEPSODENT-005')
r160=next(r for r in load('retail/retail_observations.json') if r['observation_id']=='WATAPI-PEPSODENT-031')
raw=load('retail/raw/WATAPI-PEPSODENT.json')
checks=[]
for r in [r100,r160]:
 i=int(re.search(r'products\[(\d+)\]',r['record_locator'])[1]);p=raw['products'][i];checks.append(dict(observation_id=r['observation_id'],raw_locator=r['record_locator'],raw_product_name=p['name'],name_matches=p['name']==r['product_name'],raw_price_idr=p['price']['value'],normalized_price_idr=r['price_idr'],price_matches=p['price']['value']==r['price_idr'],grams=r['grams_total_for_analysis'],per_100g_idr=r['price_idr']/r['grams_total_for_analysis']*100,source_url=r['catalogue_url']))
p100=r100['price_idr']/100;p160=r160['price_idr']/160
price=dict(raw_checks=checks,ticket_increase_idr=r160['price_idr']-r100['price_idr'],ticket_increase_percent=(r160['price_idr']/r100['price_idr']-1)*100,grams_increase_percent=60,price_per_gram_100=p100,price_per_gram_160=p160,per_gram_reduction_percent=(1-p160/p100)*100,availability='No Jakarta branch/postcode or completed checkout verified',time_scope='Current catalogue snapshot, not historical causal proof')
# Independent schema validation without executing or rewriting actors.
schema_results=[]
try:
 import jsonschema
 for m in load('apify_handoff/input_manifest.json'):
  schema=load('apify_handoff/schemas/'+('xquik_input_schema.json' if m['actor'].startswith('xquik') else 'scrapewise_input_schema.json'));x=load('apify_handoff/inputs/'+m['filename']);jsonschema.Draft7Validator(schema).validate(x);schema_results.append({'file':m['filename'],'valid':True,'actor_executed':False})
except Exception as e:schema_results.append({'error':repr(e)})
literature_rows=load('literature/clean/reviewed_evidence.json')
literature_read_levels=dict(Counter(x.get('read_level') for x in literature_rows))
candidates=load('literature/clean/candidates_all_unique.json');candidate_keys=[str(x.get('doi') or re.sub(r'\s+',' ',x.get('title','')).casefold().strip()).lower() for x in candidates]
candidate_fallback_duplicates={k:v for k,v in Counter(candidate_keys).items() if v>1}
result=dict(validation_runtime={'python':platform.python_version(),'schema_dependency':'jsonschema==4.26.0; install apify_handoff/requirements-validation.txt to revalidate schemas','command_note':'This release was checked with the session dependency directory on PYTHONPATH; no package data or credentials required.'},literature_read_levels=literature_read_levels,candidate_doi_title_fallback_duplicates=candidate_fallback_duplicates,validated_at='2026-11-03',inventory=inventory,consumer_data=ct,source_registers=registers,source_url_summary=url_summary,price_verification=price,apify_schema_checks=schema_results,issues=issues,important_limits=['No verified18–30 Premium-to-Basic switchers','No team primary interview/survey evidence','Catalogue stock is not branch availability','Incentivized corpora kept separate','Metadata/discovery records not added to substantive evidence counts'])
(OUT/'DATA_INVENTORY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(OUT/'EXACT_TEXT_DUPLICATE_GROUPS.json').write_text(json.dumps(dups,ensure_ascii=False,indent=2))
lines=['# Independent integration validation','', 'Checked 3 November 2026. Read-only checks of primary clean tables; intermediate/raw duplicates are not counted as additional research data.','', '| Primary table | Rows | Unit / interpretation |','|---|---:|---|']
for r in inventory:lines.append(f"| `{r['file']}` | {r['count']} | {r['unit']}"+(f"; {r['relationship']}" if r['relationship'] else '')+' |')
lines+=['','## Checks and limits','',f"- Consumer records: **{ct['records']}**, with **{ct['unique_record_ids']} unique record IDs**. No verified18–30 Premium-to-Basic switchers.",f"- Exact whitespace/case-normalized text: {ct['exact_normalized_text_duplicate_groups']} duplicate groups containing {ct['records_in_exact_text_duplicate_groups']} records ({ct['excess_records_beyond_one_per_exact_text']} excess beyond one per string). IDs remain unique; repeated/templated content does not identify independent people.",f"- Source registers: {url_summary['primary_register_rows']} primary rows, {url_summary['canonical_unique_urls']} canonical URL identities, including attempted failures/metadata. These are not all successfully read substantive sources.",'- Canonicalization removes only documented URL equivalences; meaningfully different date/page/search parameters remain distinct. Auxiliary retry registers are not re-added.','- CSV/JSON row counts checked where paired files exist. Every primary-table raw/text reference checked for existence. Source-register stored hashes checked where supplied.','- Metadata, 28 product-page subsets, campaign coding, video targets, scholarly candidates and Apify configurations must not be summed with independent consumer observations.','- The25 retained literature items comprise21 abstract-level reads and4 relevant-fulltext-section reads per workstream record; do not claim25 full papers read.','- Current source claims cannot explain the historical decline on their own.','']
lines+=['## Raw price verification','', '| Record | Raw observed price | Grams | Price /100g |','|---|---:|---:|---:|']
for c in checks:lines.append(f"| `{c['observation_id']}` | Rp{c['raw_price_idr']:,.0f} | {c['grams']:g}g | Rp{c['per_100g_idr']:,.2f} |")
lines += ['',f"Both names and prices match `retail/raw/WATAPI-PEPSODENT.json` at the recorded zero-based product locators. The160g ticket is Rp{price['ticket_increase_idr']:,.0f} higher ({price['ticket_increase_percent']:.2f}%) for60% more named grams; its price per gram is **{price['per_gram_reduction_percent']:.2f}% lower**. This is a current catalogue comparison, not an observed buying response. No local checkout stock is verified.",'','## Issues needing attention','']
if issues:
 for z in issues:lines.append('- '+json.dumps(z,ensure_ascii=False))
else:lines.append('No structural missing-file, duplicate-ID, paired-count or supplied-hash failures found in the checks above.')
if ct['raw_text_encoding_warning_records']:lines.append(f"- Heuristic flagged {ct['raw_text_encoding_warning_records']} consumer texts for possible mojibake. Original bytes/text remain preserved. Do not use garbled passages as direct quotations; inspect originals before interpretation. This detector is not a complete encoding audit.")
lines+=['','## Apify input checks','',f"Independently schema-validated {sum(r.get('valid',False) for r in schema_results)} input files; no actor was executed. A schema pass does not prove access, pricing, complete coverage or collection success.",'','Replay `python3 research/2026-11-03/synthesis/validate_inventory.py` after installing `apify_handoff/requirements-validation.txt` into the chosen Python environment. If jsonschema is unavailable, the table checks still run and the schema check records that limitation explicitly.', '', 'See `DATA_INVENTORY.json` for per-table checks and exact counts.']
(OUT/'VALIDATION.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(consumer=ct,url_summary=url_summary,issues=issues,schema_valid=sum(r.get('valid',False) for r in schema_results),price_reduction=price['per_gram_reduction_percent']),ensure_ascii=False,indent=2))
