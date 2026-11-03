# Scaled Reddit archive collection: real access, corpus and limits

Collected3November2026. No paid service, API key, browser cookie, account session, Apify actor or third-party scraping dependency was used. Standard-library Python retrieved publicly exposed ArcticShift archive endpoints.

## Collection results

|Measure|Count|Interpretation|
|---|---:|---|
|Targeted threads|11|Purposively discovered;10r/indonesia+1r/Jakarta|
|API comment nodes retrieved|582|Raw tree nodes; not users or representative respondents|
|Unique comments retained|389|Includes contextual discussion and keyword candidates|
|Keyword candidate comments|266|Contains at least one configured dental/category term; not fully validated consumers|
|Dental-thread context comments|123|Retained to preserve local conversational context; may be short replies or jokes|
|Excluded comment nodes|193|Deleted/removed/empty, moderation bots, or non-dental mixed-thread content|
|Within2022–H1'26 case window|309|Timestamp classification, not proven youth/switcher eligibility|
|Outside case window|80|Primarily2021 discussion; historical context only|
|Manually inspected illustrative examples|24|Derived annotations pointing into the389records, not additional observations|
|Paid spend|$0|Actual run|

`reddit_records.csv/json` is the clean corpus. `manual_evidence_examples.csv/json` identifies24selected records, themes, interpretations, limitations and exact source-comment links. `threads.json` documents target/thread coverage, returned nodes and collapsed markers. `collection_log.json` preserves request settings/statuses. `raw/` preserves actual API responses and documentation/probe outputs.

The clean corpus excludes author handles. It does not infer age, location, income, gender, premium tier or switching from a profile. Every record has `age_verified=false` and `premium_basic_switch_verified=false`. Some comments self-report age; that is distinct from verified eligibility.

## Why this expansion is useful

The biggest improvement over a handful of web excerpts is **recovering comment-level text, exact parent relationships, timestamps and stable IDs** for coherent conversations. That allows a human analyst to check the buying episode and replies without treating fragments as independent survey responses.

The resulting corpus remains small compared with a whole-platform archive, but it is relevant to the requested mechanisms. Downloading millions of unrelated Reddit posts would increase storage and classification work without automatically providing more qualified Indonesian young-adult Premium-to-Basic purchase histories.

### Household purchasing appears directly, with rival interpretations

The June2023 go-to-toothpaste thread contains several useful statements:

- `jmyol7g`: the speaker is repeatedly bought Herbal by someone else; buyer identity and payer are unspecified.
- `jmytna4`: a mother purchases Ciptadent; the suggested reason in the reply is partly joking and cannot be coded as verified affordability motivation.
- `jmz7mka`: the wife buys different brands and prefers a salty taste that the commenter dislikes. This illustrates chooser-user disagreement within one household.
- `jn2d5tk`: a shared household uses Systema partly because the mother finds it comfortable for sensitive teeth. **Household sharing can support a specialized choice**, a rival to the hypothesis that shared tubes necessarily undermine Premium.

These are actual archived public statements, not team interviews. They establish examples of mechanisms, not their prevalence or relevance to the case’s exact switching cohort.

### “Clean feeling” is heterogeneous

Record `jmyhulz` links mint intensity to feeling fresh and feeling that brushing occurred. Record `jmyklul` instead prefers subtle, non-burning Enzim sensation. `jmyycgk` favors lower foam. These examples support investigating sensory fit and evaluation cues, while contradicting a single universal “strong mint is better” story.

None establishes clinical cleaning performance. Reported discomfort, relief, foam beliefs and ingredient claims remain consumer statements. Medical interpretations in comment threads are not validated dental guidance.

### Discount choice is observable language, not estimated elasticity

`jmyoa3g` and `jmyrku5` describe buying whichever product is discounted during the shopping trip. `jmz9hrk` combines sensitivity need with discount-dependent competitor or PepsodentSensitive choice. `jmzc51f` describes a promotion-first rule with Herbal as fallback.

These statements make deal-led replenishment a reasonable mechanism to test. They do not measure causal price elasticity, normal-price retention, transaction shares or the extent of the case decline. Herbal must not automatically be reclassified as Basic merely because it is a default; the case itself includes Herbal among Premium examples.

