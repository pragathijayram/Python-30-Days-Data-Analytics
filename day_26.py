# Day 26: AI-Assisted Data Analysis & Automated Insights

import pandas as pd

# 1. Sample sales data across different quarters
data = {
    "Quarter": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3", "Q4", "Q4"],
    "Region": ["North", "South", "North", "South", "North", "South", "North", "South"],
    "Revenue": [120000, 95000, 150000, 110000, 135000, 105000, 160000, 125000]
}
df = pd.DataFrame(data)

print("--- Complete Sales Dataset ---")
print(df)

# 2. Automated Aggregation (Finding top-performing regions using Pandas)
print("\n--- Automated Insights: Total Revenue by Region ---")
region_summary = df.groupby("Region")["Revenue"].sum()
print(region_summary)

# 3. Finding overall maximum revenue and quarter
max_revenue_row = df.loc[df["Revenue"].idxmax()]
print("\n--- Top Performing Record ---")
print(f"Highest Revenue of {max_revenue_row['Revenue']} achieved in {max_revenue_row['Quarter']} ({max_revenue_row['Region']} Region)")