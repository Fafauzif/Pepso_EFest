# X user-run exports: cleaned corpus and close reading

Start with [FINDINGS.md](FINDINGS.md), then [CODEBOOK.md](CODEBOOK.md) and [QA.md](QA.md). This folder adds the four user-run X exports to the research handoff without pooling search-selected posts into population evidence.

## Verified counts

| Unit | Count |
|---|---:|
| Raw-export occurrences | 16,165 |
| Unique IDs in the four exports | 12,990 |
| Repeated-ID occurrences | 3,175 |
| Earlier known-post IDs | 6 |
| Earlier/new overlapping IDs | 1 |
| Combined distinct X IDs | 12,995 |
| Actual close-read annotations | 109 |
| Verified target-age / Premium-to-Basic switcher records | 0 / 0 |

The five net additional earlier IDs are brand-owned. The overlapping consumer story is category downtrading from imported toothpaste to unspecified Pepsodent; it is not confirmed Pepsodent Premium-to-Basic switching.

## Data

- `records.jsonl.gz` and `records.csv.gz`: normalized unique new-export records, with rule-based candidate tags and de-identified account grouping keys.
- `occurrences.jsonl.gz`: exact source-file/index provenance across all four exports.
- `evidence.jsonl` and `evidence.csv`: 109 source-linked assistant close-reading notes, including random/purposive selection labels and interpretation limits.
- `review_selection.json`: fixed 100-record selection; `review_sample.json` includes full source text.
- `legacy_x_overlap.json`: earlier six-post overlap and original earlier metadata/excerpt.
- `stats.json`, `review_stats.json`, and `context_and_versions.json`: denominators, repetition, review units, and conversation limitations.
- Duplicate/template files: audit candidates, not presumed independent consumers or automatic deletion decisions.

The original byte-preserving archives are in [../raw/user_runs](../raw/user_runs). This folder's scripts can read `.json.gz` archives directly.

## Offline rebuild

```bash
python research/2026-11-03/closure/x/build_x.py
python research/2026-11-03/closure/x/annotate_review.py
python research/2026-11-03/closure/x/verify_x.py
```

All commands run from repository root, require only standard-library Python, and make no network or paid-tool calls. The qualitative notes are versioned analyst inputs, not newly inferred annotations on rebuild.
