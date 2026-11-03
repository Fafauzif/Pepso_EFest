# Complete substantive session handoff — 3 November 2026

This file reconstructs the substantive visible conversation and accepted decisions. It is not a verbatim platform export and cannot recover unavailable messages, hidden state, missing attachments, or browser/account sessions. Read START_HERE.md in the repository root first. The original context pack and earlier reports remain available; this supplement supersedes their current-state claims where specifically noted.

## The user and intended way of working

The team is working on the Economics Festival 2026 Pepsodent case. User Fauzi wants thoughtful diagnosis, teaching, competing explanations and possible strategy directions, not a fixed campaign prematurely chosen. The user supplied https://github.com/Fafauzif/Pepso_EFest and requested a clone for context. The baseline commit is 423cce08921b611fd01fbf6d25a0f86b65986f76. A final git ls-remote check returned that same HEAD/main. The user confirms no newer local/team edits and intends the repository to be private. The assistant does not set remote visibility, push commits, publish a site, or submit competition work.

The user asked for unusually extensive secondary research, actual data collection, a detailed Markdown output, and a downloadable data/code archive. They explicitly requested subagents, broad tool exploration, Agent-Reach or equivalents, scraping libraries, and examination of reverse-api-engineer. They preferred assistant-led public collection to manual setup, with Apify as a later optional route. They asked for corpus numbers, then executed Apify runs themselves and returned their exports. The user decided the available secondary evidence is sufficient to move toward hypothesis synthesis and primary-research design. No more bulk/paid collection is needed for this closure release.

Final user decisions: private team repository; English analysis with Indonesian fieldwork tools; actual fieldwork access uncertain; package all available relevant research and context; user will use GitHub Desktop and extract/replace into the clone; final ZIP should be uploaded to Filebin. All relevant Markdown context files must travel with the package so a new assistant can continue. This requirement is addressed with this file, the original context pack, CURRENT_STATE, the original and new research reports, a source register, and a resume prompt. A new assistant must actually read those files; cloning alone does not import a chat or authenticated services.

## Case and measurement anchor

Target: young adults aged 18–30 described in the case as moving from Pepsodent Premium toward Basic. The case horizon ends H1 2026; the supplied case reports Premium mix/share moving from 27% in 2022 to 20% in H1 2026. Preserve the original case's denominator and wording before doing math. It is not demonstrated that seven percentage points equals seven percent fewer premium buyers or an individually observed transition. Premium sales, Basic growth, realized price, packs, channels and denominator mix are competing accounting explanations.

The original case, guidebook, manually transcribed chart values, mentoring notes and teaching material are retained in context/E_Fest_2026_Pepsodent_Master_AI_Context_Pack.md and sources/transcripts/. Transcripts are not original PDF facsimiles. Some requested original PDFs and a pasted input were never supplied; docs/MISSING_INPUTS.md remains authoritative about their absence.

## Questions and intuitions the user wants examined

The central intuition is toothpaste as a replenishment business. The value chain includes formulation, manufacturing, distribution, retail, use and replenishment. Consumers can choose only among available alternatives at the shopping occasion. The user initially suspected premium Pepsodent might be difficult to find in ordinary Alfamart/Indomaret and wondered whether this implies D2C; the earlier research found historical minimarket promotions, so broad absence is unsupported. Online existence still does not establish exact branch/SKU stock.

The user asks how Pepsodent promotes premium products, what positioning it takes, where campaigns run, how it differs from brands such as Enzim and Closeup White Now, and what Pepsodent embodies in a sentence. Premium benefits should be understood against existing brand meaning rather than an invented identity. Retailers may favour fast-turning products even when the manufacturer seeks premium mix, but that remains an unverified mechanism.

Sensory questions include aftertaste, felt cleanliness, freshness, foam, dryness, irritation and what a noticeable result means. Felt cleanliness is not equivalent to clinical benefit. The user's informal reference to enzymatic toothpaste should not be silently equated with every enzyme-containing product or every Enzim formulation.

