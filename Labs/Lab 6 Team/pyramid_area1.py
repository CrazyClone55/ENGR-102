# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 6 team : pyramid_area1
# Date: 27 September 2023


# To ask for inputs (side length/ number of layers)
sideLength = float(input("Enter the side length in meters:"))
numberOfLayers = int(input("Enter the number of layers:")) 

triangleTopArea = ((3**0.5)/4)*(sideLength**2)

def outerArea():
    outerArea = 0
    for i in range(1, numberOfLayers+1):
        outerArea += i*(sideLength**2)*3
    return outerArea

def topArea():
    topArea = 0
    for i in range(numberOfLayers,0,-1):
        layerTopArea = (i**2)*triangleTopArea
        aboveLayerArea = ((i-1)**2)*triangleTopArea
        topArea += layerTopArea - aboveLayerArea
    return topArea
# Final amount of foil needed       
print(f'You need {outerArea()+topArea():.2f} m^2 of gold foil to cover the pyramid')