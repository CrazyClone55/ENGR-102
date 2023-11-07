# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 9
# Date: 1 November 2023

from math import pi
def parta(radiusSphere, radiusHole):
    volume = (4/3*pi)*(radiusSphere**2-radiusHole**2)**(3/2) 
    #used integral to revolve a shpere minus the center portion to get forumla
    return volume

def partb(n):
    if n%4==2:
        return False
        #if n mod 4 is 2 it cannot be expressed as the sum of consecutive odd integers so return false
    list=[]
    i=1
    flag=False
    while not flag:
        j=i-1
        while j>=0:
            if ((i*i)-(j*j))==n:
                for k in range(j+1,i+1):
                    list.append((2*k)-1)
                flag=True
                break 
            j-=1
        i+=1 
    if len(list)==1:
        return False
        #return false if only one number is in list meaning it couldnt find numbers for a sum
    return list 

def partc(char, name, company, email):
    #find longest entry
    list = []
    list.append(len(char))
    list.append(len(name))
    list.append(len(company))
    list.append(len(email))
    
    longestEntry = max(list)
    
    cardWidth = longestEntry + 6
    
    #create rows indiviually
    row1 = char*cardWidth
    row2 = char + " "*((cardWidth-2-len(name))//2) + name + " "*(cardWidth-2-len(name)-(cardWidth-2-len(name))//2) + char
    row3 = char + " "*((cardWidth-2-len(company))//2) + company + " "*(cardWidth-2-len(company)-(cardWidth-2-len(company))//2) + char
    row4 = char + " "*((cardWidth-2-len(email))//2) + email + " "*(cardWidth-2-len(email)-(cardWidth-2-len(email))//2) + char
    row5 = row1
    #append them together with line breaks
    return row1 + "\n"+  row2 + "\n" + row3 + "\n" + row4 + "\n" + row5


def partd(list):
    list.sort()
    #find minimum
    minimum = list[0]
    #find median
    if len(list)%2==0:
        median = (list[len(list)//2]+list[(len(list)//2)-1])/2
    else:
        median = list[len(list)//2]
    #find maximum
    maximum = list[-1]
    
    return minimum, median, maximum
    
def parte(times, distances):
    #create new list of velocities between consecutive times
    velocities = []
    for i in range(len(times)-1):
        velocities.append((distances[i+1]-distances[i])/(times[i+1]-times[i]))
    return velocities


def partf(list):
    #determine if two of the numbers in the list add to 2027
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]+list[j]==2027:
                return list[i]*list[j]
    return False