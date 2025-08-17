"""
Question 1: Mart Discount Program

Write a Python program to calculate a discount based on the total shopping amount entered by the user.

* If the shopping amount is 5000 or above, apply a 20% discount.
* If the shopping amount is 3000 or above, apply a 10% discount.
* If the shopping amount is 1000 or above, apply a 5% discount.
* If the shopping amount is less than 1000, no discount is applied.

The program should display the discount message and the final payable amount.
"""

print("=== Mart Discount Program ===")

amount = float(input("Enter your total shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20   # 20% discount
    final_amount = amount - discount
    print("Congratulations! You got 20% discount.")
    print("Your Payable Amount:", final_amount)
elif amount >= 3000:
    discount = amount * 0.10   # 10% discount
    final_amount = amount - discount
    print("You got 10% discount.")
    print("Your Payable Amount:", final_amount)
elif amount >= 1000:
    discount = amount * 0.05   # 5% discount
    final_amount = amount - discount
    print("You got 5% discount.")
    print("Your Payable Amount:", final_amount)
else:
    print("No discount applied. Your Payable Amount:", amount)
