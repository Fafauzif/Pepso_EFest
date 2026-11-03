#!/usr/bin/env python3
"""Offline integrity/reconciliation checks for the portable release; stdlib."""
import argparse,gzip,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'research/2026-11-03/closure'
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--skip-manifest',action='store_true');a=ap.parse_args()
    if not a.skip_manifest:
        for line in (ROOT/'MANIFEST.sha256').read_text().splitlines():
            expected,rel=line.split('  ',1);p=ROOT/rel;assert p.is_file(),rel;assert sha(p)==expected,rel
    register=json.loads((C/'raw/UPLOAD_REGISTER.json').read_text())
    for e in register['files']:
        p=C/e['archive_path'];assert sha(p)==e['archive_sha256'],e['archive_path']
        if e['encoding']=='gzip_exact_original_bytes':
            with gzip.open(p,'rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==e['original_sha256']
        else:assert sha(p)==e['original_sha256']
    inv=json.loads((C/'integrated/INVENTORY.json').read_text());ids=set();platforms=Counter();total=0
    for e in inv['shards']:
        p=C/'integrated'/e['path'];assert p.stat().st_size==e['bytes'];assert sha(p)==e['sha256'];n=0
        with gzip.open(p,'rt',encoding='utf-8') as f:
            for line in f:
                r=json.loads(line);key=r['record_key'];assert key not in ids,key;ids.add(key)
                assert r['text_original'].strip(),key
                assert r.get('age_verified') is False,key
                assert r.get('premium_to_basic_verified') is False,key
                assert r['calendar_period_is_case_eligibility'] is False,key
                platforms[r['platform']]+=1;n+=1
        assert n==e['rows'];total+=n
    assert total==inv['written_records_all_retained_scopes']==314476
    assert dict(platforms)==inv['platforms']
    assert sum(e['written_retained'] for e in inv['sources'])==total
    large=ROOT/'release/LARGE_FILES.json';logical=0
    if large.exists():
        for e in json.loads(large.read_text())['files']:
            h=hashlib.sha256();size=0
            for part in e['parts']:
                p=ROOT/part['path'];assert sha(p)==part['sha256'];assert p.stat().st_size==part['bytes']
                with p.open('rb') as f:
                    while block:=f.read(1024*1024):h.update(block);size+=len(block)
            assert size==e['bytes'] and h.hexdigest()==e['sha256'],e['path'];logical+=1
        files=[ROOT/line.split('  ',1)[1] for line in (ROOT/'MANIFEST.sha256').read_text().splitlines()]+[ROOT/'MANIFEST.sha256']
        assert all(p.stat().st_size<45*1024*1024 for p in files if p.relative_to(ROOT).as_posix() not in {e['path'] for e in json.loads(large.read_text())['files']})
    print(json.dumps({'status':'passed','archived_inputs_verified':len(register['files']),'master_written_inventory_records':total,'unique_record_keys':len(ids),'platforms':dict(platforms),'legacy_logical_files_verified':logical,'manifest_checked':not a.skip_manifest,'scope':'Integrity/count reconciliation; not representative sampling, qualitative truth, or clinical validation.'},indent=2))
if __name__=='__main__':main()
