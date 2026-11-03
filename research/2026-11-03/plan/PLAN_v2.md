# Pepsodent E-Fest: deep research and data collection plan

**Version:** 2.0 — 3 November 2026, Asia/Jakarta  
**Status:** Authorized and executed scope. The accepted-scope note and Version 2 expansion supersede the historical intake questions. See the research report and actual inventory for completed collection.  
**Workflow clarification:** Assistant-accessible tools first; research, collection and deep analysis next; gap-specific Apify actors and ready-to-paste inputs afterward, for Fauzi to run himself. Apify access is not a dependency for the assistant-led run.

**Requested outputs:** A detailed teaching and research report in Markdown, a chat summary, a reproducible data ZIP, and an organized repository update at the end of the work.  
**Planning inputs:** Fauzi’s 3 November notes; the attached twelve-question image; the cloned `Fafauzif/Pepso_EFest` repository, particularly `context/CURRENT_STATE.md`, the original master context pack, and the cleaning/data dictionary documentation.

## 1. What this investigation needs to accomplish

The central question is: **At a real replenishment occasion, why does a former Premium buyer aged 18–30 choose Basic, and which change could make returning to Premium relevant, affordable, repeatable, and commercially worthwhile?**

The scope is specifically return to Premium. General premium acquisition, product awareness, and social reach can inform it, but are different outcomes. Someone who has never personally purchased Premium, someone who used their parents’ tube, someone who buys Basic for the family while retaining Premium personally, and someone who actually replaced Premium with Basic are different research cases.

The investigation will reconstruct the offer, the shopping environment, experienced benefits, purchase authority, and replacement decision. It will also teach the business reasoning behind each question. It will preserve alternatives until evidence distinguishes them.

Proposed final report answers will use a consistent structure:

1. Direct answer, with confidence and a short explanation.
2. The business mechanism in plain language.
3. Case facts and newly collected evidence, with source locators.
4. The strongest competing explanation and contradictory evidence.
5. What can be estimated, with transparent assumptions and ranges.
6. What remains unknowable from the available sources.
7. What the answer changes for the next research or strategy decision.

No actor run, interview, review dataset, or literature conclusion is implied by this plan. The tool checks below are preliminary feasibility research only.

## 2. Starting position and conceptual corrections

### 2.1 Existing evidence

The case says Premium’s share of Pepsodent sales fell from 27% in 2022 to 20% in H1 2026. That is a seven-percentage-point mix change. The basis of “sales” needs checking before treating it as value or volume share. Absolute Premium revenue decline, unit decline, customer retention, and contribution decline do not follow automatically.

The supplied switcher chart describes 540 switchers within a case survey of 1,200 people aged 18–30 across ten cities. Multiple responses overlap. It is organizer-provided case evidence, not our team’s fieldwork.

The repo adds 300 keyword observations. They support search-language exploration, with unverified country metadata and inferred headers in two captures. They do not identify respondents’ ages, actual switching, willingness to pay, or sales. Missing volume remains distinct from zero. The missing fourth pasted file remains missing.

The current working interpretation is that brand trust may survive while the reason to upgrade weakens. This is provisional. Availability, affordability, poor variant fit, sensory experience, household authority, episodic need, promotions, and measurement can each generate similar outcomes.

### 2.2 Useful refinements to your notes

| Your observation | Refined question or distinction |
|---|---|
| Toothpaste is a replenishment business | Separate usage, stock on hand, purchase frequency, and paid repeat. Buying less often can reflect a larger pack or stockpiling. |
| Premium might be hard to find in minimarkets | Measure exact variant × pack × branch/location × date. Not seeing it personally is a hypothesis-generating observation. |
| Retailers prefer fast turnover, so perhaps D2C dominates | Test channel economics and observed distribution. Retail incentives alone do not establish D2C. |
| Online sales might be D2C | Separate brand-owned checkout, marketplace official stores, authorized retailers, pharmacies, and independent sellers. A brand-branded marketplace storefront alone does not establish who operates it or bears inventory. |
| Premium is affordable to try but expensive to sustain | Separate checkout payment, cost per gram, household consumption, promotion expiry, and the buyer’s perceived extra benefit. |
| Smaller packs may look worse value | Test competing interpretations: cheaper entry, lower risk, portability, specialist treatment cues, expensive-per-gram, or faster depletion. |
| Parents pay for many 18–30-year-olds | Your experience motivates the question; it does not estimate prevalence. Measure user, chooser, payer, and replenishment manager separately. |
| Independent purchasing creates switching costs | More precisely, it can reveal a previously hidden out-of-pocket cost and change the available budget. Conventional switching costs are the effort or loss associated with changing an incumbent choice. |
| “Clean feeling” may determine preference | Separate sensory experience, visible appearance, symptom relief, and clinical efficacy. Freshness or foam is not automatically a measure of cleaning effectiveness. |
| Sensitivity users stop when better | Examine perceived need resolution, price, side effects, professional advice, and substitution. Do not turn this consumer hypothesis into medical advice. |
| Lots of variants cause choice overload | An empirical possibility, not a universal law. More assortment could improve fit, and low motivation or price could explain rejection even when selection is easy. |
| “Enzymatic” is a competitor | Resolve whether you mean the Enzim brand, another named product, or an enzymatic formulation. Product existence, Indonesian availability, and comparable benefits need verification. |

## 3. Scope, time, and sequencing

### 3.1 Two separate time windows

**Case-explanation window:** Evidence about the decline should concern 2022 through 30 June 2026, with explicit dates and historical availability checks. A later article describing earlier activity must be labeled with both event and publication dates.

**Current execution window:** Prices, assortment, campaigns, tool access, and consumer conversation observed now can inform today’s options. They cannot independently establish the historical causes of the H1 2026 outcome.

Undated pages remain undated. A current product page does not prove that variant existed throughout the case period. Archive timestamps establish a capture, not necessarily the first appearance of a campaign or price.

### 3.2 Schedule options

The supplied guidebook records a submission deadline of 5 November 2026 at 12:00 WIB. Today is 3 November. The research should therefore have a deadline-focused path even if the broader learning project continues later.

| Option | Intended use | Proposed work budget, not a completion promise |
|---|---|---|
| Deadline-focused | Support decisions before the competition deadline | First 60–90 minutes for access and source mapping; roughly 4–6 hours for core evidence; 2–3 hours for synthesis and packaging, adjusted to actual access and your remaining writing time |
| Extended | Build the fuller learning and evidence asset | Multiple research passes over roughly 2–4 working days, subject to tool access and available primary evidence |

