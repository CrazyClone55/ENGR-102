# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 7
# Date: 6 October 2023
vowels = ["a", "e", "i", "o", "u", "y"]

inputWord = input("Enter word(s) to convert to Pig Latin: ")

#split input at spaces into list of words
wordlist = inputWord.split(" ")
output = ""
#for each word in the list check if it starts with vowel or not
for word in wordlist:
    #if its not a vowel, iterate until you reach a vowel while adding the first letter to the end
    if word[0] not in vowels:
        while word[0] not in vowels:
            word = word[1:] + word[0]
        output = output + word+ "ay" + " "
    else:
        output = output + word + "yay" + " "
        
print("In Pig Latin, \""+inputWord+"\" is: "+output)