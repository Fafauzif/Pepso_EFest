# Current Pepsodent project state after survey analysis

Updated 4 November 2026, Asia/Jakarta. Base repository commit: `a9c168a718f20b13097ae82488c77815958521d5`.

This update supersedes earlier status statements that no primary survey results or recommended solution exist. It preserves the case facts and source limitations. The recommendation is a team working proposal, not a company-approved or experimentally validated program.

## Current deliverables and reading order

Read the detailed English analysis at `research/2026-11-04/survey_results/analysis/Pepsodent_Survey_Analysis_and_Strategy.md`, then the Indonesian report in `documents/Pepsodent_Executive_Summary_and_Appendices.docx`. The Word document contains three main pages, two reference pages and 28 appendix pages. Its 12 figures show the measured survey relationships, mechanisms and explicitly modeled economics. It follows the supplied Nexora report’s restrained publication style rather than a slide deck.

Source references and transfer limits are in `sources/references_apa.json` and `sources/benchmark_sources.json`. Survey aggregates are in `data/aggregates`; the scenario calculator is in `model/model.py`; the private-input reproducer is in `scripts/analyze_survey.py`. The supplied screenshot business content, personas, competitor scores and watermarks were not reused.

The requested outputs are a Markdown analysis, an executive-summary DOCX and this repository overlay ZIP. No PDF submission, official declaration, team identity or logos were created. Team/member details, permitted official logos, final PDF and competition declarations remain to be added by the team. The original competition asks for three alternatives, selection of one, six Ps and an Indonesian main summary of at most three pages.

## Primary evidence now received

The uploaded workbook contains 50 submitted records and 49 included accounts; one under-18 submission is excluded. Inclusion was checked using consent, age, Indonesia-use, completion and collection-phase fields, with substantive raw/CLEAN reconciliation. All 49 included respondents are in education: 42 study and seven study while working. Forty are aged 18–20 and nine aged 21–24; none are aged 25–30. This is an exploratory student convenience cohort, not a nationally representative youth sample.

Twenty-nine acquisition months are known: 27 fall in August–November 2026 and two in August 2025. The majority of dated events postdate the case’s H1 2026 endpoint. They inform mechanism design but do not independently explain the historical seven-point Premium share decline.

The workbook’s RINGKASAN tab formats ten count cells as Excel dates. Counts were recomputed from response rows. Five included records have automatic quality flags. An approximate price of Rp190 for an 85 g pack is an additional unresolved anomaly. No silent multiplication, replacement, or deletion was used. Price certainty and gram/pack ambiguity prevent a defensible elasticity, willingness-to-pay or unit-price index. The manual REVIEW tab is empty, and no verified Premium-to-Basic migration rate was established.

## Findings that change earlier hypotheses

The strongest finding is role separation within a single acquisition. Thirty of 49 choose personally, 31 shop personally, and 41 report family funding. Twenty-four of 30 self-choosers use family money. Crucially, 23 of 49 choose AND shop personally while family supplies the money. Twenty-one of 25 people living alone or in kos also use family money for this toothpaste acquisition. These fields do not measure all living expenses, income, household veto or general financial independence. Self-shopping is therefore the principal execution route; forwarding a choice to a parent is optional rather than the default intervention.

Manual desired-product coding yields 31 explicit no-preference accounts, 12 named brands or variants, three dash placeholders, two functional requirements and one vague evaluation. Among the 31 with no specific preference, 22 nevertheless report obtaining the product they wanted. Overall fulfillment of 34/49 is not verified exact-SKU fulfillment or evidence of a valued specialist preference. Acceptable default use may be a rational endpoint. The pattern persists under quality-flag and recall sensitivities.

The strict matched category subset has 21 accounts: ten compare both categories, six only the other category, three only toothpaste, and two neither. Toothpaste comparison is 13/21 versus 16/21 for other care; the within-person difference is 14.3 percentage points and the exact discordance test is p = .5078125. The six other-only accounts split into three skincare and three haircare. Among 16 high-recall pairs, discordance narrows to three versus two. Do not turn this into a universal skincare-versus-toothpaste insight, a wealth signal, or toothpaste willingness to pay.

Prompted reasons are capped at three selections: available-money fit 30, habit 28, comfort 23, specific benefit 15, promotion/value pack 15. Nineteen combine money fit with habit. Eight of 15 specific-benefit selectors do not compare toothpaste; eight of 28 habit selectors do compare. Habit can preserve a successful specialist choice. Twenty value the previous product’s benefit, but they are not 20 lapsed Premium users.

Thirty-seven report a depleted or nearly depleted previous tube, seven alternate products, two stopped while product remained, one temporarily uses something else, and two cannot recall. Only two report failed search. Neither supply failure nor forgetting is demonstrated as the dominant problem. Thirty-eight acquire through minimarkets or supermarkets; two more use warung, six use online retail, two do not know and one uses another route. Support the ordinary shelf purchase as well as a digital link.

A shared Sensitive Expert account is a valuable counterexample: family choice, funding and purchase can sustain valued specialist use. Brand-only and mixed answers remain unresolved for tier classification. No confirmed historical Premium-to-Basic causal sequence, clinical response or regular-price retention cohort was collected.

## Recommended strategy and what was selected

The user explicitly asked for strategic recommendations and three pillars, superseding older restrictions against premature concept selection. Three focus alternatives are compared against the same outcome and cost screen: exact-choice purchase service; relevant-benefit experience; and replacement assistance. The second focus is selected as the core of **Pepsodent Sesuai Saya**. It is delivered through three operational pillars:

- **Meaningful relevant benefit:** clarify one personally valuable job, provide truthful approved comparison and a voluntary experience opportunity where appropriate, and assess whether the experience matters. Basic remains suitable when it meets the job. Already satisfied specialist users can bypass unnecessary trial.
- **Executable purchase:** preserve exact SKU, pack, grams, current ticket, unit price and shopping route. Self-shopping is primary, including when family funds. Share an item only if another shopper needs it. No credit, compulsory household bundle or presumed parental authorization.
- **User-selected replacement:** ask when the user wants to check remaining product, permit delay or cancellation, confirm actual price/route, and observe paid replacement without a further program-funded incentive. No fixed 30-day depletion assumption or automatic subscription.

