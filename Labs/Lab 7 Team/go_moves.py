# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 7 team : go_moves
# Date: 4 October 2023

from colorama import Fore, Style

playGame = True #boolean to keep track of if the player wants to continue playing the game
white = chr(9675) # displays empty circle: ○
black = chr(9679) # displays filled circle: ●

# board, 2 dimensional list of 9 rows and 9 columns filled with "."
board = [["." for i in range(9)] for j in range(9)]

#function to print board neatly
def print_board():
    print(Fore.RED + Style.BRIGHT + "\tGO" + Fore.RESET + Style.NORMAL)
    for i in range(9):
        print(" ", end="")
        for j in range(9):
            print(board[i][j], end=" ")
        print()
    
#function that can be looped to ask for input until the player enters a valid input
def place_piece(row, col, piece):
    row = int(row) -1
    col = int(col) -1
    if row < 0 or row > 8 or col < 0 or col > 8:
        print("Invalid space. Please enter a space actually on the board.")
        return True
    elif board[row][col] == ".":
        board[row][col] = piece
        return False
    else:
        print("Invalid space. Please enter a space that is not already occupied.")
        return True
        

#keep letting the players play piece until the game is over
while(playGame):
    print_board()
    #black goes first
    #boolean to keep track of if the player has entered a valid input
    loopInput = True
    while(loopInput):
        #subract 1 so that the player can enter 1-9 instead of 0-8
        row = input("Black, Enter the row you want to place your piece: ")
        if row == "stop":
            playGame = False
            break
        col = input("Black, Enter the column you want to place your piece: ")
        loopInput = place_piece(row,col,black)
    print_board()
    
    #white goes second
    loopInput = True
    while(loopInput):
        row = input("White, Enter the row you want to place your piece: ")
        if row == "stop":
            playGame = False
            break
        col = input("White, Enter the column you want to place your piece: ")
        loopInput = place_piece(row,col,white)
print("\n\n\n\n\n\n")
print_board()
print("Thanks for Playing!")