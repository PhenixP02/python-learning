text = "Mississippi"
length = len(text)
first = text[0]
last = text[-1]
middle = text[length // 2]
print(length, first, last, middle)

email = "student@example.com"
user = email[0:7]
domain = email[8:]
ext = email[-3:]
print(user, domain, ext)


string1 = "ab" * 3
string2 = "123"
string3 = string2[0:] + string2[::-1]
print(string1, string3)

text ="Python Programming"
print(text.upper()) # ALL UPPER CASE
print(text.lower()) # All Lower Case
print(text.swapcase()) # SWAPS ALL CASES
print(text.title())# TITLE FORMAT

# Predict True or False:
print("Hello123".isalpha()) # _____
print("123.45".isdigit()) # _____
print("Hello World".isalnum()) # _____ (note the space!)
print("".isspace()) # _____
print("HELLO!".isupper()) # _____

text = "Hello World"
print(text.find("World"))
print(text.find("o"))
print(text.find("xyz"))

print(text.index("World"))
# print(text.index("xyz")) ## ERRORS OUT
print("-"*30)
text = "Mississippi"
print(text.count("s")) # Returns: _____
print(text.count("ss")) # Returns: _____
print(text.count("pip")) # Returns: _____

sentence = "To be or not to be"
# Find "be": sentence.find("be") = _____
print(sentence.find("be"))
# Count "to": sentence.count("to") = _____
print(sentence.count("to"))
# Find "or": sentence.find("or") = _____
print(sentence.find("or"))
# Count "o": sentence.count("o") = _____

text = " Hello World "
print(text.strip()) # Returns: _____________
print(text.lstrip()) # Returns: _____________ (left only)
print(text.rstrip()) # Returns: _____________ (right only

print("-"*30)
text = "Hello World"
print(text.replace("o", "0")) # Returns: _____________
print(text.replace("World", "Python")) # Returns: _____________
print(text.replace("l", "")) # Returns: _____________ (removes 'l')

messy = " Python Programming "
# Remove all spaces: messy.strip() = _____________
print(messy.strip())
# Just remove left spaces: messy.______() = _____________
print(messy.lstrip())
text = "I like cats. Cats are nice."
# Replace "cats" with "dogs":
print(text.replace("cats", "dogs"))
# text.replace(_______, _______) = _____________

print("-"*30)
print("PRACTICE PROBLEMS")
print("-"*30)

print("Problem 1: ")
user_input = " Hello123 "
# Clean the input: user_input.________() = _______
print(user_input.strip())
# Check if alphanumeric: ____________.isalnum() = _______
print(user_input.isalnum())
# Convert to uppercase: ____________.upper() = _______
print(user_input.upper())

print("\nProblem 2:")
name = " jOHn DOE "
# Format as "John Doe":
# Step 1: Strip spaces: _____________
print(name.strip())
# Step 2: Convert to title: _____________
print(name.title())
# One line: name.________().________()
print(name.strip().title())

print("\nProblem 3: ")
password = "Pass123"
# Has uppercase? not password.islower() = _____
print(not password.islower())
# Has lowercase? not password.isupper() = _____
print(not password.isupper())
# Has digit? (check each character - we'll learn loops later)
print(password.isalnum())

print("\nProblem 4: ")
url = "https://www.example.com"
# Is secure? url.startswith("https") = _____
print(url.startswith("https"))
# Get domain: url.replace("https://", "").replace("www.", "") = _____
print(url.replace("https://", "").replace("www.",""))
# Is .com site? url.endswith(".com") = _____
print(url.endswith(".com"))