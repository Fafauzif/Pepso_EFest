#!/usr/bin/env python3
"""Independent audit of user exports; accepts originals or losslessly gzipped copies.

Run from any directory with --input-dir pointing at closure/raw/user_runs.
Optional --previous-zip checks the earlier downloadable release when available.
No network requests or writes to inputs occur. The output is a fresh QA report.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import gzip
import hashlib
import json
from pathlib import Path
import zipfile


def payload(path: Path) -> bytes:
    return gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes()


def source_name(path: Path) -> str:
    return path.name[:-3] if path.suffix == '.gz' else path.name


def audit(input_dir: Path, previous_zip: Path | None = None) -> dict:
    files = sorted(x for x in input_dir.iterdir() if x.is_file())
    lookup = {source_name(f): f for f in files}
    out = {'inputs': []}
    for name, f in sorted(lookup.items()):
        raw = payload(f)
        out['inputs'].append({'name': name, 'bytes': len(raw),
                              'sha256': hashlib.sha256(raw).hexdigest()})

    def load(name):
        return json.loads(payload(lookup[name]))

    ids, xs = set(), []
    for name in sorted(x for x in lookup if x.startswith('dataset_x') and x.endswith('.json')):
        d = load(name)
        i = {str(r['id']) for r in d}
        dates = [dt.datetime.strptime(r['created_at'], '%a %b %d %H:%M:%S %z %Y') for r in d]
        xs.append({'file': name, 'rows': len(d), 'unique': len(i),
                   'overlap_earlier': len(i & ids), 'new': len(i - ids),
                   'blank': sum(not bool(r.get('text', '').strip()) for r in d),
                   'dates': [min(dates).isoformat(), max(dates).isoformat()]})
        ids |= i
    out['x'] = {'files': xs, 'unique_combined': len(ids),
                'total_occurrences': sum(r['rows'] for r in xs)}

    tname = next(x for x in lookup if x.startswith('dataset_tiktok') and x.endswith('.json'))
    t = load(tname)
    out['tiktok'] = {
        'rows': len(t), 'unique_cids': len({r['cid'] for r in t}),
        'videos': len({r['videoWebUrl'] for r in t}),
        'blank_text': sum(not bool(r.get('text', '').strip()) for r in t),
        'replies': sum(bool(r.get('repliesToId')) for r in t),
        'case_period_comment_dates': sum('2022-01-01' <= r.get('createTimeISO', '') < '2026-07-01' for r in t),
        'video_counts': dict(collections.Counter(r['videoWebUrl'] for r in t))}

    ts, ri = [], set()
    for name in sorted(x for x in lookup if x.startswith('dataset_tokopedia') and x.endswith('.json')):
        d = load(name)
        rr = [r for r in d if r.get('type') == 'product_review']
        ii = {str(r['reviewId']) for r in rr}
        ts.append({'file': name, 'row_types': dict(collections.Counter(r.get('type') for r in d)),
                   'distinct_review_ids': len(ii), 'new_review_ids': len(ii - ri),
                   'nonempty_reviews': sum(bool((r.get('reviewText') or '').strip()) for r in rr),
                   'date_fields_both_present': sum(bool(r.get('reviewTime') and r.get('reviewDate')) for r in rr),
                   'date_field_disagreements': sum(bool(r.get('reviewTime') and r.get('reviewDate') and r['reviewTime'][:10] != r['reviewDate'][:10]) for r in rr),
                   'missing_reviewTime': sum(not bool(r.get('reviewTime')) for r in rr),
                   'missing_reviewDate': sum(not bool(r.get('reviewDate')) for r in rr),
                   'reviewDate_case_period': sum('2022-01-01' <= r.get('reviewDate', '') < '2026-07-01' for r in rr),
                   'ratings': dict(collections.Counter(r.get('rating') for r in rr))})
        ri |= ii
    out['tokopedia'] = {'files': ts, 'distinct_review_ids_combined': len(ri)}
    out['shopee'] = []
    for name in sorted(x for x in lookup if x.startswith('dataset_shopee') and x.endswith('.json')):
        d = load(name)
        out['shopee'].append({'file': name, 'rows': len(d),
                              'types': dict(collections.Counter(r.get('type') for r in d)),
                              'countries': dict(collections.Counter(r.get('country') for r in d))})
    if previous_zip is not None:
        with zipfile.ZipFile(previous_zip) as f:
            inf = f.infolist()
            h = hashlib.sha256()
            with previous_zip.open('rb') as src:
                for block in iter(lambda: src.read(1024 * 1024), b''):
                    h.update(block)
            out['previous_release'] = {
                'zip_bytes': previous_zip.stat().st_size, 'sha256': h.hexdigest(),
                'entries': len(inf), 'file_entries': sum(not x.is_dir() for x in inf),
                'extracted_bytes': sum(x.file_size for x in inf),
                'over_100MiB': [x.filename for x in inf if x.file_size > 100 * 1024**2],
                'over_45MiB': [{'path': x.filename, 'bytes': x.file_size} for x in inf if x.file_size > 45 * 1024**2],
                'zip_crc_error': f.testzip()}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input-dir', required=True, type=Path)
    ap.add_argument('--previous-zip', type=Path)
    ap.add_argument('--output', required=True, type=Path)
    args = ap.parse_args()
    out = audit(args.input_dir, args.previous_zip)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    expected = (out['x']['unique_combined'] == 12990 and
                out['x']['total_occurrences'] == 16165 and
                out['tiktok']['unique_cids'] == 2380 and
                out['tokopedia']['distinct_review_ids_combined'] == 266)
    print(json.dumps({'output': str(args.output), 'known_input_counts_match': expected}))
    raise SystemExit(0 if expected else 1)


if __name__ == '__main__':
    main()
