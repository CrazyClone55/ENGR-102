# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 10 team : sum_squares
# Date: 8 November 2023

from time import time

def all_smaller_squares(n):
    #return all squares that are smaller than n
    squares = []
    for i in range(0,n):
        if i**2 <= n:
            squares.append(i)
    return squares

def list_nums(n):
    squares = all_smaller_squares(n)
    for i in range(len(squares)):
        for j in range(len(squares)):
            for k in range(len(squares)):
                for l in range(len(squares)):
                    if squares[i]**2 + squares[j]**2 + squares[k]**2 + squares[l]**2 == n:
                        return [squares[i],squares[j],squares[k],squares[l]]
                
                    
def count_sets(n):
    count = 0
    combinations = []
    squares = all_smaller_squares(n)
    #print(squares)
    list1 = squares.copy()
    list2 = squares.copy()
    list3 = squares.copy()
    list4 = squares.copy()
    for i in range(len(list1)):
        for j in range(len(list2)):
            for k in range(len(list3)):
                for l in range(len(list4)):
                    if list1[i]**2 + list2[j]**2 + list3[k]**2 + list4[l]**2 == n:
                        temp = [list1[i],list2[j],list3[k],list4[l]]
                        temp.sort()
                        if not temp in combinations:
                            combinations.append(temp)
                            count += 1
    #print(combinations)
    return count
               
    
# how to measure how long your function takes to run:
t1 = time() # get start time
print(count_sets(10000)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result

        