Affordability questions include inexpensive acquisition versus expensive repeated use, discounted trial followed by Basic, small packs and grams, price per gram versus refill cash outlay, and what repeated discounting means. A promotion can coexist with loyalty; observing a discounted listing does not identify incrementality, willingness to pay, or price elasticity.

Purchase-occasion questions: What ran out? Who noticed? Who chose? Who paid? Who used it? Which alternatives were available? What price was actually paid? What happened afterward? The user notes their own toothpaste is bought by parents. A student may prefer premium while following a family tube; starting independent purchasing may change budget and control simultaneously. One specialist user may share a tube with several people. The direction of household influence can differ by situation.

Other hypotheses: sensitivity relief is interpreted as a reason to stop treatment; a preferred variant is hard to find and substitution becomes habitual; a premium benefit feels temporary or one-off; variant choice feels complicated and Basic is an acceptable default. These remain hypotheses unless actual purchase sequences establish them. Basic may be rationally sufficient for some people.

The user also asks for public/indirect datasets, product reviews, social listening on X/Threads, literature, historical promotions, and evidence-backed estimates where direct data are missing. The specific challenge is sustaining or returning to premium, not simply recruiting more first-time premium trialists. Large-scale collection was explicitly requested, but count inflation is not an acceptable substitute for relevance.

## The 12 business-leader questions in the supplied image

1. What actually deteriorated: revenue, volume, realized price, penetration, repeat, contribution, or only sales share?
2. Which variants, channels, cohorts and purchase situations explain the change?
3. What did former Premium buyers choose at the last replacement and why was it better for them?
4. How much demand survives without deep discounts?
5. What does Basic do sufficiently well, and for whom is it a rational final choice?
6. Who uses, chooses and pays in the households we want to influence?
7. Is the failure one of relevance, selection, experience, affordability, availability or measurement?
8. Which explanation would most change the decision if true?
9. What observation would make us abandon a preferred explanation?
10. How much growth is incremental to Pepsodent, Unilever and the category?
11. Which social outcome could improve and what would demonstrate improvement?
12. What must be true economically and operationally for a concept to create value?

These are analysis prompts, not additional empirical observations. Updated answers are in closure/synthesis/DIAGNOSIS_AND_TEACHING.md; unresolved items stay unresolved.

## Assistant-led collection before the user-run Apify exports

The earlier release contains a full retained research pack, approximately 402.5 MB zipped. It includes original keyword data and context plus public-HTTP/API and server-rendered collections, literature appraisal, retail/campaign/history observations, tools and reproducibility notes. Its report is research/2026-11-03/REPORT_FULL.md. Do not confuse its final extension with the earlier smaller first-phase counts.

The integrated earlier written store has 298,846 platform records: Amazon external context 286,706; Watsons 7,419; Lazada 681; ORESA 2,228; TryandReview 1,423; Reddit 389. There are 301,526 source written occurrences and 2,680 repeated identity occurrences. Rating-only/missing-text exclusions are separately recorded. The Watsons raw collection includes 2,772 rating-only records; their existence is preserved without calling them written reviews. The separate six-post public-X sample is checked against new X observations rather than blindly added.

The Amazon pass screened 26,125,466 review rows plus 857,856 metadata rows. It retained candidate observations and written records; the full upstream millions were not downloaded into this repo. Of retained written title candidates, 196,872 are classified adult/general toothpaste candidates, not verified adult users. Adjacent products, accessories, children/pet candidates and known title-classification errors remain flagged. International evidence is separate from the Indonesian case and cannot determine the target cohort's behaviour.

Earlier research also retained 96 retail offer contexts, 53 usable brand pages, a 28-product-page subset, 18 curated campaign observations, 12 historical promotion events, 8 health-indicator rows, one BPS definition, 148 literature candidates with 25 retained appraisals (21 abstract-level and 4 relevant-full-text-section reads), and 300 original keyword rows. These are overlapping/different units and must not be summed as people or reviews.

