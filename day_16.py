# Day 16: Python Sets

# 1. Creating a set with duplicate values (Duplicates will be automatically removed)
store_categories = {"Electronics", "Groceries", "Apparel", "Electronics", "Groceries"}
print("Unique Store Categories (Set):", store_categories)

# 2. Creating two sets for store branches in different cities
branch_set_a = {"Bengaluru", "Mysuru", "Hubballi"}
branch_set_b = {"Hubballi", "Mangaluru", "Belagavi"}

# 3. Set Operations
# Union (|) - Combines all unique branches from both sets
all_branches = branch_set_a | branch_set_b
print("All Unique Branches (Union):", all_branches)

# Intersection (&) - Finds common branches present in both sets
common_branches = branch_set_a & branch_set_b
print("Common Branches (Intersection):", common_branches)

# Difference (-) - Finds branches present in set A but not in set B
exclusive_to_a = branch_set_a - branch_set_b
print("Branches only in Set A (Difference):", exclusive_to_a)