Each pillar’s description, root constraint, mechanism, workings, quantitative process targets and direct/indirect benchmarks are detailed in the analysis and appendices 13–18. Constraints are hypotheses to test, not proven causes for every respondent. The novelty is an exact choice and experience record carried into a real purchase and replacement; a new quiz, scanner, mini tube or reminder alone is not novel. Existing products, channels and capabilities require permission and commercial confirmation before use.

Keep professional education/referral separate from cosmetic promotion. The strategy does not diagnose, promise disease reduction, create new efficacy claims or use a doctor as a product testimonial. Dental support is available irrespective of Premium purchase.

## Economics and evaluation

The model is normalized to 10,000 screened contacts per equivalent comparison arm over 180 days. Base assumptions: 40% qualify; first paid acquisition is 40% versus 25% among 4,000 qualified units; conditional second purchase is 60% versus 45%. This yields 1,600 versus 1,000 first events and 960 versus 450 second events: 600 + 510 = 1,110 incremental paid 100 g equivalents. These are authored scenario inputs, not survey estimates or imported benchmark effects.

At an assumed Rp6,000 net portfolio contribution per equivalent after displaced-product contribution, benefits before program cost are Rp6.66 million. An illustrative Rp40 million learning envelope produces a Rp33.34 million short-window loss. Downside and upside also lose Rp39.4925 million and Rp19.48 million respectively. The base operating-cost ceiling is Rp666 per screened contact before fixed-cost allocation. Under fixed 4,000 qualified users and at most two events, maximum incremental volume is 6,550 versus 6,666.67 required to recover Rp40 million at Rp6,000. Conversion alone cannot close that constrained model’s gap.

The decision is a gated low-cost test using existing assets, not a new-app investment, positive ROI forecast or mass rollout. Retail shelf price multiplied by the case margin is not manufacturer contribution. Actual realization, COGS, channel/returns costs, own-Basic and sister-brand displacement, and control-arm measurement/recruitment cost must be known before approving spending. Do not subtract Basic twice from a parameter already net of displacement.

A proposed 120-participant feasibility cohort checks execution, not effectiveness. The primary confirmatory cohort must match the case: ages 18–30 with adequately documented prior Premium and current Basic histories; broader need-qualified users are exploratory and reported separately. A planning illustration for 11.25% versus 16.25%, two-sided 5% significance and 80% power requires approximately 744 independent units per arm, 930 with 20% loss, rounded to 1,000 before any clustering adjustment. Its five-point detectable effect differs from the scenario’s 12.75 points. No trial has been run; the model normalization does not price that actual trial.

Measure paid second purchase per ALL assigned units, not only repeat among initial buyers. Record ordinary retail promotions; no new program subsidy does not mean no retailer discount. Dedupe transactions across pillars and shared tubes. Targeted process figures are authored operational goals. Referral completion’s proposed target is 50% of all professionally referred participants within 90 days; consent to follow-up and unknown status are separate, and completion among reachable volunteers is secondary. Knowledge and observed technique require their own comparison; sales are not health outcomes.

## Retained context and data handling

The earlier 314,476 written-record archive remains an inventory across platforms and scopes, not independent Indonesian target switchers. Original master context and raw sources retain their limitations. No new bulk collection, interviews, paid actor run, participant contact, purchase, remote push, public publication or competition submission occurred in this task.

The overlay contains aggregates, source metadata, scenario code, figures and the deliverables. It excludes the raw survey workbook, contact fields, original response IDs, follow-up codes, respondent-level coding manifests, screenshots, .git and the large older corpus. Reproduction of survey calculations requires the owner’s private workbook. The full prior combined context is retained below the new analysis with an explicit historical label; prior root files are archived under the dated results directory.


## Full current analysis carried forward

# Pepsodent survey analysis and strategic recommendation

Prepared for the E Fest team from the survey export supplied on 4 November 2026 and the Pepso_EFest repository at commit `a9c168a718f20b13097ae82488c77815958521d5`. This report is a decision document for private team use. It separates primary observations, case facts, interpretation and proposed tests. External benchmarks establish relevant mechanisms or capabilities, not a transferable Pepsodent sales lift.

## Recommended decision

Select **Pepsodent Sesuai Saya**, a service that helps an appropriate personal toothpaste choice survive the next real purchase. Its three pillars are: establish a meaningful additional benefit; make the exact product, pack, price and purchase route executable; and support a user-selected replacement followed by verified paid repeat. Retain Basic when it meets the person's needs. The commercial objective is additional profitable Premium purchasing by suitable users, rather than upgrades regardless of fit.

The strongest new insight is **family funding alongside personal purchasing control**. Twenty-three of 49 included respondents choose and shop personally while family supplies the money. A program built mainly around persuading parents to buy the requested tube would therefore be poorly matched to much of this sample. The second important insight is that apparent preference fulfillment often lacks a named preference: 31/49 explicitly report none, and 22/31 nevertheless say they obtained what they wanted. There may be an acceptable routine to respect before there is a specialist choice to preserve.

These results justify a targeted test, not a national rollout. The sample has no respondents aged 25–30, no verified Premium-to-Basic histories, no treatment exposure and no measured willingness to pay. In the illustrative commercial model, all three 180-day scenarios lose money after the proposed learning budget. A useful outcome from this work is therefore a sharper offer and a clear decision about what must become true before scaling.

## Evidence map and source boundaries

