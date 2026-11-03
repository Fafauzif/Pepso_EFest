# Decision-linked evidence ledger

This is an analyst claim ledger. Source reports and row-level annotation tables retain exact text and provenance. Evidence types and limitations are not interchangeable. No row establishes population prevalence or authenticated target switching.

## E01: Metric definition

The case reports Premium share moving from 27% to 20%; absolute revenue, volume and retention remain unresolved.

- Type: organizer_case
- Locator: `Case transcript lines149ff`
- Source: [../../../../sources/transcripts/Case_Study_Transcript.md](../../../../sources/transcripts/Case_Study_Transcript.md)
- Limit/rival: Organizer premise, not consumer observations.
- Decision: Define comparable-period denominators and the sales bridge.
- Hypotheses: H11

## E02: Accounting scenario

With a hypothetical comparable total rising from 100 to 135, a 20% share leaves Premium at 27, equal to the initial 27.

- Type: derived_arithmetic
- Locator: `case_economics.json`
- Source: [../../synthesis/case_economics.json](../../synthesis/case_economics.json)
- Limit/rival: Requires a revenue-share interpretation and comparable periods; not actual company growth.
- Decision: Do not equate share decline with the same decline in revenue.
- Hypotheses: H11

## E03: Case affordability

Case examples: Basic 190 g at Rp24,100; Sensitive Expert 100 g at Rp41,900 or promotional Rp23,500. Premium unit-price ratios are approximately 3.30 and 1.85.

- Type: organizer_case_and_derived
- Locator: `case_economics.json`
- Source: [../../synthesis/case_economics.json](../../synthesis/case_economics.json)
- Limit/rival: Illustrative SKU prices, not portfolio averages or manufacturer realization.
- Decision: Separate checkout affordability from sustained unit cost.
- Hypotheses: H02;H08;H09;H10

## E04: Historical channel presence

An official Indomaret regional flyer advertises Sensitive Expert 100 g at Rp19,900 against Rp39,900 in June–July 2025.

- Type: first_party_document
- Locator: `26Jun–9Jul2025; PDFp18 printedp16`
- Source: [../../history_publicdata/promotion_events.json](../../history_publicdata/promotion_events.json)
- Limit/rival: Specified edition and period; branch stock was not verified.
- Decision: Narrow absence claims to exact-SKU and local replacement questions.
- Hypotheses: H03

## E05: Existing packs

Current 100 g and 160 g Sensitive Expert offers and a 60 g minimarket catalogue listing exist.

- Type: catalogue
- Locator: `WATAPI-PEPSODENT-005;-031;minimarket indexedcapture`
- Source: [../../retail/findings.md](../../retail/findings.md)
- Limit/rival: Current catalogue evidence; no verified Jakarta checkout stock.
- Decision: Check awareness and access to existing packs before proposing a new one.
- Hypotheses: H02;H03;H09

## E06: Marketing already exists

Beauty/fashion, professional support, self-check, ShadeScan, science explanation and sampling routes are documented.

- Type: first_party_brand_audit
- Locator: `Brand artifact IDs in findings`
- Source: [../../brand_campaigns/findings.md](../../brand_campaigns/findings.md)
- Limit/rival: Existence is not effectiveness; current materials may postdate the case.
- Decision: Specify the missing mechanism before proposing an existing type of execution.
- Hypotheses: H04;H07

## E07: Household payer transition

A commenter contrasts parent-purchased Sensodyne at home with concern about paying 50k when living in a kos.

- Type: public_self_report
- Locator: `TikTok 7552195449504547585; original row 1861`
- Source: [../tiktok/qualitative_evidence.json](../tiktok/qualitative_evidence.json)
- Limit/rival: Age, pack, actual paid price and next purchase are unknown; not a Pepsodent switch.
- Decision: Ask who funded the last replacement and whether the payer changed.
- Hypotheses: H01;H02

## E08: Household authority plus sensation

A commenter reports parental limits on changing brands and dry/acid sensations with dark Pepsodent while a white product felt acceptable.

- Type: public_self_report
- Locator: `TikTok 7425778994514150149;original row 2216`
- Source: [../tiktok/qualitative_evidence.json](../tiktok/qualitative_evidence.json)
- Limit/rival: Exact SKU, tier and clinical cause are unknown.
- Decision: Separate authority, experience and money.
- Hypotheses: H01;H06

## E09: Competitor return

A commenter reports no perceived sensitivity relief with Pepsodent and improvement after returning to Sensodyne.

- Type: public_self_report
- Locator: `TikTok 7425822711702553350;original row 681`
- Source: [../tiktok/qualitative_evidence.json](../tiktok/qualitative_evidence.json)
- Limit/rival: Unspecified Pepsodent variant; no clinical comparison or Basic replacement sequence.
- Decision: Probe the exact need, product, experience and next choice.
- Hypotheses: H04;H06

