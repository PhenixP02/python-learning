# Exercise 1
# Phenix Payton
# 8/25/25 
# Practice with Variables 

# integer variable for age
age = 23

# float variable for GPA
gpa = 4.0

# String variable for name
name = "Phenix"

# Boolean variable for whether you like Python
likes_Python = True

#None variable for something not yet defined
future_Job = None

print("Age:",age,"-Type", type(age))
print("GPA:",gpa,"-Type", type(gpa))
print("Name:",name,"-Type", type(name))
print("Likes Python:",likes_Python,"-Type", type(likes_Python))
print("Future Job:",future_Job,"-Type", type(future_Job))

# 1. Add 1 to age and print result
age = age + 1
print("Next year I'll be:",age)
# 2. Add 0.1 to GPA and print result
gpa = gpa + .1
print("If I improve:",gpa)
# 3. Multiply your name by 3 and print result
name = name * 3
print("Name repeated:", name)
# 4. What happens if you try: age + name? (Try it and comment out if it errors)
ageName = age + name
print("Age + Name:", ageName)
# Errors When attemting to add a String and Integer!