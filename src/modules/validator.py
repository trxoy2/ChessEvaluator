import pandas as pd

def clean_and_validate_data(df):
    
    print("\n🧹 Cleaning and validating data...")

    # Raise an error if the input DataFrame is empty
    if df.empty:
        raise ValueError("The input DataFrame is empty.")

    # Record initial row count
    initial_rows = len(df)
    
    # Drop rows where 'url' is null
    df = df.dropna(subset=["url"])

    # Fill missing 'type' values with 'null'
    df["type"] = df["type"].where(pd.notna(df["type"]), None)

    # Normalize 'type' column (lowercase, strip whitespace)
    #df["type"] = df["type"].str.lower().str.strip()

    # Print URLs where type is 'null'
    null_type_urls = df[df["type"].isna()]["url"].tolist()
    if null_type_urls:
        print("URLs with null type:", null_type_urls)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Raise an error if any column is completely empty after processing
    if df.empty:
        raise ValueError("All rows were dropped, resulting in an empty DataFrame.")
    if df["url"].isna().all():
        raise ValueError("The 'url' column is empty after processing.")
    if df["type"].isna().all():
        raise ValueError("The 'type' column is empty after processing.")
    
    # Calculate dropped rows
    final_rows = len(df)
    dropped_rows = initial_rows - final_rows
    print(f"Total rows dropped due to null url or duplicates: {dropped_rows}")

    return df