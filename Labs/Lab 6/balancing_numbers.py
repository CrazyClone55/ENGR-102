# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 6
# Date: 29 September 2023
n = int(input("Enter a value for n: "))

#comment
sum1 = 0
for i in range(1, n):
    sum1 += i
sum2 = 0
startnum = n+1
while sum2 < sum1:
    sum2 += startnum+1
    startnum+=1
r = startnum-n-1

sum2 -= r
if sum1 == sum2:
    print(f"{n} is a balancing number with r={r}")
else:
    print(f"{n} is not a balancing number")