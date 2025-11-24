# Print all combinations of colors and sizes
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
# Write nested loops to print "red S", "red M", etc.
for color in colors:
    for size in sizes:
        print(f"{color} {size}")
    print()


num = 1
for row in range(4):
    for col in range(4):
        print(f"{num}", end=" ")
        num += 1
    print()

numbers = [2, 7, 3, 8, 5]
# Print pairs like "(2,8) = 10"
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 10:
            print(f"({numbers[i]}, {numbers[j]}) = 10")
            
# Create seating for 3 rows (A-C) with 4 seats each (1-4)
# Output: A1, A2, A3, A4, B1, B2, etc.
rows = ["A", "B", "C"]
seats = [1, 2, 3, 4]
for i in range(len(rows)):
    for j in range(len(seats)):
        print(f"{rows[i]}{seats[j]}")
    print()

# Find which students have the same score
students = ["Ann", "Bob", "Cal", "Dan"]
scores = [85, 92, 85, 78]
# Print pairs with matching scores
for i, student1 in enumerate(students):
    for j, student2 in enumerate(students[i+1:]):
        if scores[i] == scores[i+j+1]:
            print(f"{student1} and {student2} have the same score: {scores[i]}")
            
            
# Calculate the average of these scores
scores = [85, 92, 78, 95, 88]
total = 0
count = 0
# Your accumulator code here
for score in scores:
    total += score
    count += 1
# Print the average
print(total, count)
if count > 0:
    average = total/count
    print(f"Average is: {average}")


# Build string with only uppercase letters
text = "Hello World 2024!"
uppercase_only = ""
# Your accumulator code here
for char in text:
    if char.isupper():
        uppercase_only += char
print(uppercase_only)
# Expected: "HW"
    