# Current project state — 4 November 2026 (Asia/Jakarta)

## Read this first

This state supersedes older planning/status instructions where they conflict. Read [the new session handoff](../research/2026-11-04/context/SESSION_HANDOFF.md), [latest buying situations](../research/2026-11-04/synthesis/BUYING_SITUATIONS_AND_PILLARS.md), and [decision register](../research/2026-11-04/context/DECISIONS_AND_LIMITS.md). Older research/data remain authoritative for their own source observations, not for current operational preferences.

The current deliverable is an additive context/code overlay for the existing repository. Clone reviewed in this chat: `59f28effdf47dbdc5feea33458998bba03e3227f`. No remote push, visibility change, competition submission, paid actor run, respondent invitation or new primary response was performed by the assistant.

## User direction and current research stage

- User wants distinctive, case-specific insights, with evidence, credible opposites and red-teaming. They liked the household-preference insight and especially the contrast between detailed skincare/personal-care consideration and casual toothpaste choice.
- They like routing by actual buying situation. No age-24 cutoff is established; 18–24 and 25–30 are possible descriptive cuts, not exclusive pillar eligibility.
- Immediate executive-summary research is survey-only. Roughly 40–60 respondents may be reachable. Interviews may be possible later for the proposal; do not require them before helping now.
- The planned quantitative-to-qualitative primary sequence becomes explanatory sequential mixed methods only when later interviews are linked to survey results and integrated. No completed mixed-methods study exists.
- Analysis/teaching in English; questionnaire in natural, neutral Bahasa Indonesia.
- User explicitly wants one-shot Apps Script setup. Do not reintroduce required openForPilot/launchSurvey steps.
- The case still asks for three ideas and selection of one. A three-pillar architecture is a working proposal, not a selected final concept, validated intervention or forecast.

## Latest buying-situation architecture

| Buying situation | Current pillar | Important qualification |
| --- | --- | --- |
| A valued preference does not control the household basket | Carry the choice into the purchase | Someone else paying alone is not proof of obstruction |
| Toothpaste has not earned personally meaningful extra spend | Earn the extra spend / give the upgrade a meaningful job | Personal-care interest is not wealth; Basic may be sufficient |
| A valued product does not get replaced | Secure the replacement | Distinguish price/access/timing from misfit, stock and temporary use |

The second pillar was refined after the user highlighted selective category involvement. Earlier selection/education-focused pillar drafts remain as history. The situations can overlap and change for one person; they are not a forced MECE classification or universal funnel.

New purposive readings of the existing corpus include household fallback (jmyv9ux), purchaser-dependent choice (jmyy6vi/jmyktx0), and within-account category contrasts (l5b2lmz/l5gjjk8). Self-described ages are not independently verified. No new platform collection occurred. The older 294 annotations and 314,476 written-record inventory are unchanged. See the replay script and source excerpts for exact provenance and counterexamples.

Case arithmetic remains firm: Basic Rp24,100/190 g is Rp12,684.21/100 g; promotional Premium Rp23,500/100 g has a 2.49% lower ticket but 1.8527x the unit price. This illustrates trial versus sustained affordability, not measured usage or switching causality. The share decline remains seven percentage points, not an identified equivalent decline in absolute Premium revenue, repeat or profit.

## Current survey artifact and Google status

**Current source: [Code.gs v1.1.1](../research/2026-11-04/survey_apps_script/Code.gs).** Paste the complete file into the SAME Apps Script project used for earlier attempts; run `createSurvey()` once. It reuses saved assets, builds missing forms, links/checks separate response/contact workbooks, verifies structure, opens forms and prints `SHARE_THIS_LINK`. No deployment, API key, manual spreadsheet setup or separate pilot/launch function is required. Keep the saved property key `EFEST_TOOTHPASTE_SURVEY_V1` to recover prior assets.

The 36-item main form uses consent/age/Indonesia/comparison routing, with six other-category items skipped when inapplicable. It asks about real product acquisition, separate roles, prior product/experience, desired choice, spontaneous then structured reasons and a parallel personal-care category. It performs no A/B test, validated latent-scale scoring or clinical assessment. The 8–10 minute estimate has not been respondent-tested.

Raw response tabs and REVIEW are preserved. CLEAN/RINGKASAN are descriptive derived outputs. Product hints are not verified tier membership; manual review remains necessary. Contacts are optional and held in a separate workbook, linkable by a voluntary code. No automatic messages are sent. A convenience sample cannot supply national prevalence or a conventional population sampling margin of error.

Two actual user-reported runtime failures are recorded in [USER_RUNTIME_REPORTS.md](../research/2026-11-04/sources/USER_RUNTIME_REPORTS.md): first invalid-data at the optional closed-message setter location; then missing response destination from getDestinationId. v1.1.1 removed the first call and narrowly handles the second, with recovery of completed v1.1 items and no relinking when a destination already matches.

