# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 5
# Date: 27 September 2023
from math import log10

userInput = input("Enter the excess temperature: ")
#tries to parse the input as a float, if it fails, it is not possible to calculate the surface heat flux
try:
    userInput = float(userInput)
except:
    print("Surface heat flux is not available")
    exit()
#having this check here prevents it from passing a negative to the log functions
if userInput<1.3 or userInput>1200:
    print("Surface heat flux is not available")
    exit()
#define the slope and equations for each line
#slope is defined as a variable since it is static
#the equatoin is a function so I just pass it the x value/userInput
line1slope = log10(7000/1000)/log10(5/1.3)
def line1equation(x):
    return 1000*(x/1.3)**line1slope
line2slope = log10((1500000)/7000)/log10(30/5)
def line2equation(x):
    return 7000*(x/5)**line2slope
line3slope = log10((25000)/(1500000))/log10(120/30)
def line3equation(x):
    return (1.5*10**6)*(x/30)**line3slope
line4slope = log10((1500000)/25000)/log10(1200/120)
def line4equation(x):
    return (25000)*(x/120)**line4slope
#then it checks which line the user input is on and uses the corresponding equation
if userInput<=5:
    y = line1equation(userInput)
    #its less than or equal to make sure that it will calculate the value on the line
    #even though the next one would cover that point
    #this is necesary because there is no equation to cover 1200 if it was just <
elif userInput<=30:
    y = line2equation(userInput)
elif userInput<=120:
    y = line3equation(userInput)
elif userInput<=1200:
    y = line4equation(userInput)
else:
    #if the user input is not on any line, it is not possible to calculate the surface heat flux
    print("Surface heat flux is not available")
    exit()
print(f"The surface heat flux is approximately {y:.0f} W/m^2")