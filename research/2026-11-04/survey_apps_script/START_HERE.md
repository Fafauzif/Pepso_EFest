# One-shot Google Forms survey — v1.1.1

## Replace the failed script

1. In the SAME Apps Script project, replace the entire contents of Code.gs with this package's Code.gs. COPY_PASTE.txt is an identical plain-text copy.
2. Save, select **createSurvey**, and click **Run**. Authorize if Google asks.
3. At completion, copy the URL after **SHARE_THIS_LINK:** in the execution log. This is the respondent link to share.

That is the whole setup. No openForPilot, launchSurvey, Deploy, API key, or manual spreadsheet setup is needed. The main form and optional contact form open automatically. Do not delete Script Properties or create a new project to recover the failed attempt: the same project can reuse the saved form and spreadsheet IDs.

If you do not already have a project, create one at https://script.google.com/, paste the code, and run createSurvey once.

## What changed

- Fixed the second reported failure: getDestinationId throws when there is no response destination. The new helper handles only that known absence, then sets and checks the destination. Other errors remain visible.
- Both completed forms from the failed v1.1 run are reused, without rebuilding their questions.

- Removed setCustomClosedFormMessage, the optional configuration call at the reported failure location.
- Removed the separate pilot and launch functions.
- Publishes recovered unpublished forms before configuring response state, then opens them automatically after building and verification.
- Settings are individual calls so any future failure identifies the actual line instead of a long chain.
- Accepts and recovers state saved by version 1.0.0. Reruns reuse the same assets without resetting responses.
- Prints SHARE_THIS_LINK before optional analysis refresh, so a summary-sheet error does not hide the working link.

## Data and optional follow-up

The survey wording and branching are unchanged: 36 main question items, with the six-question personal-care comparison skipped when not applicable. The main survey does not ask for a name, email or phone. Interested participants may create a code and use the separate optional contact form linked after submission. Contacts are stored in a separate workbook. The same owner can link contacts and survey answers by code, so this is not full anonymity for volunteers.

The response workbook contains:

- **PETUNJUK**: links and brief instructions.
- **KAMUS**: variable codes and exact wording.
- **CLEAN**: submitted responses with eligibility and completion flags.
- **RINGKASAN**: descriptive counts and denominators.
- **REVIEW**: manual product-tier review, preserved on refresh.

The original Google Forms response tab is never cleared or renamed. CLEAN/RINGKASAN are generated tables; keep manual notes in REVIEW or a new tab. In REVIEW, use BASIC, PREMIUM, OTHER or UNKNOWN for exact case-appropriate current/previous product names, plus a note. Automatic product-name hints do not establish verified switching.

A fresh one-shot setup counts all complete qualifying responses submitted after its first createSurvey call. If continuing an older project that already had a recorded launch time, that original time is preserved; earlier responses remain labelled BEFORE_START. The reported failed attempt should have no substantive responses.

## Optional maintenance

- **getSurveyLinks** prints links again.
- **refreshResponses** refreshes CLEAN and RINGKASAN. Normally this runs automatically after each main-form submission. If account policy blocks trigger installation, refresh manually.
- **verifySurvey** checks the form's structure and key settings.
- **closeSurvey** stops new submissions. Running createSurvey again reopens it without deleting responses.

No sign-in-based one-response limit or email collection is enabled. Google Workspace policy can still restrict responder access. If a signed-out respondent sees an access restriction, check the form editor's Publish/Manage responder access setting or use a permitted personal Google account. The script cannot override organization policy.

## Testing boundary

Syntax validation and 184 local assertions passed, including 126 routing combinations, the failed-v1.0 migration, idempotent reruns, automatic opening, raw-response preservation, and a regression mock that throws if the old closed-message setter is called. These tests use Google-service mocks and do not claim authenticated execution in your Google account. The next live verification is the one createSurvey run in your account.

## Package contents

Code.gs and COPY_PASTE.txt are the same script. KUESIONER.md contains the exact wording. ANALYSIS_PLAN.md explains interpretation. TEST_RESULTS.json and test-survey.cjs document local checks; do not paste test-survey.cjs into Apps Script.

Official API reference: https://developers.google.com/apps-script/reference/forms/form
