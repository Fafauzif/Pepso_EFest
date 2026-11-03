# Literature data package

This directory contains newly collected external literature evidence, not team interview/survey microdata. It preserves the original case pack and keyword dataset unchanged.

## Files

- `findings.md`: decision-focused teaching and interpretation.
- `source_register.json`: study IDs LIT001–LIT025, DOI links and raw-file/section locators.
- `clean/reviewed_evidence.csv` and `.json`:25 retained studies with analyst extraction, read level, transfer limits and funding-review status.
- `clean/candidates_all_unique.json`:148 deduplicated discovery metadata records. Most are not deeply appraised.
- `clean/screening_log.json`:retained vs discovery-only status. This is not independent systematic-review screening.
- `clean/jakarta_published_channel_counts.csv`:12 selected aggregate rows transcribed from published Table2; no individual respondent data.
- `raw/`:original public API responses, three open fulltext XML files, the Jakarta article PDF/extraction, selected web-tool responses and access logs.
- `scripts/`:public HTTP collection and curation scripts; no credentials, paid service or Apify dependency.
- `quality_report.json`:coverage counts and cost.

## Data dictionary

`study_id` is the local stable identifier;`doi` identifies the publication;`read_level=fulltext` means relevant fulltext sections were reviewed, not every reference or every table independently audited. `finding_paraphrase`, `applicability_limit` and `funding_review` are analyst annotations. Missing funding information means unknown, not zero funding. `is_post_case_publication` isolates the August2026 foam paper. Metadata dates and version conventions vary by provider; citation year does not establish historical availability of a marketed SKU.

The discovery pool deduplicates DOI where available, otherwise title. It can retain preprints or alternative records under distinct identifiers. It is a query-limited discovery pool, not an exhaustive bibliography. Initial429 responses are recorded; targeted follow-ups succeeded without paid access.

`jakarta_published_channel_counts.csv` reports published counts by dimension/category; do not add dimensions together because they describe the same sample. Do not interpret the sample as nationally representative, as exactly18–30, or as premium-to-basic switchers. The article uses non-probability convenience recruitment. The source's abstract and broad interpretations must be checked against its published tables.

## Reproduction

Run `python3 scripts/collect_literature.py`, then `python3 scripts/collect_targeted.py` and `python3 scripts/curate_evidence.py` from this directory or using their full paths. Current web results may change; scripts preserve the returned original payloads and access failures. The two targeted choice/Neslin follow-ups are logged in `raw/target_access_log.json`; their URLs can be rerun manually. Literature interpretation and manual published-table transcription remain analyst-reviewed transformations and are not claimed to be fully automated.

The locally saved XML articles carry source license information inside each payload. The Jakarta article is publicly downloadable from the journal; redistribution rights should be checked before public release. Keep this research within the team's intended access. Bibliographic records and links are sufficient if a later public package excludes fulltext copies.
