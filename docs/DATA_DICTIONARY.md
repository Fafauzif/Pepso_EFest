# Data dictionary

CSV empty cells represent null; JSON uses null. Lists are JSON arrays inside CSV cells and native arrays in JSON. UTF-8 CSVs use comma delimiters and quoted cells as needed.

| Fields | Meaning |
|---|---|
| observation_id | Stable source ID + result row ordinal for this raw snapshot |
| keyword / keyword_raw | Normalized key / original copied phrase |
| intent_raw / intents | Copied intent label(s), parsed list. Semrush classification, not user testimony |
| volume_raw / search_volume | Copied token / parsed estimated monthly search count; header inference caveat applies to tab files |
| volume_status | positive, zero, blank, not_available; preserve distinctions |
| kd_raw / kd_percent | Raw token / parsed SEO difficulty 0-100 |
| cpc_raw / cpc_value | Raw token / parsed reported CPC; currency separately identified |
| cpc_currency | IDR only if header confirmed it; null otherwise |
| cpc_analysis_value | CPC available for analysis only if currency confirmed and numeric outlier rule not triggered |
| serp_features_raw / serp_features | Copied feature labels / parsed list; null raw and empty list when not copied |
| serp_capture_status | copied or not_copied |
| trend_raw / trend_capture_status | Explicit n/a where shown; otherwise no usable copied trend. No recovered monthly series |
| updated_raw | Relative source freshness label, not capture timestamp |
| source_line_start / source_line_end | Inclusive 1-based raw source logical line span |
| country_requested | Indonesia per user instruction |
| country_verified_in_capture | false in this release; requested country not visibly confirmed |
| retrieval_date | null; exact capture timestamp unknown |
| packaged_date | 2026-11-03; packaging date only |
| source_id / source_file / layout | Source provenance, repo-relative raw path and parser layout |
| brands | Literal brand matches; multiple matches allowed; ambiguity caveats apply |
| theme_tags | Multi-label rule-based analyst tags; code contains full matching rules |
| quality_flags | Inferred headers, currency uncertainty, numeric outlier, ambiguous generic term, or missing intent |
| observation_ids / observation_count | Unique view only: underlying observations and their count |

## Files

- keyword_observations.csv/json: complete observations with raw and parsed values.
- keywords_unique.csv/json: one row per conflict-free normalized key, with observation references.
- duplicate_conflicts.json: unresolved differing metrics for the same key (empty in this release).
- quality_flags.csv: every flagged observation and reason.

No field represents sales, market share, unique people, clinical efficacy, age or sentiment.
