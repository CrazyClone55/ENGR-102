# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 4
# Date: 19 September 2023

a = float(input('Please enter the coefficient A: '))
b = float(input('Please enter the coefficient B: '))
c = float(input('Please enter the coefficient C: '))

#fringe cases
if (a == 0 and b == 0 and c != 0):
    print('You entered an invalid combination of coefficients!')
    exit()
if (a == 0 and b!= 0):
    print('The root is x =', -c/b)
    exit()
if b**2 - 4*a*c < 0:
    print('The roots are x =', (-b/(2*a)), '+', ((4*a*c - b**2)**0.5)/(2*a), 'i and x =', (-b/(2*a)), '-', ((4*a*c - b**2)**0.5)/(2*a), 'i')
    exit()
    
#main equation
x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

#output
if (x1 == x2):
    print("The root is x =", x1)
else:
    print("The roots are x =", x1, " and x =", x2)
    