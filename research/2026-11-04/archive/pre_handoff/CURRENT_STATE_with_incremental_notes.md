# Current project state — 3 November 2026 (Asia/Jakarta)

## 4 November 2026 exploratory insight update

The user supplied Mentoring Notes — Problem Analysis in BCC.pdf and requested sharper, non-obvious insights. A targeted reanalysis of the existing non-Amazon corpus and Reddit thread context identified useful household fallback accounts (jmyv9ux, jmyy6vi, jmyktx0) and within-person personal-care/toothpaste involvement contrasts (l5b2lmz, l5gjjk8). See research/2026-11-04/INSIGHT_STRESS_TEST.md for source locators, method, counterexamples and falsifiers. These are purposive secondary readings, not new fieldwork, prevalence estimates, independently verified ages or confirmed Premium-to-Basic sequences. Existing 294 annotation counts are unchanged. Candidate interpretation: a specialist preference can lose to a household-supplied fallback at replenishment; a separate rival is low incremental toothpaste value despite detailed personal-care interest. The case promotion's lower tube ticket still carries 1.85x Basic's unit cost. No final strategy selected; the previous evidence boundaries remain.

## Accepted scope

Survey v1.1.1: user reported “The form currently has no response destination” at createSurvey line 214 and attached their exact v1.1 script. Confirmed unsafe getDestinationId call before setDestination. Added responseDestinationId_ which catches only the known no-destination exception, and ensureResponseDestination_ for both forms; verifies target after linking and does not relink an already-matching destination. Accepts v1.0/v1.1 state and preserves completed questions from failed v1.1 setup. Corrected the test double to throw for an unlinked form instead of returning null. Passed 184 local assertions, including built-but-unlinked v1.1 recovery preserving item IDs, no duplicate linking, and permission-error propagation. Existing ZIP Library ID retained, now version 2; both direct script preview paths updated. Live Google run still not performed by assistant.

Survey v1.1.0 update: the user reported Google runtime “Invalid data updating form” at configureForm_ line 318 (the chained optional setCustomClosedFormMessage call) and explicitly requested one-shot creation with no pilot/launch steps. Removed that setter and unnecessary quiz configuration, split remaining setters into individual lines, published recovered draft forms before changing response state, and made createSurvey build/open both forms automatically and print SHARE_THIS_LINK. Removed openForPilot and launchSurvey; retained saved property key for recovery of the failed v1.0 attempt. Local tests now pass 172 assertions including the old-setter failure regression, 126 routes and migration from unpublished v1.0 state. Actual Google execution of v1.1 remains unverified here. The existing ZIP Library identity is retained with revised contents; source preview is output/survey-pepsodent-oneshot/Code.gs and the old preview Code.gs was also updated. No responses created or collected by the assistant.

The user requested a usable Apps Script survey with natural Indonesian wording. Created Pepsodent_Survey_AppsScript_v1.zip (Library ID libfile_e16f9bbfb8e481919ef707601fea7448), containing single-paste Code.gs, identical COPY_PASTE.txt, START_HERE.md, exact generated KUESIONER.md, ANALYSIS_PLAN.md, and local tests/results. Script creates closed main/contact Forms and separate response/contact workbooks, uses consent/age/Indonesia/comparison branching, marks responses before launchSurvey as pilot, preserves raw response tabs and manual review, and computes descriptive counts only. There are 36 main question items; 6 comparison items can be skipped. Syntax and 169 local mock assertions passed, including 126 route combinations; no authenticated Google execution or browser test was performed. First Google authorization, responder access, wording comprehension and actual duration remain user-side pilot checks. No form has been created in the user's Google account, no invitations sent and no primary responses collected here. Source preview lives under /workspace/scratch/b2a4077cffdb/output/survey-pepsodent; the persisted ZIP is the portable deliverable. Do not claim causal or population findings from this instrument.

