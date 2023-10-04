# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel 
# Section: 527
# Assignment: Lab 1
# Date: 23 August 2023
from math import sin, radians

print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")
print("my guess for the value of f(1) is 1")

for i in range(8):
    x = 1 + 10**(-i-1) #x is the value of 1.1, 1.01, 1.001, etc.
    f = (sin(x-1))/(x-1) #f is the value of f(x) for the given x
    print(f)
    
print()
print("my guess was spot on")
    