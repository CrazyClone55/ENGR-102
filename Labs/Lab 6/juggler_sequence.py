# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 6
# Date: 29 September 2023
from math import floor

#comment
n = int(input("Enter a positive integer: "))
print("The Juggler sequence starting at", n, "is: ")
print(n, end = "")
count = 0
while n != 1:
    print("", end = ", ")
    count +=1
    if n % 2 == 0:
        n = floor(n**0.5)
        print(n, end="")
    else:
        n = floor(n**1.5)
        print(n, end="")
print("\nIt took", count, "iterations to reach 1")
        