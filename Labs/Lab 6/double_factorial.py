# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 6
# Date: 29 September 2023

def doublefactorial(input):
    output = 1
    for i in range(input, 0, -2):
        output = output * i
        #comment
    return output