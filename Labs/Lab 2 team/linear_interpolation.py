# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 2 team
# Date: 30 August 2023
from math import pi
x1 = 10
x2 = 55

y1 = 2027
y2 = 23027

slope = (y2-y1)/(x2-x1)
circumference = 2*pi*6745

x0 = 25
y0 = None


#part 1
print("Part 1:")
y0 = slope*(x0-x1)+y1
print("For t = "+ str(x0) +" minutes, the position p = "+str(y0)+" kilometers")
    
    
#part 2
x0 = 300
print("Part 2:")

y0 = slope*(x0-x1)+y1
y0 = y0 % circumference
print("For t = "+ str(x0) +" minutes, the position p = "+str(y0)+" kilometers")