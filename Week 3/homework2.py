# Problem 3:Time Zone Converter

print("+"+"-"*25+"+")
print("|   Time Zone Converter   |")
print("+"+"-"*25+"+")
print("\n")

# Get Input
hour = int(input("Enter current hour (EST, 0-23): "))
minute = str(input("Enter current minute (0-59): "))
print("\n")
print("+"+"-"*20+"+")
print("|   CURRENT TIMES   |")
print("+"+"-"*20+"+")
print("\n")

# Time in each Zone
cst_hour = (hour - 1) % 24
mst_hour = (hour - 2) % 24
pst_hour = (hour - 3) % 24

# EST to 12-hour
if hour < 12:
    est_ampm = "AM"
else:
    est_ampm= "PM"
est_12 = hour % 12
if est_12 == 0:
    est_12 = 12

# CST to 12-hour
if cst_hour < 12:
    cst_ampm = "AM"
else:
    cst_ampm = "PM"
cst_12 = cst_hour % 12
if cst_12 == 0:
    cst_12 = 12

# MST to 12-hour
if mst_hour < 12:
    mst_ampm = "AM"
else:
    mst_ampm = "PM"
mst_12 = mst_hour % 12
if mst_12 == 0:
    mst_12 = 12

# PST to 12-hour
if pst_hour < 12:
    pst_ampm = "AM"
else:
    pst_ampm = "PM"
pst_12 = pst_hour % 12
if pst_12 == 0:
    pst_12 = 12

# Display Table
print("|Time Zone | Time   | 12-hr Format|")
print("|----------|---------|----------|")
print(f"|EST       |  {hour}:{minute}  | {est_12}:{minute}{est_ampm} |")
print(f"|CST       |  {cst_hour}:{minute}  | {cst_12}:{minute}{cst_ampm} |")
print(f"|MST       |  {mst_hour}:{minute}  | {mst_12}:{minute}{mst_ampm} |")
print(f"|PST       |  {pst_hour}:{minute}  | {pst_12}:{minute}{pst_ampm} |")