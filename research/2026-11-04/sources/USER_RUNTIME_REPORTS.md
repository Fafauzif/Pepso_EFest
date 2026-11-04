# User-reported Google execution logs

These are visible messages reported by the user, not logs retrieved through a signed-in Google session. Clock times are preserved as supplied; their console timezone was not independently confirmed.

## First failure — initial v1.0

User asked to remove the pilot/open stages and make setup one-shot.

```text
11:13:00 Notice Execution started
11:13:00 Info Self-checks passed. Main questions: 36
11:13:08 Error
Exception: Invalid data updating form.
configureForm_ @ Code.gs:318
(anonymous) @ Code.gs:191
withLock_ @ Code.gs:344
createSurvey @ Code.gs:180
```

The reported location was the end of a setter chain, including optional setCustomClosedFormMessage. The assistant removed that call and unnecessary quiz configuration, split remaining setters and changed operation to one-shot v1.1.0. The precise Google backend reason for the first invalid-data exception remains unverified.

## Second failure — user-submitted exact v1.1.0

The user's attached source is preserved byte-for-byte in User_Submitted_Survey_v1_1_0_Exact.txt, including original line endings.

```text
11:17:55 Notice Execution started
11:17:54 Info Self-checks passed. Main questions: 36
11:18:27 Error
Exception: The form currently has no response destination.
(anonymous) @ Code.gs:214
withLock_ @ Code.gs:336
createSurvey @ Code.gs:180
```

The unsafe line queried getDestinationId before any destination had been set. The service throws for this state; the initial local mock incorrectly returned null. Current v1.1.1 catches only the known no-destination exception, links/verifies the spreadsheet and leaves already matching links intact. The regression suite now models the thrown exception and recovery without rebuilding completed questions. There is no user-reported successful v1.1.1 execution in the visible chat.