Historical scheduling proposal, superseded by the user’s instruction not to optimize around timing: the deadline-focused version prioritizes offer/positioning, retail access, usable product reviews, and household/replenishment mechanisms. Historical discount reconstruction and broad social listening continue only where access is productive. We should preserve time for your team to use the findings.

### 3.3 Order of work

1. Resolve the clarification questions at the end of this document.
2. Establish definitions, source registry, access constraints, and collection caps.
3. Map products and channels before scraping reviews about ambiguous variants.
4. Pilot assistant-accessible collection tools, audit usefulness and access, then scale successful routes. Test Agent-Reach and other suitable tools; do not assume installation guarantees data access.
5. Read literature alongside emerging mechanisms, including rival explanations.
6. Synthesize with explicit confidence; answer all user questions and the image’s twelve questions.
7. Identify unresolved evidence gaps and prepare the user-run Apify handoff: verified actor shortlist, exact input JSONs, limits, cost estimates, and export/import instructions.
8. Validate, package the actual collected data ZIP and Apify configuration files, and prepare the repository update. Integrate user-returned Apify exports later if supplied.

Depth means checking mechanisms and contradictions. It does not mean maximizing scraped rows regardless of relevance.

## 4. Workstream A — business performance and what the decline actually means

**Questions:** What deteriorated? Which variants, channels, cohorts, and occasions could account for it? What is knowable without internal records?

Collect the exact case definitions and search dated official Unilever/Pepsodent material for relevant disclosed measures. Build a claim table distinguishing company-level results, category results, brand results, and tier/SKU results. Do not use company margins as Pepsodent tier margins.

Build an accounting bridge only with consistent units:

`Premium revenue = purchasing households × purchase occasions per purchasing household × grams per occasion × realized manufacturer revenue per gram`.

Alternatively use pack units with pack mix explicitly controlled. Do not multiply frequency by annual total consumption and count frequency twice.

**Output:** A performance fact register, a metric-definition table, and an “answerable / modelable / internal-data-required” classification. If tier-level data are unavailable, produce bounded scenarios rather than invented trends.

**Decision relevance:** A share problem, an absolute revenue problem, a discount-realization problem, and a contribution problem can justify different responses.

## 5. Workstream B — Pepsodent meaning, Premium positioning, and marketing execution

**Questions:** What does Pepsodent embody? What does each Premium variant promise? How is Premium promoted, where, and against which alternatives?

Separate three layers: the brand’s intended positioning; what its observed content actually emphasizes; and what consumers independently describe. One sentence about “what Pepsodent means” will be a sourced synthesis with these layers distinguished, not a claim to read every consumer’s mind.

### Collection design

- Product pages, packaging, brand channels, official campaign announcements, retailer campaign pages, and accessible public advertising libraries.
- Public brand, creator, affiliate, dental-education, and consumer posts, classified by source type.
- Historical dated examples where retrievable; current examples in a separate group.
- Comparison set proposed for validation: Pepsodent Basic; Pepsodent Sensitive Expert, whitening, herbal and other case-defined Premium offers; matched Indonesian offerings from Sensodyne, Enzim, Colgate, and Closeup White Now where verified.
- Compare sensitivity with sensitivity and whitening with whitening before making broader brand-level contrasts. Price alone does not establish the case’s premium tier.

For every content item record date, platform, account type, product/pack, headline promise, evidence cue, sensory language, target need, purchase link, promotional offer, and observable interaction. Treat paid/organic/affiliate as unknown unless there is evidence. An accessible ad library may expose only a subset of activity; it does not prove total media investment.

**Proposed depth:** 40–80 distinct marketing/content artifacts across brand and competitor need states if accessible. This is a coverage target, not a representative sample.

**Outputs:** SKU taxonomy; positioning comparison; channel map; dated campaign inventory; examples of brand-consumer alignment and mismatch. Visibility and engagement will not be relabeled reach, spend, incrementality, or return on advertising.

## 6. Workstream C — actual availability and shopping friction

**Questions:** Can shoppers find the exact Premium variant when replenishing? Are minimarkets missing it? Is an apparent availability problem local, channel-specific, or merely unobserved?

### Collection design

Use official retailer listings, delivery catalogues where accessible, pharmacy/health-and-beauty listings, supermarket listings, official marketplaces, and optional team-supplied shelf checks. Candidate channels include Alfamart/Alfagift, Indomaret/Klik Indomaret, Watsons, Guardian, supermarkets and official marketplace stores; access and geographic coverage must be tested.

Capture exact SKU/pack, seller, branch or delivery location, timestamp, listed/in-stock/add-to-cart state, quoted price, shipping or purchase conditions, and variant ambiguity. Do not infer nationwide shelf absence from a website search returning nothing.

Use separate statuses: available to purchase in the observed location; listed but out of stock; listed but availability unclear; not found by this search; access blocked; not checked. Online catalogue presence and physical shelf presence remain separate measures.

**Proposed depth:** 15–25 normalized SKU/pack combinations across at least four channel types and two agreed locations where feasible. If the city is unspecified, start with a clearly labeled Jakarta reference location; no private home address is needed.

**Useful optional fieldwork:** A small standardized shelf audit in stores your team can reach, recording store type, location area, date, exact variant, price and shelf availability. This would remain a purposive local check.

**Outputs:** Availability matrix, channel coverage gaps, and a factual answer to the D2C hypothesis. Distribution breadth and demand causality will remain separate.

## 7. Workstream D — prices, packs, discounts, and sustained cost

**Questions:** What was the promotion history? Does cheap trial lead to expensive replacement? How does pack size affect perceived value and household economics?

### Price collection and chronology

Record seller, channel, variant, grams, pack count, displayed list price, unconditional selling price, voucher conditions, membership conditions, minimum basket, shipping, date observed, date valid, and historical/current classification.

Compare:

- Ticket price and price per 100g.
- Same-SKU promotional and non-promotional observations where genuinely comparable.
- Acquisition cost and replacement cost.
- Individual and shared-household scenarios.
- Stockpiling, multi-buy bundles, and alternate formats.

A strikethrough price is a displayed reference price, not automatically the price previously paid. A coupon requiring a larger basket is not an unconditional shelf discount. “Sold” counters and cumulative reviews do not establish a dated sales series.

Historical evidence can include dated retailer flyers, official campaign terms, archived pages, and dated public purchase accounts. Prefer actual dated prices over retrospective claims. If there are too few observations, label the output a promotion-event catalogue rather than “discount history” or a price-frequency estimate.

