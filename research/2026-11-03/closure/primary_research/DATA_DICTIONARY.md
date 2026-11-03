# Data dictionary and entry rules

All files in `templates/` are **blank instruments**. Each CSV has one header row and zero participant rows. `SCHEMAS.json` gives the exact ordered column names. Copy templates into a dated fieldwork folder before filling them. Do not put raw contacts, original identifying audio, or unredacted receipts in Git.

## Units and joins

| Template | One row represents | Main identifier / joins |
|---|---|---|
| recruitment_tracker | One screened prospect's recruitment progression | screen_id; participant_id only when assigned |
| screening_log | One screening event | screen_id; not a completed interview |
| consent_log | Permissions for one interview/participant interaction | participant_id + interview_id; consent version |
| interview_index | One completed/attempted interview | interview_id → participant_id |
| case_sku_roster | One product/variant/pack tier-classification entry | sku_id; source + valid period |
| purchase_events | One actual purchase/replacement event | event_id → participant_id + interview_id; sku_id if resolved |
| evidence_coding | One quoted/paraphrased evidence unit | evidence_id → interview_id/event_id + locator |
| diary_events | One follow-up contact/event report, including no-event/nonresponse | diary_entry_id; related_interview_id; event_id if reported |
| shelf_observations | One observer/SKU/outlet/time observation | observation_id + sku_id; not a respondent |
| choice_tasks | One task presentation/response | task_id → participant_id/interview_id; task version and card order |
| pilot_changes | One instrument/process revision decision | change_id → pilot_interview_id |
| coding_disagreements | One disagreement and its review history | disagreement_id → evidence_id |
| hypothesis_updates | One dated hypothesis review | update_id + hypothesis_id + linked evidence_ids |

The number of purchase events, quotations, or diary contacts must not be counted as the number of independent people. A participant may have multiple interviews. A payer/co-user informant receives a distinct participant_id and is linked in notes, not merged into the target participant's identity.

## Common field types

- IDs, codes, source locators, and versions are **strings**, even if a team chooses digits. Preserve leading zeros.
- Dates use ISO `YYYY-MM-DD` only when known. `*_on` fields refer to the data-collection interaction unless otherwise specified. `event_date_raw` preserves the respondent's wording. An approximate month becomes earliest/latest bounds with `date_precision=month`, not a guessed exact day.
- Times are local with timezone stated in the wave README. Durations are minutes, observed or estimated with a note.
- Monetary values with `_idr` are numeric rupiah without formatting separators. A genuine observed zero is `0`; unknown is empty plus the appropriate status/reason. Do not assume a zero price because a person received a product from someone else.
- Gram fields and tube counts are positive numeric values when known. Never convert ml to grams without an explicit justified product-specific conversion; normally leave unresolved.
- Text fields use original language and CSV quoting. `*_verbatim` preserves wording; normalization belongs in a separate field.
- Multi-value codes/IDs may be separated by `|` within the CSV cell. This is a storage convention, not a statement that multiple causes were ranked.

## Missingness, zeros, and inapplicability

Do not use one symbol to mean every kind of missingness. Keep the value empty where numeric/date parsing requires it and record why in its paired status or `uncertainty_notes`/`*_notes` as `field_name=reason`. Reasons: `not_asked`, `participant_does_not_know`, `participant_does_not_recall`, `declined`, `not_applicable`, `not_observed`, `unresolved`, or `not_yet_occurred`. Preserve any original “tidak tahu” wording in the relevant verbatim field.

For instance, a nonbuyer may not know the paid price; that is different from explicitly paying zero from their own pocket and different from the product's actual transaction price being zero. A participant who has not yet needed another tube has no completed next purchase; this is not zero loyalty. A contact that receives no response is not a no-purchase observation.

## Critical status definitions

