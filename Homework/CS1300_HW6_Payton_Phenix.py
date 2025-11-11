
"""
CS 1300 - Homework #6
Name: Phenix Payton
Date: 11/10/25
Description: Introduction to Lists
"""

# Part 1: List Creation Basics
print("="*50)
print("PART 1: LIST CREATION")
print("="*50)
# Example shown for you:
# Create a list of three colors
example_colors = ["red", "blue", "green"]
print("Example:", example_colors)
# Now you try:
# 1. Create a list called 'my_classes' with 4 class names (like "English", "Math",etc.)
my_classes = ["English", "Math", "Science", "Computer"]
print(my_classes)
# 2. Create a list called 'my_grades' with 5 test scores (use any numbers between60-100)
my_grades = [90, 85, 92, 89, 87]
print(my_grades)
# 3. Create an empty list called 'my_notes'
my_notes = []
print(my_notes)
# 4. Print all three of your lists


# Lists can hold different types of data!
# 1. Create a list called 'about_me' with:
# - Your first name (string)
# - Your age (integer)
# - Your height in feet (decimal number like 5.5)
# - Whether you like pizza (True or False)
about_me = ["Phenix", 23, 5.92, True]
print(about_me)
# 2. Create a list called 'mixed_bag' with:
# - The number 42
# - The word "Hello"
# - The value 3.14
# - Another list containing [1, 2, 3]
mixed_bag = [42, "Hello", 3.14, [1, 2, 3]]
print(mixed_bag)
# 3. Print both lists


# Method 1: Create a list of 10 zeros using multiplication
# Hint: [0] * 10 creates [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0] * 10
print(zeros)
# Method 2: Convert a string to a list of characters
# Convert "HELLO" to ['H', 'E', 'L', 'L', 'O']
my_string = "HELLO"
letters = list(my_string)
print(letters)
# Method 3: Create a list that repeats [1, 2] three times
# Result should be [1, 2, 1, 2, 1, 2]
pattern = [1, 2] * 3
print(pattern)
# Print all three lists

# Part 2: Accessing List Elements
print("="*50)
print("PART 2: Accessing List Elements")
print("="*50)
# Given this list of months:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Access and print these elements:
print("The list:", months)
print("List length:", len(months))
# 1. Print the first month (remember: first element is at index 0)
print(months[0])
# 2. Print the sixth month (careful with the index!)
print(months[5])
# 3. Print the last month using positive index (hint: use len() - 1)
print(months[len(months)-1])
# 4. Print the last month using negative index (hint: -1)
print(months[-1])
# 5. Print December using its positive index
print(months[11])
# 6. Print January using a negative index
print(months[-12])
# 7. Print the month at index 7
print(months[7])

