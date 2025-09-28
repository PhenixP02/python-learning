### Phenix Payton
### CS1300
### Homework 4
### Due: 9/29/25

"PROBLEM 1"
print("\n")
print("=== Temperature Converter & Weather Advisor ===")
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
if scale == "C":
    print(f"Converting {temp} degrees Celcius to Fahrenheit")
    new_temp = round((temp * (9/5) + 32),2)
    print(f"{temp} * 9/5 + 32 = {new_temp}F")
    if new_temp >= 80:
        print("It is hot outside!")
    elif new_temp >= 65:
        print("it is warm outside.")
    elif new_temp >= 50:
        print("it is cool outside")
    elif new_temp >= 30:
        print("It is chilly outside.")
    else:
        print("It is cold outside!")
elif scale == "F":
    print(f"Converting {temp} degrees Fahrenheit to Celcius")
    new_temp = round((temp - 32) * (5/9),2)
    print(f"({temp} - 32) * (5/9) = {new_temp}C")
    if temp >= 80:
        print("It is hot outside!")
    elif temp >= 65:
        print("It is warm outside.")
    elif temp >= 50:
        print("It is cool outside")
    elif temp >= 30:
        print("It is chilly outside.")
    else:
        print("It is cold outside!")
else:
    print("Scale must be 'C' or 'F' ")
print("\n")



"PROBLEM 2"
print("=== Movie Theater Ticket System ===")
# Get customer information
age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()

price = 15
discount = 0
is_tuesday = False
if day == "tuesday":
    is_tuesday = True
    price = 7
    print(f"Tuesday discount, all tickets ${price}!")
else:
    time = int(input("What hour is showtime (0-23)? "))
    if time < 17:
        discount += 3
        print(f"Matinee discount, ${discount} off!")
    else:
        print("Come back before 5pm (17 in 24-hour) for matinee discount!")
if is_tuesday != True:
    if age >= 65:
        price = 10
        print(f"Senior discount, ticket costs ${price}")
    elif age <= 12:
        price = 8
        print(f"Child discount, ticket costs ${price}")
    else:
        print(f"Regular ticket price: ${price}")
print("\n")
final_price = price - discount
print(f"Applying any discounts (Ticket Price - Discount): ${price} - ${discount} = ${final_price}")
print(f"Final ticket price is: ${final_price}")
print("\n")



"PROBLEM 3"
print("=== Grade Calculator ===")
# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
if test1 < 0 or test1 > 100:
    print("ERROR: Test score out of range (Must be 0-100)")
    exit()
test2 = float(input("Enter Test 2 score (0-100): "))
if test2 < 0 or test2 > 100:
    print("ERROR: Test score out of range (Must be 0-100)")
    exit()
test3 = float(input("Enter Test 3 score (0-100): "))
if test3 < 0 or test3 > 100:
    print("ERROR: Test score out of range (Must be 0-100)")
    exit()

# Grade Calculation
avg_score = round((test1 + test2 + test3)/3,2)
print(f"Average test score is: {avg_score}")
if avg_score >= 90:
    grade = "A"
    print("Great job you have an A!")
elif avg_score >= 80:
    grade = "B"
    print("Good job you have a B!")
elif avg_score >= 70:
    grade = "C"
    print("You have a C.")
elif avg_score >= 60:
    grade = "D"
    print("You have a D.")
else:
    grade = "F"
    print("You have an F :(.")

# Passing Criteria
criteria1 = grade == "A" or grade == "B" or grade == "C" or grade == "D"
criteria2 = test1 >= 60 or test2 >= 60 or test3 >= 60
is_passing = criteria1 == True and criteria2 == True
if is_passing == True:
    print("You have a passing grade and a test score over 60.")
    print("Congratulations, you passed the class!")
else:
    print("You need atleast a D and one test score over 60 to pass.")
    print("You did not pass the class.")
print("\n")



"PROBLEM 4"
print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
common_pass = ["password","qwerty","12345678"]
# Initialize criteria counters
criteria_met = 0

# Criteria Checks
is_length = len(password) > 6
is_common = password not in common_pass
is_up = any(char.isupper() for char in password)
is_low = any(char.islower() for char in password)
is_num = any(char.isdigit() for char in password)

# Criteria Met Calculation
if is_length == True:
    criteria_met += 1
if is_common == True:
    criteria_met += 1
if is_up == True:
    criteria_met += 1
if is_low == True:
    criteria_met += 1
if is_num == True:
    criteria_met += 1

# Password Strength Status
if criteria_met == 5:
    strength = "Excellent"
elif criteria_met == 4:
    strength = "Good"
elif criteria_met == 3:
    strength = "Weak"
else:
    strength = "BAD"
print(f"Password Strength: {strength}")
print(f"Criteria met: {criteria_met}/5")

# Feedback
print("Issues to Improve:")
if is_length == False:
    print("Password should be atleast 8 characters long.")
if is_common == False:
    print("Password should not be common (NO 'qwerty', '12345678', 'password').")
if is_up == False:
    print("Password should contain atleast one upper case letter.")
if is_low == False:
    print("Password should contain atleast one lower case letter.")
if is_num == False:
    print("Password should contain atleast one number.")