| Identifier | Source | Appropriate use |
| --- | --- | --- |
| S01 | Uploaded `Data survei pasta gigi — E-Fest.xlsx`, especially raw `Form responses 1`, `CLEAN`, `KAMUS`, `PETUNJUK`, `REVIEW` | Descriptions of 49 included retrospective acquisition accounts; questionnaire and data-quality audit |
| S02 | Organizer case transcript in `sources/transcripts/Case_Study_Transcript.md` and image-chart transcription in the master context | Historical business problem, illustrative organizer survey, example shelf prices and margins |
| S03 | `sources/transcripts/Preliminary_Guidebook_Transcript.md` | Target output, three-page main summary, formal Indonesian, judging criteria and deadline |
| R01 | Repository dated buying-situation synthesis, evidence ledger, brand audit and literature review | Prior hypotheses, documented capabilities and source-specific counterexamples |
| B01–B16 | Benchmark source ledger accompanying this report | Direct/indirect mechanism comparisons with their individual limitations |
| M01 | Reproducible commercial sensitivity model and assumptions | Authored scenarios and break-even calculations; never observed treatment effects |

The case describes Premium's share of Pepsodent sales falling from 27% in 2022 to 20% in H1 2026, a seven-percentage-point decline. This is not equivalent to a verified fall of seven percent in revenue, customers or units. The sales metric and aligned comparable-period denominator remain insufficiently specified. The case attributes downtrading mainly to young adults; the new survey does not independently authenticate that historical cause. The organizer's illustrative 1,200-person survey, including 540 switchers, remains separate from S01. Its overlapping switcher reasons—equivalence 44%, price gap 39%, no felt difference within two weeks 31%, Basic promotions 28% and variant uncertainty 24%—are case inputs, not results from this team.

The repository's public archive is useful for hypotheses and counterexamples. Its 314,476 retained written records are an inventory across platforms and product scopes, dominated by international Amazon material. They are not independent Indonesian young adults or a large verified switcher sample. Neither public review sentiment nor star ratings establish clinical effectiveness, willingness to pay or regular-price repeat.

## Method and data quality

S01 contains 50 submitted records. Forty-nine satisfy the exported consent, age, Indonesia-use, completion and main-collection gates. One consenting respondent reports being under 18 and terminates. The inclusion fraction of 49/50 is not a response rate: invitation counts and the recruitment frame are unavailable. Participation and purchase histories are self-reported; independence of all submissions cannot be authenticated from an open form.

The included sample consists of 40 people aged 18–20 and nine aged 21–24. Forty-two study as their main activity; seven study while working. Twenty-five live alone or in a kos, 20 with family, three with friends/housemates/in a dormitory and one in another arrangement. There are no observations aged 25–30. Results should be described as a student convenience cohort, not as Indonesian Gen Z or the entire case target of ages 18–30.

Collection occurred on 4 November 2026, 17:47–22:26 WIB. Of 29 reported acquisition months, 27 are August–November 2026 and two August 2025; 20/49 omit the month. Most dated episodes therefore postdate the case's H1 2026 endpoint. They can inform current mechanism testing without explaining the earlier share movement retrospectively.

Raw answers and CLEAN align across compared substantive fields. Twenty-nine acquisition-month strings become first-of-month datetimes in CLEAN; day 1 is a representation convention, not a reported acquisition day. Ten RINGKASAN count cells have a date format: counts such as 19, 20 and 34 can appear as dates in 1900. All reported results here are recomputed from CLEAN and checked against the raw sheet, rather than copied from those displays.

Five included records have built-in quality flags: two prices are entered despite unknown-price certainty, two approximate-price answers omit the number, and one nonparticipation response coexists with a substantive reason. Flags warrant review, not automatic deletion. A further unflagged price of 190 for an 85 g pack has uncertain currency or units. It remains unresolved. Thirty-nine respondents express confidence in most answers, eight describe some estimates and two recall many parts poorly. High confidence does not authenticate receipts or clinical outcomes.

Tier hints are not adjudicated labels. Every manual pathway remains UNREVIEWED and the REVIEW sheet has no adjudications. A brand name, colour, price or automated keyword cannot reliably establish Basic versus Premium. The export cannot produce a defensible Premium-to-Basic migration rate. Public deliverables omit respondent-level records, response identifiers, contact details and follow-up codes.

## Results that change the strategy

### Purchasing roles are separated even when the user acts independently

| Role or intersection | Count | Interpretation |
| --- | ---: | --- |
| Personally chooses brand/variant | 30/49, 61.2% | Many respondents already exercise choice |
| Personally buys/orders | 31/49, 63.3% | The user is frequently the actual shopper |
| Family supplies money | 41/49, 83.7% | Family pays for this acquisition in much of the cohort |
| Personally chooses and shops, family funds | 23/49, 46.9% | Self-shopping purchase execution should be the main route |
| Personally chooses, shops and pays | 6/49, 12.2% | Full observed role independence is uncommon |
| Family funds a personally chosen product | 24/30 self-choosers, 80.0% | Funding does not imply absent choice |
| Family funds a personally shopped product | 25/31 self-shoppers, 80.6% | Funding does not imply the parent visits the shelf |

Among 25 living alone/in kos, 22 personally choose, 23 personally shop and 21 are family-funded. Living apart does not establish independent funding of this toothpaste acquisition; neither answer measures total living expenses or income. Within the 19 family-selected accounts, family also shops in 16, the user shops in two and the shopper is unknown in one. A transferable exact-SKU shopping item may fit this latter setting, but those records are not proven cases of a blocked Premium preference.

A useful disconfirming account describes shared Sensitive Expert use, a valued benefit, family selection/funding/purchase and a family sensitivity-related reason. Another self-directed, self-funded specialist account also values its benefit. Family involvement can support specialist use. The operative question is which role needs help in this episode, rather than whether the family should be removed from the decision.

**Strategic implication:** distinguish self-shopping with a visible funding ceiling from optional handoff to somebody else. Show ticket and unit cost, preserve the exact SKU, and let a user decline the upgrade. Do not assume a parental veto, an insufficient allowance or a causal price constraint merely because family pays.

### Getting what one wanted often means acceptable acquisition rather than a specified product

Manual coding of the desired-product answer yields 31 explicit no-preference responses, 12 named brands/variants, two functional requirements without a named SKU, three dash placeholders and one vague evaluation. Dashes remain missing/unclear, not no preference. Obvious wording variants of “tidak ada pilihan khusus” are normalized; naming a product does not verify its tier.