### Scenario calculations

`cost per gram = eligible transaction price / total grams`.

`estimated days per tube = grams / (users × brushing occasions per user per day × grams per occasion)`.

`modeled 30-day household cost = price per gram × modeled daily household grams × 30`.

Usage inputs must be sourced or explicitly assumed and varied. These are financial illustrations, not dosing advice. State exclusions such as shipping and unused stock. Manufacturer contribution requires a separate net-revenue/cost bridge; shelf price and supplied margin are insufficient.

**Outputs:** Price/promotion evidence table, pack comparison, low/base/high sustained-cost scenarios, and a distinction between observed behavior and plausible price psychology. No assumed price elasticity or retention uplift.

## 8. Workstream E — sensory experience, value, repeat, and social listening

**Questions:** What does “clean,” “fresh,” “different,” or “worth it” mean in actual language? What happens after trial? Is Premium treated as episodic? Does choice confusion or inability to find a variant appear in real purchase accounts?

### 8.1 Two corpora with different purposes

**Product reviews:** Useful for stated product experience and value. Retain exact variant, review date, rating, repeat-purchase fields where supplied, and listing context. A platform repeat flag is not proof of regular-price retention or a continuous personal purchase history.

**Public conversation:** Useful for spontaneous comparisons, household purchase stories, availability mentions, meaning, and expectations. Search category and need language as well as Pepsodent. Include positive and neutral experiences and successful Premium repeat, not just complaints.

Exclude or separately classify delivery-only comments, seller service, giveaway entries, duplicates, seller copy, affiliate copy, and non-toothpaste meanings. A review about the shopping app is not a toothpaste review. Clinical claims in a review are consumer statements, not verified outcomes.

### 8.2 Proposed staged collection

1. Manually inspect about 100 substantive records across multiple products and sources to refine the codebook and search terms.
2. Pilot assistant-accessible tools on roughly 20–50 records with explicit result/time caps. Apify pilots are a later user-run step, not part of assistant collection.
3. If access and usefulness justify it, target approximately 600–1,200 substantive product reviews and 300–600 relevant public posts/comments. Lower counts are acceptable when sources are sparse or budgets restrictive.
4. Cap contribution from individual listings, posts, and creators. Preserve source-specific datasets and counts. Collect low-rating diagnostic samples separately from balanced/time-ordered samples.
5. Record retrieved, excluded, duplicate, usable, dated-within-case, and genuinely switching-relevant counts. Large raw counts do not substitute for eligible evidence.

These targets are logistical, not power calculations, prevalence estimates, or saturation thresholds. Sparse historical data may make the achievable sample smaller.

### 8.3 Initial Indonesian/English query families

| Family | Discovery terms to test and expand |
|---|---|
| Product identity | pepsodent, sensitive expert, mineral expert, whitening, herbal, complete care, complete 8; validate SKU identities first |
| Sensory experience | odol, pasta gigi, rasa, aftertaste, pahit, pedas, mint, busa, kesat, licin, bersih, segar, bau mulut |
| Comparison/value | sama aja, beda apa, worth it, mahal, murah, boros, cepat habis, ukuran kecil, isi sedikit |
| Actual purchasing | beli lagi, repurchase, repeat order, balik ke, ganti odol, sebelumnya pakai, habis, stok |
| Household roles | dibeliin, dibelikan, ortu, orang tua, ibu, mama, keluarga, serumah, kos, anak kos |
| Price/promotion | diskon, promo, voucher, normal, bundling, tanggal kembar, beli satu, cashback |
| Availability/choice | susah cari, kosong, habis stok, Indomaret, Alfamart, varian, bingung pilih, cocok yang mana |
| Episodic need | ngilu, sensitif, udah mendingan, sudah sembuh, berhenti pakai; preserve lay language without validating medical claims |

Run smaller query families rather than one giant OR string. Test both tightly matched brand queries and broad category queries. Indonesian language filters can miss mixed-language slang. Queries designed around complaints will bias any subsequent prevalence claim.

### 8.4 Coding and verification

Code need, expected benefit, sensory description, experienced result, perceived incremental value, price paid evidence, promotional trigger, availability, variant-choice difficulty, payer/user role, household sharing, and stated subsequent purchase. Allow multiple codes and emerging themes.

Maintain separate labels for explicit statement, supported interpretation, and speculation. Do not infer age, income, location, parent dependence, or switching from profile appearance. “Bought again” is different from “would buy again.”

Review a varied manual sample before automated tagging. Human-check ambiguous slang, sarcasm, strong quotes, and every record supporting a central switching mechanism. If coder agreement is measured, document the independent coding procedure; do not claim reliability merely because a model generated tags twice.

**Outputs:** Codebook, annotated records, source-specific descriptive counts with denominators, anonymized examples, contradictory cases, and a shortlist of actual purchase-sequence accounts. Do not pool a purposive social corpus into a national “sentiment score.”

## 9. Workstream F — literature and public datasets

### 9.1 Literature review questions

Search for evidence on the following mechanisms, retaining null findings and boundary conditions:

- Household decision-making, shared consumption, payer-user separation, and transition to independent purchasing.
- Promotion acquisition, reference prices, deal-prone cohorts, post-promotion repeat, and pantry stockpiling.
- Pack-size perception, unit pricing, entry affordability, duration estimates, and perceived waste risk.
- Choice overload, assortment complexity, expertise, and need specificity.
- Toothpaste taste, mouthfeel, foaming, freshness, perceived cleanliness, and adherence.
- Symptom relief, perceived need resolution, and episodic use, with clinical literature kept separate from consumer behavior.
- Masterbrand trust, specialist credibility, perceived differentiation, and brand extension.
- Physical availability, substitution at replenishment, defaults, and habit formation.

Search PubMed/PMC for dental mechanisms and scholarly databases/publisher pages for behavioral research. Use OpenAlex, Crossref, and Semantic Scholar where useful for discovery and DOI resolution; API access must be verified. Google Scholar can supplement discovery where accessible. Do not treat abstracts or search snippets as full-paper review.

For each study record DOI/URL, publication year, geography, population, category, design, sample, outcome, limitations, funding/conflicts where available, and applicability to Indonesian 18–30-year-old former Premium purchasers. Separate toothpaste-specific evidence from analogous-category evidence. Deduplicate by DOI and normalize preprint/published versions.

**Proposed depth:** Screen 40–60 candidate works and retain about 15–25 highly relevant studies or reviews if available. This will be a structured evidence review, not a claimed exhaustive systematic review. Document searches and exclusion reasons.