## E10: Whitening-to-ordinary account

A commenter describes discomfort during daily whitening use and changing to ordinary toothpaste.

- Type: public_self_report
- Locator: `TikTok 7581114937188221704;original row 2012`
- Source: [../tiktok/qualitative_evidence.json](../tiktok/qualitative_evidence.json)
- Limit/rival: Brand is unknown; symptoms are self-attributed and target eligibility is unverified.
- Decision: Retain adverse experience as a rival to a pure-price explanation.
- Hypotheses: H06

## E11: Actual stated Premium repurchase

An Ultra White reviewer explicitly reports buying again because the product fits: beli lagi krn cocok.

- Type: product_review_self_report
- Locator: `Tokopedia 1932700850;originalmain row 40;2026-02-18`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Paid price, age and the meaning of cocok are unknown; source date is unverified.
- Decision: Recruit retained Premium countercases and ask what fit means.
- Hypotheses: H04;H06;H10

## E12: Benefit sustains use

A Sensodyne reviewer links experienced benefit with not wanting to change toothpaste.

- Type: product_review_self_report
- Locator: `Tokopedia 2145103290;main row 133;2026-06-10`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Competitor account; stated commitment is not longitudinal verified retention.
- Decision: Challenge an inevitable stop-after-relief narrative.
- Hypotheses: H05

## E13: Long use and repeat

A Sensodyne reviewer describes longstanding use, benefit and repeat ordering.

- Type: product_review_self_report
- Locator: `Tokopedia 2177591268;main row 125;2026-06-30`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Self-report; price and target age are unknown.
- Decision: Examine why a benefit remains worth funding.
- Hypotheses: H05;H08

## E14: Loyalty and deal coexist

A longstanding Enzim user describes finding a TikTok bundle discount and valuing a comfortable low-foam experience.

- Type: product_review_self_report
- Locator: `Tokopedia 1469837237;main row 256;2024-05-14`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: No verified paid-price sequence or causal promotion effect.
- Decision: Do not classify promotion interest as weak loyalty.
- Hypotheses: H06;H08

## E15: Comfort plus promotion request

An Enzim reviewer describes continued use because other toothpaste feels unpleasant, while requesting more promotions.

- Type: product_review_self_report
- Locator: `Tokopedia 2310809324;main row 169;2026-09-19`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Post-case context; reported mouth ulcers do not establish clinical cause.
- Decision: Separate fit from funding and preferences for deals.
- Hypotheses: H06;H08

## E16: Pack expectation

A reviewer expected a larger pack but received two small ones.

- Type: product_review_self_report
- Locator: `Tokopedia 2191122942;main row 179;2026-07-08`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Post-case example, not a general pack-perception rate.
- Decision: Check what buyers notice about grams, count and duration.
- Hypotheses: H02;H09

## E17: Basket minimum

An Enzim reviewer objects to a minimum checkout quantity of three while wanting to try other flavours.

- Type: product_review_self_report
- Locator: `Tokopedia 2105728218;main row 186;2026-05-19`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Single checkout report, not a verified market-wide policy.
- Decision: Test basket constraints separately from unit price.
- Hypotheses: H02;H07;H08

## E18: Rating before use

An Ultra White four-star review says the product has not been tried; a five-star review says results are not yet known.

- Type: product_review_self_report
- Locator: `Tokopedia 2127271766;2121981403;main row s21,22`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Selected examples, not a percentage estimate of satisfaction.
- Decision: Read the prose before treating ratings as performance evidence.
- Hypotheses: H04

## E19: Low rating delivery

One-star non-arrival, two-star slow delivery and three-star packing complaints concern fulfilment.

- Type: product_review_self_report
- Locator: `Tokopedia 845969659;2346136191;2337020302`
- Source: [../tokopedia/qualitative_evidence.md](../tokopedia/qualitative_evidence.md)
- Limit/rival: Complaint truth is not independently verified.
- Decision: Separate fulfilment from toothpaste experience.
- Hypotheses: H03;H06

## E20: Independent purchase rival

After starting work, a writer reports changing from a censored Pepsodent name to a more expensive toothpaste and experiencing fewer mouth ulcers.

- Type: public_self_report
- Locator: `X 2015590249167274297;second export row 8;2026-01-26`
- Source: [../x/evidence.jsonl](../x/evidence.jsonl)
- Limit/rival: Exact variant, target age and clinical cause are unknown; the brand name is censored.
- Decision: Independence can enable uptrading as well as downtrading.
- Hypotheses: H02;H06

## E21: Sensory retention without visible effect

A writer reports months without an apparent difference but continues because the product feels comfortable and does not coincide with mouth ulcers.

