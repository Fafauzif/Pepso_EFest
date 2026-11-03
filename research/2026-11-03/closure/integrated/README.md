# Portable integrated written-record inventory

Read INVENTORY.json for source-specific counts and the shard index. Every records-*.jsonl.gz is independently readable gzip JSON Lines, with at most 20,000 records. There are **314,476 retained written platform records across all retained scopes**, not 314,476 consumers or eligible Indonesian toothpaste experiences. Source observations, excluded blank/rating-only records, and provenance remain in the source folders and raw archives.

The earlier298,846 store is combined with12,990newX IDs,2,372nonblankTikTok comments,263nonblankTokopedia records and5earliernonoverlappingbrandX excerpts. One earlierconsumerXstory overlaps the new exports and is represented once. Sprays, logistics praise, uncertain relevance, marketing and international/adjacent candidates are retained with source-specific flags, not silently promoted into consumer evidence. The source-specific candidate eligibility subsets are the place to begin an analysis.

## Read and rebuild

New scripts require Python 3.11+ and standard-library modules. From repository root:

```bash
python scripts/query_corpus.py --platform tiktok --contains sensodyne --limit 5
python scripts/verify_final_release.py
```

For an optional full rebuild of this inventory, first restore the old integrated input (the new master works without restoring it):

```bash
python scripts/restore_large_files.py --only research/2026-11-03/scale_pipeline/clean/export/records.jsonl.gz
python research/2026-11-03/closure/scripts/build_integrated.py
```

The restore is local and Git-ignored; do not force-add large restored exports or work databases. Rebuilding derived files invalidates packaged manifests until a new release is produced. User raw archives rebuild each new source dataset using that source's scripts; the closure raw upload archiver is only needed when adding external new uploads.

## Fields and interpretation

Original source-specific normalized fields are retained. Common fields include record_key, platform, source_record_id, source_url, text_original, record_type and source_specific_dataset. The latter points to a legacy logical file where that file is represented by lossless parts; its bytes can be restored using the command above. Other fields are intentionally not forced into false agreement.

unified_scope preserves the source-specific scope label. calendar_period_jakarta is an additional calendar bin derived from the available source date in Asia/Jakarta. It is **not** eligibility for the case. Amazon remains international context regardless of its date. Tokopedia uses an unverified date field, so its calendar bins remain provisional. The original date evidence and quality flags stay in source files.

screening_tags are transparent lexical candidates defined in RULE_PATTERNS.json. Counts in screening_counts.csv overlap, include irrelevant contexts, and are not validated behaviour frequencies, sentiment, sales, or population prevalence. For example 'ganti' may refer to a toothbrush, 'family' may appear in advertising, and 'harga' does not establish price pressure. Qualitative annotations in the platform folders are separately selected and interpreted, not inferred from tags alone.

exact_text_groups.jsonl.gz groups identical casefolded, whitespace-normalized text by fingerprint. Shared text is not proof of the same person or a bot. Even cross-platform repeats can be generic short praise. The grouping is an information-concentration diagnostic, not automatic identity merging.

age_verified and premium_to_basic_verified remain false. Source-provided author pseudonyms are observational handles, not known people; no cross-platform identity linkage is attempted. Texts and URLs may themselves be searchable. The repository is intended for the private team.

Run-level source occurrences retain the metadata needed to trace a specific version to its raw file/row. The original JSON uploads are .json.gz archives; decompressing reproduces the original upload bytes exactly. See ../raw/UPLOAD_REGISTER.json. The old source corpus provenance remains in its retained source datasets and observations export, including where represented as legacy parts.
