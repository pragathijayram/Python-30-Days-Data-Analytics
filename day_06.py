# Day 6: Python Conditional Statements (if, elif, else)

# Taking total sales input from user
total_sales = int(input("Enter the total sales amount: "))

# Decision making based on sales target
if total_sales >= 100000:
    print("Outstanding Performance! Target Achieved with a huge profit.")
elif total_sales >= 50000:
    print("Good Job! Sales target achieved successfully.")
else:
    print("Sales are low. Need to improve performance next month.")