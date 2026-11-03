# TryandReview expansion — final collection checkpoint

**Completed:**3 November2026. **Cost:**$0. **Apify runs:**0. **Status:**all three targeted public histories enumerated, with distinct IDs reconciling to the product pages' displayed counts.

| Product | Source-displayed reviews | Distinct IDs collected | Public review pages | Explicit free-product cards | Incentive not established |
|---|---:|---:|---:|---:|---:|
| Pepsodent Pasta Gigi Pencegah Gigi Berlubang |646|646|130|599|47|
| Pepsodent Complete8 Multi Protection |332|332|67|293|39|
| Closeup White Attraction Natural Smile |445|445|89|345|100|
| **Total** |**1,423**|**1,423**|**286**|**1,237**|**186**|

The initial run already contained100 TryandReview records. This expansion is a **superset**, adding **1,323 distinct record IDs**, not1,423 additional records. Prefer the corrected expansion text on duplicate IDs and retain the original baseline as lineage.

This is source coverage, not a representative sample or unique-person count. All cards display Indonesia in the profile-country field; residence and purchase demographics are unverified.379 profiles currently self-report ages18–30, but this is not verified age at historical purchase, and none are confirmed Premium-to-Basic switchers. Individual ratings can be fractional; do not convert to integer stars. A large free-product majority means recruitment and incentive bias remain central despite the fuller coverage.

## What the expansion changes analytically

The earlier100-record newest-page sample substantially underrepresented the available histories. The complete enumeration supplies more varied sensory, household, repeat and expectation narratives. It also exposes why more rows do not automatically solve inference:

- `TAR-117079` rates Closeup4.7 while reporting no visible whitening change after more than a month against a two-week promise. A favorable total score does not establish success on every benefit.
- `TAR-160280` values flavor, freshness and tube design while saying they did not closely attend to whitening. This challenges a universal “visible whitening is the decisive outcome” story.
- `TAR-160711` distinguishes freshness/breath benefit from limited tooth-color change.
- `TAR-254032` describes modest visible change but four repurchases and attractive packaging. The card marks free product; the paid-price history remains unverified.
- `TAR-161537` reports a visible result in two weeks, a positive counterexample to universal non-performance claims. This is a subjective account, not standardized clinical efficacy measurement.
- `TAR-739586` combines a low numeric rating (2.0) with positive household-stockpiling prose. Ratings alone are unsafe sentiment labels.

These nine selected manually read records are in `clean/selected_manual_evidence.json`; they are a teaching subset, not a hand-coded prevalence analysis. Clinical assertions in consumer text remain unverified.

## Access and completeness checks

The public page form and `show.js` disclose ordinary GET pagination. Four workers retrieved the286 five-row pages, reusing the original first20 pages rather than fetching duplicates. Four Closeup pages timed out together; one bounded retry recovered them. No429 was observed. Original timeout metadata is retained in `docs/original_timeout_attempts.json`. All target page sets and distinct ID counts now reconcile.

Live publication/deletion and cached pages prevent treating this as a perfectly frozen universe. Reconciliation supports enumeration of the displayed source, not completeness of all consumer opinion or every review ever submitted.

Two source-format issues were corrected from unchanged raw bytes: HTML fragments require explicit UTF-8 decoding, and individual source ratings can be decimals. The authoritative `rebuild_from_cache.py` handles both. Early parse failures did not lose raw responses and were recovered without additional retrieval. All286 raw hashes, source-ID joins, file locators, CSV/JSON row counts, UTF-8 parser labels and record-ID uniqueness were checked.

## Relevant source-size boundary

The Indonesia oral-care catalogue exposed these three substantive histories plus two Sensodyne products with only two reviews each. Those four Sensodyne reviews are discovery context, not included in this expansion. Enzim/Colgate-ID generic brand pages did not establish a further relevant local corpus. A larger Malaysia Colgate inventory was discovered but not bulk-collected because geographic mismatch cannot substitute for Indonesian case evidence.

The request to scale cannot turn this source's approximately1.4k relevant local records into millions. Larger external datasets may serve separate adjacent-market questions, with geography, period and product labels preserved.

## Canonical integration files

- `clean/tryandreview_reviews.json` and `.csv`:1,423 corrected unique review IDs.
- `source_register.json`:286 public page sources with hashes and source IDs.
- `targets.json`:three product-page totals and discovery evidence.
- `quality_report.json`:coverage reconciliation, ratings and incentive counts.
- `docs/METHOD.md`:methods, caveats, transformations and resume instructions.
- `scripts/collect_full_tar.py`:bounded resumable collection.
- `scripts/rebuild_from_cache.py`:offline authoritative rebuild.
- `DONE.json`:stable completion marker.

Do not add the baseline100 to this1,423 again. No source data in the earlier workstream were modified by this expansion.
