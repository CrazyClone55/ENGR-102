# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 4 team
# Date: 13 September 2023

#inputs
amnt_paid = float(input("How much did you pay? "))
item_cost = float(input("How much did it cost? "))

change = amnt_paid-item_cost
change = round(change, 2)

print(f"You received ${change:.2f} in change. That is...")

#calculations
if (change >= 0.25):
    quarters = change // 0.25
    change = change % 0.25
    if quarters > 1:
        print(f"{quarters:.0f} quarters")
    else:
        print(f"{quarters:.0f} quarter")
if (change >= 0.10):
    dimes = change // 0.10
    change = change % 0.10
    if dimes > 1:
        print(f"{dimes:.0f} dimes")
    else:
        print(f"{dimes:.0f} dime")
if (change >= 0.05):
    nickels = change // 0.05
    change = change % 0.05
    if nickels > 1:
        print(f"{nickels:.0f} nickels")
    else:
        print(f"{nickels:.0f} nickel")
if (change >= 0.01):
    pennies = change * 100
    if pennies > 1:
        print(f"{pennies:.0f} pennies")
    else:
        print(f"{pennies:.0f} penny")

