# Day 20: Python File Handling

# 1. Writing data to a new text file ('w' mode)
# This will automatically create a new file named 'store_report.txt'
with open("store_report.txt", "w") as file:
    file.write("Store Performance Report\n")
    file.write("Branch: Bengaluru Central\n")
    file.write("Status: Profitable and Growing.\n")

print("Data successfully written to store_report.txt")

# 2. Reading data from the text file ('r' mode)
print("\n--- Reading data from store_report.txt ---")
with open("store_report.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Appending new data to the existing file ('a' mode)
with open("store_report.txt", "a") as file:
    file.write("Manager in charge: Pragathi J\n")

print("\n--- Reading updated file after appending ---")
with open("store_report.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)