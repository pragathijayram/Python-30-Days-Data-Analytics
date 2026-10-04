# Day 7: Nested if Statements

# Taking total sales and profit status from user
total_sales = int(input("Enter the total sales amount: "))
is_profitable_input = input("Is the store profitable? (yes/no): ").lower()

# Nested if logic
if total_sales >= 50000:
    print("\nSales target of 50,000 reached.")
    
    # Inner if (Nested condition)
    if is_profitable_input == "yes":
        print("Status: Excellent! High sales and profitable business.")
    else:
        print("Status: Good sales, but need to check on profitability.")
else:
    print("\nSales are below the target. Performance needs improvement.")