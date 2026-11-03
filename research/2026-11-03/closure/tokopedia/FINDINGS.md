# What the Tokopedia and Shopee runs add to the diagnosis

**Completed analysis, 3 November 2026.** These are user-run Apify exports received in this session. The analysis is secondary evidence, not team interviews. No reviewer is verified as an Indonesian 18–30-year-old Pepsodent Premium-to-Basic switcher. Strategy directions remain conditional.

## 1. The useful result is a set of sharper mechanisms and counterexamples

The successful marketplace runs add specific accounts of **continued premium use, sensory fit, household use, small-pack interpretation, promotion interest and seller friction**. They also expose why raw review totals and star ratings can be poor substitutes for the business question. This is enough to improve an interview guide, but not to establish the cause of the seven-point premium-mix change in the case.

The clearest counterexample to a preferred story comes from a Sensodyne reviewer: “Sudah merasakan manfaatnya jadi tidak mau ganti pasta gigi.” Experiencing benefit can make continuation more attractive, rather than remove the reason to continue. A different reviewer explicitly reports longtime sensitivity-paste use and repeat orders. The interview should therefore investigate **how people interpret improvement**, including continuing protection, temporary treatment, sensory comfort, trust, and indifference. It should not assume people stop when symptoms improve.

A Pepsodent Ultra White reviewer writes “beli lagi krn cocok.” That is relevant to the replenishment mechanism: compatibility or felt fit can support another purchase. However, the review does not tell us whether that second purchase was full price, independently paid, shared with family, or made by someone aged 18–30. The appropriate claim is that a public repeat-use account exists, not that Pepsodent has solved retention.

## 2. Exactly what the files contain

| Unit | Reconciled count | Interpretation |
|---|---:|---|
| Tokopedia exported rows, two files | 335 | Mixed reviews, product observations and notices |
| Review occurrences | 309 | 43 pilot plus 266 main-file records |
| Distinct review IDs | 266 | All 43 pilot IDs recur in the main file |
| Additional distinct IDs beyond pilot | 223 | Not 266 plus 43 |
| Nonempty review text | 263 | Includes emoji, generic praise and fulfilment-only text |
| Product-card observations | 24 | Six pilot and 18 main snapshots |
| Distinct product IDs in cards | 18 | Six keyword searches, three matches each in main run |
| Products with at least one review | 16 | Absence in this export does not prove no marketplace reviews exist |
| Billing notices | 2 | Metadata excluded from review data |
| Five-star reviews | 256 of 266 | Descriptive of this purposive export only |
| Other ratings | 7 four-star, 1 three-star, 1 two-star, 1 one-star | Read the reasons before calling them product dissatisfaction |
| Broad written-toothpaste candidate subset | 256 | Excludes blank text, spray, gimmick-title candidates and one text mismatch; still includes low-information text |
| Provisional case-period candidates | 147 | Written-toothpaste candidates whose unverified reviewDate falls in Jan 2022–Jun 2026 |
| Explicit close-reading annotations | 85 | 40 seeded random calibration records plus 45 purposive examples |

The main file contains **260 toothpaste-title candidates, five reviews on a listing labelled Gimmick Pepsodent, and one whitening-spray review**. Reviews on the gimmick listing include explicit free-product/bonus language; the title alone does not verify free receipt or review incentives. Its card price is Rp500,000. It is not a defensible normal retail price. One Basic-linked review says the product prevents body odour: retain the original text and mismatch flag; exclude it from ordinary toothpaste experience analysis.

There are 11 exact-normalized repeated-text groups containing 43 records. These are mostly expressions such as “Ok” or “Bagus.” They should not be merged into a single review or called bots. Nor should their repetition be mistaken for many independent reasons to buy.

Thirty-eight of the 43 repeated IDs have changed payloads across exports. The changed fields are `reviewTime` on 35 IDs and signed `reviewImages` URLs on 11 IDs; these overlap. Review wording and ratings do not change in those duplicates. The occurrence ledger preserves both versions.

