# Independent scale-collection QA

Reviewed3November2026. Scope:collection scripts,summary files,title classification,lexical analysis,source README and an independent30-record qualitative spot check. Canonical data were not changed.

## Counts reconcile

| Quantity | Independent check | Meaning |
|---|---:|---|
| Source review rows scanned | 494,121+25,631,345=**26,125,466** | Streaming inspection across two broad Amazon categories;not all retained as toothpaste or stored in full. |
| Candidate observations retained | 2,259+287,325=**289,584** | Reviews joined to title-matched product candidates,including accessories/children/pets/alternatives. |
| Derived canonical identity fingerprints | **286,904** | Independently recomputed across both classified files;not verified unique people or original Amazon review IDs. |
| Duplicate observations | **2,680** | Exact derived-fingerprint duplicates removed at the combined analysis layer. |
| General/adult-human toothpaste-title candidates | **197,002** | Product-title rule result;not verified adult reviewers/users or complete formulation eligibility. |
| Nonempty written reviews in that title stratum | **196,872** | Independently recomputed after deduplication and whitespace-empty exclusion. |

Independent combined scope counts match `analysis_summary.json`:adult-title197,002;adjacent35,954;accessories20,959;pet/nonhuman341;brand/type unresolved1,929;child/infant30,719. Ratings and years refer only to the196,872nonempty title-candidate records. Source-category classification counts before deduplication need not equal combined unique counts.

The identity key hashes user ID,parent ASIN,timestamp and review text. It is useful deterministic deduplication,not proof of unique consumers or independent purchase events. Product IDs use parent ASIN,so metadata title/variant grouping remains another limitation.

## Scope and provenance are appropriately limited

The collector joins reviews to product metadata selected by title terms(toothpaste/dentifrice/Sensodyne/Pepsodent),then retains source row numbers and original fields. It streams large remote category files rather than preserving the full11GB+category payload locally. Scan hashes describe bytes read during that run;they are not hashes of a locally stored complete broad-category archive.

The source README labels the dataset English-language and describes historical Amazon interactions endingSeptember2023. This is an **international/historical comparator**,not Indonesian youth evidence. Product metadata price fields are crawl-time US-dollar prices,not the price paid in each review. The source verified-purchase flag is retained as a source assertion,not independently authenticated.

The inspected README includes citation instructions for Hou etal.(2024),*Bridging Language and Items for Retrieval and Recommendation*,but does not display an explicit license declaration. Do not describe the dataset as openly licensed or infer unrestricted redistribution permission from download access. Preserve source attribution and check terms for any public release. This QA does not make a legal determination.

## Thirty-record spot check

`manualsample.json` records30unique IDs,source row locators,ratings,dates,title strata,short excerpts and qualitative notes. Fifteen came from nonadult/alternative/unresolved strata(three each),and fifteen from general/adult-title candidates stratified by rating and household/repeat/price cues. Selection was deterministic and purposive. Relevant text and titles were read;this is not full-corpus manual review,independent human coding,a representative sample,or an accuracy estimate.

### Obvious classification limitations found

- **Pet-rule false positives:** cartoon cat/panda-shaped tube squeezers trigger the pet rule before the accessory rule. They remain excluded from the adult-title stratum,but the negative subtype is wrong.(AMZ-QA-13,15)
- **Adult-use false positive:**Crest Pro-Health For Me lacks a child marker in its title,while the review explicitly describes a daughter/children.(AMZ-QA-23) Adult-title must never mean verified adult user.
- **Routine-paste eligibility uncertain:**a V34purple color-corrector serum/foam title uses“toothpaste.” The rule captures it,but that does not establish comparable everyday dentifrice use.(AMZ-QA-22)
- **Conservative title false negative:**short Sensodyne Rapid Relief title lacks“toothpaste,”yet one review identifies it as toothpaste. Unresolved status correctly preserves uncertainty rather than silently discarding evidence.(AMZ-QA-08)
- **Bundle confounding:**some toothpaste titles include a toothbrush,and praise can concern the brush as well as the paste.(AMZ-QA-19,24)

These examples demonstrate limitations;their frequency in this purposive sample must not be reported as corpus error rates. No canonical classifications were edited.

## Lexical counts are retrieval aids

The code correctly labels its outputs as literal cues,not validated themes or national prevalence. Preserve that distinction. The examples show why:

- A“family”cue can mean relatives noticing appearance,rather than sharing the tube or paying.(AMZ-QA-22)
- A mother mention can be a recommendation,not use or payment.(AMZ-QA-24)
-“Buy again”appears in both favorable intention and explicit refusal;regex counts do not encode polarity or actual repeat.(AMZ-QA-25,26)
- A high rating can coexist with disliked taste.(AMZ-QA-19)
- Prefix regexes can admit lexical near-matches:the price/value pattern can capture“Costco”;pack language can describe packaging/delivery rather than pack economics. These are potential pattern limitations,not measured error counts.

Do not interpret the66,033sensory-cue matches as66,033people prioritizing sensory experience,or the3,347repeat-cue matches as observed retained customers. Counts overlap and reflect English wording and corpus construction.

## What the larger corpus changes for teaching

It supplies concrete external mechanism examples:variant substitution under availability/price friction followed by sensory disappointment;product discontinuation prompting search;past repeated ordering;small-tube complaints;parent-child sensory acceptance;and positive overall evaluation despite unpleasant taste. These are useful prompts for discriminating primary questions.

It **does not materially increase certainty about the cause or prevalence of Pepsodent Indonesia’s2022–H12026downtrading**. The target population,time,products,prices and channel context remain unmatched. The correct lesson is that multiple plausible replenishment mechanisms exist and sometimes interact—not that a large historical comparator validates a preferred diagnosis.

## Release wording

Use:“We streamed26.1million broad-category source review rows,retained289,584candidate observations,and deduplicated them to286,904derived identities;196,872nonempty records fall within a rule-based general/adult-toothpaste-title candidate stratum.”

Avoid:“We collected26million toothpaste reviews,”“196,872adult customers,”“millions of Indonesian switchers,”or“the entire corpus was manually reviewed.”