Overall, 34/49 select “I obtained the product I wanted.” However, 22 of those 34 come from the 31 explicit-no-preference accounts, and another three are dash responses. Only seven of the 12 named-preference accounts select “got wanted”; two say it was available but they chose another, and the other three select different availability answers. Some product text and fulfillment answers are inconsistent at an exact-string level; broad meanings, recall or synonyms may explain this. Neither field should be forced into being the unquestionable truth.

The pattern survives conservative checks: removing all five flagged records leaves 29/44 explicit no preference and 21/29 of those reporting fulfillment. Among the 39 most confident respondents, 25 report no preference and 19/25 report fulfillment. These checks preserve the interpretation but do not reveal an unconscious preference.

**Strategic implication:** first discover whether a relevant additional job exists. “Got what I wanted” cannot serve as an exact-SKU fulfillment metric, a measure of specialist satisfaction or proof that availability is perfect. Equally, no specific preference is not dissatisfaction. Acceptable Basic use may be a legitimate endpoint rather than a conversion failure.

### Price fit, habit and comfort overlap

The prompted question allowed at most three reasons. Its counts describe selections within that capped list, not unconstrained importance weights or spontaneous themes.

| Prompted factor | Count of 49 | Sample share |
| --- | ---: | ---: |
| Fits available money | 30 | 61.2% |
| Already accustomed to product | 28 | 57.1% |
| Taste/comfort fits | 23 | 46.9% |
| Needs a particular benefit | 15 | 30.6% |
| Promotion or economical pack | 15 | 30.6% |
| Purchaser/provider choice | 6 | 12.2% |
| Existing household stock | 5 | 10.2% |
| Previous product disappointed | 3 | 6.1% |
| No added need beyond ordinary toothpaste | 3 | 6.1% |
| Does not know/participate | 2 | 4.1% |
| Other reason | 2 | 4.1% |
| Desired product not found | 1 | 2.0% |

Nineteen of 49 select both budget fit and habit. Eight select budget plus a specific benefit, six habit plus benefit, eight comfort plus benefit and nine promotion plus habit. Price, habit and value are not exclusive segments. Familiarity can be the result of a successful specialist product, not evidence of an uninvolved buyer.

Eight of the 15 specific-benefit selectors choose without comparing products. Eight of the 28 habit selectors nevertheless compare. Comparison behavior is therefore an unreliable standalone eligibility filter for education or specialist targeting. Someone can know exactly what works and repeat it without browsing.

Fifteen identify promotion/economical packs as influential, but only seven of those recall an actual promotion; five say no promotion and three do not know. Across all 49, ten recall a promotion, 21 none and 18 are unsure. The checkbox combines deals with pack economy. It cannot quantify discount dependence, deal waiting or price elasticity.

### The cross-category insight is useful but modest

Forty-one of 49 report a recent other-personal-care acquisition: 21 skincare, 11 haircare, three body care, two fragrance, two deodorant and two other products. Thirty-six of those 41 choose it personally, four report family choice and one joint choice. Twenty-seven of 41 compare other-category products, nine do not, four do not participate and one cannot recall. For toothpaste, 18/49 compare, 19 do not, 11 do not participate and one cannot recall.

Those two marginal percentages have different denominators and role composition. The strict matched subset—participation in both choices, a positive comparison gate and interpretable answers—contains only 21 respondents:

| Toothpaste comparison | Other category compared | Other category not compared | Total |
| --- | ---: | ---: | ---: |
| Compared | 10 | 3 | 13 |
| Did not compare | 6 | 2 | 8 |
| Total | 16 | 5 | 21 |

Six compare only the other category, but three show the reverse. The within-person difference is 3/21, or 14.3 percentage points. The two-sided exact discordance test is p = 0.5078125 from nine discordant pairs. This does not establish a systematic direction, and opt-in sampling further limits population inference. The six other-only accounts are three skincare and three haircare, not six skincare enthusiasts.

Among 16 high-confidence matched respondents, the counts are ten both, three other-only, two toothpaste-only and one neither; the directional difference shrinks to 1/16. Excluding flagged responses gives 20 matched accounts with the original directional pattern. A broader 29-person subset based only on interpretable processes gives ten other-only versus three toothpaste-only, but measures a different construct and must not replace the strict denominator silently.

**Strategic implication:** selective category consideration is a targeted hypothesis worth testing. It is weaker than the purchase-role result. The sample does not show that students who buy skincare are wealthy, can afford Premium, neglect oral care or will buy after learning more.

### Replacement is the relevant occasion, but abandonment and stockout are unverified

Thirty-seven of 49 report the prior tube finished/nearly finished. Seven still use it alternately; two stopped despite some product remaining; one temporarily uses another product; two do not recall. Name changes are not permanent switching histories.

Twenty of 49 report a prior benefit that was felt and important, 13 a felt but less important benefit, 11 no meaningful difference, three no special expectation and two no recall. Sixteen of the 20 valued-benefit respondents also report depletion. They are useful for observing replacement, but not an estimated lapsed-Premium audience. The prior tier, current tier and permanent continuation remain unresolved.

Only two of 49 explicitly searched and failed to find a product. Neither supplies a clean verified exact-SKU Premium stockout episode. Four obtained an available alternative by choice; four did not search because of supplied/household stock; two had no particular choice; three were unsure; 34 selected fulfillment. Nationwide stock failure cannot be positioned as the dominant measured cause. Forgetting was not directly isolated either.

Thirty-eight of 49 acquisitions occur at minimarkets or supermarkets/hypermarkets: 22 and 16 respectively. Two use warung, making 40/49 known offline routes. Six are online, two unknown because another person bought and one another place. Digital should carry information into the actual purchase route; compulsory e-commerce subscription would ignore the most common reported channels.

Thirty-four use the current tube alone, 13 share it, one does not know and one has not used it. Shared use affects timing and the experimental unit. A fixed 30-day depletion model would be invented. Allow the person to state remaining stock and choose timing.

### Brand counts cannot become tier or churn estimates

