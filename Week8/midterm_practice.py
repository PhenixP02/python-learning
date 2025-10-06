
"Problem 2"
food_total = 45.50
drinks_total = 18.75
dessert_total = 12.25

subtotal = food_total + drinks_total + dessert_total
tax = subtotal * .08
total_with_tax = subtotal + tax

if total_with_tax >= 50:
    tip = .20
    str_tip = "20"
elif total_with_tax >= 30:
    tip = .18
    str_tip = "18"
elif total_with_tax >= 15:
    tip = .15
    str_tip = "15"
total_with_tax_tip = round(total_with_tax * (1 + tip), 2)

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Tip: {str_tip}%")
print(f"Final Total: ${total_with_tax_tip}")


"Problem 3"
products = ["laptop", "mouse", "keyboard", "monitor", "cable"]
products.append("headphones")
print(products)
products.insert(3, "webcam")
print(products)
products.remove("cable")
print(products)
products[1] = "wireless mouse"
print(products)
print(products[:-4:-1])

print(f"Total products in stock: {products}")
print(f"First product alphabetically: {products[-1]}") # Midterm exam says it is at index positon 2 which is 'keyboard' but that does not come before 'headphones' alphabetically
print(f"Products at even indices: {products[0::2]}")