### 9.2 Public-data discovery

| Candidate source | Potential contribution | Important limit |
|---|---|---|
| BPS/Susenas publications and metadata | Household expenditure, household composition, life-stage and budget context | Check actual available variables; grouped personal-care spending cannot isolate toothpaste or a brand. Microdata may require separate access. |
| SKI/Riskesdas official tables | Oral-health conditions and reported brushing behavior/timing | Health need does not establish Premium demand; timing does not equal observed brushing technique. |
| Google Trends | Relative search-interest patterns, seasonality, matched query comparisons | Normalized index, not sales, unique users, or sentiment; use anchors for comparisons across batches. |
| Existing Semrush captures | Search vocabulary, needs, product-name discovery | Country/header issues remain; no historical series was recovered. |
| Official campaign archives and retailer flyers | Dated positioning, pack, distribution, and promotion observations | Incomplete surviving archive and selection bias. |
| Public research repositories | Potential published survey or review corpora | Verify Indonesian product identity, collection window, provenance, license, and whether rows are product reviews rather than app reviews. |
| Corporate reports | Strategic direction and disclosed financial context | Company-level figures cannot fill brand-tier or customer-level gaps. |

No identified public dataset currently establishes confirmed 18–30-year-old Pepsodent Premium-to-Basic transitions. Discovery may find useful indirect evidence; the report will not pretend those gaps disappear.

## 10. Workstream G — purchase episodes and targeted primary evidence

This is optional team-assisted collection, not something a scraper can replace. No people will be contacted by the assistant under the current task.

If the team can obtain real accounts, propose 6–10 exploratory conversations across confirmed former Premium users, current repeat Premium users, and parent-funded/shared-tube users. Recruit for relevant purchasing situations, not a convenience sample silently labeled nationally representative. Include cases that contradict the favorite explanation. The number is a feasible starting target, not a saturation claim.

### Purchase reconstruction

1. Confirm age eligibility and distinguish personal use from household purchase.
2. Reconstruct the last three toothpaste purchases or replenishment events.
3. What ran out? Who noticed? Who selected, paid, and used it?
4. Which exact SKU, pack and seller? What price was paid, with which conditions?
5. What alternatives were actually available? Was the preferred variant sought?
6. What benefit was expected, what was experienced, and over what period?
7. What happened at the next purchase, and what made that choice better then?
8. Did Premium remain at home, was Basic bought for someone else, or was stock purchased elsewhere?
9. What observation would challenge the respondent’s first explanation, without leading them?

Ask behavior before showing concept ideas. Record anonymized IDs, date/method, question version and any supplied permission status. Do not invent consent, transcripts, receipts, ages, or responses. If no primary evidence is supplied, this workstream becomes an explicit unanswered-evidence gap.

## 11. Tool plan: what is available, what is only a candidate

### 11.1 Capability audit in this session

- Web search and page reading: available and exercised for preliminary tool/source discovery.
- Python, Git and Node: available. Python can perform standard-library HTTP requests, parsing, CSV/JSON processing, hashing and ZIP creation. Pandas is installed.
- Agent-Reach, Playwright, requests, BeautifulSoup, trafilatura, the Apify Python client, and yt-dlp: not installed in the Python/environment check conducted for this plan. Installation would not itself prove source access.
- Browser tools: available as a potential interaction fallback, not tested for the target commerce/social sites. No signed-in account or authenticated session is assumed.
- Apify: no relevant plugin returned by this session’s plugin search. A direct API route or permitted browser route remains a candidate; no token, account connection, balance, or actor access has been verified.
- Semrush: the existing captures are available. The prior handoff says you have access, but this session has no verified signed-in connection.
- Source-site HTTP reachability, regional output, pagination completeness, and historical coverage remain to be tested during the pilot.

### 11.2 Candidate tool decisions

| Route | Role | Validation before use | Fallback |
|---|---|---|---|
| Built-in search and official pages | Catalogues, campaigns, reports, literature discovery | Open underlying source; verify dates, scope and product identity | Dated primary documents and clearly labeled indexed leads |
| Standard-library HTTP and parsers | Small public pages/APIs; structured extraction | One endpoint, response status/content, stable identifiers and pagination | Search/page reading or small manual extraction |
| Agent-Reach: `Panniantong/Agent-Reach` | Candidate wrapper for supported web/social/video tools | Review current code/dependencies, pin version, test one public target; inspect session behavior before installation/configuration | Existing web tools or source-specific route |
| Apify Xquik: `xquik/x-tweet-scraper` | Candidate public X search and purchase-language discovery | Verify exact actor identity, current Free-tier rate, separate platform usage, date filters, caps and actual pilot charges | Another validated actor or smaller accessible corpus |
| Shopee review actors | Product experience with SKU/rating/date context | Indonesia support, real review text, SKU identity, pagination, actor status and Free-plan limits | Other retailer reviews or a documented manual sample |
| TikTok/Instagram/YouTube comment tools | Consumer language attached to relevant content | Parent post context, dates, sponsor type, result limits and expected usable yield | Accessible public comments and video descriptions/transcripts |
| Threads/X search | Category and household/purchase language | Historical retrieval, query operators and duplicates | Broader indexed web search; report coverage gap |
| Playwright or browser interaction | Selected dynamic catalogues | Available browser/runtime, location, actual visible state, account requirements | Catalogues/retailer documents; record blocked status |
| OpenAlex/Semantic Scholar/Crossref/PubMed | Literature discovery and reference metadata | Current authentication/quota/terms; DOI and original-paper verification | Search official index and publisher/repository pages |

Agent-Reach is a candidate access layer, not a guarantee of universal free scraping. Its official repository describes platform-specific tooling and session handling; inspect the exact version before use. Do not import browser cookies or sessions automatically. Do not run a blanket installer simply because a README recommends it. The objective is usable evidence, so only needed components should be added.

### 11.3 Preliminary actor findings, checked 3 November 2026

**Xquik:** The current actor README advertises $0.00015 per delivered row on every plan, with platform usage charged separately. Its pricing tab did not expose a detailed tier table in the fetched text. Search also surfaced an older indexed developer issue response describing a much higher Free-tier rate. That historical fragment did not establish current pricing. The expanded run subsequently retrieved official actor metadata and confirmed the older Free rate was superseded on 29 August 2026 by $0.00015 per delivered row plus platform usage. Exact metadata, current schemas and proposed inputs are in `apify_handoff/`. No actor was run. [T2–T4]