The user subsequently clarified stage-specific access: no substantive interviews expected for the executive summary; an online survey may reach approximately 40–60 respondents, with interviews possible in the later proposal stage. This supersedes earlier interview-first planning for the immediate task. Proposed primary design: an exploratory cross-sectional survey with retrospective product-acquisition history, separate user/chooser/payer roles, a matched within-person toothpaste/non-toothpaste personal-care comparison, and limited open responses. Later interviews should be selected from informative/contradictory survey patterns and integrated, making an explanatory sequential quantitative-to-qualitative primary design if completed. No primary data collected, questionnaire finalized, survey published or interviews completed. Avoid describing convenience sampling as representative, supplying a conventional sampling margin of error, or treating age cuts as established segments. Proposed priority is actual reported Premium-to-Basic histories plus retained-Premium and Basic contrasts; do not relabel general toothpaste users as switchers. No split-sample experiment recommended for this small immediate wave. New November purchases test current mechanisms and cannot directly explain the historical H1 2026 mix decline.

On 4 November the user requested a refined three-pillar solution and challenged whether household influence should be limited to ages 18–24. A proposed behavioural architecture is recorded in research/2026-11-04/THREE_PILLAR_PROPOSAL.md: carry choice into household buying; establish personally valued specialist benefit; secure the next paid replacement with access/reminders and a separately tested limited return offer. Age-exclusive targeting and blanket discounts are not supported by current evidence. This is an analyst proposal, not an accepted or validated final strategy; preserve the brief's three-ideas-then-select-one requirement.

The repository is intended for the private team. Analysis and teaching are in English; fieldwork tools are in Indonesian. Access to participants is uncertain, so the primary-research plan has flexible versions. The user requested all available research, data and substantive chat context in an extract-and-replace ZIP, delivered through Filebin. They will commit and push with GitHub Desktop.

The user confirmed no newer edits. The final remote HEAD/main check matched the starting commit, 423cce08921b611fd01fbf6d25a0f86b65986f76. The assistant has not pushed, changed visibility, contacted participants or executed paid actors.

Secondary research is sufficient to prioritize and challenge hypotheses. No final strategy, verified target-switcher sample, primary interviews, target-cohort prevalence, price elasticity, normal-price retention estimate or causal uplift forecast exists.

## Evidence inventory

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

## What the analysis changes

Payer transitions, household authority, sensory fit, experienced benefit, availability and regular refill affordability remain competing mechanisms. New examples include explicit Ultra White repurchase because it fits, benefit-driven Sensodyne continuation, Enzim loyalty alongside promotion interest, and parent-funded Sensodyne versus self-paid boarding-house affordability. The source-linked report presents counterexamples and alternative interpretations. These accounts do not establish the causes or shares of the case's decline.

The new close-reading set contains **294 annotations: 109 X, 100 TikTok and 85 Tokopedia**. Sampling methods and independent assistant consistency checks are documented. All 266 Tokopedia texts were also screened. Close reading is not a representative survey or human field validation.

Historical minimarket promotions and larger premium packs exist. Pepsodent already has ShadeScan AI, specialist education, professional-care activity and sampling history. A generic scanner, education or discount idea needs a specifically demonstrated unmet mechanism. Basic can be a rational sufficient choice.

## Next work

Read the new decision brief, diagnosis/teaching report and 11-hypothesis matrix in research/2026-11-03/closure/synthesis/. Then use closure/primary_research/README.md to prepare two pilot interviews followed by an adaptable initial 8–12 substantive purchase-history interviews. Verify 18–30 eligibility and actual product/variant history; include contrasting retained-premium and Basic/competitor pathways.

Ask who chose, paid and used the product; what was bought previously; pack, outlet and actual paid price; available alternatives; and what happened at replacement. Optional natural replenishment follow-up can observe action rather than only stated intention. All response templates are blank. No primary fieldwork has occurred. No further broad paid collection is required before piloting this work.

## Reproduction and continuity

All 11 new attachments are archived losslessly, with original-byte SHA-256 values in closure/raw/UPLOAD_REGISTER.json. Source-specific clean tables, occurrences, exclusions, annotations, codebooks and rebuild scripts are retained. The new integrated record-aware shards work directly. Five larger legacy exports are exactly reconstructible from release/LARGE_FILES.json in the portable package; local restored paths are Git-ignored.

Read START_HERE.md and closure/context/SESSION_HANDOFF.md for the complete substantive visible-chat handoff. Previous current-state, README and combined-context versions remain in closure/context/BEFORE_CLOSURE_*. Original master and raw sources remain unchanged; missing original PDFs/inputs remain missing. This is a substantive reconstruction, not a verbatim chat export or unseen memory. The historical Filebin receipt is retained; the new delivery receipt accompanies the final archive.