Important prior corrections: Sensitive Expert 100 g appeared in official Indomaret regional flyers at 19,900 against 39,900 in June/July 2025; 160 g premium listings and small-pack options already exist; Pepsodent already has ShadeScan AI, specialist education, Halodoc-linked activity and sampling history. Generic education/scanner ideas need a specifically demonstrated unmet mechanism. Incentivized ORESA/TryandReview sources cannot be treated as representative organic users. Retail listing, price observation and actual local shelf availability are different things.

## Tools actually investigated

Working public routes included Watsons paginated review/catalogue APIs, Lazada server-rendered data, ORESA JSON, TryandReview pagination, ArcticShift Reddit trees, known-URL X HTML and streaming public Amazon files. Agent-Reach source was inspected and a backend tested; a nominal Reddit response was a block page. snscrape failed with a Python 3.12 importer issue; ntscraper returned a Nitter notice and zero posts. Failed routes are documented, not positive evidence or hidden collections.

The user supplied https://github.com/kalil0321/reverse-api-engineer. Source at commit c644f8af453136ac69489370d6c581d89b9e1bf9, version 0.14.0, was statically inspected and 34 Python files parsed. It was not installed or run, and no model/session capture/spend is claimed. The method overlapped with public request inspection already used successfully. Google Trends returned 429; no historical series was invented.

The assistant did not execute paid Apify runs. The following runs were user-executed; their returned datasets are primary source files for the closure integration, not primary field interviews.

## User-run Apify sequence and accounting

The team has three separate Free accounts with $5 credits each. Credits are not pooled. X was initially assigned one account; a friend's account handled TikTok. Later e-commerce jobs could run on either account. Last user-reported active account usage was $3.79/$5.00; last separately reported TikTok usage was $2.97/$5.00. These are user reports, not live authenticated billing checks. Do not infer the unused third account's balance or compute platform charges from dataset fees alone.

X actor: xquik/x-tweet-scraper. Four exported datasets have 100, 957, 8,468 and 6,640 rows respectively, totalling 16,165 source rows and 12,990 post IDs before reconciliation with the old six-post sample. The final run contributed 4,112 IDs not seen in the earlier three. Retweets were excluded in the recommended inputs; inspect record flags rather than assume every export setting. The 8,468-row run log showed exhausted small search branches and two branches hitting per-target caps; falling short of an overall requested count did not automatically establish a failed run. The user broadened search and added early-year slices. Irrelevant ODOL trucking, jokes/figurative smiles, affiliate copy, brand posts and international ambiguity require filtering. Current captured actor pricing was $0.00015 per post plus platform usage; old price claims were corrected in the prior audit. Future prices require a fresh check.

TikTok actor: clockworks/tiktok-comments-scraper. The user supplied 18 vt.tiktok.com links; redirect mappings and expanded URLs are retained. Recommended main input requested 180 comments per post, top-level 150, max 2 replies per comment. The export contains 2,380 comment IDs across all 18 videos, 699 replies and 8 blank texts. Using Asia/Jakarta dates, 1,648 comments fall in 2022–June 2026, 251 before 2022 and 481 after H1 2026. The earlier 1,649/251/480 counts used UTC; one comment crosses midnight at the H1 boundary, and both conventions are retained in the source analysis. Eight videos hit 180. The captured Free price was $1.25/1,000 comments, not the lower headline business-tier price. Video date and comment date are distinct. Original post captions, commercial intent and author demographics must not be guessed where unavailable.

Shopee actor: scrapewise/shopee-reviews-scraper. The intended pilot used two product URLs for Sensitive Expert and Enzim, 20 reviews each and written comments only. It returned two NO_REVIEWS_FOUND errors, reporting scans of 2,130 and 3,193 shop reviews with no matching accessible product reviews. These scanned rows were not delivered and are not part of our corpus. Raising maxReviews would not bypass the reported accessible-history limitation. The error output said reviews were not charged; startup/platform cost is not established by that statement.

A second Shopee export returned 100 UGREEN electronics reviews from shopee.sg/shop/64922680: 23 nonempty comments and 77 rating-only entries. It matched the actor's default example and was excluded. The user confirmed using the wrong actor/input. It demonstrates a technical output but contributes no toothpaste evidence. Keep the file and failure explanation; never add it to case counts.

