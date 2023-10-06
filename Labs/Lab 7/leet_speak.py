# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 7
# Date: 6 October 2023
dictionary = {"a":"4", "e":"3", "o":"0", "s":"5", "t":"7"}

inputPhrase = input("Enter some text: ")
output = inputPhrase
#iterate through the phrase as if it were a list and replace the letters in place
for letter in output:
    if letter.lower() in dictionary:
        output = output.replace(letter, dictionary[letter.lower()])

print("In leet speak, \""+inputPhrase+"\" is:")
print(output)