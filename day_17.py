# Day 17: Python Range Function and Advanced Loop Control

# 1. Using range(start, stop, step) - Printing even numbers from 2 to 10
print("--- Even Numbers using range(2, 11, 2) ---")
for num in range(2, 11, 2):
    print("Number:", num)

# 2. Using 'break' statement inside a loop
print("\n--- Using break statement ---")
for i in range(1, 6):
    if i == 4:
        print("Reached 4, breaking the loop.")
        break
    print("Current count:", i)

# 3. Using 'continue' statement inside a loop
print("\n--- Using continue statement (Skipping number 3) ---")
for i in range(1, 6):
    if i == 3:
        continue  # Skips printing when i is 3
    print("Current count:", i)