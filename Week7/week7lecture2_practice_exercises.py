
# Pheinx Payton 
# Week 7 Lecture 2 Practice Exercises
# 10/2/25


"Practice 1a"
# Create an empty list called 'colors'
# Use append() to add:
# - "red"
# - "blue"
# - "green"
# Print the list after each append
colors = []
colors.append("red")
print(colors)
colors.append("blue")
print(colors)
colors.append("green")
print(colors)
print("\n")


"Practice 1b"
# Start with this list:
numbers = [10, 30, 40]
# Use insert() to:
# 1. Add 20 between 10 and 30
# 2. Add 5 at the beginning
# 3. Add 50 at the end
# Print after each insertion
# Final result should be: [5, 10, 20, 30, 40, 50]
numbers.insert(1, 20)
print(numbers)
numbers.insert(0, 5)
print(numbers)
numbers.insert(len(numbers), 50)
print(numbers)
print("\n")


"Practice 1c"
# Start with:
sorted_list = [15, 25, 35, 45]
# You need to add 30 to keep the list sorted
# 1. Find the correct position (without loops)
# 2. Use insert() to add 30 at that position
# 3. Try adding 10 to the beginning
# 4. Try adding 50 to the end
# Keep list sorted throughout
new_val = 30
index = 0 
for i in range(len(sorted_list)):
    if sorted_list[i] >= new_val:
        break
    index += 1
sorted_list.insert(index, new_val)
new_val = 10 
#if sorted_list == [] | new_val <= sorted_list[0]:
#    sorted_list.insert(0, new_val)
#else:
#    print(f"Error--{new_val} is bigger than {sorted_list[0]}")
new_val = 50
if new_val >= sorted_list[-1]:
    sorted_list.insert(len(sorted_list), new_val)
else:
    print(f"Error--{new_val} is smaller than {sorted_list[-1]}")
print("\n")


# Extend vs Append
# list1 = [1, 2]
# list1.append([3, 4]) # Result: [1, 2, [3, 4]] - adds list as ONE item
# list2 = [1, 2]
# list2.extend([3, 4]) # Result: [1, 2, 3, 4] - adds EACH item


"Practice 2a"
# Start with:
fruits = ["apple", "banana"]
# Use extend() to add:
# - ["orange", "grape"]
# Print the result
fruits.extend(["orange", "grape"])
print(fruits)
# Now create a new list 'numbers' with [1, 2]
numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)
print("\n")
# Use extend to add [3, 4, 5]
# Print the result


"Practeice 2b"
# Predict the output, then test:
# Case 1:
list1 = [1, 2]
list1.append([3, 4])
# What is list1 now? list1 = [1, 2, [3, 4]]
# Case 2:
list2 = [1, 2]
list2.extend([3, 4])
# What is list2 now? list2 = [1, 2, 3, 4]
# Case 3:
list3 = ['a']
list3.extend('bc')
# What is list3 now? list3 = ['a', 'bc']
print(list1)
print(list2)
print(list3)
print("\n")


"Practice 3a"
# Start with:
animals = ["cat", "dog", "bird", "dog", "fish"]
# 1. Use remove() to remove "bird"
animals.remove("bird")
print(animals)
# 2. Use pop() to remove the last animal
animals.pop()
print(animals)
# 3. Use del to remove the first animal
del animals[0]
print(animals)
print("\n")
# Print after each operation


"Practice 3b"
# Start with:
queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Perform these operations:
# 1. David left the queue (remove by value)
queue.remove("David")
# 2. Serve the first person (remove and print who was served)
removed_item = queue.pop(0)
print(removed_item)
# 3. The last person gave up and left (just remove them)
del queue[-1]
# Choose the appropriate method for each
print(queue)
print("\n")


"Practice 4a"
# Given:
colors = ["red", "blue", "green", "yellow"]
# Check and print whether:
# 1. "blue" is in the list
color_check = "blue"
if color_check in colors:
    print(f"{color_check} is in the list.")
else:
    print(f"{color_check} is not in the list.")
# 2. "purple" is in the list
color_check = "purple"
if color_check in colors:
    print(f"{color_check} is in the list.")
else:
    print(f"{color_check} is not in the list.")
# 3. "RED" is in the list (note the case!)
color_check = "RED"
if color_check in colors:
    print(f"{color_check} is in the list.")
else:
    print(f"{color_check} is not in the list.")
# 4. "black" is not in the list
color_check = "black"
if color_check not in colors:
    print(f"{color_check} is not in the list.")
else:
    print(f"{color_check} is in the list.")
print("\n")


"Practice 4b"
# Given:
inventory = ["hammer", "nails", "screwdriver", "wrench"]
tool = "hammer"
# Write code to:
# 1. Check if tool is in inventory
# 2. If not, add it and print "Added [tool]"
# 3. If yes, print "[tool] already in inventory"
# Then try with tool = "hammer"
if tool in inventory:
    print(f"{tool} is already in inventory.")
else:
    inventory.append(tool)
    print(f"{tool} has been added to inventory.")
print(inventory)
print("\n")


"Practice 5a"
# Given:
fruits = ["apple", "banana", "orange"]
# Find and print:
# 1. The length of the list
print(f"The length of fruits list is: {len(fruits)}")
# 2. The last valid index
last_index = len(fruits) - 1
print(f"The last valid index is: {fruits[last_index]}")
# 3. Add "grape" and print new length
fruits.append("grape")
print(f"Length after adding grape to list: {len(fruits)}")
# 4. Remove one item and print new length
fruits.pop()
print(f"Length after removing last item on the list: {len(fruits)}")