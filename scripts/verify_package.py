#!/usr/bin/env python3
"""Verify this release's data reconciliation and file checksums. Stdlib only."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/clean/keyword_observations.json').read_text())
unique=json.loads((root/'data/clean/keywords_unique.json').read_text())
report=json.loads((root/'docs/quality_report.json').read_text())
assert len(rows)==report['observation_count']==300
assert len(unique)==report['unique_view_rows']==300
assert len({r['observation_id'] for r in rows})==len(rows)
assert len({r['keyword'] for r in rows})==report['unique_keyword_count']
assert dict(Counter(r['volume_status'] for r in rows))==report['volume_status_counts']
for r in rows:
    if r['volume_status'] in {'blank','not_available'}: assert r['search_volume'] is None
    if r['volume_status']=='zero': assert r['search_volume']==0
    if r['volume_status']=='positive': assert r['search_volume']>0
    assert r['country_verified_in_capture'] is False
    if r['cpc_currency'] is None: assert r['cpc_analysis_value'] is None
    source=(root/r['source_file']).read_text(encoding='utf-8-sig').splitlines()
    assert r['keyword_raw'] in '\n'.join(source[r['source_line_start']-1:r['source_line_end']])
with (root/'data/clean/keyword_observations.csv').open(newline='') as f:
    csvrows=list(csv.DictReader(f))
assert len(csvrows)==len(rows)
for a,b in zip(rows,csvrows):
    assert a['observation_id']==b['observation_id']
    assert (b['search_volume']=='')==(a['search_volume'] is None)
normalized_sources=[]
for s in report['sources']:
    data=(root/s['path']).read_bytes()
    actual=hashlib.sha256(data).hexdigest()
    if actual!=s['sha256']:
        # Git's original '* text=auto' normalized CRLF source bytes to LF.
        # Accept only the exact cryptographically verified reversible variant;
        # keep source files and original captured hashes unchanged.
        assert b'\r' not in data, s['path']
        restored=data.replace(b'\n',b'\r\n')
        assert hashlib.sha256(restored).hexdigest()==s['sha256'], s['path']
        normalized_sources.append(s['path'])
if normalized_sources:
    print('Original source hashes match exact CRLF reconstruction after Git LF normalization: '+', '.join(normalized_sources))
manifest=root/'MANIFEST.sha256'
if manifest.exists():
    for line in manifest.read_text().splitlines():
        expected,path=line.split('  ',1)
        assert hashlib.sha256((root/path).read_bytes()).hexdigest()==expected,path
print('Verified: counts, missingness, source-line provenance, CSV/JSON consistency, source hashes and release checksums.')
