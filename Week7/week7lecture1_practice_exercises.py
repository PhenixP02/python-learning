
## Phenix Payton
## 9/29/25
## Week 7 Lecture 1 Practice Exercises


"Exercise 1a"
# Create a list called 'colors' with three color names
# Your code here:
# Create a list called 'numbers' with the values 10, 20, 30
# Your code here:
# Print both lists
colors = ["blue", "yellow", "red"]
numbers = [10, 20, 30]
print(colors, numbers)
print("\n")


"Exercise 1b"
# Create a list called 'my_info' that contains:
# - Your name (string)
# - Your age (integer)
# - Your height in feet (float)
# - Whether you like pizza (boolean)
# Your code here:
# Print the entire list
# Print the type of the list itself
my_info = ["Phenix", 23, 5.92, True]
print(my_info)
print("Mixed List")
print("\n")


"Exercise 1c"
# Given this list:
inventory = ["pen", "pencil", "eraser", "ruler", "notebook"]
# Without using loops (not covered yet):
# 1. Print how many items are in inventory
# 2. Check if "pencil" is in the list (print True/False)
# 3. Create a new list with the first and last items only
# Hint: Use len(), in operator, and indexing
print(len(inventory))
print("pencil" in inventory)
new_list = [inventory[0], inventory[-1]]
print(new_list)
print("\n")


"Exercise 2a"
# For each variable, predict if it's mutable or immutable:
a = 42 # Mutable or Immutable? immutable
print("a")
print(id(a))
a += 1
print(id(a))
b = "Python" # Mutable or Immutable? immutable
print("b")
print(id(b))
b += " Coding"
print(id(b))
c = [1, 2, 3] # Mutable or Immutable? mutable
print("c")
print(id(c))
c[0] = 99
print(id(c))
d = 3.14 # Mutable or Immutable? immutable
print("d")
print(id(d))
d += 1.01
print(id(d))
e = True # Mutable or Immutable? immutable
print("e")
print(id(e))
e = False
print(id(e))
print("\n")


"Exercise 2b"
# Create a string variable called 'greeting' with value "Good"
# Try to add " Morning" to it two ways:
# 1. Using + (creating new string)
# 2. Try to modify the first character to 'F' (will fail)
# Create a list called 'temps' with values [72, 75, 78]
# 1. Change the first element to 70
# 2. Print to verify it changed
greeting = "Good"
greeting += " Morning"
print(greeting)
## greeting[0] = "F" ERRORS
temps = [72, 75, 78]
print(temps)
temps[0] = 70
print(temps)
print("\n")


"Exercise 3a"
# Create these lists:
# 1. An empty list called 'tasks'
# 2. A list of three pets: "dog", "cat", "fish"
# 3. A list of temperatures: 72.5, 68.0, 75.3
# 4. Print all three lists
tasks = []
pets = ["cat", "dog", "fish"]
temperatures = [72.5, 68.0, 75.3]
print(tasks, pets, temperatures)
print("\n")


"Exercise 3b"
# Create these lists:
# 1. Use list() to convert the string "HELLO" to a list
# 2. Create a list of five 7's using repetition
# 3. Create a list mixing your name, age, and favorite color
# 4. Create a 2x2 nested list representing a tic-tac-toe board
from_string = list("HELLO")
print(from_string)
sevens = [7] * 5
print(sevens)
nested_list = [["X", "O"],
               ["O", "X"]]
print(nested_list)
print(nested_list[0])
print(nested_list[1])


"Exercise 3c"
even_numbers = list(range(0, 11, 2))
print(even_numbers)
print("\n") # Did not finish


"Exercise 4a"
# Given this list:
animals = ["cat", "dog", "bird", "fish", "hamster"]
# Using indexing, print:
# 1. The first animal
# 2. The last animal
# 3. The middle animal (bird)
# 4. Change "dog" to "puppy" and print the list
print(animals[0])
print(animals[4])
print(animals[2])
animals[1] = "puppy"
print(animals)
print("\n")


"Exercise 4b"
# Given this list:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# Using ONLY negative indices:
# 1. Print the last month
print(months[-1])
# 2. Print the first month
print(months[-6])
# 3. Change the second-to-last month to "MAY"
months[-2] = "MAY"
print(months)
# 4. Print the third-from-last month
print(months[-3])
print("\n")


"Exercise 4c"
# Given these lists:
list1 = [10, 20, 30, 40, 50]
list2 = []
list3 = [100]
# Write code to:
# 1. Safely print the first element of each list (handle empty)
# 2. Safely change the last element to 999 (if it exists)
# 3. Swap first and last elements of list1
# 4. Calculate the middle index of list1 and print that element
if len(list1) > 0:
    print(f"First item of list 1: {list1[0]}")
    list1[-1] = 999
else:
    print("List 1 is empty")
if len(list2) > 0:
    print(f"First item of list 2: {list2[0]}")
    list2[-1] = 999
else:
    print("List 2 is empty")
if len(list3) > 0:
    print(f"First item of list 3: {list3[0]}")
    list3[-1] = 999
else:
    print("List 3 is empty")
print(list1) #Before index position swap
list1[0], list1[-1] = list1[-1], list1[0] 
print(list1) #After index position swap

list1_mid_index = len(list1)//2 #Calculating middle index
print(list1[list1_mid_index])
print("\n")


"Exercise 5a"
# Given this list:
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Use slicing to get:
# 1. First three numbers
print(f"First three numbers: {numbers[0:3]}")
# 2. Last three numbers
print(f"Last three numbers: {numbers[-3:]}")
# 3. Middle three numbers (40, 50, 60)
print(f"Middle three numbers: {numbers[3:6]}")
# 4. A complete copy of the list
print(f"Full list: {numbers}")
print("\n")


"Exercise 5b"
# Given this list:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# Use slicing to:
# 1. Get every other letter starting from 'a'
print(alphabet[::2])
# 2. Get every other letter starting from 'b'
print(alphabet[1::2])
# 3. Reverse the entire list
print(alphabet[::-1])
# 4. Get the middle half (roughly)
print(alphabet[3:7])