Conservative alias coding gives 26 current single-brand Pepsodent mentions: 23 explicit names and three probable obvious misspellings. Four current strings name multiple brands and three are unknown. The same broad method gives 26 prior Pepsodent accounts, but only 14 clearly name Pepsodent at both events. Seven prior Pepsodent accounts now name another single brand, three mixed strings and two unknowns. Conversely, 12 current Pepsodent accounts did not clearly name it previously.

Equal brand totals conceal different reported episodes. These are neither market-share flows nor churn rates: concurrent use, household stock and recall remain plausible. Two current answers clearly name Sensitive Expert; most Pepsodent records lack exact variants. The report does not promote the automatic tier hints to findings or estimate target switcher prevalence.

### Monetary precision is insufficient for willingness-to-pay analysis

Twenty of 49 omit paid price. Twenty report not knowing it, 21 approximate certainty, seven remembering/having proof and one a free product. Twenty-nine enter a number, including two zeroes and the unresolved 190. Packs include missing grams, vague sizes and ambiguous multipacks. A common price median is deliberately omitted because quantities, certainty and the anomalous amount are not comparable. These entries do not establish a price index, income, willingness to pay or an affordability threshold.

Open responses mention familiarity, family habits, sensory fit, benefits, review/advertising cues, value and isolated ethical/affiliation considerations. These add explanatory leads, not prevalence estimates from a validated coding scale. Expected outcomes are often generic cleaning/freshness or absent, alongside some specific sensitivity/appearance jobs. Further description should retain each person's own job rather than assign skincare users to whitening automatically.

## Ranked insights and credible opposites

| Rank | Distinctive insight | What it changes | Credible opposite or boundary |
| --- | --- | --- | --- |
| 1 | Family money often accompanies personal choice and shopping | Make self-shopping with transparent cost the default; handoff optional | Family can also sustain shared specialist use; funding is not obstruction |
| 2 | Fulfillment often lacks a specified preference | Qualify a personally meaningful job before optimizing conversion | Broad acceptance can be rational satisfaction with Basic |
| 3 | Routine and benefit coexist | Preserve valued habit and comfort; do not target only active comparers | A known specialist choice may need no extra education |
| 4 | Digital support must reach an offline purchase | Use a portable exact-SKU item and retailer execution | Six online accounts still deserve a usable online route |
| 5 | Replacement offers a real observation point | Track next actual purchase and stock remaining | Depletion is not evidence of forgetting, churn or a failed preference |
| 6 | Category selectivity appears in some paired accounts | Test meaningful relevance with appropriate users | Three reverse cases and p = .508 oppose a universal story |

No analysis can allocate the seven-point historical share decline among these mechanisms from S01. The practical achievement is a better targeting and measurement design.

## Three alternatives and explicit selection

All alternatives below are evaluated against the same outcome: suitable incremental paid Premium replacement with viable portfolio contribution and a separate oral-care benefit. The comparison is team judgment under current evidence, not a scored consumer referendum. Each alternative would use existing channels, a bounded test and basic outcome capture; the selected concept does not receive an unlimited budget or guaranteed capabilities.

| Alternative focus | Complete standalone proposition | Strength | Main weakness |
| --- | --- | --- | --- |
| Exact-choice purchase service | A saved item with SKU, pack and costs, personal shopping or optional handoff, plus basic purchase and replacement outcome capture | Low complexity; fits separated purchasing roles and ordinary retail | Most self-choosers already shop personally; it cannot establish an absent additional need |
| Relevant-benefit experience program | Need-specific explanation, truthful voluntary experience and a practical purchase-and-replacement route, measured on paid repeat | Addresses why an additional benefit would matter before paying for conversion | Trial and coordination costs can exceed contribution; requires truthful claims and staged testing |
| Replacement assistance service | User-selected check-in and exact-product buying support for an already valued choice, with the same outcome and cost screen | Fits frequent depletion and avoids needless education of satisfied users | No verified Premium lapse cohort; reported failed search is rare and forgetting was not isolated |

Select the **second focus** as the core of **Pepsodent Sesuai Saya**, implemented through the three pillars below. Purchase execution and replacement are necessary operating supports, not three independent programs whose effects can be added. All alternatives must be tested against the same cost ceiling, eligible cohort and paid-repeat outcome; there is no measured comparative winner. If future evidence locates the constraint solely at purchase handoff or replacement, the cheaper focused alternative should replace the broader service.

The selection follows the evidence: many users already control shopping, many lack a particular preferred product, and replacement usually occurs in ordinary offline retail. A continuity service can distinguish whether relevance, execution or economics actually breaks. Novelty lies in the linked operating and measurement sequence, not a new AI scanner, a new household app, a small tube claimed as newly invented, or a perpetual voucher.

## Pillar one Establish personally meaningful value

**Description and root constraint.** Begin with what the current routine does adequately, then identify a relevant additional job and one suitable existing variant. Separate “cannot distinguish,” “understands but does not value,” and “wanted but disappointed.” Basic remains available. The relevant constraints are insufficient personal relevance, expectation mismatch and poor fit; none is assumed universal.

**Evidence.** S01 shows 31/49 without a specific preferred product, 15/49 selecting a specific benefit, 23/49 comfort and 20/49 an important prior benefit. These are different questions, not one latent-demand measure. S02's equivalence, no-difference and variant-confusion reasons provide additional case context. They do not prove that education will work.

**Mechanism and operation.** An optional mobile page or staff-assisted equivalent captures the current product and one desired improvement, compares a suitable SKU with the accepted routine, and presents the approved claim, directions, conditions and realistic evaluation window. It shows pack and costs before a voluntary ordinary purchase or authorized existing trial. A later check records what the person actually noticed and whether it mattered. Stop repeated sales pressure when the need is absent or the experience disappoints; route persistent symptoms to appropriate professional care. This is not diagnosis or a universal two-week guarantee.

**Quantitative impacts.** The pilot should measure benefit comprehension, realistic expectations, suitable choice, reported experience and eventual paid replacement separately. Proposed process targets are at least 80% correct benefit-and-limit comprehension, at least 70% experience follow-up completion, and no opened or decanted trial packs; these are authored targets, not uplift estimates. In M01, the authored base assumes 40% qualification among 10,000 screened contacts and first paid acquisition of 40% versus 25% under usual practice among 4,000 qualified people, or 600 additional first purchases. These are whole-program scenario inputs, not this pillar's demonstrated lift or the survey's qualification rate. A pillar-specific comparison can test explanation support versus ordinary content; it cannot inherit 600 sales automatically.

