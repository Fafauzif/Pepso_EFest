#!/usr/bin/env python3
"""Verify outputs against immutable originals, not just against each other."""
from pathlib import Path
import json,gzip,hashlib,collections,argparse,datetime
from build_x import FILES,REPO,HERE,load_bytes

def main():
 a=argparse.ArgumentParser();a.add_argument('--input-dir',type=Path);n=a.parse_args()
 bases=[n.input_dir] if n.input_dir else [HERE.parent/'raw/user_runs',REPO/'data/raw/user_runs',REPO.parent/'upload']
 b=next((p for p in bases if p and ((p/FILES[0]).exists() or (p/(FILES[0]+'.gz')).exists())),None)
 if b is None:raise SystemExit('Original raw exports not found; specify --input-dir.')
 sources={};checks=[]
 stats=json.loads((HERE/'stats.json').read_text())
 for s in stats['source_inputs']:
  p=b/s['filename'];p=p if p.exists() else b/(s['filename']+'.gz');bb=load_bytes(p)
  assert hashlib.sha256(bb).hexdigest()==s['sha256_original_bytes'];sources[s['filename']]=json.loads(bb)
 checks.append('Original decompressed bytes match four input SHA-256 values.')
 rows=list(map(json.loads,gzip.open(HERE/'records.jsonl.gz','rt')));occ=list(map(json.loads,gzip.open(HERE/'occurrences.jsonl.gz','rt')))
 assert len(rows)==len({r['source_record_id'] for r in rows})==12990
 assert len(occ)==sum(len(s) for s in sources.values())==16165
 actual_ids={str(r['id']) for d in sources.values() for r in d};assert actual_ids=={r['source_record_id'] for r in rows}
 for r in rows:
  raw=sources[r['latest_source_file']][r['latest_json_index_zero_based']]
  assert str(raw['id'])==r['source_record_id'];assert (raw.get('text') or '')==r['text_original']
  assert not r['age_verified'] and not r['confirmed_pepsodent_premium_to_basic_switch'] and not r['geography_verified']
 for o in occ:
  raw=sources[o['source_file']][o['json_index_zero_based']];assert o['record_key']=='x:'+str(raw['id'])
  assert o['text_sha256']==hashlib.sha256((raw.get('text') or '').encode()).hexdigest()
 checks.append('Every unique normalized text and every occurrence locator resolves to original source row.')
 assert collections.Counter(r['scope'] for r in rows)==stats['date_scope'];assert stats['unique_post_ids']+stats['repeated_identity_occurrences']==stats['exported_rows']
 evidence=[json.loads(l) for l in (HERE/'evidence.jsonl').read_text().splitlines()];assert len(evidence)==len({r['record_key'] for r in evidence})==109
 for r in evidence:
  src=sources[r['source_file']][r['json_index_zero_based']];assert str(src['id'])==r['source_record_id'];assert src['text']==r['text_original']
 checks.append('109 close-reading annotations match original source ID and full text exactly.')
 selection=json.loads((HERE/'review_selection.json').read_text())['records'];assert len(selection)==100
 assert len([x for x in selection if x['sampling_stratum']=='random_40_all_unique_posts'])==40
 checks.append('Frozen sample has 40 uniform records plus 60 purposive-screen records; 9 supplementary records separately labelled.')
 legacy=json.loads((HERE/'legacy_x_overlap.json').read_text());assert len(legacy)==6;assert sum(x['overlaps_new_exports'] for x in legacy)==1
 assert stats['combined_platform_ids_including_legacy']==12995
 checks.append('Legacy six-source overlap reconciles to 12,995 platform IDs, without double-counting consumer post.')
 result={'status':'passed','checks':checks,'new_export_ids':12990,'occurrences':16165,'legacy_overlap':1,'combined_x_ids':12995,'close_read_records':109,'raw_sources_changed':False,'new_network_collection':False}
 (HERE/'qa_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
