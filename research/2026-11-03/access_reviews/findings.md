# Consumer evidence and access-tool findings

Collected 3 November 2026. This workstream used public pages and public pagination only. No Apify, paid actor, account login, cookie import or contact with people occurred.

## Actual collection

| Corpus | Records retained | Collection scope | Main boundary |
|---|---:|---|---|
| Lazada Indonesia | 681 distinct review IDs | 26 purposively discovered toothpaste listings; server-rendered review-page payloads | SEO-selected subset, not full histories; repeated feature phrases; reviewer age/payer unknown |
| Reddit | 75 comment records | One r/indonesia toothpaste discussion, posted 5 June 2023; public reader lines | One self-selected discussion; relative comment dates; includes jokes and unverified medical statements |
| ORESA | 298 distinct review IDs | All 298 displayed Ultra White campaign review records across three public JSON pages | Explicit cashback/review-task campaign; incentivized claims, not independent organic sentiment |
| TryandReview | 100 distinct review IDs | First ten pagination pages each for Pepsodent Basic and Complete8 (five reviews/page) | 51 explicitly mark free product; remaining49 have no established incentive status; not representative |
| **Total retained records** | **1,154** | Four source-specific corpora | Records are not unique people, confirmed switchers, or a national sample |

The 681 Lazada records comprise459 Pepsodent,172 Sensodyne,50 Colgate records. 601 fall within2022-01-01 through2026-06-30 inclusive; older and newer records remain labeled separately. Ratings:653 five-star,24 four-star,4 three-star, none one/two-star in the selected SEO material. This severe skew makes a pooled satisfaction estimate inappropriate. A bread-improver page returned by the ambiguous term “enzim” contributed50 records initially and was explicitly quarantined/excluded; its raw capture and log remain for audit.

`derived/corpus_counts.json` gives exploratory literal-term matches. They are retrieval aids, not validated psychological constructs or prevalence estimates. `derived/manually_read_evidence.json` contains22 read-and-annotated selected records with mechanisms and boundaries. It is deliberately much smaller than the full collected corpus.

## What the evidence contributes

### A satisfied Premium user can still encounter price and availability friction

Lazada record `LZD-1574262094522499`, dated11 April2025, reports that the buyer buys a bundle because the variant suits them and saves money, while complaining it is often out of stock. This is unusually useful evidence because it combines perceived benefit, economy and availability in one account. It challenges an information-only story: someone may already value the product and still face replenishment friction. It does not measure how often stockouts occur or establish that this buyer moved to Basic.

Source: https://www.lazada.co.id/product-reviews/?item_id=4777322499 ; exact raw locator is retained with the record. Listing currently names an Active Remin105g×2 offer; historical review-to-formula/pack continuity is not established.

### “Until better” is an expectation to investigate, not observed discontinuation

`LZD-1200640450822499`,1 July2023, reports lower sensitivity and intent to keep trying until the problem resolves. This supports asking about episodic need and expectations. It does not say the buyer later stopped, returned to Basic, or was medically advised to stop. Do not relabel this a confirmed post-relief churn event.

### The product reviewer may be relaying another household member’s experience

`LZD-2032630484394818`,22 November2025, relays a husband’s experience of reduced nausea, lower foam, freshness and sensitivity relief. It makes buyer/user separation and sensory comfort concrete, without proving who paid. It is a spouse report; it is not clinical evidence.

Source: https://www.lazada.co.id/product-reviews/?item_id=8721394818 .

### Promotion and good fit can coexist

`LZD-1456695189922499` describes established use, perceived sensitivity benefit and a discounted purchase. `LZD-2004082758848866` describes repeated Complete8 use, comfortable mouthfeel and a low marketplace price. These are counterexamples to treating every discounted purchase as bargain-only trial. They still cannot establish regular-price repeat or incremental profit.

### Replenishment can change the selected variant even without rejection

Sensodyne record `LZD-1551582562350987` says the usual Deep Clean ran out and the buyer is trying Whitening. An observed SKU change can arise from a replacement occasion and available alternative; it does not necessarily mean the incumbent benefit disappointed.

### There is also an uptrading-direction account

`LZD-1324625217926021`,3 January2024, describes a first Complete8 purchase after previously using red Pepsodent. It is a useful rival to assuming every observed journey moves down. No subsequent experience or repeat is supplied.

Source for both Complete8 records: https://www.lazada.co.id/product-reviews/?item_id=5429126021 .

### Household purchase authority is explicit in public conversation

In the2023 r/indonesia discussion, one participant describes buying Closeup themselves while parents choose ordinary/herbal Pepsodent. Another says their mother controls bulk household purchases and discourages separate buying. A third describes forgetting to replace a preferred sensitive product and using the supply their mother prepared. These are real public narratives, not fictional portraits, but age and parent funding were not verified.

### Clean/fresh sensation is heterogeneous

