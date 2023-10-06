# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 7
# Date: 6 October 2023
inputNum = input("Enter a four-digit integer: ")
#add leading zeros if needed
if len(inputNum) < 4:
    for i in range(4-len(inputNum)):
        inputNum = "0" + inputNum
inputNum = inputNum
iterations = []
currentNum = inputNum
ascendNum = 0
decsendNum = 0
#loop until reacah 6174
while currentNum != 6174:
    currentNum = str(currentNum)
    if len(currentNum) < 4:
        for i in range(4-len(currentNum)):
            currentNum = "0" + currentNum
    currentNum = list(currentNum)
    currentNum.sort()
    ascendNum = int("".join(currentNum))
    currentNum.sort(reverse=True)
    decsendNum = int("".join(currentNum))
    if decsendNum > ascendNum:
        currentNum = decsendNum - ascendNum
    else:
        currentNum = ascendNum - decsendNum
    iterations.append(int(currentNum))
    if currentNum == 0:
        break
print(f"{int(inputNum)}", end="")
for num in iterations:
    print(" > " + str(num), end="")
print()
print(f"{int(inputNum)} reaches {currentNum} via Kaprekar's routine in {len(iterations)} iterations")
    
    