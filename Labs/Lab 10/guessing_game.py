# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Shaan Patel
#
# Section: 527
# Assignment: Lab 10
# Date: 8 November 2023


def askInput():
    #repeat untill valid input
    repeat = True
    print("What is your guess?")
    while repeat:
        userGuess = input()
        try:
            userGuess = int(userGuess)
            return userGuess
        except ValueError:
            print("Bad input! Try again:")    
    
    
def checkInput(guess, secret, count):
    if guess>secret:
        print("Too high!")
    if guess<secret:
        print("Too low!")
    if guess == secret:
        print(f"You guessed it! It took you {count} guesses.")

secret = 27
guess = None
count = 0
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
while guess != secret:
    guess = askInput()
    count += 1
    checkInput(guess, secret, count)