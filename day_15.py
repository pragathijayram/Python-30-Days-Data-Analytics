# Day 15: Python Dictionaries

# 1. Creating a dictionary for store details
store_details = {
    "store_id": 101,
    "store_name": "Bengaluru Central Hub",
    "city": "Bengaluru",
    "monthly_sales": 85000,
    "is_profitable": True
}

print("Full Store Dictionary:", store_details)

# 2. Accessing specific values using Keys
print("Store Name:", store_details["store_name"])
print("Monthly Sales:", store_details["monthly_sales"])

# 3. Adding a new key-value pair to the dictionary
store_details["manager_name"] = "Pragathi"
print("Updated Store Dictionary:", store_details)

# 4. Getting all keys and values separately
print("All Keys:", store_details.keys())
print("All Values:", store_details.values())