# You're tracking daily temperatures for a week
temperatures = [72, 75, 71, 73, 74, 76, 70] # Sunday through Saturday
print("Original temperatures:", temperatures)
# 1. Monday's temperature was recorded wrong. Change index 1 to 77
temperatures[1] = 77
# 2. Friday's temperature should be 78 (which index is Friday?)
temperatures[5] = 78
# 3. Change Sunday (first day) to 74
temperatures[0] = 74
# 4. Change Saturday (last day) to 72 using negative index
temperatures[-1] = 72
# 5. Wednesday (middle of week) should be 75
temperatures[len(temperatures) // 2] = 75
print("Corrected temperatures:", temperatures)
# 6. Calculate and print: how many days are in your list?
print(f"List length: {len(temperatures)}")
# 7. What's the index of the last day? (print it)
print(f"Index of last day: {len(temperatures) - 1}")


# Given this small list:
colors = ["red", "blue", "green"]
# 1. Check if index 1 exists before accessing it
if 1 < len(colors):
    print("Color at index 1:", colors[1])
else:
    print("Index 1 doesn't exist")
# 2. Now you try: Check if index 5 exists before trying to access it
if 5 < len(colors):
    print(f"Color at index 5: {colors[5]}")
else:
    print("Index 5 doesn't exist")
# 3. Check if the list is empty before accessing the first element
if 0 < len(colors):
    print(f"First element is: {colors[0]}")
else:
    print("list is empty")
# 4. Safely access the last element (check if list has at least 1 item first)
if 0 < len(colors):
    print(f"Last element is: {colors[-1]}")
else:
    print("list is empty")
# 5. Try to print the element at index -4 (but check if it's valid first)
if 3 < len(colors):
    print(f"Element at index -4: {colors[-4]}")
else:
    print("Index -4 doesn't exist")
# Hint: negative indices from -len(list) to -1 are valid
# 6. What's the smallest valid negative index for this list? Print it.
print(f"Smallest valid negative index: {-len(colors)}")


# Part 3: List Slicing
print("="*50)
print("PART 3: List Slicing")
print("="*50)
# Slicing lets us get multiple elements at once!
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", numbers)
print("Remember: list[start:end] gives elements from start up to (but notincluding) end")
# Example:
print("Example - numbers[0:3]:", numbers[0:3]) # Gets indices 0, 1, 2
# Now you try:
# 1. Get the first 4 numbers
print(f"First 4 numbers: {numbers[0:4]}")
# 2. Get the last 3 numbers (use negative indices)
print(f"Last 3 numbers: {numbers[-3:]}")
# 3. Get numbers from index 2 to index 6 (30, 40, 50, 60)
print(f"Index 2 to Index 6: {numbers[2:6]}")
# 4. Get all numbers from index 5 to the end
print(f"Index 5 to the end: {numbers[5:]}")
# 5. Get all numbers from start up to index 4
print(f"Start to index 4: {numbers[:5]}")
# 6. Make a complete copy of the list using [:]
print(f"Copy of list: {numbers[:]}")
# 7. Get an empty slice (like numbers[3:3]) and see what happens
print(f"Empty slice: {numbers[3:3]}")


# We can use a step value: list[start:end:step]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print("Alphabet:", alphabet)
# Example:
print("Every other letter:", alphabet[::2]) # Start to end, step by 2
# Now you try:
# 1. Get every third letter starting from 'a' (indices 0, 3, 6, 9, 12)
print(f"Every third from 'a': {alphabet[::3]}")
# 2. Get every other letter starting from 'b' (indices 1, 3, 5, 7, ...)
print(f"Every Other from 'b': {alphabet[1::2]}")
# 3. Reverse the entire list using slicing (hint: use step of -1)
print(f"List reversed: {alphabet[::-1]}")
# 4. Get the first half of the alphabet
print(f"First half: {alphabet[:len(alphabet) // 2]}")
# Hint: Calculate middle index using len() // 2
# 5. Get the second half of the alphabet
print(f"Second half: {alphabet[len(alphabet) // 2:]}")
# 6. Get letters from index 2 to 8, but only every other one
print(f"Every other letter, index 2 to 8: {alphabet[2:9:2]}")
# 7. Reverse just the first 5 letters (get them, then reverse)
first_five = alphabet[0:5]
print(f"First 5 reversed: {first_five[::-1]}")


# You have hourly temperature readings for a day (24 hours)
hourly_temps = [55, 54, 53, 52, 52, 54, 58, 62, 66, 70, 73, 75, 76, 77, 77, 76, 74, 71, 68, 65, 62, 59, 57, 55]
print(f"24-hour temperature data ({len(hourly_temps)} readings)")
# 1. Get morning temperatures (first 6 hours, 12am-5am)
print(f"Temps first 6 hours (12am - 5am): {hourly_temps[0:6]}")
# 2. Get afternoon temperatures (12pm-5pm, which is indices 12-17)
print(f"Afternoon temps (12pm - 5pm): {hourly_temps[12:18]}")
# 3. Get evening temperatures (last 6 hours, 6pm-11pm)
print(f"Evening temps (6pm-11pm): {hourly_temps[18:24]}")
# 4. Get every other hour's temperature for the whole day
print(f"Every other hour temp: {hourly_temps[::2]}")
# 5. Get the middle 4 hours of the day (hours 10-13, so indices 10-14)
print(f"Middle 4 hours (10am - 1pm): {hourly_temps[10:14]}")
# 6. What were the temperatures for hours 6-9am? (indices 6-9)
print(f"Temp hours 6-9am: {hourly_temps[6:10]}")


# Part 4: List Methods - Adding Items
print("="*50)
print("PART 4: List Methods - Adding Items")
print("="*50)
# append() adds ONE item to the end of a list
shopping_list = []
print("Starting with empty list:", shopping_list)
# Add these items one at a time using append():
# 1. Add "milk"
shopping_list.append("milk")
# 2. Add "bread"
shopping_list.append("bread")
# 3. Add "eggs"
shopping_list.append("eggs")
# 4. Add "cheese"
shopping_list.append("cheese")
# 5. Add "apples"
shopping_list.append("apples")
print("Final shopping list:", shopping_list)
# 6. What happens if you try to append two items at once?
#shopping_list.append("butter", "yogurt")
# Comment out the line after you see the error!
# 7. Create a list with your 3 favorite foods using append()
favorites = []
# Add your three favorites here
favorites.append("Burger")
favorites.append("Tamale")
favorites.append("Teriyaki Chicken")
print("My favorites:", favorites)


# insert() adds an item at a specific position
line = ["Alice", "Bob", "Charlie"]
print("Original line:", line)
# 1. David cuts to the front! Insert "David" at index 0
line.insert(0, "David")
print("After David cuts:", line)
# 2. Eve joins between Alice and Bob (what index?)
line.insert(2, "Eve")
print("After Eve joins:", line)
# 3. Frank joins at the end (what index? Use len())
line.insert(len(line), "Frank")
print("Final line:", line)
# Now create a schedule:
schedule = ["Math", "History", "Science"]
print("\nOriginal schedule:", schedule)
# 4. Add "Lunch" between History and Science
schedule.insert(2, "Lunch")
# 5. Add "Homeroom" at the beginning
schedule.insert(0, "Homeroom")
print("Updated schedule:", schedule)


# extend() adds ALL items from another list
primary_colors = ["red", "blue", "yellow"]
print("Primary colors:", primary_colors)
# 1. Create a list of secondary colors
secondary_colors = ["green", "orange", "purple"]
# 2. Add all secondary colors to primary_colors using extend()
primary_colors.extend(secondary_colors)
print("All colors:", primary_colors)
# Compare append vs extend:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# 3. Append [4, 5] to list1 (this adds the list as one item!)
list1.append([4, 5])
print("After append([4, 5]):", list1)
# 4. Extend list2 with [4, 5] (this adds each item separately)
list2.extend([4, 5])
print("After extend([4, 5]):", list2)
# 5. Create your own example showing the difference
my_list = ["a", "b"]
# Try both append and extend with ["c", "d"] and print results
my_list.append(["c", "d"])
print(my_list)
my_list = ["a", "b"]
my_list.extend(["c", "d"])
print(my_list)


# Part 5: List Methods - Removing Items
print("="*50)
print("PART 5: List Methods - Removing Items")
print("="*50)
# remove() deletes the FIRST occurrence of a value
pets = ["dog", "cat", "bird", "cat", "fish", "cat"]
print("Original pets:", pets)
# 1. Remove "bird"
pets.remove("bird")
print("After removing bird:", pets)
# 2. Remove "cat" (notice it only removes the first one!)
pets.remove("cat")
print("After removing one cat:", pets)
# 3. Check if "hamster" is in the list before trying to remove it
if "hamster" in pets:
    pets.remove("hamster")
else:
    print("hamster not found in list")
# 4. Create a list with duplicate values
numbers = [5, 3, 8, 3, 9, 3, 2]
print("\nNumbers:", numbers)
# 5. Remove all 3's (one at a time, checking each time)
if 3 in numbers:
    numbers.remove(3)
    print("Removed first 3:", numbers)
# Remove the remaining 3's (you'll need more if statements)
if 3 in numbers:
    numbers.remove(3)
    print("Removed second 3:", numbers)
if 3 in numbers:
    numbers.remove(3)
    print("Removed third 3:", numbers)
    

# pop() removes AND RETURNS an item by index
stack = [10, 20, 30, 40, 50]
print("Original stack:", stack)
# 1. Remove and save the last item
last_item = stack.pop(-1)
print(f"Popped {last_item}, stack is now: {stack}")
# 2. Remove and save the first item (index 0)
first_item = stack.pop(0)
print(f"Popped {first_item}, stack is now: {stack}")
# 3. Remove the item at index 1
stack.pop(1)
print("Current stack:", stack)
# Working with a queue:
queue = ["Person1", "Person2", "Person3", "Person4"]
print("\nQueue:", queue)
# 4. Serve (remove) the first person in line and print who was served
first_served = queue.pop(0)
print(f"First person served was: {first_served}")
# 5. The last person gives up and leaves (remove but don't save)
queue.pop(-1)
print("Remaining queue:", queue)


# del can remove items by index or slice
data = [100, 200, 300, 400, 500, 600, 700]
print("Original data:", data)
# 1. Delete the first element using del
del data[0]
print("After deleting first:", data)
# 2. Delete the element at index 2
del data[2]
print("After deleting index 2:", data)
# 3. Delete a slice from index 1 to 3 (not including 3)
del data[1:3]
print("After deleting slice:", data)
# Working with unwanted data:
readings = [0, 5, -999, 10, 15, -999, 20] # -999 represents bad data
print("\nReadings with errors:", readings)
# 4. Find and remove the first -999 using remove()
readings.remove(-999)
# 5. Check if there are more -999 values and remove them
if -999 in readings:
    readings.remove(-999)
else:
    print("All bad readings removed")
if -999 in readings:
    readings.remove(-999)
else:
    print("All bad readings removed")
print("Clean readings:", readings)


# Part 6: Membership and Length Operations
print("="*50)
print("PART 6: Membership and Length Operations")
print("="*50)
# Check if items are in a list
valid_grades = ['A', 'B', 'C', 'D', 'F']
print("Valid grades:", valid_grades)
# 1. Check if 'B' is a valid grade
if "B" in valid_grades:
    print("B is a valid grade")
else:
    print("B is not a valid grade")
# 2. Check if 'E' is NOT a valid grade
if "E" in valid_grades:
    print("E is a valid grade")
else:
    print("E is not a valid grade")
# 3. Ask user for a grade and check if it's valid
user_grade = 'C' # Pretend user entered this
# Check if user_grade is in valid_grades
if user_grade in valid_grades:
    print(f"{user_grade} is a valid grade")
else:
    print(f"{user_grade} is not a valid grade")
# Working with a menu:
menu_options = [1, 2, 3, 4, 5]
print("\nMenu options:", menu_options)
# 4. Check if option 3 is available
if 3 in menu_options:
    print("Option 3 is available")
else:
    print("Option 3 is not available")
# 5. Check if option 9 is NOT available
if 9 not in menu_options:
    print("Option 9 is not available")
else:
    print("Option 9 is available")
# Student roster:
enrolled = ["Alice", "Bob", "Charlie", "Diana"]
print("\nEnrolled students:", enrolled)
# 6. Check if "Eve" needs to be added (not in list)
if "Eve" not in enrolled:
    print("Eve is not enrolled")
else:
    print("Eve is already enrolled")
# 7. Only add "Frank" if not already enrolled
if "Frank" not in enrolled:
    print("Enrolling Frank")
    enrolled.append("Frank")
    print(f"Updated enrollement list: {enrolled}")
else:
    print("Frank is already enrolled")
# 8. Create a list of students to check
to_check = ["Alice", "Eve", "Bob", "George"]
# For each student, print whether they're enrolled or not
if to_check[0] in enrolled:
    print(f"{to_check[0]} is enrolled")
else:
    print(f"{to_check[0]} is not enrolled")
if to_check[1] in enrolled:
    print(f"{to_check[1]} is enrolled")
else:
    print(f"{to_check[1]} is not enrolled")
if to_check[2] in enrolled:
    print(f"{to_check[2]} is enrolled")
else:
    print(f"{to_check[2]} is not enrolled")
if to_check[3] in enrolled:
    print(f"{to_check[3]} is enrolled")
else:
    print(f"{to_check[3]} is not enrolled")
# (Do this without loops - check each one individually)


# len() tells us how many items are in a list
tasks = ["homework", "dishes", "laundry", "shopping", "exercise"]
print("Tasks:", tasks)
# 1. How many tasks are there?
print(f"There are {len(tasks)} tasks on the list")
# 2. What's the index of the last task? (remember: len() - 1)
print(f"The index of the last task is: {len(tasks) - 1}")
# 3. Check if list has more than 3 tasks
if 3 < len(tasks):
    print("List has more than 3 tasks on it")
else:
    print("List has 3 or less tasks on it")
# 4. Calculate the middle index
mid_index = len(tasks) // 2
print(f"Middle index is: {mid_index}")
# 5. Access the middle task safely
print(f"Middle task is: {tasks[mid_index]}")
# Empty list checks:
inbox = []
print("\nInbox:", inbox)
# 6. Check if inbox is empty (two ways)
# Way 1: Check if len() == 0
if len(inbox) == 0:
    print("Inbox is empty (WAY 1)")
# Way 2: Empty lists are "falsy"
if bool(inbox) == False:
    print("Inbox is empty (WAY 2)")
if not inbox:
    print("Inbox is empty (using 'not inbox')")
# 7. Create a waiting list with max capacity of 4
waiting = ["P1", "P2"]
max_capacity = 4
print(f"\nWaiting list ({len(waiting)}/{max_capacity}):", waiting)
# How many more can join?
spaces_available = max_capacity - len(waiting)
print(f"Spaces available: {spaces_available}")
# Add two more if there's room
if len(waiting) < max_capacity:
    waiting.append("P3")
if len(waiting) < max_capacity:
    waiting.append("P4")
print(f"Updated waiting list ({len(waiting)}/{max_capacity}):", waiting)
print()


# BONUS: Simple Inventory System
print("="*50)
print("BONUS: Simple Inventory System")
print("="*50)
# Starting inventory
inventory = ["apples", "bananas", "milk", "bread", "eggs"]
quantities = [10, 15, 5, 8, 24] # Matching quantities for each item
print("=== Store Inventory System ===")
print("Items:", inventory)
print("Quantities:", quantities)
print()
# Task 1: Display the inventory nicely
# Print each item with its quantity (use indexing, not loops)
print("Current Inventory:")
# Print first item and quantity
print(f"First item is {inventory[0]} and there are {quantities[0]} left")
# Print second item and quantity
print(f"Second item is {inventory[1]} and there are {quantities[1]} left")
# ... continue for all items
print(f"Third item is {inventory[2]} and there are {quantities[2]} left")
print(f"Fourth item is {inventory[3]} and there are {quantities[3]} left")
print(f"Fifth item is {inventory[4]} and there are {quantities[4]} left")
# Task 2: A customer buys 3 apples
# Find apples (index 0) and reduce quantity by 3
quantities[0] -= 3
print(f"There are now {quantities[0]} apples left")
# Task 3: Restock milk
# Milk is at index 2, add 10 more
quantities[2] += 10
print(f"There are now {quantities[2]} milks left")
# Task 4: Add a new item
# Add "cheese" to inventory with quantity 12
inventory.append("cheese")
quantities.append(12)
print(f"Cheese added to inventory: {inventory}")
print(f"Cheese quantity added: {quantities}")
# Task 5: Remove items with 0 quantity
# If any quantity is 0 or less, remove both the item and quantity
# (Check each one individually since we can't use loops)
if quantities[0] <= 0:
    inventory.pop(0)
    quantities.pop(0)
    print("Apples removed")
if quantities[1] <= 0:
    inventory.pop(1)
    quantities.pop(1)
    print("Bananas removed")
if quantities[2] <= 0:
    inventory.pop(2)
    quantities.pop(2)
    print("Milk removed")
if quantities[3] <= 0:
    inventory.pop(3)
    quantities.pop(3)
    print("Bread removed")
if quantities[4] <= 0:
    inventory.pop(4)
    quantities.pop(4)
    print("Eggs removed")
if quantities[5] <= 0:
    inventory.pop(5)
    quantities.pop(5)
    print("Cheese removed")
# Task 6: Report
# Print total number of different items (use len())
print(f"Total number of different items: {len(inventory)}")
# Print items that need restocking (quantity < 5)
# Check each item individually
if quantities[0] < 5:
    print(f"{inventory[0]} needs restocked")
if quantities[1] < 5:
    print(f"{inventory[1]} needs restocked")
if quantities[2] < 5:
    print(f"{inventory[2]} needs restocked")
if quantities[3] < 5:
    print(f"{inventory[3]} needs restocked")
if quantities[4] < 5:
    print(f"{inventory[4]} needs restocked")
if quantities[5] < 5:
    print(f"{inventory[5]} needs restocked")
print("\nFinal Inventory:")
# Print the updated inventory and quantities
print(inventory)
print(quantities)