## 3. Reading the stars correctly

The marketplace export is 96.2% five-star at the record level. It would be misleading to report that 96.2% of premium toothpaste users are satisfied. The search is purposive; the sample is small and seller/ranking-selected; many reviewers describe arrival rather than use; and neither exposure nor purchaser eligibility is established.

Examples in the reviewed Pepsodent Ultra White records include:

- `tokopedia:2127271766`: four stars, “Belum di coba ksh bingang 4 dulu.”
- `tokopedia:2121981403`: five stars, “Blm tau hasilnya kak.”
- `tokopedia:1996090240`: five stars, “Rasa blm dipakai … perfoma mantap seperti Iklannya.”
- `tokopedia:1884985356`: five stars, “Belum dicoba.”

These are not proof that the reviewers never used the product later. They show that **the review event may precede meaningful experience**. A five-star observation can represent provisional approval, transaction completion, an expectation, or a response to the seller's fulfilment.

The low-rating counterexamples are equally important. `2346136191` gives two stars for slow shipping; `2337020302` gives three stars for untidy packing; `845969659` gives one star and alleges the parcel never arrived. The allegations are unverified. None establishes failed sensitivity relief or an unsatisfactory toothpaste formulation. A questionnaire that asks only “were you satisfied?” can blend product, seller, delivery, and price into one noisy answer.

## 4. Mechanism evidence to carry into primary research

All dates in the following table are the **source reviewDate field, unverified against the marketplace**. The exact original text and JSON locator appear in [qualitative_evidence.md](qualitative_evidence.md); ID links can be searched in the clean table. This table is purposive and cannot estimate the share of consumers with a mechanism.

| Record ID | Source date | What it contributes | What it does not establish |
|---|---|---|---|
| 1932700850, Pepsodent Ultra White | 2026-02-18 | Explicit “beli lagi krn cocok”; another purchase tied to fit | Full-price retention, age, payer, or effect relative to alternatives |
| 2177591268, Sensodyne triple pack | 2026-06-30 | Longtime sensitivity-paste use plus “sdh repeat order” | A measured retention rate or prior Pepsodent switching |
| 2145103290, Sensodyne triple pack | 2026-06-10 | Benefit experienced and desire not to change | A completed future purchase or clinical efficacy |
| 2106524516, Sensodyne triple pack | 2026-05-19 | Years of use, dentist recommendation and promo price coexist | That promotion caused loyalty or recommendation caused use |
| 2339058026, Sensodyne triple pack | 2026-10-09 | “Pasta gigi fave keluarga”; family use with sensitive-gum reference | Payer/chooser identity, household composition; also post-case |
| 2310809324, Enzim 42 g | 2026-09-19 | Always uses Enzim; alternatives feel unpleasant; requests more promos | Proof of causally induced mouth ulcers, price dependence; post-case |
| 1469837237, Enzim six-pack | 2024-05-14 | Longtime user discovers TikTok promotion and values low-foam lip comfort | Incremental brand acquisition from TikTok or verified platform-independent purchase history |
| 1079042828, Enzim six-pack | 2024-08-14 | Low foam preferred because reviewer associates foam with painful lips | Allergy diagnosis or formulation causation |
| 2137866402, Enzim 42 g | 2026-06-07 | Non-spicy taste and family liking | Who chose or paid, or clinical effect |
| 2191122942, Enzim 42 g listing | 2026-07-08 | Expected a larger size; received two small packs | Smaller packs always reduce value or cause downgrading; post-case |
| 2146597418, Enzim 42 g | 2026-06-11 | Pack suitable for travelling | Same preference for a shared household tube |
| 2105728218, Enzim 42 g | 2026-05-19 | Minimum checkout quantity of three makes trying other flavours harder | Brand-level choice overload or general retailer policy |
| 2085363055, Enzim 42 g | 2026-05-07 | Longtime user shops online after seeing a lower price than offline | Brand switching, exact savings, causal elasticity |
| 2382666161, mixed-size Enzim listing | 2026-11-03 | Multiple purchases because only this paste fits | Age, premium tier, regular-price repeat; post-case |
| 2356551626, mixed-size Enzim listing | 2026-10-18 | “belum nyoba, fomo aja sih beli enzim haha” | Continued use or successful experience; post-case |

