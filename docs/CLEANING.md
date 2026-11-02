# Cleaning specification and ledger

## Observation unit and keys

One copied keyword result row in one source capture. Observation IDs are source ID plus 1-based result-row ordinal. Source line bounds refer to the UTF-8 text split into logical lines; raw bytes remain unchanged. The normalized keyword key uses Unicode NFKC, casefold and collapsed whitespace. It does not stem, translate, fix spelling or merge odol/pasta gigi, merk/merek, or Sensitive/Sensitiv variants.

## Source parsing

Source 01 and source 02: parse seven tab-separated fields. Missing headers mean the mapping keyword/intent/volume/KD/CPC/SERP features/updated is inferred and flagged. Keep every blank cell and relative update label. No trend field is present.

Source 03: skip browser navigation and entered query list to `Selected:` / `0`; read result groups until `Contact us`. Intent labels are followed by decorative I/N/C/T codes; retain label(s) and discard only redundant codes. Updated labels end each row. Positive/zero rows have volume, KD and CPC tokens. Missing rows explicitly have n/a volume, n/a trend, KD and n/a CPC. No copied SERP values are fabricated. Compare the exact multiset of 100 entered query terms with the 100 parsed result terms, rather than counting navigation/seed text as extra observations.

## Values

Strip thousands commas in numeric tokens; parse volume and KD as integer and CPC as decimal. Preserve original strings in *_raw fields. An empty token -> null with status blank; n/a -> null with status not_available; explicit 0 -> numerical zero with status zero. No imputation, winsorization, rounding corrections or blank-to-zero replacements.

CPC currency: IDR confirmed only by source 03 header. Null for sources 01/02. Flag numeric CPC >100000 as a review heuristic, without declaring it an error or changing it. `cpc_analysis_value` is null when currency is unconfirmed or the heuristic is triggered. It is otherwise the parsed value. Threshold is a diagnostic convention, not a statistically estimated cutoff.

Market: user's requested Indonesia is metadata; no copied country selector verifies it. Keep false country_verified_in_capture. Dates: retain Now / 1 month / 20 min as raw display labels, not inferred capture dates. Packaging date is 2026-11-03; retrieval_date remains null.

## Deduplication

Retain all source observations. Group by normalized keyword for the unique view. Identical selected metric signatures collapse only in the unique view while listing every observation ID. Different signatures go to duplicate_conflicts.json and are excluded from unique view rather than arbitrarily resolved. Current release has no duplicate groups. Revisit this policy if later captures supply different periods/countries; those should not be treated as accidental duplicates.

## Derived annotations

Rule-based theme_tags are multi-label exploratory analyst annotations implemented in the script; they are not Semrush categories or validated sentiment. `brands` matches literal known brand names with word boundaries; comparison queries can have multiple brands. Exact generic brand strings close up/formula/enzim are flagged for ambiguity. Do not infer premium tier from a keyword or a theme tag.

## Validation completed

300 observations reconcile to 100 rows from each of three files. 300 normalized keys. All numeric volumes nonnegative, KD 0-100, raw strings retained, query/result set for source 03 matched exactly. Four volume states reconcile to 300. Four CPC numeric outliers flagged. Generated outputs were reproduced and compared by byte hash. Original master, pasted inputs and supplied PDF were checked against their included copies. ZIP tested for corruption.
