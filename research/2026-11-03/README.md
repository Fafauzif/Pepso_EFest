# Pepsodent deep research release —3 November2026

Start with **REPORT_FULL.md**, the single-file teaching report plus specialist annexes. `PEPSODENT_DEEP_RESEARCH.md` is the shorter main narrative. The user-approved enlarged plan is `plan/PLAN_v2.md`; historical intake questions in its original sections are superseded by accepted scope and scale extensions.

## Actual scale

-26,125,466originalAmazonreviewrows screened, plus857,856productmetadatarows. Only matched source rows retained; the whole source dump is not included.
-298,846canonical written records/fingerprints in the integrated store:286,706international title-matched candidates and12,140source-specific marketplace/campaign/forum records. They are not unique people.
-The international adult/general-toothpaste-title subset is196,872written candidates. Other retained scopes—children,accessories,alternatives,pets,unresolved—remain explicit and must be excluded for an adult toothpaste comparison. ManualQA found limitations in title-based screening.
-Source-targeted corpus:7419Watsonswritten reviews,681Lazada,2228ORESA,1423TryandReview,389Redditcomments. AdditionalXtable has5brandposts+1consumerstory, outside the integratedreview/commentcount.
-Watsonsalso retained2772ratings-only/blank records;198blankAmazoncandidates are excluded from writtenstore. Repeatedidentityobservations and templatedtext do not identify independent people.
-No verified18–30PepsodentPremium-to-Basicswitchers. No primaryinterviews or shelfchecks. NoApifyactor executions or paidservice spending.

The original phase1datasets remain preserved. ExpandedTARreplaces the earlier100records in the integratedstore; archiveRedditreplaces overlapping75readerexcerpts. Do not add all versions together.

## Files

-`REPORT_FULL.md`: main teaching/diagnosis plus annexes and methods.
-`PEPSODENT_DEEP_RESEARCH.md`: main narrative, question answers, conditional directions.
-`synthesis/SCALE_SYNTHESIS.md`: what expanded evidence changes.
-`synthesis/DATA_INVENTORY.json`, `VALIDATION.md`: phase1structuralchecks.
-`scale_pipeline/clean/collection_stats.json`, `independent_qa.json`: finalintegratedcounts/validation.
-`scale_pipeline/clean/export/records.jsonl.gz`, `records.csv.gz`: portablecanonicalwrittenrecords withscope/incentive/provenance.
-`scale_pipeline/clean/export/observations.jsonl.gz`: sourceoccurrences/payloadvariationprovenance, not additionalindependentconsumers.
-`scale_pipeline/clean/export/excluded_nontext_rows.jsonl.gz`: blank/nontext exclusionledger.
-`scale_amazon/`: streamingsourcehashlogs, matchedrawrecords, normalization,classification,analysis,independentQA.
-`scale_reviews/`: complete selectedTryandReviewhistories withcorrectedUTF8/fractionalratings.
-`scale_lazada/`: despiteitsname, successfulfullhistorycorpusisWatsons; failedLazadapaginationdocumented.
-`scale_discovery/`: additionalORESAcampaigns, exactcampaignwindows, rejecteddatasetregister.
-`scale_reddit/`: publicArcticShiftarchivecomments, threadcontext, IDlocators andcuratedexamples.
-`scale_tools/`: clientcapabilitymatrix, knownURLXsample, runtimefailures, and user-suppliedreverse-api-engineer audit.
-`retail/`, `brand_campaigns/`, `history_publicdata/`, `literature/`, `access_reviews/`: original specialistdata/methods/findings.
-`apify_handoff/`:12schema-validated optionaluser-runinputs, actualmetadataprices/schemas, instructions; no executionneeded forcompletedcorework.

## Interpretation and package boundaries

This is a private team research asset. Retain originalsourceattribution/rights; noopenlicense is asserted overthirdpartycontent. Sourcepage/campaignincentives, sourcecountry, historicalperiod andreadingdepth are explicit. A globallysourced historicalcorpus mustnot be used to calculate Indonesianyouthprevalence, clinicaleffectiveness, causalswitching orforecastuplift.

The deliverable excludes the rebuildableintermediateSQLite database and unrelatedelectronicsdatasetCSVfiles. It retains hashes/retrievaland rejectionlogs for the discardedlargedatasets and canonicalcompressedexports for the integratedresearch. It also excludesGit internals, privatecredentials, installedtool environments andPythoncaches. The originalprojecthandoff/master andrawkeywordcaptures remain unchanged in the repositorysnapshot.

## Reproduce and validate

From therepositoryroot:

```bash
python3 scripts/verify_package.py
python3 research/2026-11-03/scripts/analyze_existing.py
python3 research/2026-11-03/synthesis/validate_inventory.py
python3 -m unittest discover -s research/2026-11-03/scale_pipeline/tests -v
```

Schema validation uses the isolated pinned `jsonschema` dependency described in `apify_handoff/requirements-validation.txt`; schema-valid inputs do not prove runtimeextraction. Collection scripts can refreshpublicsources but are not required to inspectthissnapshot. Live refreshes are newdated observations; do not overwrite the historicalrelease unintentionally.

The full26million-review stream reads roughly14GB acrossmetadata/reviews; the sourcehashlogs verifytheactualcompletedreads. Do not rerunthat scan merely toinspectthe retainedsubset. The SQLite store is rebuilt fromcanonicalinputs as documented in `scale_pipeline/README.md`; it is not bundled because portablegzipCSV/JSONL already retain thedata/provenance and keep individualfiles suitableforrepoupload.

Legacy keywordsourcehashes reflectoriginalCRLFbytes; Gittextnormalization changed them toLF beforethisrun. The top-level verifier accepts only exacthash-matchingCRLFreconstruction and stateswhen that exceptionoccurs. Originalsourcefiles andoriginalrecordedhashes remainunchanged. Currentreleasechecksums describeactualpackagedbytes.

No remotepush orcompetition submissionhasoccurred. Three strategydirections remainconditionaland unselected. Nextprimaryresearch should reconstructactualpurchasesand householdroles afterthis secondaryevidence review.
