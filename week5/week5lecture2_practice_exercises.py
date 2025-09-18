import sys
'''
practice exercise 1-a
'''
# TODO: Complete this program
# Ask for age and print the appropriate category
# Child: 0-12
# Teen: 13-17
# Adult: 18-64
# Senior: 65+
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior. ")

'Practice 2 a'
#TODO: Complete this program
# Regular price: $12
# Child (under 12): $8
# Senior (65+): $8
# Tuesday discount: All tickets $6
age = int(input("Enter your age: "))
day = input("What day is it? ").lower()
if day == "tuesday":
   print("It's Tuesday, all tickets $6!")
else:
    print("Come back Tuesday for $6 tickets!")
    if age < 12:
        print("Child ticket costs $8.")
    elif age >= 65:
        print("Senior ticket costs $8.")
    else:
        print("Regular ticket price (NO Senior or Child Discount) $12.")


"Problem 3a"
# TODO: Complete this program
# Correct username: "student"
# Correct password: "learn123"
# Both must be correct to login
username = input("Username: ")
password = input("Password: ")
# Use 'and' to check both conditions
if username == "student" and password == "learn123":
    print("Welcome student!")
else:
    print("Incorrect Login Credentials")

"Problem 4a"
# TODO: Complete this program
# Weekend: Saturday or Sunday
# Holiday: If user says "yes"
# Either weekend OR holiday = day off
day = input("What day is it? ").lower()
is_holiday = input("Is it a holiday? (yes/no): ").lower()
# Use 'or' to check for day off
if (day == "sunday" or day == "saturday") or is_holiday == "yes":
    print("You have the day off!!")
else:
    print("No day off today :(")

"Problem 5a"
# TODO: Complete this program
# Check if input is not empty AND starts with 'A'
# Use short-circuit to prevent error on empty string
user_input = input("Enter a word: ")
# Check safely using short-circuit
# Hint: Check if not empty first, then check first letter
if user_input != "" and user_input[0] == "A":
    print("Input Accepted.")
else:
    print("Input Rejected")