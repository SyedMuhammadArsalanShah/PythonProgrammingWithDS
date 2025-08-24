# ==========================
# Python Lecture: Loops, Even/Odd, and Leap Year
# ==========================

# 1. Basic Loop (without input)
print("=== Example 1: Simple Loop ===")
for i in range(5):  # goes from 0 to 4
    print("Hello World", i)

print("\n")

# 2. Starting and Ending Loop (without input)
print("=== Example 2: Starting and Ending Loop ===")
for i in range(2, 8):  # goes from 2 to 7
    print("Number:", i)

print("\n")

# 3. Step Loop (without input)
print("=== Example 3: Step Loop ===")
for i in range(1, 20, 3):  # start=1, end=19, step=3
    print("Number with Step 3:", i)

print("\n")

# 4. Even and Odd Numbers (without input)
print("=== Example 4: Even and Odd Numbers (No Input) ===")
for a in range(10):  # fixed range 0 to 9
    if a % 2 == 0:
        print("Even:", a)
    else:
        print("Odd:", a)

print("\n")

# 5. Even and Odd Numbers (with input)
print("=== Example 5: Even and Odd Numbers (With Input) ===")
num = int(input("Enter a number: "))
for a in range(num):
    if a % 2 == 0:
        print("Even:", a)
    else:
        print("Odd:", a)

print("\n")

# 6. Leap Year Finder (without input)
print("=== Example 6: Leap Year Finder (No Input) ===")
startYear = 2000
endYear = 2010
leapCounter = 0

for year in range(startYear, endYear + 1):
    if year % 4 == 0:
        leapCounter += 1
        print("Leap Year:", year)
    else:
        print("Not a Leap Year:", year)

print("Total Leap Years Found:", leapCounter)

print("\n")

# 7. Leap Year Finder (with input)
print("=== Example 7: Leap Year Finder (With Input) ===")
birthYear = int(input("Enter your Birth Year: "))
meraYear = int(input("Enter the Current Year: "))

meraCounter = 0  # to count leap years

for a in range(birthYear, meraYear + 1):
    if a % 4 == 0:
        meraCounter = meraCounter + 1
        print("Leap Year:", a)
    else:
        print("Not a Leap Year:", a)

print("Total Leap Years Found:", meraCounter)
