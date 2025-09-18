'''
Practice 1-a: Temperature checker
'''
# Fill in the blanks with the correct comparison operators

current_temp = 72

# Check if it's freezing (32 degrees or below)
is_freezing = current_temp <= 32
print(f"Is it freezing? {is_freezing}")

# Check if it's exactly room temperature (72 degrees)
is_room_temp = current_temp == 72
print(f"Is it room temperature? {is_room_temp}")

# Check if it's not 100 degrees
not_boiling = current_temp != 100
print(f"Is it not 100 degrees? {not_boiling}")

'''
Practice 1-b: Grade categories
'''
# Write Boolean expressions for each grade category

score = 85

# Check if the grade is an A (90 or above)
is_A = score >= 90 # Write your expression here
print(f"Score: {score}")
print(f"Is it an A (>=90)? {is_A}")

# Check if the grade is failing (below 60)
is_failing = score < 60  # Write your expression here
print(f"Is it failing (<60)? {is_failing}")

# Check if the grade is between 80 and 89 (B grade)
# Hint: You'll need two comparisons here!
is_B = score >= 80 and score <= 89
print(f"Is it a B (80-89)? {is_B}")

# Check if the grade is NOT a perfect score (not 100)
not_perfect = score != 100 # Write your expression here
print(f"Is it not perfect (!= 100)? {not_perfect}")

'''
# Practice 1-c: Shopping cart validation system
'''
# Create Boolean expressions for an online store

# Shopping cart data
num_items = 3
cart_total = 45.50
coupon_code = "SAVE10"
is_member = True

# TODO: Create these Boolean expressions

# 1. Check if cart qualifies for free shipping (total >= $50)
free_shipping = cart_total >= 50
print(f"Is shipping free? {free_shipping}")

# 2. Check if cart is empty (0 items)
cart_empty = num_items == 0
print(f"Is cart Empty? {cart_empty}")

# 3. Check if customer entered the correct coupon code
valid_coupon = "SAVE10"
print(f"Is coupon code valid? {valid_coupon == coupon_code}")

# 4. Check if customer gets member discount (is a member AND cart > $25)
member_discount = is_member == True and cart_total >= 25
print(f"Get member discount? {member_discount}")

# 5. Check if this is a small order (less than 5 items AND total under $30)
small_order = num_items <= 5 and cart_total >= 30

# Display results
print("Shopping Cart Analysis:")
print(f"Items in cart: {num_items}")
print(f"Cart total: ${cart_total}")
print(f"Free shipping eligible: {free_shipping}")
print(f"Cart is empty: {cart_empty}")
print(f"Valid coupon: {valid_coupon}")
print(f"Member discount applies: {member_discount}")
print(f"Small order: {small_order}")

'''
# Practice 2-a: Weather advisor
'''
# Add if statements to give appropriate advice
temperature = 72 # Try changing this value!
print(f"Current temperature: {temperature}°F")
print("Weather advice:")
if temperature > 90:
    print("It's very hot! Stay hydrated!")
if temperature < 32:
    print ("It's freezing! Bundle up!")
if temperature == 72: 
    print ("Perfect weather!")
# Test with different temperatures: 95, 25, 72
'''
# Practice 2-b: Discount calculator
'''
# Write if statements to apply discounts
# Customer information
purchase_amount = 125.00
is_student = True
is_senior = False
is_veteran = False
print("=== Discount Calculator ===")
print(f"Original amount: ${purchase_amount:.2f}")
discount = 0
# TODO: Add if statements for each discount
# If purchase > $100, add 10% discount
if purchase_amount > 100:
    discount = discount + (purchase_amount * 0.10)
print(" 10% discount for purchases over $100")
# If customer is a student, add $5 discount
if is_student == True:
    discount += 5
    print(" $5 student discount applied")
# If customer is a senior (over 65), add 15% discount
if is_senior == True:
    discount = discount + (purchase_amount * .15)
    print(" 15% senior discount applied")
# If customer is a veteran, add $10 discount
if is_veteran == True:
    discount += 10
    print(" $10 veteran discount applied")
# Calculate and display final amount
final_amount = purchase_amount - discount
print(f"\nTotal discount: ${discount:.2f}") #### FLOAT TO 2 DIGITS (:.2f)
print(f"Final amount: ${final_amount:.2f}") #### FLOAT TO 2 DIGITS (:.2f)

## No Practice 2_c (Ran out of time)

'''
Practice 3_a: Daily decision maker
'''
# Complete the if-else statements
# Decision 1: Weekend or Weekday?
day = "Tuesday" # Try "Monday" too!
print(f"Today is {day}")
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday!")
# Decision 2: Hot or Cold Beverage?
temperature = 85 # Try different values!
print(f"\nTemperature: {temperature}°F")
# Complete this if-else statement
if temperature > 70:
    print("It is hot outside today!")
else:
    print("It is less than 70 degrees out today.")
# Decision 3: Light or Dark Mode?
current_hour = 11 # 8 PM in 24-hour format
print(f"\nCurrent hour: {current_hour}:00")
# Write an if-else to choose display mode
# make dark mode a variable
# Use dark mode after 6 PM (18:00) or before 6 AM
if current_hour >= 18:
    dark_mode = True
    print("Displaying in dark mode.")
