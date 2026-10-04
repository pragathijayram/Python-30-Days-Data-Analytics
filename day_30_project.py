# Day 30: Capstone Data Analysis Project - Smart Sales Performance Analyzer

import pandas as pd
import numpy as np
import datetime

def run_capstone_project(file_path):
    print("=" * 60)
    print("       AI-POWERED SALES DATA ANALYSIS & REPORT GENERATOR")
    print("=" * 60)
    
    # 1. Load Dataset
    print("\n[Step 1] Loading Dataset...")
    df = pd.read_csv(file_path)
    print(f"Total Records Loaded: {len(df)}")
    
    # 2. Data Cleaning & Preprocessing
    print("\n[Step 2] Cleaning and Preprocessing Data...")
    if df["Sales"].isnull().any():
        median_val = df["Sales"].median()
        df["Sales"] = df["Sales"].fillna(median_val)
        print(f"-> Missing values handled (Filled with median: {median_val})")
    else:
        print("-> No missing values found. Data is clean.")
        
    # 3. Advanced Analysis (Aggregation & Grouping)
    print("\n[Step 3] Generating Analytical Insights...")
    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    top_row = df.loc[df["Sales"].idxmax()]
    
    print(f"-> Total Cumulative Sales: {total_sales}")
    print(f"-> Average Sales per Record: {round(avg_sales, 2)}")
    print(f"-> Top Performing Sale: Product '{top_row['Product']}' with Sales of {top_row['Sales']} ({top_row['Month']})")
    
    # 4. Generating Final Automated Report Text File
    report_filename = "final_sales_insight_report.txt"
    print(f"\n[Step 4] Exporting Final Summary to '{report_filename}'...")
    
    report_content = f"""
    ========================================
             FINAL SALES ANALYSIS REPORT
    ========================================
    Generated Timestamp: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    Summary Metrics:
    - Total Revenue Generated: {total_sales}
    - Average Performance: {round(avg_sales, 2)}
    - Peak Performance Record: {top_row['Product']} ({top_row['Sales']} Sales in {top_row['Month']})
    
    Project Status: SUCCESS (Ready for Portfolio & LinkedIn)
    ========================================
    """
    
    with open(report_filename, "w") as report_file:
        report_file.write(report_content)
        
    print("-> Final report successfully generated and saved!")
    print("\n" + "=" * 60)
    print("   CONGRATULATIONS! 30-DAY PYTHON DATA ANALYTICS ROADMAP COMPLETED!")
    print("=" * 60)

# Running our capstone project script
run_capstone_project("cleaned_sales_data.csv")