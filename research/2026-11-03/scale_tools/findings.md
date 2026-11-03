# Scale-tool assessment and bounded public X collection

Checked3November2026. The goal was to identify useful collection capabilities without accounts, imported sessions, paid APIs, fabricated credentials or bypassing access controls. Tool inspection was followed by bounded public-route tests and two actual Python-client tests. No Apify was used.

## Result that changes the available collection route

**Some known public X profiles and post URLs return useful server-rendered HTML without login.** This worked for the Sensodyne Indonesia profile linked by its brand material and for one discovered consumer post. It did not make logged-out keyword search available, and it does not establish complete profile history or a scalable historical search interface.

Six records were retained in `clean/x_public_sample.csv/json`:five Sensodyne-owned marketing posts from August2023 and one consumer purchase account dated20June2026. The consumer describes replacing an imported toothpaste with Pepsodent amid household spending changes. The original X page was retrieved and contained the relevant passage; an indexed mirror was only the discovery lead. The official oEmbed response succeeded but truncated the long post before the toothpaste section. It cannot independently verify that part of the account.

This purchase account is a useful example of category-spending trade-offs. It is **not** verified18–30, an identified Pepsodent Premium-to-Basic switch, a receipt-verified paid price, or a prevalence measure. Exact Pepsodent variant remains unknown. The five brand posts show marketing language, not independent consumer approval. No ages or demographic attributes were inferred.

The parser removed a duplicate rendering of the focal consumer post and excluded three replies not substantively about toothpaste. Normalized records preserve an excerpt, original word count, source URL, post ID, analyst summary, raw-page locator, and flags for the unverified attributes. Public Snowflake IDs were used to derive timestamps, with displayed dates checked; the derivation is explicitly labeled.

## Tested public routes

| Route | Actual result | Decision |
|---|---|---|
| `x.com/search?q=pepsodent` | HTTP200 after redirect to login onboarding;no posts in returned shell | No keyword-search corpus obtained. |
| Guessed historical `@TanyaPepsodent` profile | HTTP200 but unrelated current display and zero posts | Not an authenticated/verified brand account;do not use as brand evidence. |
| Alternate guessed `@PepsodentID` | HTTP404 | Does not identify the correct handle or prove no X activity. |
| Official syndication profile endpoint | HTTP429 | Rate limit;no records;no retry loop. |
| `nitter.net/search` | HTTP200 maintainer notice dated10October2026,not a timeline | Zero tweet records;status alone was misleading. |
| `xcancel.com/search` | HTTP451 and service-suspension notice | No collection;no attempt to evade suspension. |
| `x.com/gigingilu` | Public HTML with five post entries and Sensodyne identity | Five brand-owned records retained;not a full-history claim. |
| Official X oEmbed for discovered user post | HTTP200 JSON but longpost text truncated | Useful metadata/date corroboration;insufficient alone for toothpaste paragraph. |
| Original discovered user-post URL | HTTP200 HTML includes relevant longpost | One purchase-story record retained. |

The Nitter notice describes its own status and legal situation. It is not used to make sweeping legal claims about all scraping. The XCancel response is a service-specific observed suspension. No rotation through unlisted instances or session/fingerprint workarounds was attempted.

## Python-client capability matrix

Versions are the PyPI releases returned at inspection time. Repository-main source files were inspected and hashed separately; a current main branch is not assumed identical to a release wheel.

