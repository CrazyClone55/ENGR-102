# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 4 team
# Date: 13 September 2023

############ Part A ############

a = str(input("Enter True or False for a: "))
b = str(input("Enter True or False for b: "))
c = str(input("Enter True or False for c: "))

if a == "True" or a == "T" or a == "t":
    a = True
elif a == "False" or a == "F" or a == "f":
    a = bool(False)
else:
    exit("Please enter True, T, t, False, F, or f")

if b == "True" or b == "T" or b == "t":
    b = bool(True)
elif b == "False" or b == "F" or b == "f":
    b = bool(False)
else:
    exit("Please enter True, T, t, False, F, or f")

if c == "True" or c == "T" or c == "t":
    c = True
elif c == "False" or c == "F" or c == "f":
    c = bool(False)
else:
    exit("Please enter True, T, t, False, F, or f")

############ Part B ############

print("a and b and c: " + str(a and b and c))
print("a or b or c: " + str(a or b or c))

############ Part C ############

print("XOR: " + str((a or b) and not(a and b)))
print("Odd number: " + str(((a or b or c) and not((a and b) or (a and c) or (b and c))) or (a and b and c)))

############ Part D ############

print("Complex 1: " + str((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)))
print("Complex 2: " + str((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))))

#print("Simple 1: " + str((b and not a)or(b and not c)or(a and not b)))
#print("Simple 2: ")