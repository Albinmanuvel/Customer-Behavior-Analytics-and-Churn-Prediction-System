import pandas as pd
import os

# Define file paths
RAW_DATA_PATH = os.path.join("data", "raw", "bigbasket_products.csv")
PROCESSED_DATA_PATH = os.path.join("data", "processed", "cleaned_bigbasket_products.csv")

def load_data(file_path):
    """Load the raw dataset."""
    try:
        data = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def clean_data(df):
    """Clean and preprocess the dataset."""
    # Drop duplicates
    df = df.drop_duplicates()
    print(f"Removed duplicates. Remaining rows: {df.shape[0]}")

    # Handle missing values (example strategy: fill or drop)
    missing_columns = df.columns[df.isnull().any()]
    for col in missing_columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(0)
    print(f"Handled missing values in columns: {list(missing_columns)}")

    # Convert prices or numeric fields to numeric type if needed
    if 'Price' in df.columns:
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned dataset saved to {output_path}")
    except Exception as e:
        print(f"Error saving cleaned dataset: {e}")

def main():
    # Load raw data
    data = load_data(RAW_DATA_PATH)
    if data is not None:
        # Clean data
        cleaned_data = clean_data(data)
        # Save processed data
        save_cleaned_data(cleaned_data, PROCESSED_DATA_PATH)

if __name__ == "__main__":
    main()