The same thread contains strong-mint seekers and people preferring subtle Enzim sensation/less foam. One participant prioritizes mint despite not identifying sensitivity as the reason for choosing a sensitivity brand. Another describes a specialist-channel trip as effort. A single “stronger mint = better product” proposition would miss this heterogeneity. Consumers’ irritation and symptom claims remain unverified clinical statements.

### Pack economics can work in both directions

The thread’s Antiplaque account describes an initially painful price but unexpectedly long perceived duration from using little. The Basic marketplace corpus includes an explicit buyer appreciation of two225g tubes at low price. These mechanisms concern different comparisons: ticket price, grams, usage intensity and perceived duration. They should not be compressed into a single affordability score.

Reddit source: https://www.reddit.com/r/indonesia/comments/1414a8a ; source-line bounds and original text remain in `clean/reddit_comments.json`.

## Why the large review counts need caution

1. Many Lazada reviews contain comma-separated product-feature phrases, sometimes alongside natural prose. Their provenance may be platform suggestions, seller language, machine translation or reviewer copy. We did not establish which. They are not automatically spontaneous consumer vocabulary.
2. Positive ratings can accompany “not tried yet,” delivery comments, hopes for a result, or reserve-stock purchases. At least20 Lazada records match explicit pre-use/uncertain-result wording under the documented lexical rule; this is a flag count, not an exhaustive content audit.
3.249 Lazada records match service/delivery language; overlap with actual product experience is allowed. Do not discard them silently or treat all as product satisfaction.
4. ORESA’s explicit sampling/compliance campaign and TryandReview’s free-product labels make them separate evidence strata. Pooling them with unsolicited conversation would blur incentives.
5. Current profile age appears in TryandReview and is preserved as self-reported, not verified age at purchase. Two source profiles display0; that literal value is retained as unverified source metadata, not a real age claim.
6. All corpora lack verified Premium-to-Basic transitions among confirmed18–30-year-olds. New records expand the mechanism evidence; they do not validate the case’s population mechanism.

## Tool audit: Agent-Reach and alternatives

The official `Panniantong/Agent-Reach` repository was cloned to scratch and inspected at commit `7a38047acf26a729cbb27851e3cb81639da86b29`, version1.6.1. Inspected the dependency list, public web channel, Reddit channel, HTTP runner, CLI and configuration behavior. The broad setup installer was not run. The public Jina web backend was imported and called directly with bounded timeouts, without installing dependencies or touching sessions.

Two actual tests are in `raw/agent_reach_tests.json`: Reddit returned a network-block page as a nominal item (marked unusable in our audit); Lazada returned readable content. This illustrates why a nonempty successful wrapper response is not proof of usable data. The repository’s own public-web channel says agents with working built-in search/fetch should use those first. The public Reddit browser backend requires separate OpenCLI/browser setup; no cookie/session route was attempted.

The best actual route here was direct standard-library HTTP to public Lazada SSR, public ORESA pagination, and public TryandReview form pagination. Built-in web reading supplied the Reddit thread where anonymous direct JSON timed out. No need to buy an actor merely because one exists.

Direct Watsons review endpoints were probed at two code forms and returned empty `reviews` arrays. That is an endpoint result, not proof the products have no reviews. FemaleDaily homepage was accessible but product discovery did not identify a useful toothpaste corpus. Blibli page reader returned403 although search snippets exposed comments; snippets were not included in the quantitative corpus. Initial Mandjur probe timed out; no Mandjur corpus is claimed.

## Remaining high-value gaps

- Negative experiences and disappointed users are underrepresented in the SEO-selected marketplace sample. Deliberate low-rating sampling would be diagnostic, with separate denominators.
- Exact paid prices at first and subsequent purchases, repeated purchases across channels, and comparison against regular prices remain unavailable.
- Source-site completeness and consumer uniqueness are not established across corpora.
- Historical variant identity and formula/package changes need manual SKU matching before attributing older reviews to current offers.
- Primary purchase reconstruction remains the strongest next step for the payer/chooser/switching questions. Public accounts should guide those interviews rather than substitute for them.

## Reproduction and files

Run scripts only in their own workstream directory. `collect_lazada.py` uses retained discovery JSON and cached public responses; `collect_oresa.py` retrieves the public campaign endpoint; `collect_tryandreview.py` retrieves20 selected public pages; `extract_reddit_capture.py` rebuilds comments from retained reader-line captures; `annotate_reviews.py` creates exploratory flags, counts and selected manual annotations. A refresh is a new snapshot, not an identical reproduction guarantee.

All retained source records have original URLs and raw-file locators. Logs record result counts and HTTP failures. Neither an actor advertisement nor a search snippet is counted as a collected consumer record. Raw ORESA responses include unnecessary public member names/avatar URLs; use the cleaned tables for analysis and omit those fields from any public release. The project’s confidential source materials remain subject to its existing handling rules.
