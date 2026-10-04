# Day 9: Practice and Revision - Store Performance Evaluator

print("--- Welcome to Store Performance System ---")

# 1. Taking inputs (Using input() and Type Casting)
store_name = input("Enter Store Name: ")
monthly_sales = int(input("Enter Monthly Sales Amount: "))
customer_rating = float(input("Enter Customer Rating (out of 5): "))

# 2. Decision making using Nested If and Logical Operators
if monthly_sales >= 60000:
    print("\n--- Evaluation for", store_name, "---")
    
    # Nested if with logical conditions
    if customer_rating >= 4.0:

        print("Grade: A+ (Outstanding Performance & High Customer Satisfaction!)")
    else:
        print("Grade: A (High Sales, but Customer Rating needs improvement.)")

elif monthly_sales >= 30000:
    print("\n--- Evaluation for", store_name, "---")
    
    if customer_rating >= 4.0:
        print("Grade: B (Decent Sales with good customer feedback.)")
    else:
        print("Grade: C (Average performance, needs attention.)")

else:
    print("\n--- Evaluation for", store_name, "---")
    print("Grade: D (Sales are below expected target. Major improvements needed.)")