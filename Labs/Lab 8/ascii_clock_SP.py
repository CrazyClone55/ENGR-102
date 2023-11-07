# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Shaan Patel
#               
# Section:      527
# Assignment:   Lab 8.10
# Date:         25 October 2023

clock_type = ""
time = []
allowed_characters = []

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