# Independent QA: input audit and analytical risks

Checked 3 November 2026. This audit recomputes counts directly from the unchanged uploaded JSONs and checks the previous release ZIP. It does not yet certify the new analysis or final archive, which were still being built at this checkpoint.

## Input reconciliation

The machine-readable result is [independent_input_audit.json](independent_input_audit.json). Its input hashes identify the bytes examined.

* X: 16,165 exported source occurrences, 12,990 distinct post IDs. The fourth export adds 4,112 IDs and repeats 2,528 already seen. No blank text fields in these exports. All exported post timestamps are within 2022–June 2026, but this does not establish Indonesia residence, age, actual use, or category relevance.
* TikTok: 2,380 distinct comment IDs, 18 submitted video contexts, 699 replies, eight blank text fields. There are 1,649 comments dated 2022–June 2026. The remainder are older or later context, not silently discarded. Eight videos returned exactly 180 comments; this demonstrates an input cap was reached, not full thread coverage.
* Tokopedia: latest 266 distinct review IDs include all 43 pilot IDs. The latest export contains 263 nonempty review texts, 18 product rows, and one notice. Across both files there are still 266 distinct review IDs, not 309. Date strings disagree between `reviewTime` and `reviewDate` in **186 of the 198 latest reviews with both fields present**, while **68 have no reviewTime**. The pilot has 40 disagreements among 43 reviews. Preserve fields and uncertainty; a relative date conversion must not be treated as an exact observed date. Only 153 latest `reviewDate` strings fall in 2022–June 2026; this eligibility depends on that source field, not independent date verification. An initial QA calculation incorrectly counted missing reviewTime as a disagreement, yielding 254; that calculation was corrected before release without changing sources.
* Shopee: one targeted file has two error records and zero reviews. Another has 100 Singapore UGREEN electronics reviews. Both must be retained as audit inputs but excluded from toothpaste analysis. The scanned-shop counts in errors are not delivered records.

## What the previous release actually contains

The earlier archive has 1,949 file entries and 615,579,784 uncompressed bytes. ZIP CRC passes. Its actual size is 402,496,490 bytes and SHA-256 is `d450d45454b3bcdc263cfdd7044675fbd3d41b7e3c9f105b075440dd76b78b85`.

No earlier archive member reaches 100 MiB. Five members exceed the preferred new 45 MiB target. If their paths are replaced with chunks, the release must include an explicit reconstruction map, original byte count/hash, and all required parts; ordinary extraction alone does not reconstruct a byte-split gzip stream. Existing loaders or documentation must explain portable access. Dropping these earlier files without equivalent content would violate the user's completeness requirement.

The earlier 298,846-record integrated store includes 286,706 international Amazon candidates. The adult/general toothpaste title candidate subset is not the same as verified adult users. Its metadata screening has documented false positives/negatives. The prior independent QA reports zero age-verified records and zero confirmed target Premium-to-Basic switchers.

## Findings that would mislead if left unqualified

| Risky claim | Required correction |
|---|---|
| Millions of collected relevant toothpaste reviews | Millions were screened upstream; retained candidate and written-record counts are separate |
| 266 new reviews after the pilot | 266 unique total, 223 additional IDs |
| 263 usable Tokopedia reviews | 263 merely nonempty; emoji, generic praise, spray results, mismatched content, and delivery-only text still need flags |
| Five-star ratings demonstrate benefit or retention | Before-use ratings and generic service praise are observable; explicit experience and repurchase need separate coding |
| Low stars imply toothpaste dissatisfaction | In the pilot, low-rating complaints concern delivery/packing |
| TikTok's 18 videos describe one product or creator type | Video-level context must be established from retained material, not guessed from handles |
| A comment mentioning parents proves an 18–30 switcher | It supports a household mechanism; age, actual sequence, and target eligibility remain unverified |
| Current listings prove H1 2026 local stock | Listing, historical offer, shopper-reported difficulty, and verified shelf stock are different evidence |
| Keyword or thematic frequencies estimate consumers | These are selected-source text frequencies, not people, representative prevalence, sales, or causal effects |
| Same text establishes bot activity | Copying/templating can be flagged; source identity and intent require additional evidence |
| No Apify runs took place | Assistant did not execute paid collection, but user executed and supplied Apify exports; current-state claims must distinguish this |
| All context is preserved verbatim | The available source files and substantive visible-session handoff can be preserved; unavailable PDFs/messages must remain identified as unavailable |

## Release gates still to check

1. Exact source hashes or documented byte-perfect restoration for compressed originals.
2. Raw locator consistency across annotations and archived inputs.
3. Quotation fidelity and no unsupported certainty in interpretations.
4. Reconciled platform IDs, occurrences, nonempty text counts, eligible subsets, and sampling denominators.
5. Distinct previous-release, historical, new-analysis, and currently accepted context documents.
6. Every earlier archive member retained, intentionally updated, or replaced by a verifiable lossless representation.
7. No credentials, database caches, `.git`, nested delivery ZIP, or file at/above GitHub's hard limit.
8. Fresh extraction/readability and documented build/validation commands.
9. Final Filebin upload size/hash and actual expiry, not an assumed duration.

This is a preliminary audit. A final QA document should identify which gates actually passed and which limits remain.
