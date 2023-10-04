# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
# 
# Section: 527
# Assignment: Lab 3
# Date: 6 September 2023

from math import sin, radians

def appliedForce(a, mass):
    return mass * a #N

def wavelength(d, theta):
    return 2 * d * sin(radians(theta)) #nm

def decay(initial, time):
    return initial*(1/2)**(time/3.8) #grams

def pressure(moles, volume, temp):
    gasConstant = 8.314
    return (moles*gasConstant*temp)/volume/1000 #kPa

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
a = float(input("\nPlease enter the acceleration (m/s^2): "))
print(f"\nForce is {appliedForce(a, mass):.1f} N")
print()
print("This program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm): "))
angle = float(input("\nPlease enter the angle (degrees): "))
print(f"\nWavelength is {wavelength(d, angle):.4f} nm")
print()
print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initial = float(input("\nPlease enter the initial amount (g): "))
print(f"\nRadon-222 left is {decay(initial, time):.2f} g")
print()
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("\nPlease enter the volume (m^3): "))
temp = float(input("\nPlease enter the temperature (K): "))
print(f"\nPressure is {pressure(moles, volume, temp):.0f} kPa")
