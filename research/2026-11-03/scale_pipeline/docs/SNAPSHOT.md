# Final aggregate snapshot: 3 November 2026

The pipeline reconciles eight finalized canonical source files into **298,846 unique supplied-ID written records**. This is a database identity count, not a count of unique people or independently verified product experiences.

| Source family | Canonical written records | Main interpretation limit |
|---|---:|---|
| Amazon external historical dataset | 286,706 | Broad title-matched context; country not Indonesia-verified; includes explicitly separated other product types |
| Watsons Indonesia source | 7,419 | Syndication/independence and reviewer country not established; 1 written record concerns adjacent whitening serum |
| ORESA campaigns | 2,228 | Sampling/cashback/review-task selection; incentive status retained per campaign |
| TryandReview | 1,423 | 1,237 explicit free-product disclosures; source selection and self-reported profiles |
| Lazada Indonesia source | 681 | Product/fulfilment mixed text; purchaser age and actual prior tier unknown |
| Reddit public archive | 389 | 266 keyword candidates and 123 dental-thread context records, not 389 confirmed switchers |
| Total | 298,846 | Populations and source mechanisms must remain separate |

The Indonesia-targeted/source-specific rows total **12,140**, including the Reddit context rows and one Watsons adjacent serum row. Calling all of these Indonesian youth toothpaste buyers would be incorrect. No age or Premium-to-Basic transition was independently verified.

Amazon written records divide into **196,872 adult-human-toothpaste title candidates**, 35,936 adjacent powder/alternative, 30,698 child/infant, 20,931 accessory/container, 1,928 brand-matched unresolved type, and 341 pet/nonhuman. These are rule-based product-title categories, not manual formulation verification. The whole 286,706 must not be presented as adult toothpaste reviews.

There are **301,526 source written occurrences**, including 2,680 repeated supplied-identity occurrences whose payload differences are preserved. Differences may be source metadata or category context; they are not automatically contradictory reviews. There are 4,241 possible copied-text groups, which are only normalized-string flags. Generic repeated wording does not prove copying or fraud and does not identify a person.

**2,970 nontext rows** are retained separately: 2,772 Watsons rating-only/blank rows and 198 Amazon Health-and-Household rows without substantive text. They remain in the original canonical files and the excluded-row export. They do not enter the written-text corpus. There were zero malformed-row ingestion errors.

## What was validated

The final DELETE-journal SQLite database passed `PRAGMA integrity_check`. Gzip JSONL and CSV exports were fully parsed, with record counts reconciled against the store. Every individual portable export is below 90,000,000 bytes:

| Export | Rows | File bytes |
|---|---:|---:|
| `records.jsonl.gz` | 298,846 | 67,676,612 |
| `records.csv.gz` | 298,846 | 63,633,349 |
| `observations.jsonl.gz` | 301,526 | 85,710,074 |
| `excluded_nontext_rows.jsonl.gz` | 2,970 | 145,065 |

Source-file versions and hashes are exported separately. The earlier failed derived database was removed from deliverable paths and rebuilt from unchanged canonical source inputs; the precise failure cause was not established. No original evidence was lost or edited to repair it. The working SQLite database is a rebuildable intermediate excluded from release packaging and Git.

## What a million records would mean for storage

The observed snapshot contains 393,340,003 UTF-8 bytes of original observation payloads and 52,291,794 UTF-8 bytes of canonical review/comment text. Its checkpointed SQLite file is 1,058,160,640 bytes. Linear extrapolation to a million canonical records gives approximately **3.54 GB SQLite**, **1.30 GB observation payloads** and **175 MB text**, under this exact source/record mix. These estimates exclude original HTML/media, backups and extra export copies; index structure and record lengths can change at scale.

The compressed canonical JSONL is about 226 bytes per record in this snapshot, or roughly 226 MB per million under the same compression/source mix. That is a storage calculation, not evidence that another million eligible records exist and not a collection-time forecast. The dataset remains insufficient to estimate national youth switching prevalence, regardless of row count.

## Rebuilding

From the repository root:

```bash
python3 research/2026-11-03/scale_pipeline/scripts/build_snapshot.py --max-records 1000000 --export
```

The command verifies the eight source paths listed in `docs/snapshot_inputs.json`, resumes unchanged inputs, preserves provenance, checks SQLite integrity and optionally exports compressed data. No downloads, Apify jobs or package installs occur. Keep `work/` out of release archives and Git; all needed source inputs, scripts, manifests and portable exports remain available.
