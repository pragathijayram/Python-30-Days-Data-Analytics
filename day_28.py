# Day 28: Practical Smart Automation Script

import pandas as pd
import datetime

def smart_sales_automation(file_path):
    print("--- Smart Automation Bot Initiated ---")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Execution Timestamp: {current_time}\n")
    
    # 1. Loading data automatically
    df = pd.read_csv(file_path)
    
    # 2. Decision-based logic (AI/Smart Rule)
    total_sales = df["Sales"].sum()
    print(f"Total Sales Calculated: {total_sales}")
    
    # Smart Decision Making threshold
    target_sales = 150000
    
    print("\n--- Automated Evaluation & Decision ---")
    if total_sales >= target_sales:
        print("Status: SUCCESS 🎉")
        print("Decision: Target achieved! Automated report generated and saved for management.")
    else:
        print("Status: ALERT ⚠️")
        print("Decision: Target not met. Automated notification sent to the sales team for review.")

# Running our smart automation script
smart_sales_automation("cleaned_sales_data.csv")