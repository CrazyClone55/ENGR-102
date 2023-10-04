# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 3 team
# Date: 6 September 2023

#Activity 1
def poundsToNewtons(input):
    return input * 4.44822

def metersToFeet(input):
    return input * 3.28084

def atmospheresToKilopascals(input):
    return input * 101.325

def wattsToBTUPerHour(input):
    return input * 3.41214

def LpsToGpm(input):
    return input * 15.850323141489

def celciusToFarenheit(input):
    return (input * 9/5) + 32

userInput = float(input("Please enter the quantity to be converted: "))

print(f"{userInput:.2f} pounds force is equivalent to {poundsToNewtons(userInput):.2f} Newtons")
print(f"{userInput:.2f} meters is equivalent to {metersToFeet(userInput):.2f} feet")
print(f"{userInput:.2f} atmospheres is equivalent to {atmospheresToKilopascals(userInput):.2f} kilopascals")
print(f"{userInput:.2f} watts is equivalent to {wattsToBTUPerHour(userInput):.2f} BTU per hour")
print(f"{userInput:.2f} liters per second is equivalent to {LpsToGpm(userInput):.2f} US gallons per minute")
print(f"{userInput:.2f} degrees Celsius is equivalent to {celciusToFarenheit(userInput):.2f} degrees Fahrenheit")



