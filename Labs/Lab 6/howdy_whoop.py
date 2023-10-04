# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 6
# Date: 29 September 2023

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))
for i in range (1,101):
    #comment
    if i % int1 == 0 and i % int2 == 0:
        print("Howdy Whoop")
    elif i % int2 == 0:
        print("Whoop")
    elif i % int1 == 0:
        print("Howdy")
    else:
        print(i)