**Benchmarks and improvement.** Sensodyne Indonesia already offers a saveable check-up profile, advice/product information and sample/coupon pathways [B01]; Colgate India offers product matching [B02]. Pepsodent already has Denta-Scan and ShadeScan capabilities [B03, B05]. These direct benchmarks support feasibility while reducing novelty claims. The proposed improvement is evaluating actual fit and connecting the result to a later paid purchase. Indirect trial-distribution research finds context-dependent effects [B06–B08], including a recent null counterexample. None supplies a local uplift. Manufacturer claims must retain their conditions [B04].

## Pillar two Make the actual purchase executable

**Description and root constraint.** Turn a qualified product choice into an exact purchasable item through the user's normal route. The main path serves self-shoppers. Where another person shops, a voluntary shareable item carries the same information. The constraints are loss of SKU precision, invisible recurring cost, role separation and purchase-route friction—not a presumed parental veto.

**Evidence.** Twenty-three of 49 choose and shop personally with family funding; 24/30 self-choosers and 25/31 self-shoppers are family-funded. Thirty-eight of 49 use modern offline retailers. The product must therefore work as a shelf decision and budget conversation as well as a digital link.

**Mechanism and operation.** Produce an item showing the exact variant name, pack photograph, grams, number of tubes, currently observed ticket, price per 100 g, timestamp/source and supported benefit. The self-shopper keeps it as a phone image/list item and selects a normal retailer. Do not promise live availability without retailer confirmation. An online route can link the exact variant where validated. If a different payer's approval or funding is needed, provide an honest cost comparison through the person's existing communication channel. If somebody else buys, the optional item can be shared; it is not a compulsory family chat or specialist bundle. Record what actually entered the basket and why a substitute was accepted.

**Quantitative impacts.** Use exact intended-to-acquired SKU/pack match, paid acquisition per assigned eligible unit, actual ticket/unit cost and payer acceptance where relevant. Establish a baseline because 34/49 broad “got wanted” answers are not SKU matches. Proposed process targets are at least 90% complete saved items (identifiable SKU, grams and dated price), at least 80% correct variant recognition among confirming optional-share recipients, and at least 90% verified acquisition capture among reported acquisitions. Report non-openers, non-confirmers and unverified purchases separately. These are operational targets, not current results. M01's incremental first purchases must remain assigned to the combined program until a separate comparison isolates this component. No extra pillar sales are added.

**Benchmarks and improvement.** AnyList documents shared lists and item photographs [B14], a direct functionality analogue for optional handoff. An archived Pepsodent mobile campaign linked family messaging to a buy-now route [B13], but its media metrics cannot establish sales incrementality. Shopping-list experiments support externalizing exact planned items [B12], not persuading a parent to spend more. The improvement is truthful pack-cost comparison plus execution in the observed physical route, with a recorded match rather than a click as the result.

## Pillar three Support the next chosen replacement

**Description and root constraint.** After a valued experience, offer user-selected replacement assistance through an existing channel. The problem being tested is whether a wanted choice fails at the next acquisition because of timing, route, exact SKU or acceptable outlay. The survey does not establish forgetting or stockout as its dominant root cause.

**Evidence.** Thirty-seven of 49 encounter depletion and 16 of 20 valued-prior-benefit accounts also report depletion. These support observing continuation, not labeling 20 people lapsed Premium users. Only 2/49 report failed search. Shared use in 13/49 further cautions against a fixed depletion schedule.

**Mechanism and operation.** Ask whether the person wants the same variant, how much remains and when contact would be useful. Offer opt-in timing, snooze, cancellation and an exact-SKU retailer route. No compulsory subscription or automatic shipment is necessary. Confirm retailer price/availability only to the degree supported. A bounded incentive, if tested, has its own assignment and budget; record whether it merely brings forward a planned purchase. Follow the next paid replacement without another program-funded incentive and retain actual retail promotion information.

**Quantitative impacts.** The primary outcome is verified paid second purchase per all assigned person/household units by a common follow-up date, not only repeat among successful first purchasers. In M01's base illustration, second purchases are 960 versus450, or 510 additional, following 1,600 versus1,000 first purchasers. These are combined-program authored outcomes. Conditional repeat 60% versus45% alone is not a causal retention effect because the program changes who becomes a first buyer. All reminder timing must be user-selected, with at least 95% of opt-outs processed within one working day and no automatic charges or shipments. Record purchases, grams and price; no further program subsidy does not automatically mean the full standard shelf price was paid.

**Benchmarks and improvement.** Oral-B's US replenishment service documents user-selected schedules, skipping, date changes and cancellation [B10]. It demonstrates control functionality, not demand for Indonesian toothpaste subscriptions. The implementation-intentions experiment [B09] supports testing a specific date-and-time plan beyond a generic reminder, but its regression-adjusted vaccination effect must not be transferred into sales. Availability experiments [B11] justify checking substitution where people shop; they do not overturn the low reported stockout count. Improvement lies in permission, actual stock, exact choice and measured paid repeat, with a stop when value is absent.

## Economic model and quantitative impact envelope

### Price architecture from the case

Basic at Rp24,100/190 g equals Rp12,684.21 per 100 g. Premium at Rp41,900/100 g is 3.3033 times that unit price. Promotional Premium at Rp23,500/100 g is2.49% cheaper per tube than Basic but 1.8527 times as expensive per gram. A manageable trial ticket therefore does not prove sustainable recurring affordability. These are case examples, not respondents' paid-price averages or current retailer quotations.

The supplied38% and55% gross margins cannot be multiplied by shelf prices to create an actual Unilever contribution forecast. Manufacturer realization, trade funding, variable costs, pack economics and cannibalization are missing.

### Reproducible assumptions rather than a disguised forecast