### Continued use can rest on comfort as well as a specialist promise

“Clean” is not a single sensory standard in this export. Pepsodent Ultra White is described as sweet mint and fresh; one reviewer says it avoids their usual gagging sensation. Enzim users praise mildness, lack of foam, and comfort on the lips. Low foam can be a positive fit rather than a sign of weak cleaning. The data do not reveal the true clinical source of that sensation and do not establish ingredient allergies.

This makes the interview task more concrete. Ask what felt different, during brushing and afterward; whether it was pleasant; what the person expected; and whether that difference mattered at the next purchase. Avoid prompting “it feels cleaner, right?” Ask for the respondent's own words before offering categories.

### Discounts can coexist with stable brand preference

Requests for more discounts and enthusiasm about a promotion do not imply failure to repeat. The same Enzim account describes continued use and discomfort with alternatives while requesting promotions. A Sensodyne account combines years of use, a dentist recommendation and a good promotional price. Another Enzim user compares online and offline prices while keeping the same brand.

Three mechanisms remain distinct: a discount recruits someone who otherwise would not trial; a loyal buyer stocks up when the deal appears; and an existing buyer changes channel without changing brand. Reviews seldom distinguish these cleanly. The primary timeline should record prior product, actual paid prices, promotion exposure, purchase timing, number of packs, and subsequent replacement.

### Small packs can mean inconvenience, fit, portability or low commitment

One Enzim reviewer expected a larger pack; another values a small pack for travel; another describes it positively as “kecil imut.” The 190 g Basic reviewer says the size is standard for approximately a month of use. None provides a reliable universal rate because users per tube and dose are unknown.

The useful hypotheses are situation-specific. Does someone want a personal specialist tube while the family uses Basic? Is a small tube a lower-risk trial? Does repeated purchase become inconvenient? Are bundle quantity and title confusing? Does the unit price or the cash required at checkout dominate? Test these separately.

### Seller rules can create choice friction

The minimum-three-unit complaint is unusually concrete: the buyer wanted flexibility to select other flavours. That is a seller basket restriction, not necessarily psychological overload from too many variants. A solution directed at messages or product education would not automatically fix it. Primary research should distinguish “I could not select what I wanted,” “I did not understand the variants,” and “I did not want to spend time deciding.”

## 5. Price and pack observations are contexts, not actual consumer spending

The product cards were collected on 3 November 2026 and can describe offered title/price contexts. They are **after the case horizon**. They do not reconstruct historical price, personalized voucher redemption, delivery charges, actual paid prices, stock, or willingness to pay. Variant prices and title-described pack counts require confirmation against the selected SKU.

Conditional title-based calculations illustrate why both ticket price and unit price are useful:

| Product-card title context | Listed price | Title-implied mass used for illustration | Conditional Rp per 100 g |
|---|---:|---:|---:|
| Basic anticavity 190 g twin pack | 33,100 | 380 g | 8,711 |
| Sensitive Mineral Expert 160 g twin pack | 91,168 | 320 g | 28,490 |
| Ultra White Ultimate Bright 90 g | 59,900 | 90 g | 66,556 |
| Sensodyne Repair & Protect 3×100 g | 105,264 | 300 g | 35,088 |
| Enzim Fresh Mint 63 g, six pieces | 90,300 | 378 g | 23,889 |

These are unadjusted **illustrations conditional on titles representing the actual sold pack**; they are not comparable paid baskets, official case-tier prices, or a recommendation to buy. A card whose title spans 42/63/124/160 g cannot be normalized from one displayed price without identifying the selected variant. A free-gift live-stream bundle has a different basket proposition from a plain tube. The Gimmick Pepsodent Rp500,000 entry and whitening sprays are excluded from this comparison.

