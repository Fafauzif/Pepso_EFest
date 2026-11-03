#!/usr/bin/env python3
"""Meaningful local reconciliation and source-locator checks; no network."""
import csv,gzip,json,pathlib
from clean_analyze import HERE,NAMES,load

def read(name):
 with gzip.open(HERE/name,'rt',encoding='utf8') as f:return [json.loads(l) for l in f]
def main():
 records=read('reviews_clean.jsonl.gz');occ=read('review_occurrences.jsonl.gz');products=read('product_observations.jsonl.gz');notices=read('billing_notices.jsonl.gz');excluded=read('excluded_shopee.jsonl.gz');annotations=read('qualitative_evidence.jsonl.gz');stats=json.loads((HERE/'stats.json').read_text())
 assert len(records)==len({r['record_key'] for r in records})==266
 assert len(occ)==309 and len(occ)-len(records)==43
 assert len(products)==24 and len({r['productId'] for r in products})==18
 assert len(notices)==2 and len(excluded)==102
 assert sum(r['age_verified'] for r in records)==sum(r['premium_to_basic_verified'] for r in records)==0
 assert sum(bool(r['text_normalized']) for r in records)==263
 assert sum(r['eligible_written_toothpaste_candidate'] for r in records)==256
 assert sum(r['date_fields_disagree'] for r in records)==186
 with gzip.open(HERE/'reviews_clean.csv.gz','rt',encoding='utf8',newline='') as f:assert len(list(csv.DictReader(f)))==len(records)
 assert len(annotations)==len({a['record_key'] for a in annotations})==85
 bykey={r['record_key']:r for r in records}
 for a in annotations:assert a['original_text']==bykey[a['record_key']]['text_original']
 # Original occurrence payload retained byte-equivalent as parsed JSON; locators stay exact.
 source_rows={}
 for s in stats['source_files']:
  name=s['original_filename'];p=HERE.parent/'raw/user_runs'
  try:rows,_=load(name,p)
  except FileNotFoundError:rows,_=load(name,HERE.parents[4]/'upload')
  source_rows[name]=rows
 for o in occ:assert source_rows[o['source_filename']][o['json_index_zero_based']]==o['raw_payload']
 for r in records:
  loc=r['last_source'];src=source_rows[loc['source_filename']][loc['json_index_zero_based']]
  assert r['text_original']==src.get('reviewText') and r['rating']==src.get('rating')
 print('PASS: unique identity, occurrences, type separation, eligibility, dates, CSV/JSON counts, annotations and exact source locators')
if __name__=='__main__':main()
