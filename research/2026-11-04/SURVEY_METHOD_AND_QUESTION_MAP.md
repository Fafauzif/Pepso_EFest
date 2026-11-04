# Survey method and implementation map

Current shipped script: survey_apps_script/Code.gs v1.1.1. This file connects strategic questions to the actual instrument and distinguishes the planning discussion from implementation. The user wants a survey-only executive summary now, possible interviews later, approximately 40–60 reachable respondents, and one-shot usable setup.

## Design and sample

Use an exploratory cross-sectional online survey with retrospective reports of the most recent toothpaste acquisition and the previous product. “Acquisition” includes someone else buying, gifting or supplying the tube. The three buying situations are hypotheses to investigate, not segments to impose on every answer. Recruit age-eligible Indonesia users with relevant reported histories and contrasts. A generic toothpaste user is not automatically a former Premium-to-Basic switcher.

The n=50 example (25 switchers / 15 retained Premium / 10 Basic contrasts) was an illustrative recruitment aspiration. The actual form does not enforce these categories, recruit anyone, verify history, or guarantee those counts. Do not conduct many small age × role × pathway comparisons or label convenience percentages national prevalence. Show counts/denominators, source of recruitment, field dates and actual inclusion decisions.

The immediate survey contains no A/B allocation, vignette, conjoint task, price experiment, willingness-to-pay ladder, validated psychometric scale or automatic cluster classification. The paired-category module is an observational comparison within one respondent, not experimental control. Later interviews can explain contrasting results; integrating them would create explanatory sequential quantitative-to-qualitative primary research. Two short open text answers alone do not make the current design a completed mixed-methods study.

## Actual question map

| Section | Codes | Purpose and boundaries |
| --- | --- | --- |
| Consent | consent | Decline terminates; the submitted gate response is not a completed target response. |
| Age | age | Four in-range bins (18–20, 21–24, 25–27, 28–30); under/over/refusal terminate. Not independently authenticated. |
| Scope | scope | Reports toothpaste use while living in Indonesia during the last six months. Does not date every event in the case window. |
| Profile | living, activity, city | Household/life context. City optional; no full address or income inferred. |
| Latest acquisition | current_product, acquired_month, pack, chooser, payer, shopper, users, channel, paid_price, price_certainty, promo, tooth_deliberation, expected_benefit | Specific product and event; separate roles; optional MM/YYYY/pack/price; actual versus approximate/unknown/free price. Expected benefit here concerns the current acquisition and aligns with other_expected. |
| Previous product and replacement | previous_product, previous_status, previous_experience, desired_product, reason_open, reasons, availability | Permits same product, concurrent/temporary use, new tube not yet used and first use. Spontaneous explanation precedes max-three structured reasons. No prior paid-price sequence is collected. |
| Other-category gate | comparison_gate | Most recent non-toothpaste personal-care acquisition within three months; no/recollection unavailable skips six questions. |
| Other category | other_category, other_product, other_chooser, other_deliberation, other_expected, other_reason | Most recent, not favourite/most expensive. Parallel deliberation and expected outcome. Not limited to skincare; includes hair/body/deodorant/fragrance/other. |
| Finish | recall, note, followup_code | Recall certainty establishes reaching the final section; optional note and voluntary matching code. Estimated 8–10 minute duration has not been observed. |

There are 36 main question items across nine sections. Qualifying respondents who skip comparison see 30 items. Required and optional fields are defined in KUESIONER.md/Code.gs; don't infer exact completion time from item count. The form's lack of a prior paid-price history means it cannot establish discount-driven trial-to-regular-price abandonment. Interviews or a later panel would need the missing sequence.

## Product pathways and classification

Exact name/variant is requested with permission to say unknown. The conservative text helper creates hints only for clearly named examples; it does not verify case-tier membership or classify every Herbal/Complete product. Manual REVIEW uses BASIC/PREMIUM/OTHER/UNKNOWN plus a note for current and previous variants. The resulting name pathway remains self-report. Read actual use, previous stock, reasons and timing before calling abandonment or switching cause.

