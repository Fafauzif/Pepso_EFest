# Independent package QA and final verification boundary

3 November 2026. Checked the preliminary portable stage at `final_release_stage/Pepso_EFest` independently of the packaging implementation. The final archive may contain additional QA files, so the stage snapshot's file count is not the final delivery count.

## Passed at the inspected stage

* Every one of the earlier ZIP's **1,949 members** is accounted for: **1,933 byte-identical**, **11 intentionally updated**, and **five represented by exact lossless byte parts**. The changed documents are root instructions/manifests, current context/source register, and derived inventory/validation documents. Original raw inputs and original master are not silently changed.
* All **12 part files** pass their individual hashes. Concatenating the parts for each of the five logical files produces exactly the prior ZIP member's byte count and SHA-256. Reconstruction was verified by streaming, without creating oversized tracked files.
* No staged file is over 45 MiB or at/above 100 MiB. The largest at that checkpoint is **37,488,217 bytes**. No `.git`, work database, cache, environment directory, or Windows-invalid path name was found in the staged file inventory.
* The new written master remains usable without legacy-file restoration. The stage query tool returned a source-linked TikTok record through the portable shards.
* `python scripts/verify_final_release.py --skip-manifest` passed on the inspected stage: 11 archived inputs, 314,476 unique written keys, exact platform counts, and five legacy logical files verified. This invocation deliberately did **not** certify the full manifest.
* The inline Markdown scanner examined 230 local link targets. Three unresolved targets occur only in preserved source/history snapshots: two upstream project-local links in the reverse-api-engineer README snapshot, and one original root-relative link in BEFORE_CLOSURE_README.md. No active new-report/start-here local links were unresolved in that scan. These historical snapshots should retain their original source semantics rather than be silently rewritten.
* A limited high-specificity credential scan found no credential filenames, Apify-token, GitHub-token, or private-key blocks. OpenAI-like substring matches were embedded in ordinary words/URL/HTML slugs such as gsk, Crozdesk and run-task; there were zero standalone key-like boundary matches. No matched value was exposed in QA output. This is a limited check, not a guarantee against every possible credential format.

Machine-readable details: stage_package_check.json, stage_markdown_link_scan.json, stage_secret_pattern_scan.json, and stage_secret_pattern_review.json. Original/decompressed input hashes and source-text checks are documented separately in ANALYSIS_QA.md.

## Resolved build-order issue and final gate

The first full-manifest check on the preliminary stage failed because the packaging owner was concurrently running a legacy inventory validator that **writes** DATA_INVENTORY.json and VALIDATION.md. This was a generated-document timing issue, not evidence of altered raw sources. The correct build order is:

1. Run mutating rebuilds/legacy validators before release generation.
2. Build the final stage, coverage map, and fresh manifest after all content is frozen.
3. Run only read-only verification against that final stage/archive.

The packaging owner confirmed this order will be used for the final rebuild. The new installation guidance was also corrected to Python **3.11+**, because the new verification/restore helpers use hashlib.file_digest; historical Python 3.10 guidance applies to the earlier keyword-only scripts.

The root integration owner separately recorded a fresh offline rebuild in offline_rebuild_check.json: restore the prior integrated input from parts, rebuild the master, and compare all 16 shard byte sizes/hashes. That result is the owner's reported execution log; it should be read alongside this independent source-text/shard audit, not represented as another independent implementation.

**Final-manifest and ZIP CRC/hash verification must be recorded after the last rebuild.** The Filebin size/hash/expiry receipt necessarily follows creation of the ZIP and is a transfer-level check. This document does not claim to have inspected an archive or upload that did not yet exist at the QA checkpoint.

## Analytical limits remain after technical checks pass

Checksums establish integrity and reproducibility, not truth. The corpus is selected, mixes applicability and incentive strata, contains irrelevant/contextual candidates, and authenticates no target-age Pepsodent Premium-to-Basic sequence. Qualitative evidence is assistant-reviewed and selected; it is not a representative consumer survey or a validated causal model. See ANALYSIS_QA.md for the corrected date accounting, quotation checks, and interpretation boundaries.
