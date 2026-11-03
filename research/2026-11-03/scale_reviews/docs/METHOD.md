# Expanded TryandReview public histories: collection method

This expansion enumerates public review pagination exposed by the source site's own product-page form and JavaScript. No paid actor, login, browser session, cookie import, interaction with reviewers, or private API was used. Public product pages display review totals; their `filtersReviewsForm` exposes `/id/reviews/{product_id}` and the public `show.js` invokes GET with `page`. Requests used four concurrent workers, a short per-request pause, bounded timeouts, immediate halt flag on HTTP429, and per-page checkpoints. Existing first-ten-page baseline captures were reused rather than downloaded again.

The Indonesia oral-care category inventory and Sensodyne brand discovery exposed five toothpaste product pages: Pepsodent Basic, Pepsodent Complete8 Multi Protection, Closeup White Attraction Natural Smile, and two Sensodyne variants with two reviews each. The main scale run targets the first three, with displayed totals646,332,445 respectively. A Malaysia Colgate inventory was discovered but not collected, since geography-mismatched bulk would not substitute for Indonesian diagnosis. The unsuccessful Enzim/Colgate-ID generic brand routes did not establish a relevant corpus. Discovery HTML and search outputs are retained as discovery, never counted as consumer records.

## Technical transformations and corrections

Raw public responses are unchanged. Review IDs stay strings with `TAR-` prefix. Individual ratings are numeric and may be fractional (for example4.3), so do not coerce them to integer or treat every individual review as an integer-star observation. An early integer parser rejected affected pages; their raw responses had already been saved. `rebuild_from_cache.py` recovers those pages without additional requests and preserves the original parse-error messages in source metadata.

Review fragments lack HTML charset metadata. Parsing raw bytes using lxml's fallback introduced mojibake into some early parsed text. The authoritative rebuild explicitly decodes the original bytes as UTF-8 before DOM parsing. This is a documented decoding correction from preserved raw bytes, not a guessed textual repair. The scale corpus supersedes baseline TryandReview text for duplicate platform IDs; retain both source snapshots as lineage but count each review ID once.

Original relative review-date and usage-month labels remain raw. They are not converted to precise review timestamps, and cannot independently establish whether a record falls within the case period. Current profile ages/country are self-reported, not verified demographics at the historical purchase. Literal source age0 remains a flagged source anomaly rather than a real age claim. The `received_free_explicit` label is applied only when the card says the reviewer received the product for free; other cards are `not_established`, not automatically organic/self-paid.

`source_register.json` contains per-page source IDs, actual public URLs, raw paths and hashes. Each cleaned record includes the matching source ID and an ordinal locator within that raw response. For baseline-reused captures, the authoritative rebuild restores the original collection timestamp when available and marks the cache reuse. Extraction/rebuild does not claim a fresh HTTP retrieval.

## Coverage and interpretation

A source-displayed count is a coverage target, not a population denominator. Reconciliation means the enumerated pages yielded that many distinct platform review IDs. It does not prove unique people, stable point-in-time completeness, representative sampling, independent accounts, age eligibility, purchase recency, or Premium-to-Basic behavior. Live publication/deletion or cached baseline pages can affect a snapshot. Profile-country labels describe the source display, not verified residence.

Free-product cohorts are a large part of this source. Their experiences may be informative, but incentives, recruitment, source moderation, and self-selection matter. Separate products and incentive strata. Do not report a pooled national satisfaction rate or treat a high total score as success on every claimed benefit. The selected manual evidence includes a high-rated review reporting no whitening change and a low-rated review containing positive prose, demonstrating this distinction.

`clean/selected_manual_evidence.json` is a purposively selected nine-record teaching table, not a complete hand-coded corpus. No coder-reliability or saturation analysis occurred. Clinical and cosmetic effects reported by users remain unverified subjective statements.

## Reproduction

1. Run `scripts/collect_full_tar.py` to resume missing public pages from `targets.json`. Successful cached extraction pages are reused. Do not blindly retry429 responses or bypass source restrictions.
2. Run `scripts/rebuild_from_cache.py` to regenerate the authoritative UTF-8/fractional-rating corpus and count reconciliation without network access.
3. Validate all source IDs, raw-file locators, hashes, record-ID uniqueness, count targets and baseline overlap before integration.

The root synthesis should deduplicate against the original100 TryandReview records by `record_id`, preferring this corrected expansion for text while retaining baseline lineage. Additional records are the distinct scale IDs absent from those100; files, pages, product counts and review counts are different units.
