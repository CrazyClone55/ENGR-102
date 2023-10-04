# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
# 
# Section: 527
# Assignment: Lab 3
# Date: 6 September 2023
def triangle(input):
    return input**2 * 3**0.5 / 4
    
def square(input):
    return input**2

def pentagon(input):
    return 0.25*((5*(5+(2*5**0.5)))**0.5)*input**2
    
def dodecagon(input):
    return 3*(2+3**0.5)*input**2
#I have no reason for comments, everthing explains itself
    
sideLength = float(input("Please enter the side length: "))
print(f"\nA triangle with side {sideLength:.2f} has area {triangle(sideLength):.3f}")
print(f"A square with side {sideLength:.2f} has area {square(sideLength):.3f}")
print(f"A pentagon with side {sideLength:.2f} has area {pentagon(sideLength):.3f}")
print(f"A dodecagon with side {sideLength:.2f} has area {dodecagon(sideLength):.3f}")