| Tool/version | Official source and intended role | Access/dependencies established by inspection | Execution status and conclusion |
|---|---|---|---|
| PRAW8.0.3 | [PRAW documentation](https://praw.readthedocs.io/en/stable/getting_started/authentication.html),[PyPI](https://pypi.org/project/praw/) | Reddit OAuth wrapper;read-only access still needs an appropriate registered application configuration. Credential requirements vary by grant/application type. | Docs/package metadata inspected;no account/app credentials available;not executed as a live authenticated client. It is not a credential-free archive. |
| asyncpraw8.0.3 | [Official authentication docs](https://asyncpraw.readthedocs.io/en/stable/getting_started/authentication.html),[PyPI](https://pypi.org/project/asyncpraw/) | Async Reddit API wrapper with analogous authorization boundaries;async concurrency does not expand permission or history coverage. | Inspected,not installed/executed;Reddit archive testing delegated separately. |
| twscrape0.20.1 | [Official repository](https://github.com/vladkens/twscrape),[login source](https://github.com/vladkens/twscrape/blob/main/twscrape/login.py) | Account/session-based X client;login code uses user account/session state. Optional curl backend is additional dependency,not permission. | Source and PyPI metadata inspected;not installed/run because no account/session was authorized or supplied. No cookies imported. |
| ntscraper0.4.0 | [Official repository](https://github.com/bocchilorenzo/ntscraper),[PyPI](https://pypi.org/project/ntscraper/) | Parses Nitter instances;depends on requests,BeautifulSoup,lxml,tqdm. Its README warns that instance access may fail. | Installed in isolated environment and executed for at most3results on explicitly selected nitter.net. Returned an empty-page message and `tweets:[]`,`threads:[]`. Exit0 did not mean successful collection. |
| snscrape0.7.0.20230622 | [Official repository](https://github.com/JustAnotherArchivist/snscrape),[PyPI](https://pypi.org/project/snscrape/) | Older Python client with requests/lxml/BeautifulSoup dependencies and Twitter source code. | Installed and executed with correct console entrypoint for at most3results. On Python3.12.14 it failed before network retrieval:legacy importer uses unavailable `find_module`. This is an observed local compatibility failure,not proof every fork or interpreter fails. |
| Crawl4AI0.9.5 | [Official repository](https://github.com/unclecode/crawl4ai),[PyPI](https://pypi.org/project/crawl4ai/) | General crawler/extractor;declares browser and broad processing/LLM dependencies. These do not grant X/Reddit authentication. | Source/dependency metadata inspected;not installed. Existing public HTTP/HTML parsing already reached the useful pages without its large stack. |
| Scrapling0.5 | [Official repository](https://github.com/D4Vinci/Scrapling),[PyPI](https://pypi.org/project/Scrapling/) | Core parsing dependencies are distinct from optional browser/fetcher capabilities. A parser cannot itself supply login access. | Source/dependency metadata inspected;not installed/executed. No stealth/browser-fingerprint capability was used. |

The snscrape test first used an incorrect `python -m snscrape` invocation, which does not exist. That invocation error was preserved separately and corrected to the installed console command. The resulting Python3.12 importer failure is the actual final test result. It should not be confused with the initial command mistake.

## What scales and what does not

1. **Known-URL public HTML can be efficient.** Build a source registry from genuine indexed posts and official profile links, then request only relevant URLs and deduplicate by post ID. Logged-out rendering may expose a small subset of posts or replies.
2. **Public search is the bottleneck here.** The tested X search route required login. Millions of topic-relevant X records cannot be promised from five profile posts or a handful of indexed URLs.
3. **Client wrappers do not change underlying entitlements.** A PRAW installation is not a Reddit app credential;a twscrape installation is not an X account;a Nitter parser is not a functioning Nitter service.
4. **Successful public-commerce APIs remain more productive for the project.** Use the large actual review expansions from the other collection workstreams instead of inflating counts with unrelated X replies.
5. **Archive-scale Reddit remains a separate route.** ArcticShift/PullPush and relevant subreddit extraction were assigned to the history/public-data agent to avoid duplicated traffic. This directory does not claim those agents' records as its own.

The bounded test found a useful additional source, but it did not establish a million-record free pipeline. No payment was made. No installed client's claimed maximum throughput was treated as observed throughput.

## Files and reproducibility

- `raw/tool_inspection_log.json`:17 documentation/metadata HTTP requests with response hashes and failures.
- `raw/public_route_tests.json`:eight bounded public/source requests,with manual HTTP200-content classification.
- `raw/target_public_post_log.json` and `raw/original_post_log.json`:known post/profile follow-ups.
- `raw/client_runtime_tests.json`:final actual client commands,outputs and errors;initial erroneous invocation retained separately.
- `raw/client_install.log` and `raw/test_environment_freeze.txt`:isolated test environment provenance.
- `clean/x_public_sample.csv/json`:six retained source-specific records.
- `clean/extraction_exclusions.json`:duplicate/irrelevant reply decisions.
- `clean/capability_matrix.json/csv`:machine-readable tested/inspected distinctions.
- `scripts/`:request,client-test and normalization code. No secrets are required or embedded.

The two packages were installed in a scratch-only isolated virtual environment,not globally or inside the repository. Reproduction requires creating an environment and installing the exact versions;the scripts record the original environment path as execution provenance rather than claiming that path is portable. Ordinary public HTTP requests and lxml parsing performed the successful data extraction. The raw downloaded pages include public website scripts and are not session-cookie exports.
