# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 4
# Date: 19 September 2023
    
#use recursion insteaf of loops
def recursiveGadgets(day):
    if day>10:
        gadgets = recursiveGadgets(day-1) + day
        return gadgets
    else:
        return 0
    

day = int(input("Please enter a positive value for day: "))


if day < 0:
    print("You entered an invalid number!")
    exit()


gadgetsMade = 0

if day <= 10:
    gadgetsMade = day*10
elif (day <=50):
    gadgetsMade = 100
    gadgetsMade += recursiveGadgets(day)
elif(day<=101):
    gadgetsMade = 100
    gadgetsMade += recursiveGadgets(50)
    gadgetsMade += 50*(day-50)
else:
    gadgetsMade = 100
    gadgetsMade += recursiveGadgets(50)
    gadgetsMade += 50*(100-50)

print(f'The sum total number of gadgets produced on day {day} is {gadgetsMade}')    

    
