#lab2_2.py
# Week 2 Session 2 Lab
# Phenix Payton
# 8/28/25

print("=" * 50)
print("WEEK 2 SESSION 2 LAB")
print("=" * 50)

## Problem 1: Age Calculator
print("\n--- Problem 1: Age Calculator ---")
birth_Year = int(input("What year were you born: "))
current_Year = 2025
age = current_Year - birth_Year
print(f"You are", {age}, "years old in 2025!")

## Problem 2: Temperature Converter
print("\n--- Problem 2: Temperature Converter ---")
c_Temp = int(input("What is the temperature in Celsius? "))
f_Temp = c_Temp * (9/5) + 32
print("The Temperature in Fahrenheit is: ", f_Temp)

## Problem 3: Rectangle Measurements
print("\n--- Problem 3: Rectangle Measurements ---")
length = float(input("What is the length of the rectangle in feet? " ))
width = float(input("What is the width of the rectangle in feet? "))
area = length * width
perimeter = (2*length) + (2*width)
print(f"The Area of the rectangle is: {area}ft")
print(f"The Perimeter of the rectangle is: {perimeter}ft")

## Problem 4: Bill Calculator
print("\n--- Problem 4: Bill Calculator ---")
sub_total = float(input("What was the bill for your meal? "))
tip = float(input("What Percent of meal would you like to tip? "))
final_Total = sub_total + (sub_total * (tip/100))
round_Final_Total = round(final_Total, 2)
print("Your total including tip is: " + str(round_Final_Total))


## Problem 5: Student Info Display 
print("\n--- Problem 5: Student Info Display ---")
name = input("What is your name? ")
age = input("How old are you? ")
major = input("What is your major? ")
print(name, age, major)
print(name, age, major, sep=", ")
print(name, age, major, sep=" | ")

## Problem 6: Progress Indicator 
print("\n--- Problem 6: Progress Indicator ---")
print("Processing", end="")
print(".....", end="")
print(" Complete!")

## Problem 7: Data Table Header
print("\n--- Problem 7: Data Table Header ---")
name = input("What is your name? ")
score = input("What was your score? ")
grade = input("What was your grade? ")
print("=" * 40)
print("Name", "Score", "Grade", sep="   ")
print("=" * 40)
print(name, score, grade, sep="    ")

## Problem 8: Message Box
print("\n--- Problem 8: Message Box ---")
user_Message = input("Write a message: ")
print("+" "-" * 30)
print("| ",user_Message," |")
print("+" "-" * 30)


