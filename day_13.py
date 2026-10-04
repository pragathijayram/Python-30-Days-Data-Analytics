# Day 13: Python Lists

# 1. Creating a list of store monthly sales
monthly_sales = [45000, 52000, 48000, 61000, 55000]
print("All Monthly Sales:", monthly_sales)

# 2. Accessing elements using Index (Remember: Index starts from 0)
print("First Month Sales:", monthly_sales[0])
print("Fourth Month Sales:", monthly_sales[3])

# 3. Adding a new month's sales using append() method
monthly_sales.append(67000)
print("Updated Sales List after adding new month:", monthly_sales)

# 4. Finding total months using len() function
total_months = len(monthly_sales)
print("Total recorded months:", total_months)