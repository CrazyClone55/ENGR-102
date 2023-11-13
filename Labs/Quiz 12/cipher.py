import numpy as np

dict = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}
dict1 = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
file = open("cipher.txt", "r")

rawString = file.read()

inputString = rawString.split("\n")

matrix = np.matrix([[0]*100 for i in range(100)])

count = 0
for i in range(100):
    for j in range(100):
        matrix[i,j] = int(inputString[count])
        count += 1

number1 = 0

for i in range(5):
    number1+= matrix[i,85]
    
number2 = matrix.sum(axis=1)[4]/100
number2 = int(number2[0,0])

row = matrix[62]
row = row.tolist()[0]
number3 = sum(row[-5:])

row = matrix[0]
row = row.tolist()[0]
number4 = min(row)

row = matrix[29]
row = row.tolist()[0]
number5 = max(row)

letter1 = dict[number1]
letter2 = dict[number2]
letter3 = dict[number3]
letter4 = dict[number4]
letter5 = dict[number5]

key = letter1 + letter2 + letter3 + letter4 + letter5
key = key*5


hiddenMessage = "zsyucavqojhpwomv"
key = key[:len(hiddenMessage)]

hiddenMessage = list(hiddenMessage)
key = list(key)

for i in range(len(hiddenMessage)):
    hiddenMessage[i] = dict1[hiddenMessage[i]]
    key[i] = dict1[key[i]]
    
    
revealedMessage = [0]*len(hiddenMessage)

for i in range(len(hiddenMessage)):
    revealedMessage[i] = (hiddenMessage[i] - key[i])%26
    revealedMessage[i] = dict[revealedMessage[i]]

message = "".join(revealedMessage)

print(message)
print(key)