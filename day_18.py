# Day 18: Python Functions

# 1. Defining a simple function to greet store visitors
def greet_store_manager(name):
    print("Hello,", name, "! Welcome back to the Store Analytics Dashboard.")

# Calling the function multiple times with different names
greet_store_manager("Pragathi")
greet_store_manager("Rahul")


# 2. Defining a function to calculate total sales with tax (using return)
def calculate_total_sales(base_sales, tax_amount):
    total = base_sales + tax_amount
    return total

# Calling the function and storing the returned result
final_revenue = calculate_total_sales(50000, 4500)
print("Total calculated revenue with tax:", final_revenue)