**Shopee:** `zen-studio/shopee-product-reviews-scraper` currently displays “Under maintenance.” Its README describes a limited free sample and plan-specific paid review pricing. It should not be our production dependency without revalidation; locate an operational alternative first. Actor claims of Indonesia support or full history are vendor claims until a test succeeds. [T5]

**Apify platform:** The public pricing page lists $5 on Free, and official documentation says Free-plan usage stops when prepaid usage is exhausted. That is separate from actor-specific sample restrictions and platform services. The account’s actual remaining balance is unknown. [T6–T7]

The best tool may be less feature-rich if it returns reliable Indonesian product records cheaply. A tool advertising unlimited results is not necessarily unlimited for this account, this actor, this endpoint, or historical data.

### 11.4 Pilot acceptance and stop conditions

These checks apply to assistant-accessible tools first. For Apify they become user-run instructions in the later handoff; they do not authorize or imply assistant execution.

Before scaling, document actor/tool version, input schema, market/date settings, item limit, timeout, charge limit, requested fields, and expected cost. Validate cap semantics against the current API rather than guessing an input field name.

Inspect a 20–50-record pilot for: correct product/country; usable text; original URLs and dates; stable IDs; exact variants where possible; duplicates; promotional spam; timestamp meaning; pagination; and actual cost. Measure usable-record yield and cost per usable record.

Do not scale a tool with ambiguous billing, wrong market, missing provenance, persistently empty/blocked output, or a severely unproductive sample. Make one targeted adjustment after diagnosing the problem rather than repeated blind paid retries. Preserve failures in the collection log. A failed request is not evidence that the product, post, or demand does not exist.

### 11.5 Budget for the later user-run Apify handoff

The assistant will not run Apify. The core research and collection will use accessible public routes and local tools first. No new paid service is assumed.

After the analysis, estimate the cheapest useful Apify collection for the remaining gaps. If the previously mentioned $5 credit remains available, a possible user-run ceiling is $4 with $1 reserve. This is a provisional ceiling, not a spending instruction or a reason to use up the credit. Allocate between reviews, social conversation and retries only after actual needs and current actor pricing are known.

In the later user-run handoff, record expected result fees and platform usage separately, and ask the user to return actual run charges alongside exports. Do not promise a row count from the headline per-result price alone. No assistant-run Apify job, subscription, proxy purchase, or account upgrade is assumed.

### 11.6 Required Apify handoff after the assistant-led analysis

The handoff must be based on gaps discovered in actual research. It is not a generic list of scrapers or a substitute for attempting collection first.

For each recommended actor provide:

1. Exact developer/actor ID and direct link, last checked date, and why its output would resolve a specific remaining question.
2. Free-plan eligibility, result caps, API/console restrictions, current pricing and maintenance status. Clearly label anything that cannot be verified.
3. A minimal pilot input JSON and a separately capped main-run JSON, validated against the current actor input schema. Do not invent actor-specific fields or reuse old schemas blindly.
4. Actual product URLs, handles or query strings discovered during research, with explicit date ranges and Indonesian market settings where supported. Unresolved placeholders must be conspicuous; they must not be presented as ready to run.
5. A mapping of requested result limits to expected charges, separate platform costs, time limits and console spending controls. If a limit is a console option rather than actor input, explain that separately.
6. Expected output fields, what a good pilot looks like, and precise stop/retry criteria.
7. Console run instructions and JSON/CSV export instructions, including preservation of run ID, original input, actor build/version, logs and actual charges.
8. A mapping from the returned exports into our existing data dictionary and analysis. Explain exactly which claims may change after those exports arrive.

Produce `apify_handoff.md`, one actor comparison table, and named pilot/main `.json` input files. Exclude credentials. Keep suggested inputs separate from completed-run logs. Do not include unexecuted Apify jobs in collected-data counts.

If an actor's schema or pricing cannot be verified, mark that recommendation provisional and provide a concrete verification step. Prefer a smaller genuinely runnable handoff over a long list of speculative actors. The first report and ZIP stand on evidence actually obtained; later user-run outputs become a subsequent version with their own provenance and updated conclusions.

## 12. Answering the attached twelve leadership questions

| # | Question | Evidence or method | Likely answer boundary |
|---|---|---|---|
| 1 | What actually deteriorated? | Case metric definitions, public disclosures, consistent financial bridge | Mix change is established; absolute tier revenue/volume/contribution may remain unknown. |
| 2 | Which variants/channels/cohorts/occasions explain it? | SKU taxonomy, dated channel audit, actual purchase episodes; internal breakdown if supplied | Public evidence can locate mechanisms; it cannot allocate the seven-point decline without matching data. |
| 3 | What did former Premium buyers buy next, and why? | Explicit switching narratives and eligible purchase-history interviews | Ordinary reviews cannot reliably identify age or prior tier. |
| 4 | How much demand survives without deep discounts? | Matched paid-price cohorts, actual non-promo repeat, internal panel if available | Public prices/reviews show offers and statements, not an identified demand curve. |
| 5 | What does Basic do sufficiently well, and for whom? | Product/claim comparison, positive Basic reviews, alternatives in purchase episodes | Basic preference can be rational; do not invent inferiority to justify Premium. |
| 6 | Who uses, chooses and pays? | Household-role coding and direct purchase reconstruction | No age-based or profile-based payer assumptions. |
| 7 | Which failure mechanism is operating? | Evidence matrix across relevance, selection, experience, affordability, availability, measurement | Multiple interacting mechanisms may survive. |
| 8 | Which explanation would most change the decision? | Scenario consequences and value-of-information ranking | Importance and confidence are separate; avoid arbitrary composite precision. |
| 9 | What would make us abandon the preferred explanation? | Prewritten rival predictions and disconfirming cases | An explanation must risk being wrong. |
| 10 | How incremental is the growth? | Counterfactual source of demand, cannibalization, realized contribution model | Separate Pepsodent portfolio, Unilever portfolio, and category effects. |
| 11 | Which social outcome improves? | Behavior/health pathway, feasible measurement, controlled pilot where possible | Reach, education views, purchase and clinical benefit are different outcomes. |
| 12 | What must be true operationally and economically? | SKU/channel capability, costs, lead times, partners, margins, sensitivity | Unknown costs become explicit assumptions or information requests, not invented feasibility. |

## 13. Synthesis, estimation, and teaching method

Build an evidence matrix for each mechanism with a precise claim, population, period, source, observation, interpretation, rival explanation, contradiction, confidence, and decision implication. Several articles repeating the same study count as one underlying evidence source.

