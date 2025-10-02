# CS 1300 - Homework 2
# Phenix Payton
# 9/11/25
# Variables, Input/Output, and Type Conversion

### Problem 1: Personal Finance Calculator
print("=" * 50)
print("PERSONAL FINANCE CALCULAOTR")
print("=" * 50)
income = float(input("What is your monthly income? "))
print(f"Your monthly income: {income}")
rent = float(input("What is your monthly cost of rent? "))
print(f"Your rent/housing: {rent}")
food = float(input("What is your monthly cost of food? "))
print(f"Your food expenses: {food}")
transport = float(input("What is your monthly cost of transportation? "))
print(f"Your cost of transportation: {transport}")
other = float(input("Cost of any other monthly expenses? "))
print(f"Your other expenses: {other}")

print("=" * 50)
print("MONTHLY BUDGET REPORT")
print("=" * 50)
print(f"income:     $ {income}")
print("-" * 30)
print("Expenses:")
print(f"  Housing: $ {rent}")
print(f"  Food: $ {food}")
print(f"  Transportation: $ {transport}")
print(f"  Other: $ {other}")
print("-" * 30)
total_expense = rent + food + transport + other
remaining = income - total_expense
savings = round((remaining / income) * 100, 1)
print(f"Total Expenses:     $ {total_expense}")
print(f"Remaining Balance:     $ {remaining}")
print(f"Savings Rate:       {savings}%")


### Problem 2: Grade Statistics Calculator
print("=" * 30)
print("GRADE STATISTICS CALCULATOR")
print("=" * 30)
# Gather Test Scores
test1 = float(input("What is score for test 1? "))
print(f"Test 1 score: {test1}")
test2 = float(input("What is score for test 2? "))
print(f"Test 2 score: {test2}")
test3 = float(input("What is score for test 3? "))
print(f"Test 3 score: {test3}")
test4 = float(input("What is score for test 4? "))
print(f"Test 4 score: {test4}")
test5 = float(input("What is score for test 5? "))
print(f"Test 5 score: {test5}")
print("=" * 30)
print("GRADE REPORT")
print("=" * 30)
print("Test Scores Entered:")
print(f"  Test 1:    {test1}/100")
print(f"  Test 2:    {test2}/100")
print(f"  Test 3:    {test3}/100")
print(f"  Test 4:    {test4}/100")
print(f"  Test 5:    {test5}/100")

# Calculate Test Statistics
total_points = test1 + test2 + test3 +test4 + test5
avg_score = total_points / 5
overall = round((total_points / 500) * 100, 1)
needed = 450 - total_points

# Display Test Statistics
print("=" * 30)
print("Statistics:")
print(f"  Total Points:    {total_points}/500")
print(f"  Average Score:    {avg_score}")
print(f"  Overall Garde:    {overall}%")
print("\n")
print (f"Points needed for 90%: {needed}")
print("=" * 30)

### Problem 3:Time Zone Converter
print("+"+"-"*25+"+")
print("|   Time Zone Converter   |")
print("+"+"-"*25+"+")
print("\n")

# Get Input
hour = int(input("Enter current hour (EST, 0-23): "))
minute = str(input("Enter current minute (0-59): "))
print("\n")
print("+"+"-"*20+"+")
print("|   CURRENT TIMES   |")
print("+"+"-"*20+"+")
print("\n")

# Time in each Zone
cst_hour = (hour - 1) % 24
mst_hour = (hour - 2) % 24
pst_hour = (hour - 3) % 24

# EST to 12-hour
if hour < 12:
    est_ampm = "AM"
else:
    est_ampm= "PM"
est_12 = hour % 12
if est_12 == 0:
    est_12 = 12

# CST to 12-hour
if cst_hour < 12:
    cst_ampm = "AM"
else:
    cst_ampm = "PM"
cst_12 = cst_hour % 12
if cst_12 == 0:
    cst_12 = 12

# MST to 12-hour
if mst_hour < 12:
    mst_ampm = "AM"
else:
    mst_ampm = "PM"
mst_12 = mst_hour % 12
if mst_12 == 0:
    mst_12 = 12

# PST to 12-hour
if pst_hour < 12:
    pst_ampm = "AM"
else:
    pst_ampm = "PM"
pst_12 = pst_hour % 12
if pst_12 == 0:
    pst_12 = 12

# Display Table
print("|Time Zone | Time   | 12-hr Format|")
print("|----------|---------|----------|")
print(f"|EST       |  {hour}:{minute}  | {est_12}:{minute}{est_ampm} |")
print(f"|CST       |  {cst_hour}:{minute}  | {cst_12}:{minute}{cst_ampm} |")
print(f"|MST       |  {mst_hour}:{minute}  | {mst_12}:{minute}{mst_ampm} |")
print(f"|PST       |  {pst_hour}:{minute}  | {pst_12}:{minute}{pst_ampm} |")

### Problem 4: Recipe Scaler
print("#"*30)
print("    RECIPE SCALER  ")
print("#"*30)
print("\n")

serving_orig = int(input("Enter original serving size: "))
serving_desire = int(input("Enter desired serving size: "))
scaler = serving_desire / serving_orig
round(scaler,2)
print("\n")

# Gather Ingredients
ingredient1 = input("First Ingredient Name: ")
amount1 = float(input("Amount: "))
unit1 = input("Unit: ")
scaled_amount1 = amount1 * scaler
print("\n")

ingredient2 = input("Second Ingredient Name: ")
amount2 = float(input("Amount: "))
unit2 = input("Unit: ")
scaled_amount2 = amount2 * scaler
print("\n")

ingredient3 = input("Third Ingredient Name: ")
amount3 = float(input("Amount: "))
unit3 = input("Unit: ")
scaled_amount3 = amount3 * scaler
print("\n")

ingredient4 = input("Fourth Ingredient Name: ")
amount4 = float(input("Amount: "))
unit4 = input("Unit: ")
scaled_amount4 = amount4 * scaler
print("\n")

ingredient5 = input("Fifth Ingredient Name: ")
amount5 = float(input("Amount: "))
unit5 = input("Unit: ")
scaled_amount5 = amount5 * scaler
print("\n")

# Display New Recipe Amounts
print("#"*30)
print("   RECIEPE SCALING RESULTS  ")
print("#"*30)
print(f"Scaling factor: {scaler}x ({serving_orig} -> {serving_desire} servings)")
print("-"*20)
print("\n")
print(f"Original Recipe ({serving_orig} servings) | Scaled Recipe ({serving_desire} servings)")
print("-------------------|-----------------------")
print(f"{ingredient1}:  {amount1} {unit1}   | {ingredient1}: {scaled_amount1} {unit1}")
print(f"{ingredient2}:  {amount2} {unit2}   | {ingredient2}: {scaled_amount2} {unit2}")
print(f"{ingredient3}:  {amount3} {unit3}   | {ingredient3}: {scaled_amount3} {unit3}")
print(f"{ingredient4}:  {amount4} {unit4}   | {ingredient4}: {scaled_amount4} {unit4}")
print(f"{ingredient5}:  {amount5} {unit5}   | {ingredient5}: {scaled_amount5} {unit5}")
print("#"*30)