Tokopedia actor: lergassy/tokopedia-reviews-scraper. The first intended run used keyword search for Pepsodent Sensitive Expert, Pepsodent Ultra White and Sensodyne Repair Protect; 2 products per term and 10 reviews per product. It returned 6 product rows, 43 review IDs and one billing notice. The next run expanded to six queries (adding Basic anticavity, Enzim Fresh Mint and Closeup White Now), 3 products per term and 50 reviews each. It returned 18 product rows, 266 review IDs and one notice. All 43 pilot IDs are in the later export. There are 263 nonempty texts in the later file and 256 five-star ratings. The notices report event charges $0.0735 and $0.426; these do not establish the change in total account usage.

Product cards, reviews and notices are distinct units. Sprays/giveaways, generic logistics praise, premature before-use ratings and a likely misassigned body-odour comment need specific eligibility flags. Among the latest reviews, 198 have both date fields and 186 of those disagree; another 68 lack reviewTime. A preliminary 254/266 comparison incorrectly counted missing fields as conflicts and is superseded by this correction. Retain both fields and the original relative label. The new platform analyses provide the final reconciled analytical counts, not this preliminary chronology. Final new close-reading annotations total 294 (109 X, 100 TikTok, 85 Tokopedia), with separate random-calibration and purposive selection labels.

## What the new evidence changes

Examples worth investigating include TikTok cid7552195449504547585, describing parent-funded Sensodyne at home versus a 50k outlay when boarding. It supports a plausible payer transition, but does not identify a verified 18–30 Pepsodent Premium-to-Basic switcher. Tokopedia review1932700850 reports Ultra White repurchase because it fits; Sensodyne2145103290 reports benefits as a reason to stay rather than stop. Enzim loyalty alongside requests for promotions challenges a simple discount-versus-loyalty dichotomy. Delivery complaints are not product failure; five stars are not proven post-use satisfaction.

The next useful evidence is actual recent purchase history among confirmed target/contrast participants. Public records can reveal wording, plausible mechanisms and counterexamples, but not the prevalence or causal share of the case decline. No final strategy, verified primary sample, recruitment, fieldwork, experiment, normal-price retention estimate, or causal forecast exists.

## Final handoff architecture

The final package retains all available prior research and new inputs, preserving original raw/master files. New raw JSON uploads are archived as .json.gz; decompression reproduces exact original bytes verified in closure/raw/UPLOAD_REGISTER.json. SHA-256 and zero-based JSON array locators trace annotations to original records. Clean views omit unnecessary profile detail while private raw records remain traceable.

Large legacy files may be stored as lossless byte parts to keep every Git file below the size target; release/LARGE_FILES.json and scripts/restore_large_files.py explain exact reconstruction. Ordinary analysis uses the new portable master shards. Do not commit the outer delivery ZIP, rebuilt SQLite databases, .git, credentials or environments. User actions: extract ZIP outside the clone, copy contents of the enclosed Pepso_EFest folder into the existing repo root, replace overlaps, review Desktop diff, commit and push. Filebin is temporary; the repo and downloaded archive are the lasting copies.

Primary tools are designed for uncertain access: two pilots, initial 8–12 substantive interviews, contrasting purchase histories and cross-cutting payer/shared-use roles, optional near-replenishment follow-up, a later survey bank. Counts are practical starting points, not saturation or statistical claims. Fieldwork documents are in Indonesian; teaching and analysis are in English.

## Resume prompt

> Read AGENTS.md, START_HERE.md, context/CURRENT_STATE.md, research/2026-11-03/closure/context/SESSION_HANDOFF.md, and closure/synthesis/DECISION_BRIEF.md. Then read the hypothesis matrix and primary-research kit. Use the original master only for historical case/guidebook context, and source-linked evidence for claims. Confirm the actual clean-data inventory, case-period and incentive limits, and current unresolved hypotheses. No final solution or causal allocation is selected; no primary interviews exist. My next task is [insert task].
