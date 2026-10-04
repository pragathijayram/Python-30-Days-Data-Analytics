# Day 24: Python Pandas Library for Data Analysis

import pandas as pd

# 1. Loading our previously created CSV file using pandas
df = pd.read_csv("cleaned_sales_data.csv")

# 2. Displaying the first few rows using head()
print("--- First 5 Rows of DataFrame (head) ---")
print(df.head())

# 3. Getting dataset structure and info using info()
print("\n--- DataFrame Information (info) ---")
print(df.info())

# 4. Getting statistical summary of numerical data using describe()
print("\n--- Statistical Summary (describe) ---")
print(df.describe())