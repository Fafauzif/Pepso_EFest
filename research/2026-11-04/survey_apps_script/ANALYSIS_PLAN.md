# Analysis plan — executive-summary survey

Version 1.1.1, 4 November 2026. No responses have been collected as part of creating this package.

## Purpose and design

Exploratory cross-sectional online survey with retrospective accounts of the most recent toothpaste acquisition, the previous product, and a within-person comparison with the most recent non-toothpaste personal-care acquisition. No randomized intervention, vignette, or A/B test is included. The wider primary-research plan can become explanatory sequential quantitative-to-qualitative mixed methods if later interviews are selected to explain survey patterns and integrated into interpretation.

The 40–60 response goal is a practical recruitment target, not a population-precision or statistical-power justification. Prioritize actual reported Pepsodent Premium-to-Basic histories and retain contrasting Premium users and Basic pathways. Report who was reached and who was not. Ages 18–24 and 25–30 are descriptive cuts, not established consumer segments.

## Inclusion

Main phase begins at the first `createSurvey` timestamp in the one-shot version. An existing launch timestamp from an older version is retained. Include only consented, completed responses in the stated age range that report toothpaste use while living in Indonesia during the previous six months. Any historical responses before that timestamp are marked BEFORE_START and excluded; the one-shot version has no separate pilot workflow. A submitted refusal or age/scope screenout is not a full survey completion. Do not relabel unreviewed or uncertain variants as Premium-to-Basic switchers.

Record recruitment channels, field dates, exclusions and actual sample counts. Restrict conclusions to the recruited sample. Do not claim a national margin of sampling error for convenience recruitment. Do not use weighting to make the sample appear representative without a defensible sampling and adjustment design.

## Three buying situations to investigate

These can overlap. Do not force each respondent into exactly one pillar or code their answers to confirm the preferred strategy.

| Situation | Supporting pattern to examine | Rival or boundary |
| --- | --- | --- |
| Preference does not reach household basket | Specific preferred product differs from acquired product; another person chooses/supplies it; narrative connects that arrangement to the outcome | Someone else paying alone is not obstruction. The buyer may willingly fund Premium. |
| Upgrade does not earn extra spend | Respondent participates in choices; toothpaste expectations remain routine; another personal-care category receives more comparison or a more specific desired outcome | Product interest does not demonstrate income or ability to afford Premium. Basic can be sufficient. |
| Valued product does not get replaced | Previous specialist benefit was felt and valued, but price, forgetting or exact-variant access appears in the replacement account | Misfit, changed need, parallel use, remaining stock or a gift can explain the same name transition. |

## Useful outputs

1. A product-pathway table after manual variant review: prior product versus last acquired product. Label it reported acquisition pathways, not independently verified abandonment.
2. A preferred-versus-acquired comparison with chooser, payer and shopper roles. Review actual free text before calling a mismatch.
3. A paired-category table among respondents who participated in both choices and remember both processes. Compare whether alternatives were considered. Treat open responses about expected outcomes separately. This is observational self-report, not a treatment effect or a complete psychological involvement scale.
4. A table of reasons with explicit denominators among relevant reviewed switchers, plus retained-Premium counterexamples. Checkbox percentages overlap and need not sum to 100%.
5. A small set of anonymized written explanations, with respondent codes and exact wording retained privately. Mark paraphrases as paraphrases. Never invent interview quotes.

RINGKASAN automatically reports only simple counts. It does not decide which mechanism dominates, conduct significance tests, score latent constructs, infer willingness to pay, estimate promotional lift, or validate a clinical claim.

## Data-quality checks

- Retain unknown, missing, explicit zero, free product and approximate price as distinct values.
- Review `PRICE_*`, `MONTH_*`, `REASONS_CONFLICT` and reused-code flags; they do not automatically justify deletion.
- Record reasons for exclusion without overwriting the raw log.
- Do not infer an actual purchase price from a listing or assign a missing price to zero.
- Names without a clear variant remain uncertain.
- A recently acquired tube not yet used is not a completed use experience. Alternating products or temporary household use is not necessarily abandonment.
- Most recent toothpaste and most recent other-category events may be at different times. The paired comparison does not control all contextual differences.
- Do not split 40–60 respondents into numerous small age × household × pathway cells. Report small group denominators plainly.

## Case timing

The case horizon ends June 2026. The optional MM/YYYY acquisition field helps distinguish timing. Later experiences can test current mechanism plausibility but do not establish the causes of the historical sales-share decline. Missing dates remain missing; do not infer a historical event from a present-day product.

## Follow-up interviews for the proposal

With separate permission and a matching voluntary code, select contrasting survey patterns: preferred Premium but supplied Basic; low toothpaste differentiation alongside more deliberate personal care; valued benefit followed by lapse; and cases where family funding or independent buying sustained Premium. Reconstruct the actual events, probe rival explanations and integrate these accounts with the survey results. Ask for documentary prompts only voluntarily. No interview or diagnosis is part of this survey package.

## Appropriate reporting language

Use “Among the respondents we reached, X of Y reported…” and specify the eligible subgroup. Use “consistent with”, “suggests investigating”, and “self-reported” where appropriate. Report material contrary cases.

Avoid “X% of Indonesian youth…”, “we proved the cause”, “the three pillars are validated”, “discounts increased retention”, or “Premium improved dental health” from this survey alone.
