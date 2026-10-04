# Day 19: Python Built-in String, List, and Number Functions

# 1. String Functions (Data Cleaning)
raw_customer_name = "   pragathi j.   "
cleaned_name = raw_customer_name.strip().title()
print("Cleaned Customer Name:", cleaned_name)

feedback = "The service was BAD and slow."
updated_feedback = feedback.replace("BAD", "GOOD")
print("Updated Feedback:", updated_feedback)

# 2. List Functions (Data Organization)
sales_figures = [45000, 72000, 31000, 59000]
sales_figures.sort()
print("Sorted Sales Figures:", sales_figures)
print("Total number of sales records:", len(sales_figures))

# 3. Number Functions (Calculations)
revenue_values = [1200.50, 450.25, 890.75]
total_revenue = sum(revenue_values)
print("Total Sum of Revenue:", total_revenue)
print("Rounded Total Revenue:", round(total_revenue, 1))