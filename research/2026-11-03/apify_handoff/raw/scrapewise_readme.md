# Shopee Reviews Scraper: ratings, comments and seller replies by shop or product

Scrape **Shopee reviews** of any **shop** or **product** in **Singapore, Brazil, Indonesia, Malaysia, Thailand, the
Philippines, Vietnam and Taiwan** into one table: stars, the buyer's comment, product and variation bought, the three
detailed scores (product quality, seller service, delivery), the seller's reply, how many photos and videos the buyer
attached, likes and date. Filter by stars, keep only reviews with a comment or with photos, and schedule it with
**Only reviews newer than** to pay only for new reviews.

No Shopee account, no cookies, no API key. Works with Shopee's 2026 site, where product reviews are hidden from
visitors who are not logged in.

## At a glance

- **Price per 1,000 reviews, Free plan:** US$ 3.00 (US$ 2.55 on Gold and above)
- **Fee per run:** US$ 0.005
- **8 countries:** SG, BR, ID, MY, TH, PH, VN, TW
- **Inputs:** shop links, shop ids, shop usernames, product links (`/product/<shop>/<item>` or `...-i.<shop>.<item>`)
- **Depth:** up to 5,000 reviews per shop
- **Filters:** min and max stars, only with a comment, only with photos or videos, newer than a date or period
- **Shop summary (free):** shop rating, total reviews split into good / normal / bad, followers, products, response rate
- **Speed:** about 1,000 reviews in 5 to 10 seconds
- **Error rows** (invalid link, shop not found, product without reviews in reach): free, with an `errorCode`

## One real row

From a test on 2026-10-20, shop `https://shopee.sg/shop/64922680` (Ugreen Official Store, Singapore):

```json
{
  "type": "review",
  "reviewId": "114695358760",
  "country": "SG",
  "shopId": "64922680",
  "shopName": "Ugreen Official Store",
  "itemId": "1427996834",
  "productName": "UGREEN Waterproof Phone Case for Moblie Phone for iPhone 12 13 14 15 Pro Max , for moblie phones up to 7.9 inches",
  "variation": "【7.2 inches】Crystal Upgraded",
  "productUrl": "https://shopee.sg/product/64922680/1427996834",
  "rating": 5,
  "comment": "Value For Money:looks nice\nProduct Quality:quality is nice\n\nBought this during discount time. Quality looks really nice",
  "ratingProductQuality": 5,
  "ratingSellerService": 5,
  "ratingDeliveryService": 5,
  "imageCount": 1,
  "videoCount": 0,
  "tags": ["Value For Money", "Product Quality", "Best Feature(s)"],
  "likeCount": 0,
  "sellerReply": "Thank you for your love and recognition of UGREEN! If you meet any issue with our product, please feel free to contact us.🥰",
  "sellerReplyAt": "2026-10-20T11:24:28Z",
  "isOverseasSeller": false,
  "originRegion": "SG",
  "createdAt": "2026-10-20T11:11:29Z",
  "scrapedAt": "2026-10-20T11:27:35Z",
  "sourceInput": "64922680"
}
```

## What you can do with it

- **Product research before you source:** read the 1 and 2 star reviews of the best sellers in your niche and find
  what buyers complain about (size, battery, packaging, fake items) before you pick a supplier.
- **Competitor monitoring:** schedule a competitor's shop weekly with `newerThan: "7 days"` and follow their new
  complaints, scores and how fast they reply.
- **Brand protection:** watch your own official shop and your resellers in 8 countries from one Task.
- **Sentiment and AI analysis:** feed comments, stars and the three detailed scores to an LLM or a sentiment model;
  `variation` tells you which color or size the complaint is about.
- **Seller service audit:** `sellerReply`, `sellerReplyAt` and `ratingSellerService` show who answers and how fast.
- **Cross-border vs local sellers:** `isOverseasSeller` and `originRegion` separate shops shipping from abroad.

## Input

The simplest input, one shop:

```json
{
  "startUrls": ["https://shopee.sg/shop/64922680"],
  "maxReviews": 100
}
```

One product, only complaints with a written comment:

```json
{
  "startUrls": ["https://shopee.sg/product/64922680/1427996834"],
  "minRating": 1,
  "maxRating": 2,
  "onlyWithComment": true,
  "maxReviews": 200
}
```

Several shops in other countries, last 30 days, with a shop summary row:

```json
{
  "shopIds": ["ugreen.my", "331309804"],
  "country": "MY",
  "startUrls": ["https://shopee.ph/ugreen.ph"],
  "newerThan": "30 days",
  "maxReviews": 1000,
  "includeShopSummary": true
}
```

| Field | What it does |
|---|---|
| `startUrls` | Shop links (`/shop/<id>` or `/<shop-username>`) and product links (`/product/<shop>/<item>` or `...-i.<shop>.<item>`) from any of the 8 countries |
| `shopIds` | Shop ids or shop usernames |
| `country` | SG, BR, ID, MY, TH, PH, VN or TW, used for `shopIds`. Links use their own domain |
| `maxReviews` | Reviews per shop or product (default 100, up to 5,000) |
| `minRating`, `maxRating` | Star range, 1 to 5 |
| `onlyWithComment` | Skip reviews without text |
| `onlyWithMedia` | Keep only reviews with photos or videos |
| `newerThan` | `2026-09-01`, `30 days`, `2 weeks`, `6 months` |
| `includeShopSummary` | One free `type: "shop"` row per shop |

