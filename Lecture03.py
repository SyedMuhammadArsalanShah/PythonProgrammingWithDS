
"""
Question 2: Pakistan Forces & Civilian Eligibility Checker

Write a Python program that checks whether a candidate is eligible for selection 
in Pakistan Army, Navy, Air Force, or Civilian Jobs based on the following criteria:

Army:
- Age: 17–23 years
- Height: Minimum 162.5 cm
- Education: Intermediate or Bachelor
- Marks: At least 50%
- Medically fit
- Running: 1 mile in 8 minutes or less

Navy:
- Age: 16–21 years
- Height: Minimum 157 cm
- Education: Matric or Intermediate
- Marks: At least 45%
- Medically fit
- Running: 1 mile in 9 minutes or less

Air Force:
- Age: 16–22 years
- Height: Minimum 163 cm
- Education: Intermediate or Bachelor
- Marks: At least 60%
- Medically fit
- Running: 1 mile in 7.5 minutes or less

Civilian Jobs:
- Age: 18–30 years
- Education: Bachelor or Master
- Marks: At least 50%
- Medically fit

The program should ask the user to select one option (Army, Navy, Air Force, or Civilian), 
then take input values (age, height, education, marks, medical fitness, running time) 
and display whether the candidate is Eligible or Not Eligible.
"""



print("=== Pakistan Forces & Civilian Eligibility Checker ===")

print("\nSelect Force/Category:")
print("1. Pakistan Army")
print("2. Pakistan Navy")
print("3. Pakistan Air Force")
print("4. Civilian Jobs")

choice = int(input("Enter your choice (1-4): "))

age = int(input("Enter your Age: "))
height = float(input("Enter your Height in cm: "))
education = input("Enter your Education (Matric/Intermediate/Bachelor/Master): ")
marks = float(input("Enter your Percentage Marks: "))
medical = input("Are you Medically Fit? (yes/no): ").lower()
running = float(input("Enter your Running Time for 1 mile (in minutes): "))

# Army Criteria
if choice == 1:
    print("\n--- Army Selection ---")
    if (17 <= age <= 23 
        and height >= 162.5 
        and education.lower() in ["intermediate", "bachelor"] 
        and marks >= 50 
        and medical == "yes" 
        and running <= 8):
        print(" You are Eligible for Pakistan Army.")
    else:
        print("You are NOT Eligible for Pakistan Army.")

# Navy Criteria
elif choice == 2:
    print("\n--- Navy Selection ---")
    if (16 <= age <= 21 
        and height >= 157 
        and education.lower() in ["matric", "intermediate"] 
        and marks >= 45 
        and medical == "yes" 
        and running <= 9):
        print(" You are Eligible for Pakistan Navy.")
    else:
        print(" You are NOT Eligible for Pakistan Navy.")

# Air Force Criteria
elif choice == 3:
    print("\n--- Air Force Selection ---")
    if (16 <= age <= 22 
        and height >= 163 
        and education.lower() in ["intermediate", "bachelor"] 
        and marks >= 60 
        and medical == "yes" 
        and running <= 7.5):
        print("You are Eligible for Pakistan Air Force.")
    else:
        print(" You are NOT Eligible for Pakistan Air Force.")

# Civilian Jobs Criteria
elif choice == 4:
    print("\n--- Civilian Selection ---")
    if (18 <= age <= 30 
        and education.lower() in ["bachelor", "master"] 
        and marks >= 50 
        and medical == "yes"):
        print("You are Eligible for Civilian Job in Armed Forces Department.")
    else:
        print("You are NOT Eligible for Civilian Job.")

else:
    print("Invalid Choice!")






