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

#Activity2

time1 = float(input("Enter time 1: \n"))
x1 = float(input("Enter the x position of the object at time 1: \n"))
y1 = float(input("Enter the y position of the object at time 1: \n"))
z1 = float(input("Enter the z position of the object at time 1: \n"))
time2 = float(input("Enter time 2: \n"))
x2 = float(input("Enter the x position of the object at time 2: \n"))
y2 = float(input("Enter the y position of the object at time 2: \n"))
z2 = float(input("Enter the z position of the object at time 2: \n"))
print()

xSlope = (x2 - x1) / (time2 - time1)
ySlope = (y2 - y1) / (time2 - time1)
zSlope = (z2 - z1) / (time2 - time1)

timeDifference = time2 - time1
times = [time1, time1+timeDifference/4, time1+timeDifference/2, time1+timeDifference*3/4, time2]

def interpolate(slope, inputTime, y1):
    return slope * (inputTime - times[0]) + y1

print(f"At time {times[0]:.2f} seconds the object is at ({interpolate(xSlope, times[0], x1):.3f}, {interpolate(ySlope, times[0], y1):.3f}, {interpolate(zSlope, times[0], z1):.3f})")
print(f"At time {times[1]:.2f} seconds the object is at ({interpolate(xSlope, times[1], x1):.3f}, {interpolate(ySlope, times[1], y1):.3f}, {interpolate(zSlope, times[1], z1):.3f})")
print(f"At time {times[2]:.2f} seconds the object is at ({interpolate(xSlope, times[2], x1):.3f}, {interpolate(ySlope, times[2], y1):.3f}, {interpolate(zSlope, times[2], z1):.3f})")
print(f"At time {times[3]:.2f} seconds the object is at ({interpolate(xSlope, times[3], x1):.3f}, {interpolate(ySlope, times[3], y1):.3f}, {interpolate(zSlope, times[3], z1):.3f})")
print(f"At time {times[4]:.2f} seconds the object is at ({interpolate(xSlope, times[4], x1):.3f}, {interpolate(ySlope, times[4], y1):.3f}, {interpolate(zSlope, times[4], z1):.3f})")

