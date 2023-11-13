# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#
# Section: 527
# Assignment: Lab 11
# Date: 15 November 2023

filename = input("Enter the filename: ")
character = input("Enter a character: ")
input_file = open(filename, "r")
filename=filename[:-4]+".txt"
output_file = open(filename, "w")

#read in all lines
lines = input_file.readlines()
#split it at the commas
for i in range(len(lines)):
    line = lines[i]
    line = line.strip()
    line = line.split(",")
    lines[i] = line
#convert it to ints
for line in lines:
    for i in range(len(line)):
        line[i] = int(line[i])
#process it
for line in lines:
    output = ""
    char = False
    for i in range(len(line)):
        if char:
            output += character*line[i]
        else:
            output += " "*line[i]
        char = not char
    output_file.write(output + "\n")







print(f"{filename} created!")