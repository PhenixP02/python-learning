# exercise2.py
# Type Detective
# Phenix Payton
# 8/25/25
# Mystery variables - determine their types!
mystery1 = 42
mystery2 = "42"
mystery3 = 42.0
mystery4 = "42.0"
mystery5 = True
mystery6 = "True"
# TODO: Print each mystery variable and its type
print("Mystery 1:", mystery1, "is type:", type(mystery1))
print("Mystery 2:", mystery2, "is type:", type(mystery2))
print("Mystery 3:", mystery3, "is type:", type(mystery3))
print("Mystery 4:", mystery4, "is type:", type(mystery4))
print("Mystery 5:", mystery5, "is type:", type(mystery5))
print("Mystery 6:", mystery6, "is type:", type(mystery6))

# Predictions
# Prediciton 1: mystery1 + mystery3 = 84.0 float
result1 = mystery1 + mystery3
print("mystery1 + mystery3 =", result1, "Type", type(result1))

# Prediction 2: mystery2 + mystery4 = "4242.0" string
result2 = mystery2 + mystery4 
print("mystery2 + mystery4 =", result2, "Type", type(result2))

# Convert mysery2 to an integer an add to mystery1
converted = int(mystery2)
sum_result = converted + mystery1
print("Converted sum:", sum_result)
# Convert mystery5 to an integer
bool_as_int = int(mystery5)
print("True as integer:", bool_as_int)
# Can you convert mystery6 to boolean?
str_as_bool = bool(mystery6)
print("String as boolean:", str_as_bool)
