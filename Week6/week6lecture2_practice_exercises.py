

    




### 9/25/25
### Phenix and Evan
### Week 6 Lecture 2 Practice Exercises

'''
Practice 1-a
'''
# TODO: Create a store system with these features:
# 1. Display a menu of 5 items with prices
# 2. Let user select one item
# 3. Ask for quantity
# 4. Apply discounts:
# - 10+ items: 10% off
# - Member: additional 5% off
# 5. Calculate tax (8%)
# 6. Show final receipt
print("=== CORNER STORE ===")
# Your code here
print("1.Milk  2.Apple  3.Bread  4.Banana  5. Cereal")
choice = input("\nSelect an item (1-5): ").strip()
# Validate choice first
valid_choices = [ "1", "2", "3", "4", "5"]
price = 0
quantity = 0
milk_price = 2.50
apple_price = 1
bread_price = 2
banana_price = .25
cereal_price = 3
if choice not in valid_choices:
    print("Invalid Choice!")
elif choice == "1":
    quantity = int(input("How many gallons milk?"))
    price = quantity * milk_price
elif choice == "2":
    quantity = int(input("How many apples?"))
    price = quantity * apple_price
elif choice == "3":
    quantity = int(input("How many loaves of bread?"))
    price = quantity * bread_price
elif choice == "4":
    quantity = int(input("How many bananas?"))
    price = quantity * banana_price
elif choice == "5":
    quantity = int(input("How many boxes of cereal?"))
    price = quantity * cereal_price
print(f"Total before disocunt and tax: ${price}\n")
discount = 0
tax = 1.08


is_member = input("Are you a member?").strip()
if is_member == "yes":
    discount += .05
    print("You get member discount!")
else:
    print("Become a member to save money!")
if quantity >= 10:
    discount += .1
    print("Discount for 10+ items!")
else:
    print("Buy 10+ items for discount.")
sub_total = price * tax
print(f"Total before discount: {sub_total}")
total = sub_total * (1.00 - discount)
total = round(total,2)
print(f"Your total with discount is: {total}")




"Practice 2-a"
# TODO: Create a contact form with validation for:
# 1. Name (required, 2-50 chars)
# 2. Email (must contain @ and .)
# 3. Subject (required, max 100 chars)
# 4. Message (required, 10-500 chars)
# 5. Show all errors at once with helpful messages
print("=== CONTACT FORM ===")

name = input("What is your name? ")
if len(name) < 2:
    print("Invalid name (Too long/Too short)")
else:
    print(f"Thank you {name}")

email = input("What is your email? ").strip().lower()
email_valid = True
if email == "":
    print("Email cannot be blank!")
    email_valid = False
elif " " in email:
    print("Email cannot contain spaces")
    email_valid = False
elif email.count("@") != 1:
    print("Email must contain exactly one @ symbol")
    email_valid = False
elif email.count(".") < 1:
    print("Email must contain atleast one '.' ")
    email_valid = False
if email_valid == True:
    print(f"Your name is {name} and your email address is {email}.")



"Practice 3a"
from math import ceil
# TODO: Create a savings calculator that:
# 1. Asks for current savings
# 2. Asks for savings goal
# 3. Asks for monthly contribution
# 4. Calculates months to reach goal
# 5. Provides encouragement based on progress
# 6. Suggests ways to reach goal faster
print("=== SAVINGS GOAL TRACKER ===")
current_savings = float(input("How much savings do you currently have? "))
goal_savings = float(input("How much money would you like in your savings? "))
monthly_cash = float(input("How much can you contribute to your savings every month? "))

goal_diff = goal_savings - current_savings
print(goal_diff, goal_savings, monthly_cash)
print(f"You are ${goal_diff} away from your goal.")
months_away = (goal_diff / monthly_cash)
print(f"You are {months_away} months from your goal.")