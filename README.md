# Customer Behavior Analytics System

## Project Overview
This project aims to analyze customer behavior patterns using BigBasket's product dataset. The primary focus is to derive insights into customer purchasing trends, product preferences, pricing impact, and discount influence on sales.

While the initial plan included churn prediction, dataset constraints limited the availability of customer-specific transactional data. As a result, the project pivots towards comprehensive product analytics and behavioral insights, helping businesses understand consumer engagement, brand loyalty, and category-level demand.

## Key Objectives

 🔹 Product Performance Analysis – Identifying high-performing products and categories based on rating, sales price, and discount trends.
 🔹 Customer Behavior Insights – Understanding how pricing, discounts, and brand influence purchase decisions.
 🔹 Sentiment & Review Analysis – Examining product ratings and descriptions to assess customer satisfaction levels.
 🔹 Pricing & Discount Impact – Analyzing how price differences and discounts affect customer preferences.
 🔹 Feature Engineering for Future Predictions – Preparing the dataset for potential predictive modeling by cleaning and structuring the data.

## Technologies Used
 Python (Pandas, NumPy, Scikit-Learn) – Data preprocessing, feature engineering, and exploratory data analysis (EDA).
 Data Visualization (Matplotlib, Seaborn, Tableau ) – Graphical insights into customer behavior trends.
 Machine Learning (K-Means clustering , XGBoost model) – implementation of customer segmentation and predictive modeling. ( Not fully perfected )


## Project Structure

``` bash
Customer-Behavior-Churn-Prediction/
├── data/                         # Data-related files
│   ├── raw/                      # Raw, unprocessed datasets
│   ├── processed/                # Cleaned and transformed datasets
│   ├── external/                 # additional datasets for enrichment
│   ├── outputs/                  # Model predictions, clustering results, etc.
│   └── README.md                 # Explanation of the data folder contents
├── notebooks/                    # Jupyter notebooks for EDA, modeling, etc.
│   ├── 01-data-exploration.ipynb # Data exploration and visualization
│   ├── 02-rfm-analysis.ipynb     # RFM analysis and clustering
│   └── README.md                 # Explanation of the notebooks folder
├── src/                          # Source code for the project
│   ├── etl/                      # ETL pipeline scripts
│   │   ├── preprocessing_data.py # Data transformation logic
│   ├── analysis/                 # RFM and clustering code
│   │   ├── rfm.py                # Functions for RFM analysis
│   │   ├── clustering.py         # K-means or DBSCAN clustering
│   ├── modeling/                 # Machine learning scripts
│   │   ├── ML_model.py           # Code for prediction model
│   │   ├── shap_analysis.py      # SHAP value generation
│   ├── utils/                    # Helper functions and utilities
│   │   ├── data_preprocessing.py # Data preprocessing utilities
│   │   ├── visualizations.py     # Custom visualization scripts
├── dashboards/                   # Tableau/Power BI dashboards or Streamlit app code
│   ├── tableau/                  # Tableau workbook files
│   └── README.md                 # Explanation of the dashboards folder
├── tests/                        # Unit and integration tests
│   ├── test_model.py             # Test churn prediction model
├── requirements.txt              # List of dependencies for the project
├── config.yaml                   # Configuration file (e.g., database credentials, API keys)
├── README.md                     # Project overview and setup instructions
├── LICENSE                       # Project license
└── .gitignore                    # Ignore unnecessary files in Git


```

## Features
- **Data Preprocessing**: Handles missing values, duplicates, and data type conversions
- **Exploratory Data Analysis**: 
  - Product pricing analysis
  - Rating distribution
  - Category-wise analysis
  - Price-rating correlation studies
- **Feature Engineering**:
  - Price difference calculation
  - Discount percentage analysis
  - Rating normalization

## Key Insights
- Product pricing patterns across different categories
- Correlation between product ratings and prices
- Discount impact analysis
- Category-wise product distribution

## Dataset
The analysis uses the BigBasket products dataset which includes:
- Product details (name, category, sub-category)
- Pricing information (sale price, market price)
- Customer ratings
- Product descriptions
- Brand information


## Getting Started

### Prerequisites

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Running the Analysis
1. Data Preprocessing:
```bash
python src/etl/preprocessing_data.py
```

2. Open the Jupyter notebooks in the `notebooks/` directory for detailed analysis:
   - Start with `data-exploration.ipynb` for initial data understanding
   - Move to `rfm-analysis.ipynb` for in-depth analysis

## Future Improvements
- Implementation of customer segmentation
- Addition of time-series analysis
- Enhanced visualization dashboard
- Recommendation System – Suggesting products based on past behavior.


## Contributing
Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss the proposed changes.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
[albinmanuvel31@gmail.com]

Linkedin - [www.linkedin.com/in/albin-manuvel-6607a9221]



