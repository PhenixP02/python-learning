print("=== Memory Investigation ===")
# Create variables with small integers
a = 100
b = 100
print(f"a = {a}, memory address = {id(a)}")
print(f"b = {b}, memory address = {id(b)}")
print(f"a and b same object? {id(a) == id(b)}")
print()
# Create variables with large integers
c = 10000
d = 10000
print(f"c = {c}, memory address = {id(c)}")
print(f"d = {d}, memory address = {id(d)}")
print(f"c and d same object? {id(c) == id(d)}")
print(f"c is d: {c is d}")
# Create variables with strings
e = "Python"
f = "Python"
print(f"e = '{e}', memory address = {id(e)}")
print(f"f = '{f}', memory address = {id(f)}")
print(f"e and f same object? {id(e) == id(f)}")

# Q1: Why do a and b share the same memory address?
# They are small integers and so Python uses the same memory address
# to save memory and for faster performance.

# Q2: Why might c and d have different memory addresses?
# My script is actually returning them as the same object and memory space. 
# When doing some research,I found that because visual studio uses the 
# CPython interpreter, it uses a special optimization called the peephole optimization

# Q3: What happens with string variables e and f?
# The string variables e and f also point to the same memory address space.

print("\n=== Variable References ===")
# Create a variable
original = 500
print(f"original = {original}, id = {id(original)}")
# Create a reference to the same object
reference = original
print(f"reference = original")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Same object? {id(original) == id(reference)}")
# Now modify original
original = original + 100
print("After: original = original + 100")
print(f"original = {original}, id = {id(original)}")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Still same object? {id(original) == id(reference)}")
# YOUR TURN: Create your own example with strings
# Create a string variable
# Create a reference to it
# Modify the original using concatenation
# Check if they still point to the same object
original_str = "Hello"
print(f"original string = {original_str}, id = {id(original_str)}")
# Reference to original string
reference1 = original_str
print(f"reference 1 = original string")
print(f"reference 1 = {reference1}, id = {id(reference1)}")
print(f"Same object? {id(original_str) == id(reference1)}")
# modification to original string
original_str = original_str + " World"
print("After: original_string = original_string +  World")
print(f"original string = {original_str}, id = {id(original_str)}")
print(f"reference 1 = {reference1}, id = {id(reference1)}")
print(f"Still same object? {id(original_str) == id(reference1)}")

print("\n=== Memory Changes with Operations ===")
# Track memory changes with different operations
x = 200
print(f"Initial: x = {x}, id = {id(x)}")
# Save the original id
original_id = id(x)
# Try different operations and check if id changes
x = x + 50
print(f"After x = x + 50: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
x = 200
# YOUR TURN: Test these operations (one at a time, reset x=200 between each)
x = x * 2
print(f"After x = x * 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
x = 200
x = x - 100
print(f"After x = x - 100: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
x = 200
x = x / 2
print(f"After x = x / 2: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
x = 200
x = x // 3
print(f"After x = x // 50: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
x = 200
x = x % 7
print(f"After x = x % 7: x = {x}, id = {id(x)}, changed? {id(x) != original_id}")
# What pattern do you notice about memory addresses after operations?
# Your observation: The memory address always changes after performing an operation on a variable.