# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel 
# Section: 527
# Assignment: Lab 2 individual
# Date: 23 August 2023
from math import sin, radians

a = 1.5 #m/s^2
mass = 27 #kg
force = mass * a #N

d = 0.025 #nm
theta = 35 #degrees
wavelength = 2* d * sin(radians(theta)) #nm

gramsInital = 27
t = 5 #days
halfLife = 3.8 #days
amountLeft = gramsInital*(1/2)**(t/halfLife) #grams

moles = 5
volume = 0.27 #m^3
temp = 415 #K
gasConstant = 8.314
pressure = (moles*gasConstant*temp)/volume #Pa
kpa = pressure/1000 #kPa

print("Force is " + str(force) + " N")
print("Wavelength is " + str(wavelength) + " nm")
print("Radon-222 left is " + str(amountLeft) + " g")
print("Pressure is " + str(kpa) + " kPa")
