"""
Question: Assignment Menu Program

Write a Python program that performs the following tasks:

1. Account Creation & Login:
   - Ask the user to create an account (Name, Email, Password, Contact).
   - After successful account creation, allow the user to login 
     with Email and Password.
   - If login is successful, display a menu of options.

2. Menu Options:
   The program should allow the user to select one option from the menu:

   1. Marksheet:
      - Input marks of 3 subjects (English, Urdu, Math).
      - Calculate obtained marks, percentage, and assign grades 
        according to percentage.

   2. Leap Year Checker:
      - Input a year and check whether it is a leap year or not.

   3. Even/Odd Checker:
      - Input a number and check whether it is even or odd.

   4. Positive/Negative Checker:
      - Input a number and check whether it is positive, negative, or zero.

   5. Calculator:
      - Input two numbers and perform addition, subtraction, multiplication,
        and division (check divide by zero).

   6. Temperature Converter:
      - Provide conversions:
          1. Celsius → Fahrenheit
          2. Fahrenheit → Celsius
          3. Celsius → Kelvin
          4. Kelvin → Celsius

   7. Smallest & Largest (2 Numbers):
      - Input two numbers and determine which one is the largest 
        and which one is the smallest.
      - If both numbers are equal, display a message.

3. Error Handling:
   - If login credentials are incorrect, display "Access Denied".
   - If an invalid menu option is selected, show "Invalid Option".
"""


print("=== Assignment ===")

# Account Creation
userName = input("Enter Your User Name: ")
userEmail = input("Enter Your User Email: ")
userPassword = input("Enter Your User Password: ")
userContact = input("Enter Your User Contact: ")

print("\nAccount Successfully Created!\n")

# Login
userEmailLogin = input("Enter Your User Email (Login): ")
userPasswordLogin = input("Enter Your User Password (Login): ")

if userEmail == userEmailLogin and userPassword == userPasswordLogin:
    print(f"\nWelcome {userName} to Aptech!\n")

    print("Menu Options:")
    print("1. Marksheet")
    print("2. Leap Year Checker")
    print("3. Even/Odd Checker")
    print("4. Positive/Negative Checker")
    print("5. Calculator")
    print("6. Temperature Converter")
    print("7. Find Smallest & Largest (2 Numbers)")

    option = int(input("\nSelect an Option (1-7): "))

    # ---------------- Marksheet ----------------
    if option == 1:
        print("\n--- Marksheet ---")
        eng = float(input("Enter Your English Marks: "))
        urdu = float(input("Enter Your Urdu Marks: "))
        math = float(input("Enter Your Maths Marks: "))

        obtainedMarks = eng + urdu + math
        percentage = obtainedMarks / 300 * 100

        print("\nResults:")
        print("Obtained Marks:", obtainedMarks)
        print("Percentage:", percentage, "%")

        if 80 <= percentage <= 100:
            print("Grade: A1 MashaaAllah")
        elif 70 <= percentage <= 79:
            print("Grade: A MashaaAllah")
        elif 60 <= percentage <= 69:
            print("Grade: B Alhamdulilah")
        elif 50 <= percentage <= 59:
            print("Grade: C Astagfirullah")
        elif 40 <= percentage <= 49:
            print("Grade: D (IU jaien)")
        else:
            print("Failed")

    # ---------------- Leap Year ----------------
    elif option == 2:
        print("\n--- Leap Year Checker ---")
        year = int(input("Enter a Year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, "is a Leap Year")
        else:
            print(year, "is NOT a Leap Year")

    # ---------------- Even/Odd ----------------
    elif option == 3:
        print("\n--- Even/Odd Checker ---")
        number = int(input("Enter a Number: "))
        if number % 2 == 0:
            print(number, "is Even")
        else:
            print(number, "is Odd")

    # ---------------- Positive/Negative ----------------
    elif option == 4:
        print("\n--- Positive/Negative Checker ---")
        number = int(input("Enter a Number: "))
        if number > 0:
            print(number, "is Positive")
        elif number < 0:
            print(number, "is Negative")
        else:
            print("Number is Zero (Neutral)")

    # ---------------- Calculator ----------------
    elif option == 5:
        print("\n--- Calculator ---")
        number1 = float(input("Enter Number 1: "))
        number2 = float(input("Enter Number 2: "))

        print("\nResults:")
        print("Addition:", number1 + number2)
        print("Subtraction:", number1 - number2)
        print("Multiplication:", number1 * number2)
        if number2 != 0:
            print("Division:", number1 / number2)
        else:
            print("Division: Cannot divide by zero")

    # ---------------- Temperature Converter ----------------
    elif option == 6:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")

        tempOption = int(input("Select Conversion Type (1-4): "))
        tempValue = float(input("Enter Temperature Value: "))

        if tempOption == 1:
            print("Result:", (tempValue * 9/5) + 32, "°F")
        elif tempOption == 2:
            print("Result:", (tempValue - 32) * 5/9, "°C")
        elif tempOption == 3:
            print("Result:", tempValue + 273.15, "K")
        elif tempOption == 4:
            print("Result:", tempValue - 273.15, "°C")
        else:
            print("Invalid Temperature Option")

    # ---------------- Smallest & Largest (2 Numbers) ----------------
    elif option == 7:
        print("\n--- Smallest & Largest Finder ---")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if num1 > num2:
            largest = num1
            smallest = num2
        elif num2 > num1:
            largest = num2
            smallest = num1
        else:
            print("Both numbers are equal:", num1)
            exit()

        print("Smallest Number:", smallest)
        print("Largest Number:", largest)

    else:
        print("Invalid Option Selected!")

else:
    print("\nIncorrect Email or Password! Access Denied.")
