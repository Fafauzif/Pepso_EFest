# Pepsodent: final analysis and complete repository handoff

**Draft for review — 3 November 2026, Asia/Jakarta.** This is the proposed work, not a claim that the new exports have already been integrated or that a final ZIP has been built. Answer the four questions at the end before the final analysis and packaging run starts.

## 1. Intended outcome

Deliver one complete ZIP that the team can download from Filebin, extract, and copy into the existing Pepso_EFest repository using GitHub Desktop. It should carry the earlier research release forward, add every available relevant export from this conversation, reconcile the counts, deepen the diagnosis, and prepare the team to conduct primary research. It should enable a fresh assistant or teammate to continue without this chat.

The central question remains why some Indonesian young adults who used Pepsodent Premium subsequently choose Basic at replenishment. Possible strategy directions remain conditional. This work will not select a final solution or invent causal proof from public reviews.

The reading experience should have three levels: a short decision brief; a substantial teaching and diagnosis report; and a complete audit trail of data, methods, sources, scripts, and limitations. More rows should improve evidence coverage, rather than bury the useful findings.

## 2. What is confirmed to be available

The earlier release ZIP exists locally: **402,496,490 bytes**, containing **1,949 archive entries** and about **615.6 MB of extracted contents**. Its contents will be reconciled against the final release so that earlier work is not accidentally dropped. The ZIP itself does not need to be embedded inside the new repository: its research contents, prior release manifest, and identifying checksum provide continuity without duplicating a 402.5 MB binary.

The earlier integrated written corpus contains **298,846 platform records**, with **301,526 source occurrences**. The distinction matters: repeated observations are not additional independent reviews. The platform breakdown is Amazon external context 286,706; Watsons 7,419; Lazada 681; ORESA 2,228; TryandReview 1,423; Reddit 389. The earlier six-post X collection remains a separate source until overlap with the new X exports is checked.

The Amazon work streamed and screened 26,125,466 review rows and 857,856 metadata rows. Those are screening counts. The full upstream millions were not retained locally and cannot honestly be described as millions of collected toothpaste reviews. The retained Amazon candidates include adjacent products, children's products, and title-classification errors. International observations will remain a separate contextual evidence layer.

New attachments available locally:

| Source | Files | Current preliminary reconciliation |
|---|---:|---|
| X user-run exports | 4 | 16,165 exported rows; 12,990 distinct post IDs across these files |
| TikTok comments | 1 | 2,380 distinct comment IDs across 18 videos; 699 replies; 8 blank text fields |
| Tokopedia | 2 | Latest file contains 266 distinct reviews and all 43 pilot review IDs; 263 nonempty review texts in latest file |
| Shopee failed targeted pilot | 1 | Two error records; zero delivered reviews |
| Shopee default example run | 1 | 100 Singapore UGREEN electronics reviews; zero toothpaste records |
| Other attachments | 2 | X execution log and supplied image; retain as relevant supporting artifacts with captions/context |

The latest Tokopedia export also contains 18 product listings and one billing notice. These are different units from reviews. The pilot's product observations may carry a different collection timestamp and will be kept as occurrences rather than silently discarded. Some Closeup results are whitening sprays, not toothpaste. One nominal toothpaste review discusses body odour. Both issues need explicit treatment.

Existing non-review evidence will remain included: 300 keyword observations; retail and pack observations; brand and campaign artifacts; historical promotions; public health/context indicators; literature discovery and appraisal; tool evaluations including Agent-Reach and reverse-api-engineer; original case material and available transcripts; and the original teaching/context material.

No combined new grand total will be published before cross-file identities, blank-text exclusions, product eligibility, and possible cross-source copies are reconciled.

## 3. Scope of “everything”

Include all relevant available original inputs, retained collection outputs, scripts, collection logs, actor configurations and schemas already captured, prior research reports, source registers, teaching material, and material decisions from the visible conversation. Preserve the original master and original raw captures. Keep failed and wrong-target runs in an excluded/audit area with their reasons.

Do not count these as substantive consumer evidence: error rows; billing notices; product cards; rating-only rows; the UGREEN run; temporary databases; duplicate observations; irrelevant social matches; upstream rows merely screened. Retention in the archive and eligibility for analysis are separate decisions.

Exclude credentials, authentication cookies, environment directories, installed dependencies, caches, temporary database files, and .git. Preserve reproducible setup instructions and tool-audit notes instead of vendoring entire software installations. The large SQLite work database is rebuildable from retained sources and exports; it is not required in the portable handoff.

The chat handoff will be a faithful substantive reconstruction of decisions, evidence, corrections, and outstanding work. It will not pretend to be a verbatim platform transcript or recreate unavailable messages/files. Known missing original PDFs and inputs will stay explicitly missing.