The form asks which product the user wanted in free text. It does not automatically compare desired/current strings as a validated preference gap. Manual reading is required for synonyms, nonchoices and uncertainty. A parent paying is not evidence of overriding preference. A promotion mention is not proof of price dependence.

## Matched-category analysis

RINGKASAN compares reported consideration of alternatives among respondents involved in choosing both categories (self/joint), who recall the process in each. Nonchoosers and “do not remember” are excluded from that paired denominator. Questions record comparison of products, not total attention, research time, actual spending or a latent involvement score. Expected benefits and open explanations need their own reading.

A pattern of comparison in skincare and routine toothpaste choice is consistent with selective involvement. It does not show that the person could afford Premium or that a particular benefit would change the purchase. The two acquisitions can occur at different dates and differ in other circumstances. Retain participants who show the opposite pattern or reasoned sufficiency of Basic.

## Three types of evidence and outputs

1. Reported events/roles/products, with uncertainty and event month where known.
2. Participant explanations and open responses, separated from analyst interpretation.
3. Proposed strategic implications, still conditional on mechanisms and economics.

Do not label an automatic summary “validated pillars.” Do not generate national percentages, causal uplift, clinical benefit or ROI from 40–60 convenience responses. Code outputs are descriptive counts with denominators; they are not prevalence or treatment-effect estimates.

## One-shot operation and data management

Paste all of current Code.gs into the SAME project used for the failed versions; run createSurvey once. It recovers assets through saved Script Properties, builds missing forms, links/verifies two separate workbooks, checks structure, opens forms and prints SHARE_THIS_LINK. It neither deploys a web app nor sends messages. Clearing the project properties destroys the asset registry and may create new files. Google account rules can still affect public responder access; none was checked through a signed-in session here.

Original Forms response sheets and REVIEW are not cleared. CLEAN/RINGKASAN/PETUNJUK/KAMUS are derived and regenerated. The contact form collects volunteered contact only after its own consent; the owner can link codes, so claim pseudonymous handling rather than full anonymity for volunteers. Contacts must not be committed into Git. The script avoids sign-in-based one-response limits for accessibility; it cannot guarantee one person per submission. Reused codes and price/date/reason inconsistencies are review flags, not automatic grounds for exclusion.

## Later interview design

Use optional codes/permission to select contrasts: preferred Premium but supplied Basic; deliberate other-category choice but routine toothpaste; valued benefit then lapse; and counterexamples where shared payment/independent buying sustained Premium. Link the interview to the survey result it explains and integrate contradictions in interpretation. Do not count planned interview numbers as completed respondents or import illustrative customer portraits as quotations.

## Method sources consulted during the chat

These supplied methodological guidance, not Indonesian consumer findings or a sample-size guarantee. Retrieval occurred 4 November 2026; links are not a claim of current availability in later sessions.

- NIH OBSSR, Best Practices for Mixed Methods Research in the Health Sciences: https://obssr.od.nih.gov/sites/g/files/mnhszr296/files/Best_Practices_for_Mixed_Methods_Research.pdf — integration and sequential design.
- AAPOR, Best Practices for Survey Research: https://aapor.org/standards-and-ethics/best-practices/ — neutral specific questions, testing, inclusion of unknowns and transparency.
- AAPOR, Disclosure Standards: https://aapor.org/standards-and-ethics/disclosure-standards/ — sampling/instrument/recruitment reporting.
- AAPOR, Credibility intervals statement: https://aapor.org/statements/understanding-a-credibility-interval-and-how-it-differs-from-the-margin-of-sampling-error-in-a-public-opinion-poll/ — limits of population inference from opt-in samples.
- Pew Research Center, Writing Survey Questions: https://www.pewresearch.org/writing-survey-questions/ — order effects, wording and questionnaire development.

These sources recommend pretesting as good practice. The user nevertheless rejected a separate operational pilot/launch workflow; current code does not enforce it, and no actual questionnaire pretest should be claimed. Possible future interviews are not a current prerequisite.
