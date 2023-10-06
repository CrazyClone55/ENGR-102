# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 7
# Date: 6 October 2023

inputString = input("Enter numbers: ")
#like previos split at spaces
list1 = inputString.split(" ")
list2 = []
#create new list with integers
for i in list1:
    list2.append(int(i))

#find the total sum of the list then half for the target of each side
totalSum = 0
for i in list2:
    totalSum += i
    
targetSum = totalSum/2
sumLeft = 0
sumRight = 0
leftList = []
rightList = []

#iterate through the list and add to the left list until the sum is greater than the target, then add to the right list
for i in list2:
    if sumLeft < targetSum:
        sumLeft += i
        leftList.append(i)
    else:
        sumRight += i
        rightList.append(i)

#then check it the sums are equal and print the lists
if sumLeft == sumRight:
    print("Left: ", leftList)
    print("Right: ", rightList)
    print("Both sum to ", int(targetSum))
else:
    print("Cannot split evenly")