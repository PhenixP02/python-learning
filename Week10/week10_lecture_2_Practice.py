# Stop counting when you reach 5
#for i in range(10):
#    print(i)
#    if i == 5:
#        break

#numbers = [3, 7, 9, 2, 11, 4, 13]
# Write loop with break to find and print first even number
#for num in numbers:
#    if num % 2 == 0:
#        print(num)
#        break

# Allow 3 password attempts
# Use break when correct password entered
# Password is "secure123"
#correct_password = "secure123"
#max_attempts = 3
#attempts = 0
#while attempts < max_attempts:
#    password = input("Please enter password ")
#    attempts += 1
#    if password == correct_password:
#        print("Welcome user")
#        break
#    print("Incorrect password, you will be locked out after 3 unsuccessful tries!")

# Print 0-5 but skip 3
#for i in range(6):
#    if i == 3:
#        continue
#    print(i)

#scores = [85, -5, 92, 150, 78, 45, 200]
# Use continue to skip invalid scores (must be 0-100)
# Calculate average of valid scores only

#total = 0
#count = 0
#for score in scores:
#    if score > 100 or score < 00:
#        continue
#    total += score
#    count += 1
#avg = total / count
#print(avg)

# Add else to confirm all numbers are positive
#numbers = [1, 2, 3, 4, 5]
#for num in numbers:
#    if num < 0:
#        print("Found negative!")
#        break
#else:
#    print("No negative numbers found.")

# Search for a vowel in a word
#word = "xyza"
# Write loop with else to report if no vowels found
#for letter in word:
#    if letter in [a, e, i, o, u]
#        print(f"{letter} is a vowel")
#        break
#else:
#    print("No vowels found")


# Original with continue:
#for i in range(10):
#    if i % 2 == 0:
#        continue
#    print(i)
# Rewrite without continue:
for i in range(10):
    if i != 2:
        print(i)
    