Input names from other Shopee actors also work: `urls`, `productUrls`, `shopUrls`, `url`, `shops`, `maxItems`,
`region`.

## How it works, and its limit

Reviews come from the shop's public review page, newest first, **up to 5,000 reviews per shop** (measured on
2026-10-20). Filtering by stars reaches further back in time.

**Products:** Shopee does not let visitors open the review list of a single product without logging in. For a product
link, the Actor reads its shop's reviews and keeps the ones of that product. For a product in a small or medium shop
this covers its reviews of the last weeks or months. For a product in a very large shop (thousands of reviews a day),
the 5,000 reviews in reach may cover only a few days, and an older or rarely reviewed product may not show up at all:
you then get a free `NO_REVIEWS_FOUND` row that says how many shop reviews were read. Several products of the same
shop in one run share the pages already read.

## Output fields

| Field | Meaning |
|---|---|
| `reviewId`, `createdAt` | Shopee review id and date (UTC) |
| `rating`, `comment` | Stars (1 to 5) and the buyer's text |
| `ratingProductQuality`, `ratingSellerService`, `ratingDeliveryService` | The three detailed scores (1 to 5) |
| `itemId`, `productName`, `variation`, `productUrl` | Product reviewed and the variation bought |
| `shopId`, `shopName`, `country` | Shop and country |
| `imageCount`, `videoCount` | How many photos and videos the buyer attached |
| `tags` | Shopee's review prompts the buyer answered ("Value For Money", "Product Quality") |
| `likeCount` | Helpful votes |
| `sellerReply`, `sellerReplyAt` | The shop's public answer and its date |
| `isOverseasSeller`, `originRegion` | Cross-border seller flag and where the order shipped from |
| `sourceInput`, `scrapedAt` | Which input produced the row, and when |

With `includeShopSummary`, rows with `type: "shop"` add `shopUsername`, `shopUrl`, `shopRating`, `ratingCount`,
`ratingGood`, `ratingNormal`, `ratingBad`, `followers`, `productCount`, `responseRate`, `isOfficialShop` and
`shopJoinedAt`.

**Privacy by design:** the output never includes the buyer's username, user id, avatar, order id, or links to the
photos and videos they uploaded (they may show people). You get the counts only.

### Error codes (never charged)

| Code | When |
|---|---|
| `INVALID_INPUT` | Unknown country, a search or category link, a link that is not from Shopee, bad limits |
| `NOT_FOUND` | The shop does not exist |
| `NO_RESULTS` | The shop has no reviews, or none matched your filters |
| `NO_REVIEWS_FOUND` | A product link, and none of its shop's reviews in reach were for that product |
| `BLOCKED` | Shopee refused the request after several retries; run again |
| `NOT_REACHED` | The run timeout came before this input |

## Pricing

Pay per event, no monthly fee:

| Event | Free plan | Gold and above |
|---|---|---|
| Review delivered | US$ 3.00 per 1,000 | US$ 2.55 per 1,000 |
| Run start | US$ 0.005 | US$ 0.00425 |

Shop summary rows are free. Error rows, duplicates and reviews removed by your filters are never charged. Set a
maximum cost per run in Apify and the Actor stops cleanly when it is reached.

## Use it from code and AI agents

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_API_TOKEN")
run = client.actor("scrapewise/shopee-reviews-scraper").call(run_input={
    "startUrls": ["https://shopee.sg/shop/64922680"], "maxRating": 2, "maxReviews": 100})
for review in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(review["createdAt"], review["rating"], review["productName"], review["comment"])
```

The same works from the HTTP API (`run-sync-get-dataset-items`), n8n, Make, Zapier and Google Sheets. For AI agents: `https://mcp.apify.com/?actors=scrapewise/shopee-reviews-scraper`.

Requests an agent can pass straight through:

- "What do buyers complain about at this Shopee shop?" -> `{"startUrls": ["https://shopee.sg/shop/64922680"], "maxRating": 2, "onlyWithComment": true, "maxReviews": 200}`
- "Summarize the last week of reviews for this product" -> `{"startUrls": ["https://shopee.sg/product/64922680/1427996834"], "newerThan": "7 days", "maxReviews": 500}`
- "Compare the review scores of this brand's shops in Malaysia and the Philippines" -> `{"startUrls": ["https://shopee.com.my/ugreen.my", "https://shopee.ph/ugreen.ph"], "maxReviews": 300, "includeShopSummary": true}`

## FAQ

**Do I need a Shopee account or cookies?** No.

**Why can't I get all reviews of a product?** Shopee hides the per-product review list from visitors since 2026. The
shop review page is open, and it holds the same reviews mixed across the shop's products, up to 5,000 per shop. See
"How it works, and its limit".

**Can I get only new reviews every day?** Yes. Save a Task with `newerThan: "1 day"` (or `"7 days"` for weekly) and
schedule it. Reading stops at the first older review, so you only pay for new ones.

**Are comments translated?** No, they come in the language the buyer wrote (English, Portuguese, Indonesian, Thai,
Vietnamese, Chinese...).

**Is it legal?** It reads public review pages that anyone can open without logging in, and leaves out the buyer's
identity and uploaded media. How you use the data is your responsibility under Shopee's terms and the privacy laws that
apply to you.

## Changelog

- **2026-10-20:** first release. Shops and products in 8 countries; up to 5,000 reviews per shop; star, comment,
  media and date filters; free shop summary row.

This Actor collects only publicly visible data from Shopee. Independent tool, not affiliated with Shopee.
