"""
CS1300 - Homework #5: Advanced Control Structures
Name: Phenix Payton
Date: 10/20/25
Description: Advanced conditional logic and validation
"""

"PROBLEM 1"
print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
# YOUR CODE HERE
# 1. Check if current temp is in comfortable range using chained comparison (68F-76F)
is_comfortable = 68 <= current_temp <= 76
if is_comfortable == True:
    print(f"It is a comfortable {current_temp}F")
# 2. Determine if it's night time (22-6)
is_night = hour >= 22 or hour <= 6
if is_night == True:
    print(f"Night Mode Activated, dropping 3 degrees")
    desired_temp -= 3
# 3. Apply seasonal restrictions
if season == "summer":
    min_temp = 72
    if desired_temp < min_temp:
        print("Making Seasonal Adjustments to Desired Temp.")
        desired_temp = min_temp
elif season == "winter":
    max_temp = 69
    if desired_temp > max_temp:
        print("Making Seasonal Adjustments to Desired Temp.")
        desired_temp = max_temp    
# 4. Calculate actual target temperature after adjustments
print(f"Target Temperature After all Adjustments: {desired_temp}")
# 5. Calculate time to reach target
temp_change = abs(desired_temp - current_temp)
print(f"Temp changing by {temp_change} degrees")
time_to_target = round(temp_change / 2,1)
print(f"Will take {time_to_target} hour(s)")
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
if time_to_target >= 4:
    print("Energy Effeciency Rating: POOR")
elif time_to_target >= 3:
    print("Energy Effeciency Rating: FAIR")
elif time_to_target >= 2:
    print("Energy Effeciency Rating: GOOD")
else:
    print("Energy Effeciency Rating: EXCELLENT")
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6


print()
"PROBLEM 2"
print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
score = 0
# YOUR CODE HERE
# Use conditional expressions for each check
# Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
# Check length (use conditional expression)
length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >=8 else 0
# Check for uppercase (use conditional expression)
has_upper = password != password.lower()
upper_points = 15 if has_upper == True else 0
# Check for lowercase
has_lower = password != password.upper()
lower_points = 15 if has_lower == True else 0
# Check for numbers
has_digit = any(c.isdigit() for c in password)
digit_points = 15 if has_digit == True else 0
# Check for special characters
has_special = not password.isalnum()
special_points = 15 if has_special == True else 0
# Check for common patterns
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
pattern_points = 10 if has_pattern == False else 0
# Calculate total score and determine strength level
total_points = pattern_points + special_points + digit_points + lower_points + upper_points + length_points
strength_level = "EXCELLENT" if total_points >= 90 else "GOOD" if total_points >= 60 else "WEAK" if total_points >= 30 else "EXTREMELY WEAK" 
# Display detailed analysis
print("Security Analysis:")
print(f"Length: {len(password)} characters ({length_points}/30 points)")
print(f"Upper Case Letters: {has_upper} ({upper_points}/15 points)")
print(f"Lowercase Letters: {has_lower} ({lower_points}/15 points)")
print(f"Numbers: {has_digit} ({digit_points}/15 points)")
print(f"Special Characters: {has_special} ({special_points}/15 points")
print(f"Common Pattern Detected: {has_pattern} ({pattern_points}/10 points)")
print(f"Total Score: {total_points}/100")
print(f"Strength Level: {strength_level}")
print("Recommendations:")
if len(password) < 16:
    print("Consider using 16+ characters for maximum security")
if has_digit != True:
    print("Try adding a number to your passowrd")
if has_upper != True:
    print("Try adding at least one upper case letter to your password")
if has_lower != True:
    print("Try adding at least one lower case letter to your password")
if has_special != True:
    print("Try adding at least one special character to your password")
if has_pattern != False:
    print("Don't use common patterns like 'abc' '123' 'qwerty' 'password' '111'")


