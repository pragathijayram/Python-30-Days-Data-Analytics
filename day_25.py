# Day 25: Advanced Pandas - GroupBy, Filtering, and Sorting

import pandas as pd

# 1. Creating a slightly larger sample DataFrame for analysis
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"],
    "Sales": [45000, 30000, 52000, 15000, 35000, 60000],
    "Status": ["Active", "Active", "Active", "Pending", "Active", "Active"]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

# 2. Filtering Data - Getting rows where Sales are greater than 35,000
print("\n--- Filtered Data (Sales > 35000) ---")
high_sales = df[df["Sales"] > 35000]
print(high_sales)

# 3. Sorting Data - Sorting by Sales in descending order (highest to lowest)
print("\n--- Sorted Data by Sales (Highest First) ---")
sorted_df = df.sort_values(by="Sales", ascending=False)
print(sorted_df)

# 4. GroupBy - Grouping by Product and finding total sales for each product
print("\n--- GroupBy: Total Sales by Product ---")
product_group = df.groupby("Product")["Sales"].sum()
print(product_group)