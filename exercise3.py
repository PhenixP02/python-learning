# exercise3.py
# Arithmetic Operations Lab
# Phenix Payton
# 8/25/25
# Test numbers
a = 17
b = 5
c = 2.5
print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)

# TODO: Perform each operation and observe results
# Addition
add_result = a + b
print(f"{a} + {b} = {add_result}")

# Subtraction
sub_result = a - b
print(f"{a} - {b} = {sub_result}")

# Multiplication
mult_result = a * b
print(f"{a} * {b} = {mult_result}")

# Division (/) - note the type!
div_result = a / b
print(f"{a} / {b} = {div_result} (Type: {type(div_result)})")

# Integer Division (//)
int_div_result = a // b
print(f"{a} // {b} = {int_div_result} (Type: {type(int_div_result)})")

# Modulo (%)
mod_result = a % b 
print(f"{a} % {b} = {mod_result}")

# Exponentiation (**)
expo_result = a ** b 
print(f"{a} ** {b} = {expo_result}")
print("-" * 30)

# TODO: Mixed type operations
print("Mixed Type Operations:")
# What happens with int + float?
mixed1 = a + c
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")
mixed2 = a * c
print(f"{a} * {c} = {mixed2} (Type: {type(mixed2)})")
mixed3 = a ** c 
print(f"{a} ** {c} = {mixed3} (Type: {type(mixed3)})")

print("\nSpecial Cases:")
# large numbers
big = 10 ** 100
print(f"10^100 = {big}")
print(f"Python handles large numbers: {type(big)}")

# Negative division
neg_result = -17 // 5
print(f"-17 // 5 = {neg_result} (Note: rounds DOWN)")

#Division by zero (uncomment to see error)
#error_result = 10 / 0