print()
"PROBLEM 3"
print("=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
import sys
all_valid_range = True if (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100) else False
if all_valid_range == False:
    print("ERROR INVALID SCORE DETECTED")
    sys.exit()
else:
    print("All scores in valid range (0-100)")
# 2. Check for suspicious patterns
sus_check1 = True if test1 == test2 == test3 == test4 else False
sus_check2 = True  if test2 - test1 >= 40 or test3 - test2 >= 40 or test4 - test3 >= 40 else False
sus_check3 = True if test1 == 100 and test2 == 100 and test3 == 100 and test4 == 100 else False
print("Suspicious Checks:")
if sus_check1 == True:
    print("All test scores the same. Be sure this is correct!!")
else:
    print("There is variation in scores")
if sus_check2 == True:
    print("Suspicious jump in scores!!")
else:
    print("No suspicious jump in scores")
if sus_check3 == True:
    print("All scores perfect. Be sure this is correct!!")
else:
    print("Not all perfect scores")
print("Statistics:")
average_score = (test1 + test2 + test3 + test4)/4
round(average_score,2)
print(f"- Average: {average_score}")
highest_score = test1 if (test1 >= test2 and test1 >= test3 and test1 >= test4) else test2 if (test2 >= test1 and test2 >= test3 and test2 >= test4) else test3 if (test3 >= test1 and test3 >= test2 and test3 >= test4) else test4
print(f"- Highest: {highest_score}")
lowest_score = test1 if (test1 <= test2 and test1 <= test3 and test1 <= test4) else test2 if (test2 <= test1 and test2 <= test3 and test2 <= test4) else test3 if (test3 <= test1 and test3 <= test2 and test3 <= test4) else test4
print(f"- Lowest: {lowest_score}")
score_trend = "IMPROVING" if test4 > test1 else "STEADY" if test4 == test1 else "DECLINIG"
print(f"- Trend: {score_trend}")
grade = "A" if average_score >= 90 else "B" if average_score >= 80 else "C" if average_score >= 70 else "D" if average_score >= 60 else "F"
print(f"- Grade: {grade}")
status = "PASSING" if grade != "F" else "FAILING"
print(f"- Status: {status}")


print()
"PROBLEM 4"
print("=== EVENT SCHEDULING SYSTEM ===") 
# Event 1 
print("\nEVENT 1 DETAILS:") 
event1_name = input("Event name: ") 
event1_day = input("Day (mon-sun): ").lower()[:3]  # First 3 letters 
event1_start = float(input("Start time (0-23): ")) 
event1_end = float(input("End time (0-23): ")) 
# Event 2 
print("\nEVENT 2 DETAILS:") 
event2_name = input("Event name: ") 
event2_day = input("Day (mon-sun): ").lower()[:3] 
event2_start = float(input("Start time (0-23): ")) 
event2_end = float(input("End time (0-23): ")) 
# YOUR CODE HERE
 # 1. Validate times are in range 0-24
if event1_start > 23 or event1_start < 0 or event1_end > 23 or event1_end < 0: 
    print("Invalid time for Event 1.")
    valid_time_range = False
elif event2_start > 23 or event2_start < 0 or event2_end > 23 or event2_end < 0:
    print("Invalid time for Event 2.")
    valid_time_range = False
else:
    valid_time_range = True
 # 2. Validate end time > start time for each event
if event1_end < event1_start or event2_end < event2_start:
    print("Invalid Time entry. An end time was before a start time.")
    valid_time_ends = False
else:
    valid_time_ends = True
# DAY VALIDATION
valid_event_day = False
valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"] 
if event1_day not in valid_days or event2_day not in valid_days:
    print("Invalid day entered (MUST BE: mon, tue, wed, thu, fri, sat, or sun)")
else:
    valid_event_day = True
# 3. Check for conflicts using complex conditions
# 4. Calculate gap between events if same day
print()
print("SCHEDULE ANALYSIS:")
if valid_time_range == True and valid_time_ends == True and valid_event_day == True:
    print("Events have valid times and days")
    if event1_day == event2_day and event2_start < event1_end:
        print(f"There is overlap between the two events")
        print(f"Event 1 time: {event1_start}-{event1_end} Event 2 time: {event2_start}-{event2_end}")
    elif event1_day == event2_day and event2_start > event1_end:
        event_gap = event2_start - event1_end
        print(f"You have a {event_gap}hr(s) between events")
    else:
        print("Events on different days, no time conflcits ")
 # 5. Check for early/late scheduling issues 
if event1_start < 6 or event1_start > 23:
    print("Be aware, event 1 is late/early!")
if event2_start < 6 or event2_start > 23:
    print("Be aware, event 2 is late/early!")