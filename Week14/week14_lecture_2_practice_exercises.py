rgb_tuple = (255, 128, 0)
print(rgb_tuple[0])
print(rgb_tuple[1])
print(rgb_tuple[2])
pallate = [rgb_tuple]
print(pallate)

# Create student tuples
# Store in classroom list
# Print second student's name using double subscripting
# Unpack first student's information
# Formatted Message
tuple_alice = ("Alice", "A", 15)
tuple_andre = ("Andre", "B", 16)
tuple_lisa = ("Lisa", "C", 16)
classroom = [tuple_alice, tuple_andre, tuple_lisa]
print(classroom)
print(classroom[1][0])
print(classroom[0])
print(f"Student: {classroom[0][0]} | Grade: {classroom[0][1]} | Age: {classroom[0][2]}")

#Write a function called find_range that uses *args to accept any number of numeric arguments and
#returns a tuple containing (minimum_value, maximum_value). Test your function with 3 numbers, then with 7
#numbers. Use the * operator to unpack a list called test_scores = [78, 92, 85, 88, 91] when calling
#your function.
def find_range(*args):
    if not args:
        return None
    return (min(args), max(args))
test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))


# List Comprehensions
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
# Result: [1, 4, 9, 16, 25]
squares = [x**2 for x in range(1, 6)]
# Same result, one line!


# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8]
# Only passing grades
grades = [45, 78, 92, 55, 88]
passing = [g for g in grades if g >= 60]
# Result: [78, 92, 88]


# 3x3 multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


#Create a nested list representing a simple 3x3 grid of numbers (like a number puzzle). Each row should
#be a list, and you should have 3 rows. Print the entire grid, then print just the center number using double
#indexing. Finally, use nested loops to print each row on a separate line.
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(number_grid)
print(number_grid[1][1])
for row in number_grid:
    print(row)
    
    
#Task: You have a list of student scores: [45, 78, 92, 61, 88, 73, 55, 90, 82]. Use a list comprehension
#to create a new list called passing_grades that contains only scores 60 or above. Then use another list
#comprehension to create letter_grades that converts each passing grade to a letter: 90+ is 'A', 80+ is 'B',
#70+ is 'C', 60+ is 'D'. Print both lists.

testing_grades = [45, 78, 92, 61, 88, 73, 55, 90, 82]
passing_grades = [g for g in testing_grades if g >= 60]
print(passing_grades)
letter_grades = [letter for letter in passing_grades]

def f(x, y=2, z=3):
    pass
f(1,2)
f(1)
f(x=4)

def get_num():
    x = int(input("Enter a num: "))
    return x
def square(x):
    print("Square: ", x*x)

num = get_num()
square(num)
    