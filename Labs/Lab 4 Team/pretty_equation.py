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
coefficient_A = int(input("Please enter the coefficient A: "))
coefficient_B = int(input("Please enter the coefficient B: "))
coefficient_C = int(input("Please enter the coefficient C: "))

#calculations
if coefficient_A == 1:
    A = "x^2 "
elif coefficient_A == -1:
    A = "- x^2 "
elif coefficient_A == 0:
    A = ""
elif coefficient_A < 0:
    A = "- "+ str(abs(coefficient_A)) + "x^2 "
else:
    A = str(coefficient_A) + "x^2 "

if coefficient_B == 1:
    if A == "":
        B = "x "
    else:
        B = "+ x "
elif coefficient_B == -1:
    B = "- x "
elif coefficient_B == 0:
    B = ""
elif coefficient_B < 0:
    B = "- "+ str(abs(coefficient_B)) + "x "
elif coefficient_B > 0:
    if A == "":
        B = str(coefficient_B) + "x "
    else:
        B = "+ "+ str(coefficient_B) + "x "


if coefficient_C == 0:
    C =  ""
elif coefficient_C < 0:
    C = "- " + str(abs(coefficient_C))+ " "
else:
    if B == "":
        C = str(coefficient_C)+ " "
    else:
        C ="+ " +str(coefficient_C)+ " "


print("The quadratic equation is " + A + B + C + "= 0")