## 4. Work sequence and review gates

### Phase A — Freeze inputs and establish the baseline

1. Reconcile the earlier ZIP against the working repository and original source hashes.
2. Inventory every new attachment with filename, byte size, SHA-256, source, collection time where available, and intended treatment.
3. Check the repository baseline and any newer team changes before preparing an overlay that replaces files.
4. Record the accepted scope and answers to the questions below.
5. Separate immutable original inputs, derived analysis files, and documentation so rebuilding cannot overwrite originals.

**Output:** coverage inventory, source manifest, baseline/change summary, explicit exclusions and missing inputs.

### Phase B — Clean, normalize, and reconcile

Use reproducible Python ingestion and streaming processing where appropriate. Keep original text alongside any normalized text. Preserve null, zero, blank, missing, and not applicable as different states where the source supports them.

Create a consistent analytical schema covering platform, source filename and row locator, record ID, parent/conversation/video ID, source URL, exact text, language, product/variant/pack, source and normalized dates, rating, incentives, author role where evidenced, geographical applicability, relevance status, and exclusion reason. Do not infer age, income, student status, or verified Premium-to-Basic switching from profiles.

Deduplication will distinguish:

- Repeated source occurrences of the same stable platform record ID.
- Different records sharing exact or near-identical text.
- Repeated reviewer or author IDs, where available, without claiming cross-platform person identity.
- Cross-file overlap and possible overlap with the earlier small X collection.
- Campaign templates, promotional copy, and repeated incentive wording.

Copied-text groups will remain traceable. Similar text does not automatically establish bots, paid promotion, or the same person. Changed payloads and conflicting observations will be retained as versions rather than silently overwritten.

Build separate eligibility fields for product category, relevant country/context, case period, written text, first-person experience, and stated purchasing behaviour. A record may be relevant to one analysis and unsuitable for another.

Date handling needs special attention. Tokopedia has disagreement between `reviewTime` and `reviewDate` in 40 of 43 pilot reviews. Preserve raw relative labels, both parsed fields, collection timestamps, and a date-quality flag. Do not blindly treat an estimated relative timestamp as exact. Distinguish case-period evidence through 30 June 2026 from later observations, older context, and uncertain dates. TikTok comment dates and video publication dates are separate facts.

**Output:** reconciled counts, clean tables, row-level quality flags, dictionaries, exclusions, duplicate/version ledgers, and rebuild scripts.

### Phase C — Assess relevance and information value

Analyze every retained record computationally for coverage and transparent candidate themes; conduct deeper reading on a stratified subset. Do not imply that every one of roughly 300,000 records received close qualitative review.

For X, identify candidate consumer accounts, questions, brand material, sales/affiliate copy, news, humour, figurative mentions, ODOL truck references, non-toothpaste meanings, and uncertain cases. Link replies to available context and mark missing parents. Account bios or visible language alone do not establish Indonesian residency or age.

For TikTok, map comments to the 18 submitted videos, separate roots and replies, identify off-topic material, and mark the original per-video collection caps. Use only recoverable video context; do not guess creator intent, sponsorship, or missing captions from a username. Separate creator/product context from what commenters actually report.

For Tokopedia and earlier retailer reviews, separate delivery, packing, seller trust, authenticity concerns, first-use expectations, sensory experience, reported benefit, repeated use, and explicit repurchase. Empty text, emoji-only text, and generic praise should not become rich evidence merely because a rating exists.

For Amazon, preserve its international context and title-based eligibility limitations. Compare mechanisms within eligible product groups; do not pool its volume with Indonesian social evidence to produce a headline consumer percentage.

For incentivized sources, keep explicit free-product, campaign, cashback, and unknown statuses separate. Unknown incentive status is not evidence that a review was organic.

**Output:** coverage/bias audit, eligible subsets, platform-specific descriptive summaries, and a transparent coding framework.

### Phase D — Deep qualitative analysis and counterexample search

Begin with a 40–60-record calibration sample spanning platforms, ratings, incentives, and behaviour types. Refine definitions before broader coding. Then closely review approximately 250–350 informative Indonesian/context-relevant records, with a separate smaller international comparator set. These are proposed review targets, not completed annotations or proof of saturation. If eligible evidence is sparse, report the actual yield rather than padding the sample.

Use both ordinary and purposive samples: ordinary samples reveal the proportion of low-information material; targeted samples help examine rare mechanisms. Preserve selection method so purposively selected quotations are never used as prevalence estimates. Include counterexamples and unclear records, not just vivid support for preferred hypotheses.