For each question use one of four answer states: **directly supported; supported provisionally; scenario estimate only; unresolved**. Confidence should explain the evidence quality and fit, not assign a decorative percentage.

Where estimating is useful, name the estimand, show the formula, separate observed inputs from assumptions, give plausible low/base/high cases, and identify what could reverse the conclusion. Do not assign causal switching percentages, price elasticity, youth payer prevalence, or sales uplift from purposive reviews.

Distinguish diagnosis from intervention. For example, if parent payment dominates, the relevant lever could concern household choice or personal purchase authority; if specific variants are absent, an awareness campaign may fail; if need resolution dominates, an appropriate ongoing-use proposition needs separate support. These are conditional implications, not selected solutions.

The narrative report will explain concepts through worked examples using the case numbers, clearly labeled scenarios, and real sourced purchase language where available. It will answer your questions directly rather than presenting a framework catalogue. A final section can compare research implications for possible strategy directions; selection of the competition’s final idea remains a separate decision unless requested.

## 14. Data architecture and the final ZIP

### 14.1 Proposed repository additions

Use a new dated research area and integrate compatible tables with the existing conventions. Preserve the original master, raw sources, and current keyword records. The following are proposed paths, not claims that collection has occurred:

- `research/2026-11-03/plan/` — plan and scope decisions.
- `research/2026-11-03/raw/` — permitted original responses, actor outputs and source captures.
- `research/2026-11-03/clean/` — normalized products, prices, availability, campaigns, reviews and posts.
- `research/2026-11-03/derived/` — coded themes, descriptive summaries, scenarios and evidence matrix.
- `research/2026-11-03/literature/` — references and evidence extraction, with permitted full texts only.
- `research/2026-11-03/scripts/` — collection and transformation code and pinned environment instructions.
- `research/2026-11-03/docs/` — dictionary, cleaning ledger, coverage, limitations and collection logs.
- `research/2026-11-03/report/` — detailed findings and teaching report.
- `research/2026-11-03/apify_handoff/` — gap-specific user-run instructions, actor comparison, and pilot/main JSON inputs; no implied completed runs.

At completion update `context/CURRENT_STATE.md` with evidence dates, decisions, limitations and exact continuation points; update the source register, README and changelog as needed. Do not imply the historical pack is current where it has been superseded.

### 14.2 Minimum record fields

Every observation should retain a stable record ID, source ID/type, original URL, collection timestamp/timezone, event/review/content date where known, historical/current flag, country/location evidence, product/variant/pack identity, raw-file path and record locator, collection tool/version, query or listing reference, and quality flags.

Reviews/posts additionally retain original text separately from translation/summary, rating, parent-post/listing context, account/content type, explicit use/purchase/switching evidence, and annotations with their supporting phrase. Minimize public personal identifiers in analysis tables; preserve only what is needed to verify evidence. Do not collect private profile information.

Prices retain currency, units, conditions and seller; literature retains DOI and methodological context. Never conflate extraction date with publication or transaction date.

### 14.3 Cleaning and provenance

Retain immutable raw inputs. Normalize in derived copies with scripts. Deduplicate using platform IDs and canonical URLs where possible; identify syndicated posts and quotation/repost relationships. Keep review updates and repeated observations separate where analytically appropriate. Normalize SKU aliases only with documented evidence; do not silently combine benefit lines, package sizes or formulas across countries.

Keep zero, missing, not applicable, not copied, access blocked and not checked distinct. Preserve contradictory values rather than silently selecting one. Counts and provenance must reconcile from retrieval to analysis.

### 14.4 ZIP contents and release checks

The final ZIP will include the research report, actual collected data, permitted raw captures, cleaned CSV/JSON, codebook, literature table, source/claim register, query and collection logs, scripts, dependency versions, cleaning ledger, data dictionary, limitations, README, and checksum manifest. Include failed or partial collection status and spend log where applicable.

Validate CSV/JSON consistency, row counts, IDs, date parsing, missingness, units, duplicates, references, source locators, and all calculations used in the report. Spot-check central claims back to original text. Test ZIP integrity and manifest hashes. Do not distribute session cookies, API tokens, credentials, or unnecessary personal data. Where full source redistribution is unsuitable, retain bibliographic metadata, permitted excerpts and retrieval instructions, and state the omission.

The existing repo has six checksum mismatches consistent with Git CRLF-to-LF normalization. Do not overwrite raw content to make an old manifest pass. Document the release issue; a new release should preserve verified content and have a manifest describing the actual packaged bytes, with deliberate line-ending policy documented separately.

**End-of-chat repository update:** Prepare the complete local update and ZIP for review, then carry out the agreed upload workflow. Do not claim a push has happened until it succeeds. Keep confidential case materials within the intended team access; public publication is not part of this request.

## 15. Completion criteria and fallbacks

The work is complete when every user question and all twelve image questions have a traceable answer or a clear unresolved designation; central mechanisms have rivals and disconfirming evidence; historical explanations are separated from current observations; collected data and failures are documented; and the report, ZIP and repo update are consistent.

If scraping fails, the fallback is an evidence-rich but smaller corpus, a source-based channel/positioning audit, literature review and bounded economics—not fabricated volume. If age/switching cannot be verified, report that explicitly. If historical promotion coverage is sparse, present an event catalogue. If the budget is exhausted, stop new paid retrieval and finish the analysis using actual evidence.

## 16. Historical intake questions — resolved by accepted scope

1. **Timing:** Do you want the first full findings package ready before the 5 November noon WIB submission deadline, or is this an extended research project that can continue afterward? What is your preferred handoff time?
2. **Later Apify budget:** Should the eventual user-run handoff assume the earlier $5 Free-plan credit, or another ceiling? This does not block the assistant-led research; it only changes the later actor/config recommendations.
3. **Existing inputs:** Do you have additional Semrush exports, interviews, or other research to include? Apify will be run by you afterward; no Apify connection, credentials, or session is needed for my research stage. Existing accessible sources will be used even if no further inputs are available.
4. **Geography and comparison:** Which city/area should anchor retailer availability? Is Indonesia-wide context with explicitly local retail snapshots acceptable? Does “Enzymatic” mean Enzim, and are there must-include competitors?
5. **Primary evidence:** Can your team supply short purchase-history interviews or local shelf checks, or should this run rely entirely on public evidence? This materially affects confidence about ages 18–30, household payment and actual downtrading.
6. **Output scope and language:** Should the report teach and diagnose only, or also develop three conditional strategy directions for later selection? Default proposal: clear English with Indonesian consumer wording preserved, plus formal Bahasa Indonesia in any later submission material.

