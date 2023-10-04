# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel 
# Section: 527
# Assignment: Lab 2 individual
# Date: 23 August 2023

t1 = 12
t2 = 85

x1 = 8
y1 = 6
z1 = 7

x2 = -5
y2 = 30
z2 = 9

x0 = None
y0 = None
z0 = None

slopeX = (x2-x1)/(t2-t1)
slopeY = (y2-y1)/(t2-t1)
slopeZ = (z2-z1)/(t2-t1)

#time 1
interTime1 = 30 + (30/4)*0
x0 = slopeX*(interTime1-t1)+x1
y0 = slopeY*(interTime1-t1)+y1
z0 = slopeZ*(interTime1-t1)+z1

print("At time "+ str(interTime1)+" seconds:")
print("x1 = "+ str(x0)+ " m")
print("y1 = "+ str(y0)+ " m")
print("z1 = "+ str(z0)+ " m")

print("-----------------------")

#time 2
interTime2 = 30 + (30/4)*1
x0 = slopeX*(interTime2-t1)+x1
y0 = slopeY*(interTime2-t1)+y1
z0 = slopeZ*(interTime2-t1)+z1

print("At time "+ str(interTime2)+" seconds:")
print("x2 = "+ str(x0)+ " m")
print("y2 = "+ str(y0)+ " m")
print("z2 = "+ str(z0)+ " m")

print("-----------------------")

#time 3
interTime3 = 30 + (30/4)*2
x0 = slopeX*(interTime3-t1)+x1
y0 = slopeY*(interTime3-t1)+y1
z0 = slopeZ*(interTime3-t1)+z1

print("At time "+ str(interTime3)+" seconds:")
print("x3 = "+ str(x0)+ " m")
print("y3 = "+ str(y0)+ " m")
print("z3 = "+ str(z0)+ " m")

print("-----------------------")

#time 4
interTime4 = 30 + (30/4)*3
x0 = slopeX*(interTime4-t1)+x1
y0 = slopeY*(interTime4-t1)+y1
z0 = slopeZ*(interTime4-t1)+z1

print("At time "+ str(interTime4)+" seconds:")
print("x4 = "+ str(x0)+ " m")
print("y4 = "+ str(y0)+ " m")
print("z4 = "+ str(z0)+ " m")

print("-----------------------")

#time 5
interTime5 = 30 + (30/4)*4
x0 = slopeX*(interTime5-t1)+x1
y0 = slopeY*(interTime5-t1)+y1
z0 = slopeZ*(interTime5-t1)+z1

print("At time "+ str(interTime5)+" seconds:")
print("x5 = "+ str(x0)+ " m")
print("y5 = "+ str(y0)+ " m")
print("z5 = "+ str(z0)+ " m")




