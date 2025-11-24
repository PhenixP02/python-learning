
# def process_order():
# This does too much!
#    price = float(input("Price: "))
#    quantity = int(input("Quantity: "))
#   total = price * quantity
#    tax = total * 0.08
#    final = total + tax
#    print(f"Total: ${final:.2f}")
# Split into:
# def get_order_info():
# def calculate_total(price, quantity):
   
#def get_order_info():
#    quantity = int(input("Quantity: "))
#    return price, quantity

#def calculate_total(price, quantity):
#    total = price * quantity
#    tax = total * 0.08
#    final = total + tax
#    print(f"Total: ${final:.2f}")
    
#price, quantity = get_order_info()
#calculate_total(price, quantity)


#def get_password():
#    password = input("Enter Password: ")
#    return password

#def check_length(password):
#    if len(password) < 8:
#        print("Password must be 8 or more characters long!")
#    else:
#        print("Password length is good.")
        
#def has_upper(password):
#    if password.isupper() == False:
#        print("Password should contain atleast 1 upper case letter!")
#    else:
#        print("Password has atleast one upper case letter.")

#def has_lower(password):
#    if password.islower() == False:
#        print("Password should contain atleast one lower case letter!")
#    else:
#        print("Password has atleast one lower case letter.")



#password = get_password()
#check_length(password)
#has_upper(password)
#has_lower(password)
# Currently does everything
# Check length >= 8
# Check has uppercase
# Check has lowercase
# Check has number
# Return True if all pass