### Variant availability needs exact identity

`jmz6rv4` reports that old red/blue Closeup is difficult to find in the person’s local minimarkets. It supports the general possibility of variant-specific access friction; it does **not** establish that PepsodentSensitive is unavailable. This distinction matters alongside the official historical Indomaret Sensitive promotions collected by the other workstream.

### Need satisfaction does not imply one universal repeat outcome

`jmzi5sd` describes a positive Sensodyne experience after research and exposure to dentist content. This is a potential counterexample to the idea that symptom relief always eliminates specialist preference. The comment is not a longitudinal transaction record; continuing preference must not be reported as proven regular-price repeat.

`nzq60pw` describes months of a whitening-brand experience without the expected result. `itfn8si` expresses perceived equivalence and interest in a professional alternative. The records inform expectations and substitution questions without proving objective efficacy or causal disappointment.

### One self-reported young-adult example is not a youth dataset

In the hygiene thread, `l5gjjk8` self-identifies26M and describes choosing on-sale fluoride toothpaste, usually Pepsodent. `l5q18t2` self-identifies30M and reports long-standing household use of greenCloseup. These may be useful illustrative accounts; age is self-reported and neither supplies a confirmed Premium-to-Basic sequence.

A larger general corpus does not cure an eligibility mismatch. Primary interviews should still verify exact last purchases, variant, payer, household role, paid price, experience and replacement sequence.

## What worked technically

Official ArcticShift API documentation was inspected and archived from:

https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md

The public `posts/ids` and `comments/tree` routes worked. Whole-history r/indonesia keyword searches returnedHTTP422 with a timeout explanation, even atlimit5. A date-narrowed2024post search succeeded but its single returned post had deletion/removal metadata and was not used as consumer evidence. A narrower month query still timed out. PullPush returnedHTTP522 for its public comment endpoint and403for its homepage.

The working collector therefore retrieves a defined set of relevant thread IDs. It expands tree breadth/depth explicitly and caps each request and the overall retained corpus. It reuses successful snapshots, checkpoints after each thread, logs errors, and stops if the service returns429. No collapsed `more` markers were returned in the11collected trees; that does not prove the archive contains every comment ever posted or reflects current live visibility.

ArcticShift is a third-party archive. Collection time and original post/comment time remain separate, as does the archive’s `retrieved_on` field. Record-level current Reddit visibility was not rechecked and is explicitly labeled. Removed/deleted/empty bodies and known moderation bots are excluded from the clean analytical corpus. No attempt was made to circumvent a login or private source.

## Reproduce or extend

From this directory:

```bash
python3 scripts/collect_reddit.py --thread-limit 1000 --max-records 5000
python3 scripts/annotate_examples.py
```

The collector’s target list is explicit at the top of the script. Add only genuinely relevant thread IDs, preserving dental/mixed/meme context labels. When modifying query inputs, use a new query ID or parameter-derived ID rather than overwriting an earlier raw snapshot. Existing successful snapshots are reused. Do not interpret a timeout or empty archive response as evidence that no discussion exists.

For broader discovery, partition post searches by year/month, test query yield, and fetch relevant thread IDs. The official documentation warns that very active subreddit keyword searches can time out; massive archive processing belongs in published monthly dumps rather than excessive API traffic. Bulk dumps were not downloaded during this run because they would predominantly contain unrelated material. PRAW/asyncpraw are official-API clients rather than sources of free authenticated access; they do not solve an unconnected account or incomplete archive by themselves.

## Integration cautions

1. Deduplicate comment IDs against any earlier search-excerpt corpus; these records may overlap earlier examples.
2. Do not add the24manual-annotation rows to the389comment count.
3. Keep memes and mixed-thread material separate from product experience.
4. Do not pool2021/outside-case content into the2022–H1'26 explanation. The actual retained outside-case comments here are2021.
5. A thread’s commenters are self-selected, dependent and non-random. Avoid national sentiment percentages and sampling margins of error.
6. Preserve parent context when interpreting sarcasm or replies; exact-match keyword hits are only candidates.
7. Claims about ingredients, safety, treatment or effects require independent authoritative evidence.