M01 normalizes to10,000 screened contacts in each equivalent exposed/comparator cohort over180 days. It is not a sample-size recommendation, a national addressable audience or a promise to recruit20,000 people. Qualification and purchase rates below are entirely authored. First and second paid events each represent100g equivalents for arithmetic; actual trials must record grams and paid prices.

For screened N, qualification q, first-acquisition rates aT/aC and conditional repeat rT/rC:

`incremental equivalents = N × q × [aT × (1 + rT) − aC × (1 + rC)]`

`net contribution = incremental equivalents × net contribution per equivalent − program cost`

Qualification must be assessed before treatment comparison. The per-equivalent contribution parameter is net of the relevant portfolio displacement; subtracting Basic a second time would double count it.

| Assumption or outcome | Downside | Base | Upside |
| --- | ---: | ---: | ---: |
| Need-qualified share, assumed |20%|40%|60%|
| First paid rate treated/comparator |30% / 25%|40% / 25%|45% / 25%|
| Conditional second paid rate treated/comparator |45% / 45%|60% / 45%|65% / 45%|
| Qualified people in normalized cohort |2,000|4,000|6,000|
| First paid events treated/comparator |600/500|1,600/1,000|2,700/1,500|
| Second paid events treated/comparator |270/225|960/450|1,755/675|
| Incremental first plus second equivalents |145|1,110|2,280|
| Assumed net contribution per incremental100g |Rp3,500|Rp6,000|Rp9,000|
| Contribution before program |Rp0.508m|Rp6.660m|Rp20.520m|
| Learning plus delivery budget |Rp40m|Rp40m|Rp40m|
| Net after learning budget |−Rp39.493m|−Rp33.340m|−Rp19.480m|

The Rp40m is a proposed cap: Rp30m one-time build/claims review/retailer setup/measurement/analysis plus Rp10m variable delivery and handling. It is not a supplier quote, approved budget or plan to spend. All scenarios lose money within this window. The business case is limited learning with an affordable downside, conditional on team approval, not positive short-term ROI.

At base performance, break-even total ongoing cost is Rp6.660m per 10,000 screened contacts, equivalent to Rp666/contact if all benefits materialize. A repeating Rp40m campaign would need 6,666.7 incremental equivalents at Rp6,000 contribution versus 1,110 modeled. Scale does not rescue negative variable economics. If one-time setup is genuinely sunk and delivery falls to Rp5m, base short-window net becomes Rp1.660m; this is a threshold scenario, not a rollout endorsement.

An alternative explicit bridge assumes Premium contribution Rp9,000/100g and Basic contribution Rp6,000/190g, with equal grams displaced. At own-Basic displacement shares 0%, 50%, 80%, 100%, incremental portfolio contribution per 100 g becomes Rp9,000, Rp7,421.05, Rp6,473.68 and Rp5,842.11. These are hypothetical inputs, not derivations from shelf margins. Use this bridge or the generic parameter consistently. Pepsodent gains from sister brand Closeup may not create equal Unilever gains. Existing Premium repeat should cancel against the comparator; timing shifts require longer observation.

No national share restoration, disease reduction, lifetime value or annual ROI is forecast. The absolute sales denominator, prospective response and retention horizon are not known.

At the fixed base qualification count of 4,000 and at most two paid events, even every treated qualified unit purchasing twice yields only 8,000 events versus 1,450 comparator events, or 6,550 incremental equivalents. That remains below the 6,666.7 needed to recover Rp40m at Rp6,000 each. Within this constrained two-event base, higher conversion alone cannot achieve break-even; cost, contribution or a separately justified horizon must change.

The illustrative Rp40m breakdown is Rp10m content/lightweight workflow, Rp10m measurement and verification, Rp10m operations/training, Rp6m authorized trial packs/distribution and Rp4m permissioned messaging/support. This is a cost envelope, not procurement evidence. The actual randomized trial requires its own recruitment, control-arm verification, clustering and attrition budget; the normalized model does not price that trial.

## Implementation, measurement and societal value

Begin with an operational cohort to verify comprehension, exact-SKU capture, consent, retailer handling and reminders. The completed survey need not be rerun as a prerequisite. A future pilot should recruit verified product histories, varied role arrangements and both students and nonstudents, including a prespecified 25–30 cohort. Its sample size should follow the primary outcome, baseline rate, commercially meaningful detectable effect, clustering and attrition; 49 exploratory responses are not a powered intervention trial.

Compare the integrated service against usual brand/retail practice. Randomize at household level where tubes are shared, otherwise person level; stratify on verified current tier, relevant need, role split and channel. Stage-specific comparisons may isolate benefit support, optional handoff or reminder/access versus incentive support. Their estimates have different denominators and cannot be mechanically multiplied or added. Use intention-to-treat reporting, missing-outcome sensitivity and a common follow-up date, extending observation when stock remains.

Give oral-care support irrespective of Premium purchase. A professionally approved routine module can cover appropriate brushing timing/technique, foundational fluoride care and red-flag referral. Keep public education and clinical referral distinct from cosmetic product advertising; BPOM's published boundaries on professional testimonials require execution review [B16]. ADA information supports foundational fluoride care and distinct additional functions, not Indonesian approval of a particular SKU [B15].

Social measures should distinguish module access, knowledge, behavior and clinical endpoints. Record participation and attrition; use a prespecified knowledge check and, where feasible with consent, standardized observed technique assessed without knowledge of marketing assignment. Track offered versus completed appropriate referrals separately. Clinical measures such as plaque require a qualified protocol and suitable comparison; none was collected here. Sales, samples, coupon redemptions or Premium mix are not health outcomes. Any numeric social target is a prospective operating target until measured, not a modeled prevented-caries count.

Release expansion only when exact-SKU and purchase capture work, incremental paid second purchase is positive at the prespecified commercial minimum, and mature portfolio contribution exceeds delivery cost. Stop or narrow when Basic already meets the job, experience does not deliver valued fit, only further vouchers produce buying, reminders irritate users, or portfolio contribution falls. Consumer choice, credible health assistance and learning whom not to convert are part of the design's value.

## Confirmatory cohort and common measurement registry