| Field(s) | Allowed starting values and meaning |
|---|---|
| age_18_30_confirmed | yes / no / unknown / declined; based on screening, not appearance |
| purchase_context_indonesia | yes / no / mixed / unknown; account of actual event geography |
| eligibility_status, eligible_target_status | eligible / ineligible / uncertain; include reason and scope |
| provisional_history_group, history_group, history_group_confirmed | A_switch_candidate / B_retained_premium / C_basic_or_competitor / U_uncertain; A requires a resolved sequence and case-tier verification for confirmed status |
| time_scope | case_period_2022_to_2026H1 / later_than_case / older_context / mixed_events / unknown; use event-level scope where possible |
| tier_verification_status, sku_verification_status, tier_status | verified_against_case_source / provisional / unresolved / not_applicable; source locator required for verified tier |
| case_tier | Premium / Basic / outside_case / unresolved; use case-specific definitions, not price thresholds |
| date_precision | exact_day / week_range / month / year / event_anchor_only / unknown / not_applicable |
| chooser_role, buyer_role, payer_role | self / parent_family / partner_housemate / shared / other / unknown; preserve details in notes; selecting, checking out, and funding are different roles |
| tube_context, users_context | personal / shared / parallel_personal_and_shared / mainly_other_users / unknown; do not assume number of users |
| knowledge_direct_or_third_party, knowledge_basis | directly_did_or_observed / told_by_other / mixed / unknown; receipt/photo evidence is separately referenced |
| price_certainty | receipt_or_record / exact_self_report / approximate_self_report / third_party_report / unknown / declined / not_applicable; exact self-report is not receipt verification |
| availability_status, availability_basis | observed_on_shelf / listed_online_location_selected / listing_only_location_unknown / staff_reported_unavailable / participant_reported_unavailable / not_found_in_observed_area / unknown; preserve basis and limits |
| next_action_status | completed_repurchase / continued_use_only / intended_repurchase / temporary_substitution / parallel_use / switch_sequence_reported / unknown; combine codes if a sequence truly requires it and explain |
| followup_status | not_invited / invited / consented_waiting / event_reported / no_event / no_response / declined / withdrawn / completed; operational states are not retention outcomes |
| interview_notes_permission and other permission fields | yes / no / not_requested / withdrawn; permissions asked separately |
| source_type | audio_transcript / contemporaneous_notes / participant_message / redacted_receipt / redacted_product_photo / observer_note / other; exact material identifier in source_locator |
| quote_or_paraphrase | verbatim_verified / verbatim_notes_unverified_audio / paraphrase; never put an analyst's rewrite in quotation marks as verbatim |
| evidence_relation | supports_mechanism / counterexample / rival_explanation / insufficient / outside_scope; applies to the linked hypothesis |
| chronology_status | sequence_clear_self_report / sequence_record_supported / partial / conflicting / unknown |
| mechanism_confidence_label | plausible_supported_in_events / tentative / weakened / unresolved; add narrative confidence_reason |
| target_applicability_label | direct_target_events / indirect_or_mixed / outside_target_context / unresolved; no claim of prevalence |
| review_status | pending / second_reviewed / disagreement_open / revised / excluded; preserve exclusion reason |
| include_in_substantive_analysis | yes / no / pending; pilot inclusion separately justified |

These starting categories can be revised after pilot testing. Log the version and recode transparently. A taxonomy change must not silently erase the original response.

## Important columns by template

### Recruitment and screening

`recruitment_channel` records how the person was reached, not their identity; `relationship_to_team` makes convenience/access bias visible. `student_worker_other_self_report` is optional and self-reported. `access_gap_notes` records missing contrasts, not a score of how cooperative a person was. `current_product_verbatim` and prior products are not normalized automatically. `approx_transition_period_raw` may remain vague. `eligibility_notes` explains exactly what is unresolved.

### Consent and interview index

`restricted_storage_reference` is a nonpublic internal reference, not a secret access URL or contact list. `withdrawal_deadline_agreed` and `planned_deletion_date` must reflect what the participant was actually told. `deidentified_notes_path` points to the version safe for the team repo. `guide_variant` distinguishes full and short interviews. `pilot_or_main` preserves the instrument-testing context.

### Product roster

`tier_source_locator` cites the case/company/verified classification source; it must not cite the participant's willingness to call a product premium. `valid_period_start/end` limits historical SKU membership where known. Different sizes may share a benefit promise but remain separate pack entries. Do not overwrite a disputed tier; keep classification_notes.

### Purchase events

`sequence_order` is chronological within participant history; `event_id` remains stable if ordering changes. `trigger_verbatim` states what occasioned replenishment. `paid_product_price_idr` refers to the product component only where known; shared-voucher/other-cart ambiguity is recorded in `shared_voucher_or_shipping_notes`. `alternatives_actually_considered` is not the analyst's constructed competitor set. `decision_reason_verbatim` preserves the participant explanation; `reported_experience` does not become a clinical outcome. `next_action_status` records what is known after the event.

`evidence_reference_redacted` points to a safe derivative, not an unredacted original. `source_locator` can be an anonymized notes section or audio timestamp in restricted storage; do not include authentication tokens. `uncertainty_notes` carries field-specific missingness and contradictions.

### Evidence coding and hypothesis updates

`text_original` preserves the quoted/paraphrased material; `analyst_interpretation` and `rival_interpretation` are separate. `code_ids` may contain multiple codes, but `hypothesis_id` must be identified for `evidence_relation` to have meaning. Copy the evidence unit to a separate row with a new coding relation if the same phrase supports one hypothesis and challenges another. This does not create a second independent participant observation.

`prior_prediction` should be written before using the new evidence to rationalize the hypothesis. `evidence_ids_supporting/conflicting` links actual coded evidence, not a bibliography placeholder. `conditional_strategy_implication` is prospective and contingent, never an observed result.

### Optional modules and QA

`already_used` distinguishes a purchase from a post-use experience. `selected_location_status` describes the shelf/listing location, not inferred geography. `card_order` and `price_context_and_date` preserve choice-task presentation; `after_clarification_choice` is a hypothetical response, not conversion. `coding_disagreements` preserves both initial interpretations before resolution. `pilot_changes` documents changes even when a question is removed.

## Quality checks after real collection

Check unique IDs; valid joins; no identifying contacts in analytical files; consent before eligible use; all substantive quotations linked to source; factual versus estimated dates; consistent pack math; explicit missingness; interview/event/quote denominators kept separate; any confirmed switcher has traceable SKU/time/sequence evidence; no fabricated response rows; and unresolved disagreements retained.

Run `python3 research/2026-11-03/closure/primary_research/verify_templates.py` from the repo root to verify this shipped instrument kit. That script checks the blank originals, not a future populated wave. A future data validation script should operate on the wave copy and preserve raw notes.
