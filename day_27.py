# Day 27: Automated Data Processing Pipeline

import pandas as pd
import numpy as np

def run_sales_pipeline(file_path):
    print("--- Step 1: Loading Dataset ---")
    df = pd.read_csv(file_path)
    print(df)
    
    print("\n--- Step 2: Data Cleaning (Handling Missing Values) ---")
    # If Sales column has any null/missing values, filling them with the median sales value
    if df["Sales"].isnull().any():
        median_sales = df["Sales"].median()
        df["Sales"] = df["Sales"].fillna(median_sales)
        print(f"Missing values detected and filled with median: {median_sales}")
    else:
        print("No missing values found in Sales column.")
        
    print("\n--- Step 3: Automated Analysis & Insights ---")
    total_revenue = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    top_product = df.loc[df["Sales"].idxmax()]["Product"]
    
    print(f"-> Total Revenue: {total_revenue}")
    print(f"-> Average Sales: {round(avg_sales, 2)}")
    print(f"-> Best Selling Product: {top_product}")
    
    print("\n--- Pipeline Execution Completed Successfully! ---")

# Running our automated pipeline using our cleaned sales data file
# (Make sure 'cleaned_sales_data.csv' or a sample csv exists in your folder)
run_sales_pipeline("cleaned_sales_data.csv")