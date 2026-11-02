# Release quality report

| Measure | Count |
|---|---:|
| Raw captures included | 3 |
| Parsed observations | 300 |
| Unique normalized keywords | 300 |
| Duplicate groups / conflicting groups | 0 / 0 |
| Positive volume | 138 |
| Explicit zero volume | 11 |
| Blank volume | 107 |
| Explicit n/a volume | 44 |
| CPC numerical review flags | 4 |
| Missing attached raw file | 1 |

The 151 blank/n/a volumes are retained. These counts describe this selected keyword dataset and must not be reported as consumer percentages or national prevalence. Metadata gaps are not repaired by assumption.

## CPC review queue

| Keyword | Raw CPC token | Treatment |
|---|---:|---|
| pepsodent herbal | 5216087.41 | Preserve; flag; currency unconfirmed |
| pepsodent pencegah gigi berlubang | 5205573.67 | Preserve; flag; currency unconfirmed |
| pepsodent sensitive mineral expert | 993549.09 | Preserve; flag; currency unconfirmed |
| odol untuk gigi kuning | 536019.83 | Preserve; flag; currency unconfirmed |

All source 01/02 rows also carry inferred-header and unconfirmed-currency flags. `data/clean/quality_flags.csv` is a review queue, not a file of rows to delete. Machine counts and raw-file hashes: `docs/quality_report.json`.
