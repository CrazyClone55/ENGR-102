# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 6 team : pyramid_area2
# Date: 27 September 2023

# To ask for inputs (side length/ number of layers)
sideLength = float(input("Enter the side length in meters:"))
layers = int(input("Enter the number of layers:"))


def triangleTopArea():
    return ((3**0.5)/4)*sideLength**2

def sideArea():
    return (sideLength**2)*3*layers*(layers+1)/2

def topArea():
    return (layers**2)*((3**0.5)/4)*sideLength**2

print(f'You need {sideArea()+topArea():.2f} m^2 of gold foil to cover the pyramid')