Record original phrase, interpretation, context, competing interpretation, product, period, limitations, and source locator for every substantive example. Independently re-code a subset to expose ambiguity and disagreements. Assistant/agent agreement is a consistency check, not independent human validation or ground truth.

The coding should distinguish hypothetical intention, first-person experience, advice, hearsay, first trial, reported repeated use, explicit repurchase, switching direction, household influence, and confirmed versus unconfirmed target eligibility. A positive adjective is not a repurchase claim; a purchase claim is not a longitudinal retention measure.

**Output:** coded evidence library, disagreement/QA notes, annotated examples, and counterevidence register.

## 5. Recommended substantive analyses

| Analysis | Questions and intended output | Boundary |
|---|---|---|
| Metric diagnosis | Reconstruct the case's Premium share/mix definition; show how denominator growth, Premium decline, and price/pack changes could yield the stated movement | No causal allocation without the required sales data |
| Replenishment journey | Need, trial, experienced result, running out, shopping, payer decision, replacement, continued use; map evidence and gaps at each step | Public posts rarely establish the whole sequence |
| User–chooser–payer–household | Contrast dependent purchasing, self-purchase, shared tubes, and separate specialist tubes; identify decision authority and transitions | No population prevalence from public anecdotes |
| Need and benefit | Sensitivity, whitening, gum care, freshness, cavities; distinguish perceived improvement, continuing benefit, and unclear value | Self-reports are not clinical efficacy evidence |
| Sensory experience | Taste, aftertaste, foam, freshness, dryness, irritation, comfort, felt cleanliness; inspect beneficial and adverse experiences | Do not infer formulation effects or medical diagnoses |
| Affordability and pack economics | Ticket price, price per 100 g, bundle composition, refill cash outlay, illustrative consumption scenarios | Cost-per-day scenarios require explicit dose/usage assumptions; not observed spending |
| Promotion and repeat | Distinguish trial, deal-seeking, claimed repeat, normal-price retention, and loyalty coexisting with promotions | No price elasticity, incremental lift, or causal promotion effects from these data |
| Availability and replacement | Product existence, online listing, historical flyer, reported stock difficulty, exact-variant substitution, channel convenience | Online listing is not verified local shelf availability |
| Choice and positioning | Map specialist promises, SKU confusion, recommendation sources, masterbrand associations, and competitor differences | Choice overload remains a hypothesis; campaign existence is not measured effectiveness |
| Brand, retailer, competitor comparison | Compare eligible themes and quotations within source, period, benefit group, and incentives | Search ranking and review sampling prevent market-share or preference claims |
| Review-system bias | Rating skew, before-use reviews, generic praise, templates, source/post concentration, author concentration | Star ratings are not synonymous with satisfaction or sustained use |
| Time and context | Separate case-period evidence, current context, outside-period records, and date uncertainty; map campaign chronology | A search/export time series is not a representative trend in demand |
| Incrementality and feasibility | Identify potential Premium growth, Basic cannibalization, competitor switching, channel costs, and household tradeoffs | Financial illustrations remain sensitivity scenarios, not forecasts |
| Literature triangulation | Connect mechanisms to retained studies, with geography, methods, relevance, and reading depth | Preserve abstract-only versus full-text appraisals; do not exaggerate certainty |

Use term frequency and co-occurrence only as descriptive exploration with explicit denominators. Avoid a single sentiment score or a pooled word cloud as the central diagnosis. No unsupported ML causal models, demographic inference, retention estimates, or pseudo-precise willingness-to-pay figures.

## 6. Hypotheses and decision logic

Build a living matrix with: hypothesis; mechanism; affected situation; observable prediction; supporting evidence; conflicting evidence; alternative explanation; evidence applicability; uncertainty; disconfirming observation; primary research question; and conditional strategy implication.

Initial hypotheses to challenge, not adopt:

1. The user values Premium but the household payer chooses Basic.
2. Independent purchasing changes cash constraints and the acceptable refill price.
3. The desired variant is unavailable at the ordinary replenishment occasion.
4. The promised specialist benefit is weak, slow, hard to notice, or poorly matched to the need.
5. Improvement is interpreted as an endpoint, reducing the perceived reason to continue.
6. Taste, dryness, foam, or comfort makes the premium experience less attractive despite its promise.
7. Variants are difficult to choose; a familiar Basic product becomes an acceptable default.
8. A promotion creates a trial that is not repeated at the later price.
9. Specialist value belongs to one user while the tube and household budget serve several people.
10. Basic is a rational sufficient choice for some users; apparent downgrading need not be a failure to understand Premium.
11. Some observed mix deterioration reflects measurement, mix, or growth of Basic rather than the assumed individual switching mechanism.

