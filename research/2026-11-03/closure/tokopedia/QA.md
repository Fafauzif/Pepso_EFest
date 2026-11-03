# Tokopedia/Shopee QA — completed

Run on 3 November 2026 with Python standard library. Commands:

```bash
python research/2026-11-03/closure/tokopedia/clean_analyze.py
python research/2026-11-03/closure/tokopedia/validate.py
```

The first local run used `--input-dir /workspace/scratch/70458c8119f6/upload`; portable release inputs are the original `.json.gz` exports under `../raw/user_runs/`.

## Verified

- Parsed all four source files; source hashes, byte counts, row counts and type counts retained in stats.json.
- 335 Tokopedia rows =309 review occurrences +24 product observations +2 notices.
- 309 review occurrences =266 distinct platform/ID keys +43 repeated occurrences.
- All 43 pilot IDs occur in the main export. 223 IDs are additional beyond pilot.
- No duplicate canonical record keys; 38 keys have different full payloads across exports. Differences are reviewTime (35) and signed reviewImages URLs (11), with overlap; no changed text/rating on the shared IDs.
- 263 nonempty canonical text fields; 3 blank. These are not 263 useful experience narratives.
- Product scopes reconcile:260 toothpaste-title candidates +5 gimmick-title candidate reviews +1 whitening-spray review =266.
- Broad eligible written-paste candidate subset256 excludes blank, spray, gimmick-title candidates and one possible body-odour mismatch. This flag deliberately retains generic/symbolic text; it is not a close-reading relevance verdict.
- 198 records have both dates,186 disagree by calendar day,68 lack reviewTime,0 lack reviewDate. Missing values are not counted as conflicts.
- Canonical CSV and JSONL counts agree; every canonical exact text and rating matches its immutable source locator.
- All309 original review payloads match the JSON arrays at stored zero-based indexes.
- 85 annotations have distinct IDs and exact source texts. Forty belong to seeded random calibration;45 are purposive. No age/switcher verification flags are true.
- 102 Shopee audit rows =2 error records +100 wrong-target Singapore UGREEN reviews. Zero entered oral-care analysis.
- Gzip/JSON parsing passed for generated outputs. Rebuild succeeds without external packages/network.

## What remains uncertain

- Marketplace authenticity, true buyer identity, age, residence, actual transactions, selected variant/pack mass, and clinical claims are unverified.
- reviewDate is not independently validated and reviewTime appears partly estimated; provisional case-period filters do not adjudicate chronology.
- Search rank and recent-review retrieval create selected coverage. Missing reviews are not proof of no demand or no reviews; no marketplace-wide completeness claim.
- Lexical tags and the small generic lexicon are diagnostic rules with false positives and false negatives. The 206 contextual-text candidates include many low-information records.
- Assistant annotations are interpretive, not human-fieldwork validation. The purposive examples must not be used to estimate prevalence.
- Product cards are current offered contexts, not paid prices or verified stock. Title-based price-per-100g calculations remain conditional.
- Actor billing notices are not independent statements of total account charges.

Independent team QA subsequently verified all85annotation ID/text matches and closely checked20selected annotations; see the separate closure/qa report. Such checking supports internal consistency, not external truth or population validity.
