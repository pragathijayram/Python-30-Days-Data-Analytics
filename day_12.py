# Day 12: Python While Loop

print("--- 1. Simple While Loop Counting from 1 to 3 ---")
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1  # Incrementing count to avoid infinite loop

print("\n--- 2. Interactive While Loop (Password Checker) ---")
password = ""
while password != "python123":
    password = input("Enter the correct password: ")
    if password == "python123":
        print("Access Granted! Welcome, Pragathi.")
    else:
        print("Incorrect password. Try again.")