The primary confirmatory cohort must match the business problem: age 18–30 with adequately documented previous Premium and current Basic SKU history, distinguished from temporary concurrent use. Broader need-qualified users may enter a separately reported exploratory cohort. Neither the existing 49 nor the modeled 40% qualification rate identifies that target cohort. The planned 5-point detectable difference (11.25% to 16.25%) is deliberately below the scenario’s 12.75-point difference; sample size is not evidence the larger effect will occur.

Operational targets shared with the executive-summary appendices are: at least 80% correct comprehension, 70% experience follow-up completion, 90% complete saved SKU/gram/dated-price items, 80% correct SKU recognition among confirming optional-share recipients, 90% verifiable capture of reported acquisitions, and 95% opt-out fulfillment within one working day. Every target is authored. Missing, unopened and unconfirmed cases remain visible. The social referral target is 50% completion among all professionally referred participants within 90 days, with consent-to-follow and unknown status separately reported; completion among reachable volunteers is secondary. No target implies a disease reduction or proven commercial uplift.


## References and evidence identifiers

S01. Tim Pepsodent E Fest. (2026). Data survei pasta gigi E Fest [Unpublished exploratory survey export supplied 4 November 2026]. Raw and CLEAN source preserved privately; no respondent-level records are included in the repository package.

S02. Economics Festival. (2026a). Case study Pepsodent [Supplied competition case]. `sources/transcripts/Case_Study_Transcript.md`; original chart transcription in the master context pack.

S03. Economics Festival. (2026b). Guideline preliminary round E Fest 2026 [Competition guidelines]. `sources/transcripts/Preliminary_Guidebook_Transcript.md`.

R01. Existing project research and buying-situation synthesis at repository commit `a9c168a718f20b13097ae82488c77815958521d5`. Historical hypotheses retain their original limitations.

M01. Team-authored normalized 180-day scenario model, `model/model.py`, `model/scenarios.json` and assumption registry. All rates, contribution and program costs are unvalidated assumptions.

B01. Haleon. (n.d.). Online check up. Sensodyne Indonesia. https://www.sensodyne.co.id/Pemeriksaan-online/Pemeriksaan-online.html

B02. Colgate India. (n.d.). Product match tool. https://www.colgate.com/en-in/product-match-tool

B03. Unilever Indonesia. (2024). AI Denta-Scan lengkapi layanan konsultasi gigi online “Tanya Dokter Gigi by Pepsodent”. https://www.unilever.co.id/news/press-releases/2024/ai-dentascan-lengkapi-layanan-konsultasi-gigi-online-tanya-dokter-gigi-by-pepsodent/

B04. Pepsodent Indonesia. (n.d.-a). Pasta gigi Sensitive Mineral Expert by Pepsodent Whitening. https://www.tanyapepsodent.com/p/sensitif-sensitive-mineral-expert-whitening.html/08999999032890

B05. Pepsodent Indonesia. (n.d.-b). Pepsodent Ultra White untuk gigi 5 tingkat lebih putih. https://www.tanyapepsodent.com/ultra-white.html

B06. Han, B. R., Chu, L. Y., Sun, T., & Wu, L. (2025). Commercializing the package flow: Cross-sampling physical products through e-commerce warehouses. Management Science. Advance online publication. https://doi.org/10.1287/mnsc.2020.00902

B07. Paulich, B. J., Pansari, A., & Kumar, V. (2026). Where did you receive the free sample? Sustained impact of new product sample distribution on customer purchase journey. Journal of the Academy of Marketing Science, 54, 322–347. https://doi.org/10.1007/s11747-025-01123-3

B08. Food Standards Agency, Gold, N., Cornel, P., Zhuo, S., Thornton, K., Riddle, R., McPhedran, R., Vega, L., & Zamperetti, L. (2024). Exploring the impact of giving free food samples and loyalty cards on food choices: A stepped wedge trial in workplace food outlets. FSA Research and Evidence. https://doi.org/10.46756/sci.fsa.paq622

B09. Milkman, K. L., Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2011). Using implementation intentions prompts to enhance influenza vaccination rates. Proceedings of the National Academy of Sciences, 108(26), 10415–10420. https://doi.org/10.1073/pnas.1103170108

B10. Oral-B US. (n.d.). Frequently asked questions and contact us. https://oralb.com/en-us/faq-help-center/?page=resources

B11. Conlon, C. T., & Mortimer, J. H. (2010). Effects of product availability: Experimental evidence (NBER Working Paper No. 16506). National Bureau of Economic Research. https://doi.org/10.3386/w16506

B12. Davydenko, M., & Peetz, J. (2020). Shopping less with shopping lists: Planning individual expenses ahead of time affects purchasing behavior when online grocery shopping. Journal of Consumer Behaviour, 19(3), 240–251. https://doi.org/10.1002/cb.1812

B13. InMobi. (n.d.). Pepsodent evokes confident, “Merdeka” smiles with an AI-powered brand activation. https://advertising.inmobi.com/case-study/pepsodent-evokes-confident-merdeka-smiles-with-an-ai-powered-brand-activation

B14. AnyList. (n.d.). Create and share lists. https://www.anylist.com/

B15. American Dental Association. (n.d.-b). Toothpastes. https://www.ada.org/resources/ada-library/oral-health-topics/toothpastes

B16. Badan Pengawas Obat dan Makanan. (2025, February 17). BPOM tegaskan aturan penandaan, promosi, dan iklan kosmetik wajib dilaksanakan pelaku usaha. https://www.pom.go.id/siaran-pers/bpom-tegaskan-aturan-penandaan-promosi-dan-iklan-kosmetik-wajib-dilaksanakan-pelaku-usaha

B17. American Association for Public Opinion Research. (n.d.-a). Best practices for survey research. https://aapor.org/standards-and-ethics/best-practices/

B18. American Association for Public Opinion Research. (n.d.-b). Disclosure standards. https://aapor.org/standards-and-ethics/disclosure-standards/

B19. American Dental Association. (n.d.-a). Home oral care. https://www.ada.org/resources/ada-library/oral-health-topics/home-care
