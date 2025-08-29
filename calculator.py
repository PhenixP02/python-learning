# calculator.py
# Simple Calculator with Type Handling
# Phenix Payton
# 8/29/25
print("=" * 40)
print(" ARITHMETIC CALCULATOR")
print("=" * 40)
# TODO: Create variables for two numbers
# Use meaningful variable names
first_number = 15.5
second_number = 4

# TODO: Display the numbers and their types
print(f"First number: {first_number} (Type: {type(first_number).__name__})")
print(f"Second number: {second_number} (Type: {type(second_number).__name__})")
print("-" * 40)

# TODO: Perform all arithmetic operations
print("CALCULATIONS:")

# Addition
sum_result = first_number + second_number
print(f"Addition: {first_number} + {second_number} = {sum_result}")

# Subtraction
diff_result = first_number - second_number
print(f"Subtraction: {first_number} - {second_number} = {diff_result}")

# Multiplication
product_result = first_number * second_number
print(f"Multiplication: {first_number} * {second_number} = {product_result}")

# Division (regular)
division_result = first_number / second_number
print(f"Division: {first_number} / {second_number} = {division_result}")

# Integer Division
intdivision_result = first_number // second_number
print(f"Integer Division: {first_number} // {second_number} = {intdivision_result}")

# Modulus
mod_result = first_number % second_number
print(f"Modulus: {first_number} % {second_number} = {mod_result}")

# Exponentiation
expo_result = first_number ** second_number
print(f"Exponentiation: {first_number} ** {second_number} = {expo_result}")
print("-" * 40)

# TODO: Type analysis section
print("TYPE ANALYSIS:")
# Check and display the type of each result
# Show which operations always return floats
# Show which preserve integer type
print(f"Addition result type: {type(sum_result)}")
print(f"Subtraction result type: {type(diff_result)}")
print(f"Multiplication result type: {type(product_result)}")
print(f"Division result type: {type(division_result)}")
print(f"Integer Division result type: {type(intdivision_result)}")
print(f"Modulus result type: {type(mod_result)}")
print(f"Exponentiation result type: {type(expo_result)}")

print("-" * 40)
# TODO: Fun calculations section

print("FUN CALCULATIONS:")
# Calculate the area of a circle with radius = first_number
pi = 3.14159
area = 2 * pi * first_number
print(f"Area of circle with radius {first_number}: {area:.2f}")

# Calculate compound interest
# Principal = first_number * 100, Rate = second_number%, Time = 5 years
principal = first_number * 100
rate = second_number / 100
time = 5
amount = principal * (1 + rate) ** time
print(f"${principal} at {second_number}% for {time} years = ${amount:.2f}")

# Calculate how many whole pizzas and slices
# If first_number is people and each pizza has 8 slices
# Each person gets second_number slices
import math
total_slices_needed = first_number * second_number
whole_pizzas = math.ceil(total_slices_needed / 8)
extra_slices = (whole_pizzas * 8) - total_slices_needed
print(f"{first_number} people × {second_number} slices each =")
print(f" Need {whole_pizzas} pizzas with {extra_slices} slices left over")

print("=" * 40)