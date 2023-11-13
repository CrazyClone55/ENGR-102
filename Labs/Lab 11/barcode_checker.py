# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#
# Section: 527
# Assignment: Lab 11
# Date: 15 November 2023

filename = input("Enter the name of the file: ")
file = open(filename, "r")

barcodes = []
valid_barcodes = []

for line in file:
    barcodes.append(line.strip())
    
file.close()

count = 0

for barcode in barcodes:
    #split barcode into groups 1 and 2 and the checkvalue at the end
    numbers = barcode[:-1]
    group1 = list(numbers[0::2])
    group2 = list(numbers[1::2])
    group1 = [int(s) for s in group1]
    group2 = [int(s) for s in group2]
    checkVal = int(barcode[-1])
    #sum the groups
    sum1 = sum(group1)
    sum2 = sum(group2)*3
    #add them together and pull the last digit
    totalSum = sum1 + sum2
    val = str(totalSum)[-1]
    val = 10-int(val)
    
    if checkVal == val:
        valid_barcodes.append(barcode)
        count += 1
    
print(f"There are {count} valid barcodes")
file = open("valid_barcodes.txt", "w")
for barcode in valid_barcodes:
    file.write(barcode + "\n")
file.close()
    
    