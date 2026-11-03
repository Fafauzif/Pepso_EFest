# X data and analysis codebook

This folder integrates the four user-run Xquik exports. It does not make the X sample representative of Indonesia or the case's 18–30-year-old switchers. Source search settings are only known where supplied in a run log; the exports alone cannot reconstruct every query or result cap.

## Files and units

- `records.jsonl.gz`: 12,990 unique new-export post IDs, including replies. Every row retains exact original post text and source URL. CSV is a convenience copy; canonical JSON preserves null and Boolean distinctions.
- `occurrences.jsonl.gz`: 16,165 raw-export occurrences. Each points to original filename and zero-based JSON array index; SHA-256 fingerprints preserve text and full-payload comparison.
- `legacy_x_overlap.json`: compares the earlier six known-post records without pretending their excerpts are full text. One consumer post overlaps, five brand-owned posts add IDs. Combined X identity count is 12,995, not 12,996.
- `exact_text_groups.jsonl.gz`: candidate repetition groups after NFKC, whitespace collapse, and case folding. Distinct post IDs remain distinct records.
- `possible_template_groups.jsonl.gz`: additional possible copy groups after URLs, mentions, and numbers become placeholders. These groups may merge different offers or prices. They are not proof of automation, paid promotion, or common authorship.
- `review_selection.json`: frozen 100-record selection list, seed 20261103, retained after screening improvements so its false positives remain visible.
- `review_sample.json`: full text, source locators, and rule flags for that fixed sample.
- `evidence.jsonl` / `evidence.csv`: assistant close-reading annotations for 109 records: fixed 100 plus nine purposive follow-ups/counterexamples, including the now-full-text legacy-overlapping consumer story.
- `review_stats.json`: annotation units and qualitative codes. These codes describe selected texts, not consumers.
- `stats.json`: full-corpus descriptive counts; `context_and_versions.json`: available conversation roots and changing metadata.

Original exports are archived as `../raw/user_runs/<original-filename>.gz`. Decompression reproduces original JSON bytes; see the root archive register. Earlier six-post originals remain in `../../scale_tools/` from this folder (repository path `research/2026-11-03/scale_tools`). No raw bytes were modified by these scripts.

## Normalization and identity

Stable key is `x:<source_record_id>`. Lexicographic filename order here equals the observed chronological order of the four export filenames. Latest-export payload supplies the normalized view; first and latest locators and occurrence count remain available. No text changes were found for the same ID, but 1,758 IDs have more than one full-payload hash, for example because counters/profile metadata can differ. The occurrence ledger preserves those differences without attributing an unverified cause to each one.

`author_pseudonym` is a deterministic hash of the available source author ID, falling back to username only if absent. It is a source-account grouping key, not unique people, and not anonymous while original source URLs remain linkable. Normalized views omit full bios, avatars, and follower-profile payloads. Private raw archives retain original source data for provenance.

`created_at` is parsed from the actor's timestamp and stored in ISO UTC. Source date scope is `case_historical` for 1 January 2022 through 30 June 2026, `outside_case_period`, or `unknown_date`. All 12,990 new-export IDs fall within that source-date window. Actor language is retained literally: `in` is not silently renamed or treated as confirmed residency, and short/noisy posts can be mislabelled.

`conversation_id` is a conversation-root identifier, not a verified direct-parent edge. `parent_post_id` is null because no direct-parent field was available in these exports. The flag `conversation_root_in_collected_set` only establishes that an ID matching the source root is present. It does not mean the complete conversation is collected. Of 5,263 reply posts, 572 have a collected root ID; parent context is otherwise often absent.

## Relevance is a candidate screen

Mutually exclusive `relevance_status` rules, in precedence order, flag obvious transport matches without dental/brand-use anchors, likely figurative brand mentions without anchors, accessory candidates without brand matches, broad oralcare candidates, ambiguous brand matches, ambiguous ODOL matches, and unresolved other text. The broad oralcare screen includes any dental keyword or a brand string plus a use/purchase keyword. It knowingly admits jokes, news, nonoral hacks, and commerce. It is a retrieval aid, not a count of eligible consumer stories.

Additional `candidate_tags` are overlapping regular-expression matches defined verbatim in `build_x.py`. They cover household/payer language, price/promotion, availability/replenishment, sensory wording, need/benefit, repeat/fit, switching, first-person grammar, questions, retail URLs, commercial listings, accessories, transport, figurative mentions, possible advertising jingles/memes, and boycott words. A tag is not a semantic conclusion. Examples: `ibu` may occur in an ad jingle; `cocok` may describe a celebrity as an ad model; `habis` may mean after brushing; `ganti` may concern a toothbrush; `harga` may describe an accessory.

Expanded destination URLs from original entities are retained to reveal commercial links hidden behind t.co. A retail URL or shopping-cart emoji is a commercial cue, not proof of affiliate compensation. Statements such as “no aff” are not independently verified. The possible-jingle expression was introduced after close reading exposed repeated advertising-style Sensodyne ice-eating wording (exact official ad origin not independently verified). Its 41 flagged posts are candidates, not an exhaustive meme count.

`age_verified`, `geography_verified`, and `confirmed_pepsodent_premium_to_basic_switch` remain false for all new-export records. Self-described work, family, or school situations are useful narrative context but are not recruited/verified primary data. Generic Pepsodent is not mapped to Basic, and a switch from another brand to Pepsodent is not a Pepsodent Premium-to-Basic transition.

## Qualitative reading

Forty records were sampled uniformly from all 12,990 unique new-export IDs with Python's seeded PRNG. Sixty more were drawn randomly within six purposive keyword screens: household/payer, switching, repeat/fit, sensory, availability, and price. The original screen required broad oralcare anchors and first-person wording and excluded then-detected retail/boycott markers. The selections were frozen before expanded-URL, accessory, and jingle QA improved the screen. This prevents retroactively removing inconvenient false positives from the reviewed sample.

Nine supplementary records were selected explicitly for hypothesis testing or earlier-source overlap. They are not random. All 109 were actually read in source-text form; annotations separate reported experience, intentions, advice, commercial copy, jingles, jokes, fiction, food comparisons, alternative/nonoral uses, shared purchasing, counterexamples, and unclear context. Their original full text and exact source locators are retained with analyst interpretation and limitations. The annotator is an assistant, not a respondent or independent human validator. A separate QA agent reviewed source matching and a subset of judgments; this tests consistency rather than establishing ground truth.

Do not compute a population percentage from the 109 annotations or compare the six purposive strata as demand shares. Even the random 40 describe only this search-selected exported corpus, not the platform population. Full-corpus keyword frequencies are likewise retrieval properties.

## Rebuild

Run from the repository root, using only Python's standard library:

```bash
python research/2026-11-03/closure/x/build_x.py
python research/2026-11-03/closure/x/annotate_review.py
python research/2026-11-03/closure/x/verify_x.py
```

The first command locates packaged original JSON `.gz` files, or accepts `--input-dir PATH` for the original attachment directory. It does not access X, incur charges, or refresh source data. The fixed review selection and interpretation notes are versioned analyst inputs, not newly generated model judgments on each rebuild.
