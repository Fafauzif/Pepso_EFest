#!/usr/bin/env python3
"""Replay 4 Nov exploratory retrieval, without treating matches as coded prevalence.
Stdlib; reads existing master shards and a Reddit provenance table. Writes only
small derived outputs to research/2026-11-04/synthesis/. No network or collection.
"""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
from query_corpus import iter_records
PATTERNS={
 'funding_transition':(r'bonyok|orang\s*tua|ortu|mama|papa|nyokap|bokap|suami|istri|dibeliin|dibelikan',r'kos|kost|kerja|sendiri|mahal|beli|bayar'),
 'internal_fallback':(r'pepsodent',r'balik|biasa|ganti|putih|murah'),
 'benefit_continuation':(r'cocok|nyaman|ngilu|sariawan',r'beli lagi|repeat|bertahun|setia|ganti|balik'),
 'price_reference':(r'promo|diskon|mahal',r'lama|biasa|setia|cocok|repeat|beli lagi|habis')}
IDS={'jmyv9ux','jmyy6vi','jmyktx0','jn2d5tk','jmz7mka','l5b2lmz','l5gjjk8',
     '2015590249167274297','1600113707526524928','7552195449504547585',
     '7425778994514150149','1932700850','2145103290','1469837237'}
reddit={r['record_id']:r for r in csv.DictReader((ROOT/'research/2026-11-03/scale_reddit/reddit_records.csv').open(newline=''))}
counts=Counter();selected=[];scanned=0
for r in iter_records():
 if r['platform']=='amazon_external_context':continue
 scanned+=1;t=r['text_original'];s=t.casefold()
 for k,(a,b) in PATTERNS.items():
  if re.search(a,s) and re.search(b,s):counts[k]+=1
 sid=r['source_record_id'];short=sid.rsplit(':',1)[-1]
 if short in IDS:
  out={k:r.get(k) for k in ['record_key','platform','source_record_id','source_url','text_original','content_date','incentive_status','source_locator']}
  out['text_sha256']=hashlib.sha256(t.encode()).hexdigest()
  out['selection']='purposive mechanism/counterexample reading; not representative or part of earlier 294 annotations'
  out['age_independently_verified']=False;out['confirmed_target_switching_sequence']=False
  if sid in reddit:
   origin=reddit[sid]
   out['reddit_provenance']={k:origin[k] for k in ['raw_file','raw_record_index','parent_id','created_at']}
  selected.append(out)
assert scanned==27770,scanned
assert counts=={'price_reference':138,'internal_fallback':1065,'benefit_continuation':290,'funding_transition':123},counts
assert len(selected)==len(IDS),(len(selected),len(IDS))
outdir=ROOT/'research/2026-11-04/synthesis';outdir.mkdir(exist_ok=True,parents=True)
(outdir/'INSIGHT_SCREENING_COUNTS.json').write_text(json.dumps({
 'date':'2026-11-04','non_amazon_records_searched':scanned,
 'overlapping_lexical_candidate_hits':dict(sorted(counts.items())),
 'selected_excerpt_records':len(selected),
 'existing_294_annotation_count_changed':False,
 'interpretation':'Retrieval hits and purposively selected excerpts, not people, coded mechanism prevalence, verified ages, or causal switching evidence.',
 'patterns':PATTERNS},indent=2)+'\n')
(outdir/'INSIGHT_SOURCE_EXCERPTS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in sorted(selected,key=lambda x:x['record_key'])))
print(json.dumps({'status':'replayed','non_amazon_records':scanned,'hit_counts':dict(counts),'selected':len(selected),'new_records_collected':0},indent=2))
