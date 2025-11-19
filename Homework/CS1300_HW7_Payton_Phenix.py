## Phenix Payton 
## Homewrok 7 Loops Part 1
## 11/19/25

"PROBLEM 1 TEMPERATURE ANALYZER"
# Average, Highest, Lowest, Days over 72, Convert to Celcius show both
temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]
day_count = 0
above_72 = 0
current_high = 0 #Arbitrarily low number to ensure first processed temp is set to high (May need to be set to negative value if 0F temps are expected)
current_low = 1000 #Arbitrarily high number to ensure first processed temp is set to low
total = 0
print("Temperature Analysis Report")
print("=" * 25)
for temp in temperatures:
    day_count += 1
    c_temp = round((temp - 32) * (5/9), 1) # Convert to Celcius (one decimal)
    print(f"Day {day_count}: {temp}F / {c_temp}C")
    if temp > 72: # Temp above 72F
        above_72 += 1
    if temp > current_high: # Highest Temp Tracker
        current_high = temp
    if temp < current_low: # Lowest Temp Tracker
        current_low = temp
    total += temp # Add to Running Total for Average
average = round(total / day_count, 1) # Calculate Average
print()
print("Statistics:")
print(f"Average Temp: {average}F")
print(f"Highest Temp: {current_high}F") 
print(f"Lowest Temp: {current_low}F")
print(f"Days Above 72F: {above_72}")


"PROBLEM 2 NUMBER GUESSING GAME"
print()
import random
secret = random.randint(1, 20) # Generate Secret Number
print("=== NUMBER GUESSING GAME === \n I'm thinking of a number between 1 and 20 \n You have 5 guesses!")
guess_counter = 0
guesses = []
is_correct = False
for attempt in range(5):
    guess_counter += 1
    guess = int(input(f"Guess {guess_counter}: ")) # Get input 
    guesses.append(guess) # Add to Guesses list
    if guess == secret: # Check if Correct
        is_correct = True
        break
    elif guess > secret: # If guess too high
        print("Too High! Try lower.")
    else:                # If guess too low
        print("Too Low! Try higher.")
        
if is_correct == False: # LOSE Script
    print(f"\nSorry! You've run out of guesses.\nThe number was {secret}.")
    print(f"Your guesses were: {guesses}")
    print("Better luck next time!")
else: # WIN Script
    print(f"\nCorrect! You got it in {guess_counter} guesses!")
    print("Great job!")
    print(f"Your guesses were: {guesses}")
    

"PROBLEM 3 GRADE PROCESSOR"
print()
## Valid grades are 0-100 inclusive
#Skip invalid grades using continue
#Count how many invalid grades were found
#Calculate for valid grades only:
#Average
#Letter grade distribution (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59)
grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]
valid_grades = 0
invalid_grades = 0
grades_total = 0
A_total = 0
B_total = 0
C_total = 0
D_total = 0
F_total = 0

print("Processing Grades...\n"+ "=" * 20)
for grade in grades:
    if grade > 100 or grade < 0: #Grade Validation
        invalid_grades += 1
        print(f"Skipping invalid grade: {grade}")
        continue
    else:
        valid_grades += 1
        grades_total += grade  #Running total (VALID GRADES ONLY)
    if grade >= 90:     ##Letter Grade Assignment
        letter_grade = "A"
        A_total += 1
    elif grade >= 80:
        letter_grade = "B"
        B_total += 1
    elif grade >= 70:
        letter_grade = "C"
        C_total += 1
    elif grade >= 60:
        letter_grade = "D"
        D_total += 1
    else:
        letter_grade = "F"
        F_total += 1
    print(f"Grade {valid_grades}: {grade} ({letter_grade})")

print("\nSummary Report\n" + "=" * 20)
print(f"Total grades processed: {valid_grades}")
print(f"Invalid grades skipped: {invalid_grades}")
print("\nGrade Distribution:")
print(f"A: {A_total} students")
print(f"B: {B_total} students")
print(f"C: {C_total} students")
print(f"D: {D_total} students")
print(f"F: {F_total} students")
class_average = round(grades_total/valid_grades, 1)
print(f"\nClass Average: {class_average}")