else:
    dark_mode = False
    print("Displaying in light mode")
        
'''
Practice 3_b: Movie ticket pricing
'''
# Implement age-based pricing with if-else
age = 72 # Try different ages!
day = "Tuesday" # Try different days!
print("=== Movie Ticket Pricing ===")
print(f"Customer age: {age}")
print(f"Day: {day}")
# Base ticket price
base_price = 12.00
final_price = base_price
# TODO: Implement pricing rules with if-else
# Rule 1: Children (12 and under) get 50% off, others pay full price
if age <= 12:
    final_price = base_price * 0.5
    print("Child discount applied (50% off)")
else:
    print("No child discount applied. ")
   
print("Standard pricing")
# Rule 2: Seniors (65+) get 30% off, others no discount
if age >= 65:
    final_price = final_price * 0.7
    print(" Senior discount applied (30% off)")
else:
    print(" No Senior discount")
# No additional discount
# Rule 3: Wednesday is discount day - everyone gets $2 off
if day == "Wednesday":
    final_price -= 2
    print(" Wednesday special ($2 off)")
else:
    print(" No Wednesday discount. ")
print(f"\nFinal ticket price: ${final_price:.2f}")
# Add a message based on savings
savings = base_price - final_price
if savings > 0:
    print(f"You saved: ${savings:.2f}!")
else:
    print("No discounts applied today.")

### No 3_c (RAN OUT OF TIME)

'''
Practice 4_a
'''
# Practice: Fix all indentation errors
# Each line should be properly indented
score = 85
# Fix this code:
print("Checking your grade...")
if score >= 90:
    print("You got an A!") # FIX: Add indentation
    print("Excellent work!") # FIX: Add indentation
else:
    print("Not an A") # FIX: Should be 4 spaces, not 2
if score >= 80: # FIX: Too much indentation
    print("You got a B!")
    print("Good job!")
# Fix this code:
age = 16
if age >= 16:
    print("You can drive")
if age >= 18:
    print("You can vote") # FIX: Add indentation
else:
    print("Too young to drive") # FIX: Too much indentation
    
'''
Practice 4_b
'''
# Practice: Create a grade and attendance checker
# Use proper indentation for nested conditions
grade = 85
attendance = 85
extra_credit = True
print("=== Student Evaluation ===")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Extra credit: {extra_credit}")
# TODO: Create this structure with proper indentation:
# 1. If grade >= 60 (passing)
# - Print "Passing grade"
# - If attendance >= 80
# * Print "Good attendance"
# * If extra_credit is True
# > Add 5 to grade
# > Print new grade
# - Else (attendance < 80)
# * Print "Attendance needs improvement"
# 2. Else (grade < 60)
# - Print "Failing grade"
# - Print "Must retake course"
# Start your code here:
if grade >= 60:
    print("Passing grade")
else:
    print("Failing grade")
    print("Must retake course")
if attendance >= 80:
    print("Good Attendance")
else:
    print("Attendance needs improvement")
if extra_credit == True:
    grade += 5
    print("Plus 5 Extra Credit Points")
print("\n=== End of Evaluation ===")

### NO 4_c and on (RAN OUT OF TIME)

'''
Practice 5_a
'''
# Practice: Complete the comparisons
# Fill in the correct operator to make each statement True
x = 15
y = 20
z = 15
#Make these True by adding the correct operator
print("=== Make These True ===")
print(f"x __ z = {x == z}") # Should be True (they're equal)
print(f"x __ y = {x < y}") # Should be True (x is less)
print(f"y __ x = {y > x}") # Should be True (y is greater)
print(f"x __ y = {x != y}") # Should be True (they're different)
print(f"x __ 15 = {x >= 15}") # Should be True (x is 15 or more)
print(f"y __ 20 = {y <= 20}") # Should be True (y is 20 or less)
# Now create your own comparisons
my_age = 23 # Set your age
voting_age = 18
driving_age = 16
retirement_age = 65
print("\n=== Age Comparisons ===")
# Write comparisons to check:
can_vote = my_age >= voting_age # Can you vote?
can_drive = my_age >= driving_age # Can you drive?
is_retired = my_age >= retirement_age # Are you retired?
print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is retired: {is_retired}")

'''
Practice 5_b
'''
# Practice: Range validation system
# Use chained comparisons to validate different ranges
# Test values
test_score = 78
body_temp = 98.6
ph_level = 7.2
humidity = 45
print("=== Range Validator ===")
# TODO: Check if values are in valid ranges using chained comparisons
# Test score should be between 0 and 100
if (test_score > 0) and (test_score < 100):
    valid_score = test_score
    print(f" Test score {test_score} is valid")
    if valid_score >= 90: # 90-100
        print(" Grade: A")
    elif valid_score >= 80 and valid_score < 90: # 80-89
        print(" Grade: B")
    elif valid_score >= 70 and valid_score < 80: # 70-79
        print(" Grade: C")
    elif valid_score >= 60 and valid_score < 70: # 60-69
        print(" Grade: D")
    else:
        print(" Grade: F")
else:
    print(f" Invalid test score: {test_score}")
