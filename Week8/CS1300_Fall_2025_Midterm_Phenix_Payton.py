## Phenix Payton
## CS1300 Midtrem
## 10/9/25

"""
Problem 1: String Processing
Complete each task below.
"""
# Given information (DO NOT MODIFY):
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"
# Task 1.1 (3 points): Extract and print the first name only
first_name = full_name[0:4]
print(f"First name is: {first_name}")
# Task 1.2 (3 points): Extract and print the last name only
last_name = full_name[-5:]
print(f"Last name is: {last_name}")
# Task 1.3 (3 points): Create and print initials (J.M.S.)
initial1 = full_name[0]
initial2 = full_name[5]
initial3 = full_name[-5]
initials = initial1 + initial2 + initial3
initials = ".".join(initials)
print(initials)
# Task 1.4 (3 points): Check if the email contains "university" (case-insensitive)
is_uni = "university" in email
print(f"Is a university email: {is_uni}")
# Task 1.5 (3 points): Replace all dashes in phone with spaces and print
phone = phone.replace("-", " ")
print(phone)
print("\n")


"""
Problem 2: Restaurant Rating Calculator
Calculate based on percentage rating.
"""
# Task 2.1 (3 points): Get these ratings
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0
# Task 2.2 (4 points): Calculate weighted average
# Weights: atmosphere=10%, food=45%, service=20%, cleanness=25%
# Store result in variable 'average'
total_weighted_rating = (atmosphere * .10) + (food * .45) + (service * .20) + (cleanness * .25)
average = total_weighted_rating / 1.00
# Task 2.3 (8 points): Determine restaurant rating
# Use these ranges:
# *****: 4.0 and above
# ****: 3.0-4.0
# ***: 2.0-3.0
# **: 1.0-2.0
# *: below 1.0
# Print both the average and star rating
print(f"Restaurant rating is: {average}")
if average >= 4.0:
    print("This is a ***** (5-star) Restaurant!!")
elif average >= 3.0:
    print("This is a **** (4-star) Restaurant!")
elif average >= 2.0:
    print("This is a *** (3-star) Restaurant.")
elif average >= 1.0:
    print("This is a ** (2-star) Restaurant.")
else:
    print("This is a * (1-star) Restaurant :(.")
print("\n")


"""
Problem 3: Movie Review Number Management
Manage a list of movie review numbers.
"""
# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.append(4)
print(numbers)
# Task 3.3 (3 points): The third review number (4) was entered wrong.
# Change it to 3
numbers.remove(4)
numbers.insert(2,3)
print(numbers)
# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(1)
print(numbers)
# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(1,3)
print(numbers)
# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
sub_list = numbers[0:3]
print(f"Sublist of first three reviews: {sub_list}")
# Task 3.7 (3 points): Print:
# - How many movie review numbers
# - The first review number
# - The last review number
print(f"There were {len(numbers)} total reviews.")
print(f"First review number: {numbers[0]}")
print(f"Last review number is: {numbers[-1]}")
print("\n")


"""
Problem 4: Shopping Cart System
Build a basic shopping cart with price checking.
"""
# Initial setup (DO NOT MODIFY):
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99] # Matching prices for each item
cart = []
cart_total = 0.0
# Task 4.1 (4 points): Add "milk" to cart
# Check if "milk" is in items, find its index, and add to cart
# Also add its price to cart_total
if "milk" in items:
    index = items.index("milk")
    cart.append(items[index])
    price_item = prices[index]
    print(f"Price of milk is: ${price_item}")
    cart_total += price_item
    print(f"Currently in cart: {cart}")
    print(f"Current total: ${cart_total}")
else:
    print("No milk in stock.")
# Task 4.2 (4 points): Add "eggs" to cart
# Same process as above
if "eggs" in items:
    index = items.index("eggs")
    cart.append(items[index])
    price_item = prices[index]
    print(f"Price of eggs: ${price_item}")
    cart_total += price_item
    print(f"Currently in cart: {cart}")
    print(f"Current total: ${cart_total}")
else:
    print("No eggs in stock.")
# Task 4.3 (4 points): Try to add "cookies" to cart
# Check if it exists first, print appropriate message
if "cookies" in items:
    index = items.index("cookies")
    cart.append(items[index])
    price_item = prices[index]
    print(f"Price of cookies: ${price_item}")
    cart_total += price_item
    print(cart)
    print(cart_total)
else:
    print("No cookies in stock.")
# Task 4.4 (4 points): Apply discount
# If cart_total > 6.00, apply 10% discount
# Print the original total and discounted total
print(f"Your current total is: ${cart_total}")
if cart_total > 6.00:
    print("Cart worth more than $6.00, you get a 10% discount!")
    discount = .10
    total_after_discount = round(cart_total * (1.00 - discount),2)
    print(f"Total after discount: ${total_after_discount}")
# Task 4.5 (4 points): Final report
# Print:
# - Items in cart
# - Number of items
# - Final total (with discount if applicable)
print(f"Items in your cart: {cart}")
print(f"Total number of items in cart: {len(cart)}")
print(f"Your final total: ${total_after_discount}")