- Type: public_self_report
- Locator: `X 1600113707526524928;fourth export row 371;2022-12-06`
- Source: [../x/evidence.jsonl](../x/evidence.jsonl)
- Limit/rival: Missing parent-product context; not a Pepsodent performance claim.
- Decision: Retain nonvisual value and counterexamples.
- Hypotheses: H04;H06

## E22: Replenishment sequence

A writer reports running out, changing paste, perceiving colour return, and using the earlier product again.

- Type: public_self_report
- Locator: `X 1540355497089728512;fourth export row 5812;2022-06-24`
- Source: [../x/evidence.jsonl](../x/evidence.jsonl)
- Limit/rival: Unidentified product and unverified appearance effects.
- Decision: Observe what happens afterward rather than assuming permanent abandonment.
- Hypotheses: H03;H04;H05

## E23: Retrospective household price authority

A childhood Closeup request was refused; the writer later interprets the mother’s Ritadent choice as an attempt to spend less.

- Type: public_retrospective_account
- Locator: `X 1927222520979058832;first export row 37;2025-05-27`
- Source: [../x/evidence.jsonl](../x/evidence.jsonl)
- Limit/rival: Retrospective memory, not a current target switcher or a verified explanation from the payer.
- Decision: Use as a household-role prompt, not a prevalence estimate.
- Hypotheses: H01

## E24: Household specialist rival

Shared Systema use is described as partly motivated by the mother’s comfort with sensitivity.

- Type: public_self_report
- Locator: `Redditjn2d5tk`
- Source: [../../scale_reddit/findings.md](../../scale_reddit/findings.md)
- Limit/rival: Not Pepsodent; age and payment are unverified.
- Decision: Sharing can justify a specialist choice.
- Hypotheses: H01;H09

## E25: Satisfaction with availability friction

A Lazada account combines product fit, bundle savings and reported availability difficulty.

- Type: product_review_self_report
- Locator: `LZD-1574262094522499;2025-04-11`
- Source: [../../access_reviews/clean/lazada_reviews.json](../../access_reviews/clean/lazada_reviews.json)
- Limit/rival: Historical continuity of the listing title is uncertain; no target switch is verified.
- Decision: Allow price, fit and access to interact.
- Hypotheses: H03;H08

## E26: Until-resolved expectation

A Lazada writer expects to keep trying until sensitivity resolves.

- Type: product_review_self_report
- Locator: `LZD-1200640450822499;2023-07-01`
- Source: [../../access_reviews/clean/lazada_reviews.json](../../access_reviews/clean/lazada_reviews.json)
- Limit/rival: Expectation or intention; subsequent stopping is unobserved.
- Decision: Do not turn an expectation into actual discontinuation.
- Hypotheses: H05

## E27: Different success rules

Selected reviews include favourable overall ratings without visible change, sensory appreciation and a positive whitening rival.

- Type: selected_review_examples
- Locator: `TAR-117079;TAR-160280;TAR-161537;TAR-254032`
- Source: [../../scale_reviews/findings.md](../../scale_reviews/findings.md)
- Limit/rival: Incentives, subjective outcomes, product and date limits apply.
- Decision: Ask what counts as success and what was actually purchased next.
- Hypotheses: H04;H06

## E28: Choice is conditional

Choice-overload meta-analyses identify heterogeneity and moderators.

- Type: retained_external_literature
- Locator: `LIT001;LIT002`
- Source: [../../literature/findings.md](../../literature/findings.md)
- Limit/rival: Mostly abstract-level appraisal; not a local causal estimate.
- Decision: Observe actual comparison before prescribing fewer SKUs.
- Hypotheses: H07

## E29: Promotion rivals

Cohort composition and new-versus-established customer results challenge universal discount pessimism.

- Type: retained_external_literature
- Locator: `LIT003;LIT004;LIT005;LIT006`
- Source: [../../literature/findings.md](../../literature/findings.md)
- Limit/rival: Different categories and methods; not transferable toothpaste effect sizes.
- Decision: Compare cohorts, timing, quantity and the counterfactual.
- Hypotheses: H08

## E30: Sensory versus measured outcome

A formulation trial separates sensory ratings from measured plaque and gingival endpoints.

- Type: retained_external_literature
- Locator: `LIT013;LIT014`
- Source: [../../literature/findings.md](../../literature/findings.md)
- Limit/rival: Formulations differ beyond SLS; funding and population limits apply.
- Decision: Do not equate foam or mint with clinical cleaning.
- Hypotheses: H06

## E31: Discontinuation clinical rival

An exploratory episodic CSPS study does not establish inevitable rapid relapse.

- Type: retained_external_literature
- Locator: `LIT024`
- Source: [../../literature/findings.md](../../literature/findings.md)
- Limit/rival: Limited improvements, power and funding caveats; not a buyer-retention study.
- Decision: Investigate behaviour without inventing clinical dependence.
- Hypotheses: H05
