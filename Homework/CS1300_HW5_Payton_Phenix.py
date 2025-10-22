"""
CS1300 - Homework #5: Advanced Control Structures
Name: Phenix Payton
Date: 10/20/25
Description: Advanced conditional logic and validation
"""

print("=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
import sys
all_valid_range = True if (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100) else False
if all_valid_range == False:
    print("ERROR INVALID SCORE DETECTED")
    sys.exit()
else:
    print("All scores in valid range (0-100)")
# 2. Check for suspicious patterns
sus_check1 = True if test1 == test2 == test3 == test4 else False
sus_check2 = True  if test2 - test1 >= 40 or test3 - test2 >= 40 or test4 - test3 >= 40 else False
sus_check3 = True if test1 == 100 and test2 == 100 and test3 == 100 and test4 == 100 else False
print("Suspicious Checks:")
if sus_check1 == True:
    print("All test scores the same. Be sure this is correct!!")
else:
    print("There is variation in scores")
if sus_check2 == True:
    print("Suspicious jump in scores!!")
else:
    print("No suspicious jump in scores")
if sus_check3 == True:
    print("All scores perfect. Be sure this is correct!!")
else:
    print("Not all perfect scores")
print("Statistics:")
average_score = (test1 + test2 + test3 + test4)/4
round(average_score,2)
print(f"- Average: {average_score}")
highest_score = test1 if (test1 >= test2 and test1 >= test3 and test1 >= test4) else test2 if (test2 >= test1 and test2 >= test3 and test2 >= test4) else test3 if (test3 >= test1 and test3 >= test2 and test3 >= test4) else test4
print(f"- Highest: {highest_score}")
lowest_score = test1 if (test1 <= test2 and test1 <= test3 and test1 <= test4) else test2 if (test2 <= test1 and test2 <= test3 and test2 <= test4) else test3 if (test3 <= test1 and test3 <= test2 and test3 <= test4) else test4
print(f"- Lowest: {lowest_score}")
score_trend = "IMPROVING" if test4 > test1 else "STEADY" if test4 == test1 else "DECLINIG"
print(f"Trend: {score_trend}")
grade = "A" if average_score >= 90 else "B" if average_score >= 80 else "C" if average_score >= 70 else "D" if average_score >= 60 else "F"
print(f"Grade: {grade}")
status = "PASSING" if grade != "F" else "FAILING"
print(f"Status: {status}")