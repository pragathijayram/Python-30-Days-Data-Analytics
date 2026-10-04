# Day 14: Python Tuples

# 1. Creating a tuple of store branch locations (Fixed Data)
store_locations = ("Bengaluru", "Mysuru", "Hubballi", "Mangaluru")
print("Store Locations (Tuple):", store_locations)

# 2. Accessing tuple elements using index
print("First Branch Location:", store_locations[0])
print("Third Branch Location:", store_locations[2])

# 3. Checking data type
print("Data Type of store_locations:", type(store_locations))

# Note: If you try to change tuple values like store_locations[0] = "Tumakuru", 
# Python will throw an error because tuples are immutable (unchangeable).