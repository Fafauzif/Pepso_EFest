#!/usr/bin/env python3
"""Offline source/provenance, reconciliation, and derived-file checks."""
import collections
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path
from build_tiktok import HERE,SOURCE_NAME

repo=HERE.parents[3]
candidates=[repo/'research/2026-11-03/closure/raw/user_runs'/(SOURCE_NAME+'.gz'),repo.parent/'upload'/SOURCE_NAME]
p=next((p for p in candidates if p.exists()),None)
assert p is not None,'Preserved source missing'
blob=gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes();raw=json.loads(blob)
stats=json.loads((HERE/'stats.json').read_text());assert hashlib.sha256(blob).hexdigest()==stats['source_sha256']
with gzip.open(HERE/'clean/comments.jsonl.gz','rt') as f:rows=[json.loads(l) for l in f]
with gzip.open(HERE/'clean/occurrences.jsonl.gz','rt') as f:occ=[json.loads(l) for l in f]
with gzip.open(HERE/'clean/comments.csv.gz','rt',newline='') as f:csvrows=list(csv.DictReader(f))
byid={r['source_record_id']:r for r in rows}
assert len(raw)==len(rows)==len(byid)==len(occ)==len(csvrows)==2380
assert sum(r['text_present'] for r in rows)==2372
assert sum(r['parent_record_id'] is not None for r in rows)==699
assert sum(r['parent_in_export'] is True for r in rows)==699
assert sum(not r['date_fields_agree_to_second'] for r in rows)==0
assert sum(r['case_scope']=='case_2022_H1_2026' for r in rows)==1648
assert sum(r['case_scope']=='pre_2022_context' for r in rows)==251
assert sum(r['case_scope']=='post_H1_2026_context' for r in rows)==481
assert not any(r['age_verified'] or r['premium_to_basic_verified'] for r in rows)
crossvideo=[]
for r in rows:
 s=raw[r['source_row_1based']-1]
 assert str(s['cid'])==r['source_record_id'] and s.get('text')==r['text_original']
 assert s['createTimeISO']==r['content_date']
 if r['parent_record_id']:
  assert r['parent_record_id'] in byid
  if byid[r['parent_record_id']]['video_id']!=r['video_id']:crossvideo.append(r['source_record_id'])
assert not crossvideo
ann=json.loads((HERE/'qualitative_evidence.json').read_text());assert len(ann)==len({r['source_record_id'] for r in ann})==100
for r in ann:
 s=raw[r['source_row_1based']-1]
 assert str(s['cid'])==r['source_record_id'] and s.get('text')==r['text_original']
 assert not r['age_verified'] and not r['premium_to_basic_verified']
assert sum(r['selection_method'].startswith('random') for r in ann)==36
result={'source_hash':'passed','raw_to_unique_to_occurrences_to_csv':len(raw),'all_source_ids_text_dates_match':True,'all_reply_parents_present_and_same_video':True,'date_epoch_ISO_agreement':True,'qualitative_annotation_source_matches':len(ann),'age_or_switcher_inference_flags':False,'gzip_JSONL_CSV_parse':'passed','result':'passed'}
(HERE/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
