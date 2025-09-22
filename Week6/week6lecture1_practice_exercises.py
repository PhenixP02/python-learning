
"Problem 1-a"
# TODO: Complete this program
#temp = float(input("Enter temperature (F): "))
# Use chained comparison to check if comfortable
# Comfortable range: 68-76 degrees
#if 68 <= temp <= 76:
#    print("It is comfortable out.")
#else:
#    print("It is not comfortable out.")



"Practice 1-b"   
# TODO: Complete this program
#age = int(input("Enter age: "))
# Use chained comparisons for each group:
# Baby: 0-2
# Child: 3-12
# Teen: 13-19
# Young Adult: 20-35
# Adult: 36-65
# Senior: 66+
#if 0 <= age <=2:
#   print("You are a baby.")
#elif 3 <= age <= 12:
#    print("You are a child.")
#elif 13 <= age <= 19:
#    print("You are a teen.")
#elif 20 <= age <= 35:
#    print("You are a young adult.")
#elif 36 <= age <= 65:
#    print("You are an adult.")
#else:
#    print("You are a senior.")
    
    

"Practice 2-a"
# TODO: Complete this program
#day = input("Enter day of week: ").lower()
# Use conditional expression to set day_type
# Monday-Friday = "weekday"
# Saturday-Sunday = "weekend"
#day_type = "weekend" if day == "saturday" or day == "sunday" else "weekday"
#print(f"It's a {day_type}")


"Practice 2-b"
# TODO: Complete this program
#order_amount = float(input("Enter order amount: $"))
# Use conditional expressions for:
# 1. Shipping: Free if order >= $50, else $5.99
#shipping_cost = 0 if order_amount >= 50 else 5.99
#print(f"Cost of shipping: {shipping_cost}")
# 2. Express available: Yes if order >= $25, else No
#express_ship = "Yes" if order_amount >= 25 else "no"
#print(f"Eligible for express shipping: {express_ship}")
# 3. Discount: 10% if order >= $100, else 0%
#discount = .1 if order_amount >= 100 else 0
#discount = round(discount * 100,2)
#print(f"Your discount is: {discount}%")



"Practice 3-a"
# TODO: Complete this program
#is_member = input("Are you a member? (yes/no): ").lower() == "yes"
#has_invitation = input("Do you have an invitation? (yes/no): ").lower() == "yes"
# Create truth table output showing:
# - Can attend with AND (need both)
#can_attend = is_member and has_invitation
#print(f"Ver1 Can you attend? {can_attend}")
# - Can attend with OR (need either)
#can_attend = is_member or has_invitation
#print(f"Ver2 Can you attend? {can_attend}")
# - Is excluded (has neither)
#can_attend = is_member and has_invitation
#print(f"ver3 Can you attend? {can_attend}")



"Practice 4-a"
# TODO: Complete this program
#phone = input("Enter phone (10 digits): ")
# Validate:
# 1. Contains only digits
#if phone.isdigit() == False:
#    print("Error: Must contain only digits!")
# 2. Exactly 10 digits long
#elif len(phone) != 10:
#    print("Error: Must be 10 digits long!")
# 3. Doesn't start with 0 or 1
#elif phone.startswith("0") or phone.startswith("1"):
#    print("Error: Can't start with 0 or 1")
#else:
#    print("No Errors Detected!")
# Provide specific error messages



"Problem 5-a"
# TODO: Fix the bugs in this code
username = input("Username: ")
password = input("Password: ")
# This code has bugs - fix them!
if username == "admin" and password == "secret":
    print("Welcome admin!")
elif username == "guest" or username == "visitor":
    print("Welcome guest!")
else:
    print("Unknown user")