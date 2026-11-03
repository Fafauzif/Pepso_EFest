---
license: apache-2.0
language:
- id
- en
tags:
- e-commerce,
- product-reviews
---

# Tokopedia Product Reviews 2019

## Dataset Description

This dataset contains 40,607 product reviews from Tokopedia, one of Indonesia's largest e-commerce platforms, scraped in 2019. The dataset provides valuable insights into customer sentiment and shopping behavior in the Indonesian e-commerce market.

## Dataset Summary

- **Language**: Indonesian (Bahasa Indonesia)
- **Task**: Sentiment Analysis, Product Review Analysis, E-commerce Research
- **Size**: 40,607 reviews
- **Categories**: 5 product categories
- **Unique Products**: 3,647
- **Collection Period**: 2019

## Dataset Structure

### Data Fields

- **text** (string): The review text written by customers
- **rating** (int): Rating given by the reviewer (typically 1-5 scale)
- **category** (string): Product category, one of:
  - `pertukangan` (tools/hardware)
  - `fashion` (fashion)
  - `elektronik` (electronics)
  - `handphone` (mobile phones)
  - `olahraga` (sports)
- **product_name** (string): Name of the product
- **product_id** (string): Unique identifier for the product
- **sold** (int): Number of items sold
- **shop_id** (string): Unique identifier for the shop/seller
- **product_url** (string): URL link to the product page

### Data Splits

The dataset comes as a single split containing all 40,607 reviews.

## Dataset Statistics

| Category | Count |
|----------|-------|
| Total Reviews | 40,607 |
| Unique Products | 3,647 |
| Product Categories | 5 |
| Language | Indonesian |

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("farhamu/tokopedia-product-reviews-2019")

# Access the data
reviews = dataset['train']
print(f"Number of reviews: {len(reviews)}")
print(f"First review: {reviews[0]}")
```

## Potential Use Cases

- **Sentiment Analysis**: Classify customer sentiment based on review text and ratings
- **Product Recommendation**: Analyze product preferences across different categories
- **Market Research**: Understand Indonesian e-commerce customer behavior
- **Natural Language Processing**: Train Indonesian language models for e-commerce domain
- **Category Classification**: Predict product categories from review text
- **Rating Prediction**: Predict customer ratings from review text

## Data Collection

The data was collected through web scraping of Tokopedia product pages in 2019. The scraping process captured genuine customer reviews across five major product categories, providing a representative sample of customer feedback on the platform.

## Ethical Considerations

- This dataset contains public reviews that were posted on Tokopedia's platform
- Personal information has been anonymized (shop_id and product_id are anonymized identifiers)
- The data reflects genuine customer opinions and experiences
- Users should be mindful of potential biases in the data (e.g., selection bias, temporal bias from 2019)

## Limitations

- **Temporal Limitation**: Data is from 2019 and may not reflect current market trends
- **Platform Specific**: Limited to Tokopedia platform, may not generalize to other Indonesian e-commerce platforms
- **Category Limitation**: Only covers 5 product categories
- **Language**: Primarily in Indonesian, limiting applicability to other languages

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{tokopedia-product-reviews-2019,
  title={Tokopedia Product Reviews 2019},
  author={[M. Farhan]},
  year={2025},
  url={https://huggingface.co/datasets/farhamu/tokopedia-product-reviews-2019},
  note={Indonesian e-commerce product reviews dataset from Tokopedia platform}
}
```

## Contact

For questions or issues regarding this dataset, please open an issue in the dataset repository or contact kontak.farhan@gmail.com.

## Acknowledgments

- Thanks to Tokopedia for providing a platform that enables customer reviews
- This dataset was originally shared on Kaggle but is now maintained on Hugging Face for better accessibility and integration with ML workflows