These questions were answered: no timing constraint; Jakarta reference; primary evidence later; diagnosis/teaching with non-fixed strategy directions; $15 total later Apify budget. Existing public tools were used first. Enzim was researched as an explicit comparison, with enzyme-search ambiguity preserved.

## 17. Preliminary source register for tools and source discovery

Checked 3 November 2026. These links support planning and feasibility, not substantive consumer findings. Vendor capability statements remain untested until collection succeeds.

| ID | Source | Planning relevance/status |
|---|---|---|
| T1 | [Agent-Reach official repository](https://github.com/Panniantong/Agent-Reach) and [English README](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md) | Candidate platform wrapper; not installed or execution-tested here. |
| T2 | [Xquik actor README](https://apify.com/xquik/x-tweet-scraper) | Current advertised rate and separate platform usage; no run executed. |
| T3 | [Xquik pricing tab](https://apify.com/xquik/x-tweet-scraper/pricing) | Detailed tier table not exposed in fetched text; verify live billing before use. |
| T4 | [Indexed historical Xquik issue](https://apify.com/xquik/x-tweet-scraper/issues/unexpected-credit-co-dHNgWx4numHDqVBTJ) | Older indexed price discrepancy; issue body unavailable in page fetch; not a current rate authority. |
| T5 | [Zen Studio Shopee reviews actor](https://apify.com/zen-studio/shopee-product-reviews-scraper) | Under maintenance in current page; free-sample restriction and market claims need pilot verification. |
| T6 | [Apify pricing](https://apify.com/pricing) | Platform Free allowance; account balance not checked. |
| T7 | [Apify subscription documentation](https://docs.apify.com/account/subscriptions) | Free-plan usage behavior; separate from actor-specific eligibility. |
| T8 | [OpenAlex API reference](https://help.openalex.org/api/) | Candidate scholarly metadata route; authentication and quota to check. |
| T9 | [Semantic Scholar API documentation](https://api.semanticscholar.org/api-docs) | Candidate scholarly search/metadata route. |
| T10 | [BPS household expenditure publication, September 2025](https://www.bps.go.id/assets/publication/2026/05/29/057b21b35bc236c5ede9d160/pengeluaran-untuk-konsumsi-penduduk-indonesia-september-2025.html) | Dataset/publication discovery lead; tables and exact variable scope not reviewed. |
| T11 | [BPS expenditure variable metadata](https://sirusa.bps.go.id/metadata/variabel/3bf88b6a-eaa5-5ada-82e6-8ab10e95fe5a) | Indexed metadata groups toothpaste with other personal-care goods; inspect applicable survey/year before use. |
| T12 | [Desensitizing toothpastes network meta-analysis, PubMed](https://pubmed.ncbi.nlm.nih.gov/32037944/) | Candidate dental evidence for full appraisal, not yet a reviewed clinical conclusion. |
| T13 | [Desensitizing formulations scoping review, PubMed](https://pubmed.ncbi.nlm.nih.gov/35262559/) | Candidate evidence on formulations and evaluation periods; relevance to behavior must be established separately. |

## 18. Proposed first actions after your answers

Finalize scope; create the dated source/claim registers; inspect and test Agent-Reach and suitable assistant-accessible alternatives; resolve the product taxonomy and competitor names; run the retail/content map and a review/social collection pilot; report what worked and actual usable yield; then scale productive routes. Perform the deep analysis and teaching report using the evidence actually obtained. Afterward, prepare gap-specific Apify actors and ready-to-paste JSON inputs for Fauzi to run. Package the actual data, report and proposed collection configs distinctly, then prepare the repo update. Keep all stages tied to the replenishment decision.

# Version 2: expanded, authorized execution design

The user approved the large research run after reviewing version 1.1. The accepted decisions in `ACCEPTED_SCOPE.md` supersede the earlier questions and deadline-focused scheduling suggestion. This expansion documents the deeper run rather than merely increasing a promised row target.

## A. Six specialist investigations plus an integrating review

| Investigation | Concrete work | What it must not claim |
|---|---|---|
| Access tools and consumer accounts | Inspect Agent-Reach, try public APIs/server-rendered pages, obtain authentic product experience and purchase accounts, record unsuccessful routes | Installing a wrapper means access works; a public commenter is a confirmed young switcher |
| Retail offers | Crawl accessible catalogues, preserve structured product state, compare exact packs/prices and conditional offers | Catalogue listing equals branch stock; marketplace seller equals D2C |
| Brand and campaigns | Build actual product/claim and dated campaign inventories, compare need-matched competitors | Intended positioning equals consumers' received brand meaning; one campaign represents all spend |
| Literature | Retrieve searchable metadata/abstracts, appraise high-value original papers and reviews, identify counterexamples | Category analogies prove Pepsodent-specific behavior; abstract reading equals full-text appraisal |
| History/public data | Recover dated retailer promotions and public indicator definitions, assess trend access and available granularity | Discontinuous flyers become a continuous price history; grouped expenditure becomes toothpaste spend |
| Later Apify handoff | Retrieve official actor metadata, exact input schemas and current plan pricing; prepare minimal user-run gap-filling jobs | An unrun configuration is collected evidence; headline rates establish total costs |
| Integrating review | Resolve shared definitions, deduplicate sources, analyze existing keywords and economics, challenge central claims and package reproducibility | Six agents repeating the same source create six independent confirmations |

This is parallel research, with scope divided by data source and question to reduce duplicated effort. Shared authoritative material is identified explicitly. All source counts will be deduplicated; record counts across different units will never be summed into a consumer sample.

## B. Access escalation ladder

1. Use public primary-source search and open the underlying content.
2. Try direct public HTTP with bounded timeouts, expected content checks and a descriptive user agent; retain status and response artifacts.
3. Inspect ordinary server-rendered JSON and JSON-LD on accessible pages. Treat stock/status fields according to their actual semantics.
4. Use published public APIs for scholarly metadata, product/review data or actor schemas; preserve schemas and pagination evidence.
5. Inspect Agent-Reach's source and dependencies. Test minimal components that add a needed capability, without copying browser sessions or running sweeping installer actions.
6. Use permitted browser interaction only when it adds needed access. A login wall or anti-bot block is recorded; repeated blind retries are not a collection strategy.
7. If those routes fail, produce a smaller documented corpus or a targeted later user-run Apify job. Do not hide failures behind another tool name.

For every path retain requested URL/query, method, timestamp, response status, count or parsing result, tool version, output artifact, and interpretation. An API 200 with an empty shell is not a successful product-data retrieval.

## C. Expanded sampling and stopping logic

The original review/post ranges are aspiration ranges, not a requirement to manufacture volume. Prefer useful coverage across source types, need states, benefit lines, positive/negative experiences, and historical/current windows.

For accessible retailer catalogues, traverse all useful returned pages for the selected brands, with requested and actual page counts logged. Preserve non-toothpaste records separately rather than silently reporting toothbrushes as Premium toothpaste observations. Product variants, listings and price snapshots are distinct units.

For reviews and public posts, separate original material retrieved in full from search-index snippets. A forum thread may contain many comments but one discussion context; do not present it as many independent purchase journeys. Platform-reported total review counts are metadata, not the number of collected review texts. A new capture of a pre-existing keyword file is not new collection.

For literature, automate bibliographic screening breadth where useful, then manually appraise the subset that can change the diagnosis. Search for both support and contradiction. A universal “discounting destroys loyalty” or “more choices reduce conversion” claim should be actively challenged.

Continue collection while a route is adding materially different evidence at reasonable effort. Stop a route when it repeats the same content, cannot verify source identity, supplies irrelevant records, requires unavailable access, or would consume effort better spent validating a consequential claim. Coverage gaps must appear in the release.

## D. Analysis products beyond the initial narrative

- A claim-by-claim evidence ledger, including direct support, rivals, transfer limits, dates and confidence rationale.
- A product hierarchy distinguishing masterbrand, need state, case tier, named line, exact variant, size and observed market.
- A channel map with seller/operator certainty, route to checkout, and verified vs unknown inventory location.
- Promotion-event tables with validity dates and honest reference-price semantics.
- Sensory language codes separating freshness, mouthfeel, taste, irritation, perceived cleaning, visible result and symptom experience.
- A role map separating user, chooser, payer, buyer, stock manager and household beneficiaries.
- Actual purchase-sequence evidence where explicit; otherwise hypotheses for the next interview wave.
- A structured literature evidence table with original DOI/PMID, method, population, reading level and result boundaries.
- Existing-keyword exploration retaining the original 300 observations, missingness and provenance. No summed keyword “market size.”
- Case-based price/gram and household-consumption scenarios; no dosing advice or fabricated manufacturer revenue.
- A counterfactual profit bridge separating total Premium transactions from incremental Pepsodent and Unilever contribution.
- Three conditional strategic directions, each with an evidence trigger, mechanism, operational dependencies, guardrails and disconfirmation criterion.
- A primary-research brief designed after the findings, specifying which remaining uncertainty is worth asking people about.

## E. Claim review before release

The integrating review will ask:

1. Is the claim about the organizer's illustrative case, a new external observation, a public consumer statement, a scholarly finding, or our hypothesis?
2. Does its source directly support that exact population, time window and unit?
3. Has catalogue stock been relabeled physical availability, search interest relabeled preference, or sensory experience relabeled clinical efficacy?
4. Is a current observation being used to explain a historical decline without a dated link?
5. Does the strongest rival explain the observation just as well?
6. Is a numerical result reproducible from retained rows/formulas?
7. Could a duplicated source, syndicated article, creator cluster or repeated user inflate support?
8. Are quotation and full-text redistribution kept proportionate, with links and metadata where full documents are unsuitable?
9. Are failed extractions, absent fields, contradictory reports and unverified actor limits recorded?
10. Has any proposed strategy become a selected recommendation without the user's decision?

Review is scaled to consequence. Main causal conclusions require stronger scrutiny than descriptive catalogue counts.

## F. Release and later integration

The release will distinguish three datasets: existing supplied material; newly retrieved external evidence; and proposed future collection configurations. No fictional portraits from the earlier AI learning document enter the public-consumer corpus.

The user receives the report, expanded plan and a ZIP containing the actual research tree plus reproducibility instructions. A full repository snapshot can additionally include the original handoff for manual upload; it must exclude Git internals, authentication material and transient tool environments. Report and package counts must agree with a machine-generated inventory.

Returned Apify exports or team interviews become a subsequent version. Preserve their original files, record collection method/time/cost, update the evidence ledger, and change affected conclusions explicitly. Do not silently merge convenience public reviews, recruited eligible respondents and model annotations into one pooled sample.


# Version3 scale extension: completed execution

The user explicitly requested much larger collection, ideally millions of records, and then requested that setup be handled by the assistant. This extension used actual public source APIs, full selected review pagination and streamed public research datasets. It did not require a user-run Apify job.

The executed design screened26,125,466historicalAmazonreviewrows plus857,856productmetadatarows, retaining title-matched candidates in scoped classes and deduplicating derivedidentityfingerprints. It deliberately distinguishes processing volume from relevantretention. The internationaladult-titlewritten subset is196,872; it is not Indonesianyoungswitcherevidence. The integrated writtenstore has298,846canonical records/fingerprints acrossallretainedscopes, alongside a separate six-postXtable. Detailed finalcounts/limits are in the report and machineinventory.

Collection expanded selectedWatsonshistories to10,191rating/reviewIDs(7,419written), selectedTryandReviewhistories to1,423IDs, ORESAcampaigns to2,228IDs and targetedRedditarchivecomments to389. Original smaller corpora remain preserved; preferred expanded records replace overlapping versions in the unifiedstore. Ratings-only/blank rows remain in sourcefiles but do not inflate written-textcounts.

A reusablePythonstandardlibrarySQLitepipeline now supports streamingJSONL/gzip, checkpoints, sourceversions, canonicalidentitydedup, payloadvariationprovenance, copied-textflags, scopedCSV/JSONLexports and boundedGETcollection. Its million-recordstorageprojection is calculated from actualrecordbytes; it is not a forecast of available eligible respondents or retrievaltime. SQLite is rebuildableintermediate; the portablecompressedexports and sourceinputs are the deliverable.

The tool investigation assessedPythonclients and originalsourcecode, tested publicRedditarchive/XHTML routes and recordedblocked/obsolete paths. Agent-Reach alone did not guaranteeaccess. The user-suppliedreverse-api-engineer repository was separately inspected as tooling/referencecontent; its instructions do not authorize accountaccess or blindly executinginstallers. See the finaltool audit.

Stop conditions were sourcecompletion, exactcountreconciliation, zero/blockedoutput, decliningrelevance or lackofcredentials. Millionsofunrelatedelectronicsrows were not added to toothpasteevidence;209,187suchresearchdatasetrows were screened and rejected. No paidactor was run and no userconfiguration was required for the completedrun.