**The user has NOT supplied a successful v1.1.1 execution log, form URL, response export, or completed responses.** The assistant did not execute Google services in the user's account. Local syntax and 184 mock assertions passed, including 126 routing combinations and failure recovery. These do not prove live Google access, UI rendering, respondent comprehension, or method validity. Future debugging should begin from the actual error and preserve assets/data; future analysis should begin from actual exports and eligibility.

The standalone survey ZIP has persistent Library ID `libfile_e16f9bbfb8e481919ef707601fea7448` (version 2 as last saved), titled Pepsodent_Survey_AppsScript_v1.zip; its contents are now included as source here. That filename does not mean initial v1.0 code is current. An exact user-submitted v1.1.0 source and the mentoring PDF are retained under the new dated sources folder.

## Evidence inventory (retained 3 November baseline, unchanged)


The portable master contains **314,476 retained written platform records across all retained scopes**. This is an archive inventory, not a count of independent people, eligible toothpaste experiences or Indonesian young adults.

| Platform | Written inventory records |
|---|---:|
| Amazon external context | 286,706 |
| Watsons | 7,419 |
| Lazada | 681 |
| ORESA | 2,228 |
| TryandReview | 1,423 |
| Reddit | 389 |
| X | 12,995 |
| TikTok | 2,372 |
| Tokopedia | 263 |

The earlier integrated store contributes 298,846 records. Four new X exports contain 16,165 occurrences and 12,990 post IDs. One post overlaps the earlier six-post public sample; five additional brand excerpts are retained, giving 12,995 combined X IDs. Marketing and unresolved lexical candidates remain flagged. Author pseudonyms are not known people or verified demographics.

TikTok contains 2,380 IDs, including eight blank texts, across 18 videos. All 699 replies have their parent IDs in the export. Using Jakarta dates, 1,648 comments fall within 2022–H1 2026. Earlier chat counts of 1,649 used UTC; one comment crosses midnight at the H1 boundary. Both conventions are preserved.

Tokopedia contains 266 unique review IDs, including all 43 pilot IDs. There are 263 nonempty texts, 256 broad written-toothpaste candidates and 147 provisional case-period candidates under source-specific exclusions. Date fields disagree in 186 of the 198 records where both fields are present; another 68 lack reviewTime. Missing is not disagreement. A preliminary 254/266 comparison incorrectly counted missing fields as conflicts and is superseded. Source dates remain unverified.

Shopee's two error rows and 100 Singapore UGREEN review records are archived but excluded from oral-care analysis. The reported 5,323 scanned shop reviews were not delivered. Product cards, billing notices, blanks, repeated observations and copied text are not additional independent consumer accounts.

The earlier Amazon pass screened 26,125,466 review rows and 857,856 metadata rows; the full upstream millions were not retained. International title candidates include adjacent, children's and accessory products, with documented classification errors. International evidence remains contextual. All target-age and Pepsodent Premium-to-Basic verification flags remain false.

Earlier retail contexts, brand/campaign/history observations, literature appraisals, public indicators, original teaching material and 300 keyword observations remain included. Their units and overlapping subsets must not be added together as consumers or reviews. Source-specific eligibility and incentive limitations accompany any interpretation.


## Material limits and next work

No authenticated 18–30 Pepsodent Premium-to-Basic sequence, primary interviews, team survey responses, price elasticity, regular-price retention cohort, cause allocation, incremental lift forecast or ROI exists in the material available here. Public/actor-export source truth is not authenticated by checksums. Current catalogues are not historical paid prices or branch stock. The case's illustrative survey is not team primary evidence.

If the next task is technical, use v1.1.1, the attached exact previous script and both actual error reports; do not rely on mock pass counts to dismiss real failures. If survey responses arrive, inspect raw values/variants/eligibility, retained versus temporary use and paired-category participation. Do not assume the target of 40–60 has been achieved. If preparing strategy, test competing mechanisms and the distinction between three alternatives and selected implementation pillars. Interviews are a later possible explanation phase, not completed work.

Keep event timing explicit: the case ends H1 2026. Current November experiences can inform mechanism relevance without automatically explaining the earlier mix decline. Primary contact details and response exports should not be committed to Git by default.

## Continuity and reproduction

Read the [new dated index](../research/2026-11-04/README.md), detailed [session record](../research/2026-11-04/context/SESSION_RECORD.md), method/question map, source register, runtime history and actual code. The older 3 November closure handoff and original master remain unchanged. Before-update root documents and the incremental notes were archived, rather than silently erased. CONTEXT_LATEST combines current state and both sessions' relevant context, with historical sections labelled.

The ZIP is an overlay, not a standalone data repository. It includes new/changed context and code, not a second copy of the existing corpus, .git or unrelated workspace artifacts. See root INSTALL_CONTEXT_UPDATE.md. Use `python scripts/verify_context_update_20261104.py` for the overlay and the existing release verifiers for the complete repo. Integrity checks are not substantive validation.
