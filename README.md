# Customer Behavior Analytics System

## Overview
This project analyzes customer behavior patterns using BigBasket product data. While initially intended to include churn prediction, the project focuses on comprehensive product analytics and customer behavior insights due to dataset constraints.

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
├── LICENSE                       # Project license (e.g., MIT, Apache)
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

## Technical Stack
- Python 3.12
- Pandas for data manipulation
- NumPy for numerical operations
- Seaborn/Matplotlib for visualization

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
- Integration with machine learning models for product recommendations
- Enhanced visualization dashboard

## Contributing
Feel free to fork the project and submit pull requests. For major changes, please open an issue first to discuss the proposed changes.

## License
[MIT](https://choosealicense.com/licenses/mit/)
