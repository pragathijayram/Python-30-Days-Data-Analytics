# Day 10: Assignment on Nested If Statements - Employee Evaluator

print("--- Welcome to Employee Evaluation System ---")

# 1. Taking inputs
years_of_experience = int(input("Enter Years of Experience: "))
performance_rating = float(input("Enter Performance Rating (out of 5): "))

# 2. Outer If condition (Checking Experience)
if years_of_experience >= 3:
    print("\nExperience Criteria Met.")
    
    # Inner If-Else condition (Nested Checking Rating)
    if performance_rating >= 4.5:
        print("Status: Eligible for Promotion and High Bonus! 🎉")
    else:
        print("Status: Eligible for Bonus, but Promotion is pending. 👍")

else:
    print("\nStatus: Not eligible for promotion yet (Experience < 3 years). Keep up the good work! 💪")