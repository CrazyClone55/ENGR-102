# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Lauren Falsone
#               Shaan Patel
#               Braeden Krieger
#               Zainab Almajed
# Section:      527
# Assignment:   Lab 8.10
# Date:         25 October 2023

# input the time as a list so that you dont have to create another variable
time = list(input("Enter the time: "))
# input the clock type as an integer so that you can convert the time for clock type 12 easier
clock_type = int(input("Choose the clock type (12 or 24): "))
character = input("Enter your preferred character: ")

# make the character into a list so that its easier for the computer to pull out when you index at 0
character_list = []
character_list.append(character)
# had to make a list because loop was not responding to the string in the way it should have
allowed_characters = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'x', 'y', 'z', '@', '$', '&', '*', '=']

# need to create empty lists so that you can append individual lines in order to create the clock
line_1 = []
line_2 = []
line_3 = []
line_4 = []
line_5 = []

# this section is used to calculate the time when the clock type is 12
if clock_type == 12:
    if time[0] == '0':
        hour = '12'
        minute = str(''.join(time[2:]))
        new_time = hour + ':' + minute
    elif len(time) == 4:
        hour = str(''.join(time[0:1]))
        minute = str(''.join(time[2:]))
        new_time = hour + ':' + minute
    elif int(''.join(time[0:2])) == 11 or int(''.join(time[0:2])) == 10:
        hour = str(''.join(time[0:2]))
        minute = str(''.join(time[3:]))
        new_time = hour + ':' + minute
    elif len(time) == 5 and int(''.join(time[0:2])) != 12:
        initial_hour = int(''.join(time[0:2]))
        hour_12 = initial_hour - clock_type
        hour = str(hour_12)
        minute = str(''.join(time[3:]))
        new_time = hour + ':' + minute
    elif int(''.join(time[0:2])) == 12:
        hour = str(''.join(time[0:2]))
        minute = str(''.join(time[3:]))
        new_time = hour + ':' + minute

# this is called if the clock type entered is 24
if clock_type == 24:
    new_time = time

# need to make new_time a list so the for loop is able to access each character
new_time = list(new_time)

# need to create a while loop that repeats until the user enters a valid character
while character_list[0] not in allowed_characters and character_list != ['']:
    print("Character not permitted!", end = ' ')
    character = input('Try again: ')
    character_list = []
    character_list.append(character)

# this solves for a character entered
if character_list[0] in allowed_characters:
    for i in new_time:
        if i == '0':
            line_1.append(character + character + character)
            line_2.append(character + ' ' + character)
            line_3.append(character + ' ' + character)
            line_4.append(character + ' ' + character)
            line_5.append(character + character + character)
        if i == '1':
            line_1.append(' ' + character + ' ')
            line_2.append(character + character + ' ')
            line_3.append(' ' + character + ' ')
            line_4.append(' ' + character + ' ')
            line_5.append(character + character + character) 
        if i == '2':
            line_1.append(character + character + character)
            line_2.append(' ' + ' ' + character)
            line_3.append(character + character + character)
            line_4.append(character + ' ' + ' ')
            line_5.append(character + character + character)
        if i == '3':
            line_1.append(character + character + character)
            line_2.append(' ' + ' ' + character)
            line_3.append(character + character + character)
            line_4.append(' ' + ' ' + character)
            line_5.append(character + character + character)
        if i == '4':
            line_1.append(character + ' ' + character)
            line_2.append(character + ' ' + character)
            line_3.append(character + character + character)
            line_4.append(' ' + ' ' + character)
            line_5.append(' ' + ' ' + character)    
        if i == '5':
            line_1.append(character + character + character)
            line_2.append(character + ' ' + ' ')
            line_3.append(character + character + character)
            line_4.append(' ' + ' ' + character)
            line_5.append(character + character + character)
        if i == '6':
            line_1.append(character + character + character)
            line_2.append(character + ' ' + ' ')
            line_3.append(character + character + character)
            line_4.append(character + ' ' + character)
            line_5.append(character + character + character)
        if i == '7':
            line_1.append(character + character + character)
            line_2.append(' ' + ' ' + character)
            line_3.append(' ' + ' ' + character)
            line_4.append(' ' + ' ' + character)
            line_5.append(' ' + ' ' + character) 
        if i == '8':
            line_1.append(character + character + character)
            line_2.append(character + ' ' + character)
            line_3.append(character + character + character)
            line_4.append(character + ' ' + character)
            line_5.append(character + character + character)
        if i == '9':
            line_1.append(character + character + character)
            line_2.append(character + ' ' + character)
            line_3.append(character + character + character)
            line_4.append(' ' + ' ' + character)
            line_5.append(character + character + character) 
        if i == ':':
            line_1.append(' ')
            line_2.append(':')
            line_3.append(' ')
            line_4.append(':')
            line_5.append(' ')
