# Day 21: Python Reading CSV Files using csv module

import csv

# 1. Reading CSV file line by line
print("--- Reading CSV File Contents ---")
with open("sales_data.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    # Printing each row from the CSV
    for row in csv_reader:
        print(row)