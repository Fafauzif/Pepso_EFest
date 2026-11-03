#!/usr/bin/env python3
"""Offline validation of canonical scaled Watsons reviews against every raw source row."""
import json,hashlib,re,collections
from pathlib import Path
R=Path(__file__).resolve().parents[1]
r=json.loads((R/'clean/reviews.json').read_text());sources=json.loads((R/'source_register.json').read_text());byid={s['source_id']:s for s in sources};rawcache={};keys=collections.Counter();topkeys=collections.Counter()
assert len(r)==len({x['record_id'] for x in r})
for s in sources:
 p=R/s['raw_file'];b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==s['sha256'];d=json.loads(b);rawcache[s['raw_file']]=d;topkeys.update(d.keys())
 assert len(d.get('reviews',[]))==s['rows']
 for x in d.get('reviews',[]):keys.update(x.keys())
for x in r:
 assert x['source_id'] in byid
 raw=rawcache[x['raw_file']]['reviews'][int(re.search(r'reviews\[(\d+)\]',x['raw_locator'])[1])]
 assert str(raw['id'])==x['review_id'];assert raw.get('comment')==x['review_text'];assert raw.get('rating')==x['rating'];assert raw.get('date')==x['published_raw']
 assert x['age_verified'] is False and x['premium_to_basic_verified'] is False and x['reviewer_residence_verified'] is False
 assert x['incentive_status']=='not_established'
coverage=json.loads((R/'product_coverage.json').read_text());totalsmatch=all(p['reported_total']==p['unique_review_ids'] for p in coverage)
report=dict(canonical_records=len(r),unique_record_ids=len({x['record_id'] for x in r}),raw_source_pages=len(sources),raw_hash_checks_passed=len(sources),row_id_text_rating_date_matches=len(r),source_id_joins_passed=len(r),product_contexts=len(coverage),all_reported_product_totals_match_actual_captures=totalsmatch,empty_reported_product_contexts=sum(p['reported_total']==0 for p in coverage),source_review_field_counts=dict(keys),source_top_level_field_counts=dict(topkeys),country_language_syndication_incentive_fields_exposed=[k for k in keys if re.search('country|locale|language|syndicat|source|incentiv|reward|verified',k,re.I)],no_verified_age_or_switching=True)
(R/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
