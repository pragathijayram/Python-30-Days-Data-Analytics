# Day 5: Python Input and Type Casting

# 1. Taking user input (Note: input() always returns a string)
store_name = input("Enter the Store Name: ")

# 2. Taking numeric input and converting it using int() (Type Casting)
sales_day1 = int(input("Enter Day 1 Sales: "))
sales_day2 = int(input("Enter Day 2 Sales: "))

# 3. Performing calculations
total_sales = sales_day1 + sales_day2

# 4. Displaying the result
print("\n--- Sales Report for", store_name, "---")
print("Total Sales for 2 Days:", total_sales)