# Day 8: Combining Conditions using Logical Operators

# Taking sales and customer satisfaction input from user
sales = int(input("Enter total sales amount: "))
rating = int(input("Enter customer satisfaction rating (1 to 5): "))

# Using 'and' operator to check multiple conditions
if sales >= 50000 and rating >= 4:
    print("\nResult: Outstanding Store! High sales and great customer feedback.")
elif sales >= 50000 or rating >= 4:
    print("\nResult: Good Store! Either sales are high or rating is good.")
else:
    print("\nResult: Needs Improvement in both sales and customer satisfaction.")