Give confidence in the mechanism and confidence in applicability to the target group separately. Repeated anecdotes can strengthen plausibility while leaving target prevalence unknown. Search explicitly for durable premium users, successful symptom relief followed by repeat, satisfied Basic users, and people who find Premium easy to obtain.

Return to all 12 questions in the supplied business-leader image. Each receives: current answer; evidence; important unknown; what data could answer it; and what decision changes if the answer differs. Some answers will remain unavailable without company data or primary research.

**Output:** prioritized competing hypotheses, evidence gaps, and conditional directions. No fixed campaign or final recommendation imposed.

## 7. Primary research package

The next collection should be designed around actual replacement decisions, not general opinions about premium products. Prepare the tools; do not recruit, contact, interview, or survey people during this packaging work.

Propose two pilot interviews followed by an initial 8–12 substantive purchase-history interviews, expanding only if important contrasts remain unresolved. Recruit confirmed 18–30-year-olds and seek contrasting paths: Pepsodent Premium-to-Basic, retained Premium, and Basic/competitor choices. Include students and working adults when accessible, with independent/dependent purchasing and shared/personal tube use as cross-cutting dimensions. Interview counts are practical starting points, not claims of statistical representation or saturation.

Prepare:

- Eligibility screener: age, relevant country/location, actual product/variant history, approximate sequence and dates, purchasing authority, and consent.
- Neutral 30–45-minute interview guide plus a shorter version, in the chosen language.
- Purchase timeline sheet: last two or three actual toothpaste purchases, payer, chooser, users, product, pack, outlet, price actually paid, promotion, alternatives, and what followed.
- Optional receipt/product-photo prompts with permission; retrospective certainty ratings and missing-data fields.
- Payer/co-user module to understand shared decisions without assuming the individual controls the household purchase.
- Counterfactual probes grounded in the last purchase: what if the prior variant were in stock or the price differed? Treat answers as stated preferences.
- Short optional replenishment diary or follow-up for those nearing replacement; observe a later action where practical instead of relying only on intention.
- Focused shelf-check template and a simple SKU comparison task only where a hypothesis requires them.
- Consent wording, de-identified note template, codebook, recruitment tracker, and team role split.
- A survey question bank for later refinement after pilot interviews. No claim that a convenience survey establishes population prevalence or validates a causal model.

Predefine a small decision table: which findings would strengthen, weaken, or split each hypothesis and what follow-up would be justified. The interview guide must allow price, household, availability, and benefit explanations to lose, not lead everyone toward the preferred story.

## 8. Reports, teaching, and continuity

Create a concise decision brief and a detailed Markdown teaching report. The full report should explain the reasoning chain, how each evidence type changes the diagnosis, examples with source locators, uncertainty, counterexamples, and the next observation worth obtaining. Include clear tables and a few meaningful charts where they improve understanding; avoid charts that imply representative market quantities.

Update root README, CURRENT_STATE, CONTEXT_LATEST, source register, changelog, inventory, and resume prompt. Replace stale current claims that no Apify results exist while retaining dated historical versions as history. Clearly distinguish assistant-led public collection from the user's executed Apify runs. Preserve recommended versus executed inputs and available run logs; do not reconstruct missing run settings or costs as facts.

The next assistant's start-here file should explain the case, scope, data layers, completed work, accepted decisions, unresolved hypotheses, source limitations, key paths, reproducible commands, and the immediate next primary-research action. It must not require reconstructing the chat.

## 9. Repository and download design

GitHub currently warns above **50 MiB** and blocks files larger than **100 MiB** in ordinary Git. The browser upload limit is 25 MiB, but GitHub Desktop is the intended route. The outer Filebin ZIP can exceed 100 MiB because it is a download container, not a file to commit inside the repository.

Prefer independently readable compressed data shards below **45 MiB**. Preserve provenance and make loaders understand the shard index. Where an immutable archived original needs splitting, provide lossless reconstruction and checksums; normal analysis should work from portable files without requiring reconstruction. The hard release gate is that no file intended for ordinary Git reaches 100 MiB; report any intentional files above the warning threshold. Avoid LFS setup unless ordinary portable packaging proves inadequate.

Keep reports and small reference tables human-readable. Retain raw JSON bytes through lossless archival compression where needed, with original filenames, uncompressed hashes, and documented restoration. Do not confuse record-aware derived shards with byte-split originals.

Use a clearly named staging folder with the actual repository contents inside. Instructions must say to copy that folder's contents into the local Pepso_EFest root, avoiding a nested Pepso_EFest/Pepso_EFest directory. Do not include .git or the outer delivery ZIP. Add ignore rules for rebuildable databases, caches, environments, and downloaded release ZIPs.

