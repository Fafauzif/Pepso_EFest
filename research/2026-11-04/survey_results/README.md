# Survey results and strategy

This is a context overlay, not a standalone replacement for the existing 1.3GB research repository. Base commit: `a9c168a718f20b13097ae82488c77815958521d5`. Review file changes before committing; no remote push or publication has been performed.

## Read

1. analysis/Pepsodent_Survey_Analysis_and_Strategy.md — about 6,200 words, all results and strategy in English.
2. documents/Pepsodent_Executive_Summary_and_Appendices.docx — Indonesian three-page summary, 2 reference pages, 28 appendices. Working output, not submitted.
3. sources/references_apa.json and benchmark_sources.json — source metadata, mechanisms and transfer limits.
4. model/scenarios.json — authored outcomes, not forecasts.
5. data/aggregates — recomputed survey summaries and sensitivities.

## Reproduce

Use Python 3 with openpyxl,pandas,numpy,scipy,matplotlib and python-docx (for document source extraction only). No participant contact data is needed or produced by the following calculation.

`python scripts/analyze_survey.py /private/path/to/source.xlsx /local/output/aggregates`

Pass both input and output explicitly. The original workbook is intentionally absent. The script reads included records from CLEAN, never prints original IDs, contacts or follow-up codes; it produces aggregates. Preference codes 31 none, 12 named, 3 placeholder, 2 functional, 1 vague. Candidate tier labels are unverified keyword candidates, not transition findings. Automated product coding and manual source descriptions must keep their caveats.

`python model/model.py` regenerates scenarios.json beside the model. `python scripts/make_figures.py` regenerates publication charts under figures. Figure data are intentionally explicit fixed aggregate values; rerun analysis and update figure values before reusing charts with a new survey wave.

## Privacy and evidence boundaries

Only aggregates are included. No workbook, respondent-level manifest, response IDs, phone numbers, follow-up codes, contact exports or original screenshots are bundled. Input hashes identify the owner's originals without making them public. Existing repository confidentiality obligations still apply. The supplied Nexora document and unrelated reference personas/matrices were not copied into the strategy.

The current survey diagnoses purchase situations, not historical causation. There are no verified Premium→Basic histories, no 25–30 responses, no clinical endpoints or measured treatment effects. All 180-day financial scenarios lose the illustrative Rp40 million budget. The recommended decision is a gated low-cost test using existing channels, not a new app or rollout forecast.
