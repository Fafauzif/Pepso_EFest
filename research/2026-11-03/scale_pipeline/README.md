# Scalable public-research corpus store

This is a working standard-library Python pipeline, not a claim that a million eligible Indonesian switcher accounts exist. The actual snapshot and its source-specific selection limits remain authoritative. No Apify or paid service is required.

## What it does

`corpus_store.py` reads CSV, JSON arrays, JSONL and gzip-compressed JSONL. It stores records in SQLite with original payloads, source-file hashes and row locators. It exports gzip-compressed unified UTF-8 CSV and JSONL, plus gzip JSONL containing every observation and its complete original source payload. JSONL and gzip JSONL are streamed one row at a time; JSON arrays are loaded in memory, so upstream collectors should write JSONL for genuinely large corpora.

Identity comes from a supplied record ID or documented canonical identity hash. Some collectors use original platform IDs, while curated older excerpts use analyst-assigned locators; `identity_basis` does not falsely certify every supplied ID as an original platform identifier. Records lacking IDs use source URL, text, original date fields and type together as a fallback hash. Exact normalized text only flags possible copying; it never merges people. Every source occurrence is retained in `observations`, and payload differences for the same identity are preserved rather than silently overwriting the first record. Such differences can be metadata/provenance differences, not necessarily contradictory testimony.

The database has separate source versions. An unchanged completed file is skipped. An interrupted/capped ingest resumes after its last committed row. If a file changes, it becomes a new version and its observations are retained. Do not ingest a file still being written. A metadata/log JSON object is rejected rather than mistaken for consumer data. Empty/rating-only rows and deleted/removed markers are excluded from the written corpus and retained in a separate exclusion ledger, with original payloads. These expected exclusions are distinct from malformed-row ingestion errors.

## Commands

From the repository root, after collectors have finished writing:

```bash
python3 research/2026-11-03/scale_pipeline/scripts/corpus_store.py ingest research/2026-11-03/scale_discovery/clean/oresa_new_reviews.json --max-records 100000
python3 research/2026-11-03/scale_pipeline/scripts/corpus_store.py export
python3 research/2026-11-03/scale_pipeline/scripts/corpus_store.py stats
python3 -m unittest discover -s research/2026-11-03/scale_pipeline/tests -v
```

Pass several explicit canonical files to `ingest`; do not glob every raw response, duplicate CSV/JSON pair, discovery candidate or all-products metadata file. For a large retained corpus, increase the cap deliberately and retain the command and report. Default commit batches are 1,000 rows and the ingest cap is 100,000 attempted rows.

Default SQLite state is `work/corpus.sqlite`, a rebuildable intermediate excluded from release packaging. DELETE journaling and a single writer are used. `--db /absolute/path/corpus.sqlite` goes before the subcommand if a separate database is wanted. `export --out /absolute/path/export` selects a different destination. These scripts do not create or upload a repository commit, call Apify, or contact respondents.

## Canonical fields and evidence boundaries

The unified export retains platform identity, record type, original text/title, source URL, exact supplied content date where available, raw displayed date, collection time, product name, parent post, incentive status, scope and relevance status. Self-reported age is distinct from verified age. Verification flags default to false and are copied only when explicitly true. They are never inferred from wording or appearance.

Relative dates remain raw; no capture-minus-relative calculation silently manufactures publication dates. Supplied time scopes survive. Missing scope can be derived from a parseable supplied ISO content date: case historical is 1 January 2022 through 30 June 2026, current context follows that date. A date without a timezone is not changed into a UTC timestamp.

Original source payloads preserve additional fields and exact source locators. Canonical tables are an index over the evidence, not a replacement for raw source files. A globally sourced Amazon corpus remains an external historical comparison; it must not be pooled into Indonesian youth results. Incentivized sampling remains distinct from spontaneous public conversation. Discovery keyword matches remain candidates unless manually checked.

## Bounded collection utility

`fetch_targets.py` supplies a small reusable GET-only public-URL queue. It does not discover URLs or implement source-specific page/review parsing. Use collectors’ verified public endpoints and permit only needed hosts.

A target JSONL file has one object per URL, with `target_id` and `url`. Example invocation (supply your actual verified target file and source host):

```bash
python3 research/2026-11-03/scale_pipeline/scripts/fetch_targets.py targets.jsonl --allow-host SOURCE_HOST --out collected_pages --max-requests 20 --workers 2 --interval 1
```

This command is an architecture example; `SOURCE_HOST` is an explicit placeholder, not a runnable collection target. The utility defaults to two workers, one second between starts on a host, 20 requests total, one bounded retry, a 20-second request timeout and an eight-megabyte response ceiling. CLI caps allow at most four workers, at least half a second between host starts and two retries. Successful URLs are checkpointed by URL hash; already successful URLs are skipped on resume.

HTTP 401, 403 or 429 stops new requests to that host and records the reason; already in-flight requests may finish. It does not rotate accounts, use cookies, solve challenges or buy proxies. Retry-After is logged for diagnosis; the utility does not automatically resume a rate-limited host. Other 4xx are not retried. Transient 5xx/network failures get a bounded exponential delay. The target count includes retries, so a retry cannot exceed the request ceiling.

Before using any source at larger scale, inspect the collected sample and source requirements. Repeated “success” responses can still be empty, wrong-product or challenge pages. A network log is not a consumer corpus.

## Storage planning from actual data

`clean/collection_stats.json` reports actual unique platform records, source occurrences, payload differences, possible copied-text groups, source versions, exclusions, scope/incentive breakdowns, UTF-8 payload/text bytes and checkpointed SQLite bytes.

Its one-million-record figure is a **linear storage projection from this exact snapshot**. It does not estimate available relevant records, network throughput, eligibility or collection time. The estimate excludes raw HTML/media, extra export copies and backups. Index growth, record length and provenance duplication can change bytes per record materially. Gzip input size and uncompressed text size are different quantities.

A million broad global toothpaste reviews could improve general language discovery, but still fail to identify Indonesia, ages 18–30, previous Pepsodent Premium use or the next replenishment choice. Million-row convenience data do not solve that inference problem. Scale the evidence source that can change the decision, not just the number of rows.

## Tests and validation

The included tests check checkpoint resume and idempotence, identity deduplication while preserving differing payloads, copied-text flags without merging records, missing/deleted text handling, relative-date preservation, case-window classification, and stop-on-429 behavior. They use temporary local fixtures and mocked HTTP calls; no production source is called by tests.

Each final release should additionally reconcile exported counts, source paths, ID uniqueness, timestamp meanings and source-specific inclusion rules. The database's repeated-identity count includes legitimate repeated snapshots; it is not a measure of duplicate consumers or fraudulent reviews.