An extract-and-replace overlay cannot delete obsolete files already in a user's clone. Preserve paths where practical and document any superseded files. If cleanup requires removal, provide a concrete reviewable list rather than relying on “replace all” to remove them. Newer user edits must be reconciled before replacement.

Upload the final archive to Filebin after validation; verify uploaded byte size and SHA-256 and report the actual returned expiry. Supply a second durable download copy where supported. Filebin is a temporary link-based transfer, not the permanent project home.

Reference: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github (checked 3 November 2026). Filebin expiry will be read from the actual upload response rather than assumed.

## 10. Proposed outputs

Paths are proposed; the existing dated source folders remain available.

| Deliverable | Purpose |
|---|---|
| START_HERE.md and updated README.md | Reading order and continuation instructions |
| reports/DECISION_BRIEF.md | Short findings, uncertainty, and next decisions |
| reports/DIAGNOSIS_AND_TEACHING.md | Detailed analysis and explanation |
| analysis/HYPOTHESIS_MATRIX.csv and .md | Competing mechanisms, evidence, falsifiers |
| analysis/EVIDENCE_LEDGER and quote tables | Source-linked coded claims and counterexamples |
| data/raw/user_runs/ | All new immutable exports, logs, and attachment register |
| data/clean/ and analytical subsets | Normalized, deduplicated, eligible records |
| data/audit/ | Occurrences, exclusions, conflicts, date and relevance flags |
| primary_research/ | Screener, guides, timelines, diary, optional survey bank |
| methods/ and scripts/ | Codebook, analysis methods, rebuild and QA scripts |
| context/ | Complete substantive session handoff and updated state |
| release/ | Change summary, inventory, checksums, installation/verification guide |
| Existing research/2026-11-03/ sources and annexes | Earlier collection, reports, tool audits, literature, historical artifacts |

## 11. Validation before delivery

1. Preserve and verify original-source bytes or documented exact restoration hashes.
2. Reconcile source rows, unique IDs, occurrences, exclusions, coded subsets, and report totals.
3. Validate schemas and parse every exported shard; verify gzip and ZIP integrity.
4. Check references resolve to retained source files and source locators; check selected quotations against originals.
5. Audit classification errors and disagreements, ambiguous dates, duplicate concentration, and unsupported demographic/causal claims.
6. Ensure report findings reconcile with case period, incentives, product eligibility, and source-specific denominators.
7. Rebuild derived outputs from a fresh temporary extraction using documented commands and available inputs; separate genuinely reproducible offline steps from optional network refreshes.
8. Check every repository file size, broken local links, unsafe archive paths, accidental nested directories, and missing manifest entries.
9. Simulate the overlay against the known repository baseline; review changed paths and any deletion instructions.
10. Run original keyword verification and the new integration/analysis checks. Refresh release manifests after final edits and before packaging.
11. Verify the Filebin upload's actual size/hash and provide the expiry and simple GitHub Desktop steps.

An independent analysis/QA pass should challenge the main conclusions and count reconciliation before the archive is finalized. Parallel agents can work on X, TikTok, retailer reviews, hypothesis synthesis, primary-research design, and QA, with a single integration owner to prevent conflicting edits. Delegation is for reading and analysis, not additional paid collection.

## 12. Four clarifying questions

1. **Repository visibility:** Will this remain a private team repository? The existing handoff calls for private handling of organizer materials. Recommended: private repository, original source archives retained, de-identified analysis tables where feasible. A public repository needs a different treatment of organizer material and raw identifiable social profiles.
2. **Report language:** Prefer English analysis with Indonesian interview/survey wording, mostly Indonesian throughout, or fully bilingual? Recommended: English analytical report plus Indonesian fieldwork tools, preserving original quotations.
3. **Primary-research access:** Which city/cities and kinds of people can the three teammates realistically reach—students, working adults, household payers—and roughly how many interviews are feasible? If uncertain, use an adaptable initial 8–12-interview design after two pilots, with clear minimum and expanded versions.
4. **Repository changes:** Have you or teammates changed the repository locally or on GitHub since the version supplied at the start of this chat? If yes, identify the affected folders or latest version so the replacement package can be reconciled rather than overwrite newer work.

Already settled; no need to reconfirm: include the earlier full research contents and new exports; stop broad secondary collection; provide a complete extractable ZIP and Filebin download; keep individual Git files below the platform limit; preserve original sources; focus on diagnosis/teaching and primary-research preparation; leave strategy directions conditional; do not push remotely on the user's behalf.
