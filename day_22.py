# Day 22: Python Writing Cleaned Data to CSV

import csv

# 1. Raw data including a missing value row (March)
cleaned_sales_data = [
    ["Month", "Product", "Sales", "Status"],
    ["January", "Laptop", "45000", "Active"],
    ["February", "Mobile", "30000", "Active"],
    ["April", "Laptop", "52000", "Active"]
]

# 2. Writing the cleaned data into a new CSV file named 'cleaned_sales_data.csv'
with open("cleaned_sales_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # writerows() writes all rows at once
    writer.writerows(cleaned_sales_data)

print("Cleaned data successfully written to 'cleaned_sales_data.csv'!")