The business implication is a research question: does the problem emerge at the initial ticket price, the next refill's cash requirement, comparison with a family bundle, or unit economics across time? A controlled scenario can vary those assumptions, but it cannot substitute for observed purchase history.

## 6. Dates and histories need caution before case-period claims

Both exported date fields exist on 198 canonical records; they disagree on the calendar day for **186 of those 198**. On 68 other records `reviewTime` is null. A missing field is not counted as a conflict. In the pilot the disagreement was 40 of 43; it is wrong to carry that ratio forward as if it were the whole dataset.

The source actor appears to estimate `reviewTime` from relative language such as “1 bulan lalu.” For one pilot record, `reviewDate` says 11 June while the derived timestamp falls on 6 July, changing the apparent side of the case cutoff. There is no independent adjudication of either field in this handoff. Both are preserved; provisional slices use `reviewDate` and say so.

Using that field, all canonical reviews split into 153 case-period, 101 post-case/current-context and 12 pre-2022 records. After broad written-toothpaste eligibility exclusions, 147 remain in the provisional case-period candidate subset. This is still not a verified target cohort or random sample. Later material can develop an interview mechanism but cannot demonstrate that the same condition caused the case's H1 2026 decline.

## 7. What failed and why that does not become evidence

The targeted Shopee run delivered two error records and **zero reviews**. Its messages say the actor scanned 2,130 and 3,193 shop reviews without finding matching eligible product reviews in reach. Those 5,323 rows were not exported or retained and are not part of our collected corpus. The result does not establish that the products have no reviews.

The second Shopee export contains **100 UGREEN electronics reviews from Singapore**, including 23 nonempty comments. It demonstrates an input/default-target mistake, not Indonesian oral-care demand. It is retained with an exclusion reason, source bytes and a provenance trail; none is merged into the toothpaste corpus. Error messages say no delivered-review charges for the failed pilot, but startup/platform usage is not independently audited here.

Tokopedia notices report product/review event charges of $0.0735 and $0.426, totalling **$0.4995**. These notice amounts are distinct from the user's reported $3.79 account usage, which covers a wider activity history and potentially other charges. No account balance or payment ledger was independently accessed.

## 8. What to do next

Stop broad scraping. The main new question is not whether another positive review exists. It is which explanation best fits the **last replacement decision** of a confirmed target user.

Interview contrasts should include retained Pepsodent Premium users, Pepsodent Premium-to-Basic switchers, and Basic or competitor choices; cross these with independent versus dependent purchasing and shared versus personal tubes. Ask the same neutral purchase-history questions so the preferred household or price story can fail.

Priority probes from these files:

1. “You said the product fit / helped. What exactly changed, and what did you buy the next time?”
2. “Who chose and who paid for that last tube? Did everyone use it?”
3. “Was the last order a repeat, a first trial, a stock-up or a free extra?”
4. “What was the price actually paid including pack quantity and vouchers? What did you compare it with?”
5. “When it ran out, was the same variant available in your usual shop or channel?”
6. “Did symptoms improving mean you were finished, or that you wanted to keep using it?”
7. “What was unpleasant or comfortable about brushing, in your own words?”
8. “Was the difficulty choosing a variant, selecting it in the basket, paying for the quantity, or finding stock?”

The point is to obtain discriminating evidence. The public material already supplies reasons why discount interest, habit, sensory comfort, shared use and successful specialist benefit may coexist. A diagnosis that makes only one of those visible would discard useful contradictions.

## 9. Files and reproducibility

Start with [CODEBOOK.md](CODEBOOK.md), [stats.json](stats.json), [qualitative_evidence.md](qualitative_evidence.md), and [QA.md](QA.md). `clean_analyze.py` rebuilds the compressed tables from immutable exported JSON/JSON.gz files and the assistant-authored annotation TSV. `validate.py` checks count reconciliation, schema-relevant distinctions, exact source locators, original review text, and annotation links. No network, paid services or new source collection is needed to reproduce these outputs.
