# Day 23: Python NumPy Arrays and Data Cleaning

import numpy as np

# 1. Creating a NumPy Array from sales data
sales_list = [45000, 30000, 52000, 48000, 61000]
sales_array = np.array(sales_list)
print("Sales NumPy Array:", sales_array)

# 2. Vectorized Operation - Adding bonus of 5000 to all sales instantly without loops
updated_sales = sales_array + 5000
print("Sales after adding bonus (Vectorized):", updated_sales)

# 3. Handling Missing Values (np.nan and np.where)
# Let's say we have sales data with a missing value represented by np.nan
sales_with_nan = np.array([45000, np.nan, 52000, 48000, np.nan])
print("\nOriginal Sales with Missing Values:", sales_with_nan)

# Replacing np.nan with a default value like 0 using np.where
cleaned_sales = np.where(np.isnan(sales_with_nan), 0, sales_with_nan)
print("Cleaned Sales (Replacing NaN with 0):", cleaned_sales)