# this solves for when a user does not enter a character
elif character_list == ['']:
    for i in new_time:
        if i == '0':
            line_1.append('0' + '0' + '0')
            line_2.append('0' + ' ' + '0')
            line_3.append('0' + ' ' + '0')
            line_4.append('0' + ' ' + '0')
            line_5.append('0' + '0' + '0')
        if i == '1':
            line_1.append(' ' + '1' + ' ')
            line_2.append('1' + '1' + ' ')
            line_3.append(' ' + '1' + ' ')
            line_4.append(' ' + '1' + ' ')
            line_5.append('1' + '1' + '1') 
        if i == '2':
            line_1.append('2' + '2' + '2')
            line_2.append(' ' + ' ' + '2')
            line_3.append('2' + '2' + '2')
            line_4.append('2' + ' ' + ' ')
            line_5.append('2' + '2' + '2')
        if i == '3':
            line_1.append('3' + '3' + '3')
            line_2.append(' ' + ' ' + '3')
            line_3.append('3' + '3' + '3')
            line_4.append(' ' + ' ' + '3')
            line_5.append('3' + '3' + '3')
        if i == '4':
            line_1.append('4' + ' ' + '4')
            line_2.append('4' + ' ' + '4')
            line_3.append('4' + '4' + '4')
            line_4.append(' ' + ' ' + '4')
            line_5.append(' ' + ' ' + '4')    
        if i == '5':
            line_1.append('5' + '5' + '5')
            line_2.append('5' + ' ' + ' ')
            line_3.append('5' + '5' + '5')
            line_4.append(' ' + ' ' + '5')
            line_5.append('5' + '5' + '5')
        if i == '6':
            line_1.append('6' + '6' + '6')
            line_2.append('6' + ' ' + ' ')
            line_3.append('6' + '6' + '6')
            line_4.append('6' + ' ' + '6')
            line_5.append('6' + '6' + '6')
        if i == '7':
            line_1.append('7' + '7' + '7')
            line_2.append(' ' + ' ' + '7')
            line_3.append(' ' + ' ' + '7')
            line_4.append(' ' + ' ' + '7')
            line_5.append(' ' + ' ' + '7') 
        if i == '8':
            line_1.append('8' + '8' + '8')
            line_2.append('8' + ' ' + '8')
            line_3.append('8' + '8' + '8')
            line_4.append('8' + ' ' + '8')
            line_5.append('8' + '8' + '8')
        if i == '9':
            line_1.append('9' + '9' + '9')
            line_2.append('9' + ' ' + '9')
            line_3.append('9' + '9' + '9')
            line_4.append(' ' + ' ' + '9')
            line_5.append('9' + '9' + '9') 
        if i == ':':
            line_1.append(' ')
            line_2.append(':')
            line_3.append(' ')
            line_4.append(':')
            line_5.append(' ')
# if the clock type is 12, we need to indicate if it is AM or PM
if clock_type == 12:
    if time[0] == '0' or len(time) == 4 or int(''.join(time[0:2])) == 11 or int(''.join(time[0:2])) == 10:
        line_1.append(' ' + 'A' + ' ' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
        line_2.append('A' + ' ' + 'A' + ' ' + 'M' + 'M' + ' ' + 'M' + 'M')
        line_3.append('A' + 'A' + 'A' + ' ' + 'M' + ' ' + 'M' + ' ' + 'M')
        line_4.append('A' + ' ' + 'A' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
        line_5.append('A' + ' ' + 'A' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
    elif int(''.join(time[0:2])) >= 12:
        line_1.append('P' + 'P' + 'P' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
        line_2.append('P' + ' ' + 'P' + ' ' + 'M' + 'M' + ' ' + 'M' + 'M')
        line_3.append('P' + 'P' + 'P' + ' ' + 'M' + ' ' + 'M' + ' ' + 'M')
        line_4.append('P' + ' ' + ' ' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
        line_5.append('P' + ' ' + ' ' + ' ' + 'M' + ' ' + ' ' + ' ' + 'M')
# Don't forget that you need to create a new line
    #if you do not create a new line, the first line of the clock will print on that same line as the last input statement
print("")
print(' '.join(line_1))
print(' '.join(line_2))
print(' '.join(line_3))
print(' '.join(line_4))
print(' '.join(line_5))