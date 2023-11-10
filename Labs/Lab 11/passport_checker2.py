# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#       Braeden Krieger
#       Lauren Falsone
#       Zainab Almajed
# Section: 527
# Assignment: Lab 11 team : passport_checker2.py
# Date: 15 November 2023

class Passport:
    BirthYear = None
    IssueYear = None
    ExpiraionYear = None
    Height = None
    HairColor = None
    EyeColor = None # not required
    PID = None
    CID = None
    rawData = None
    
    def __init__(self, data, rawData):
        self.BirthYear = (data.get("byr"))
        self.IssueYear = (data.get("iyr"))
        self.ExpiraionYear = (data.get("eyr"))
        self.Height = data.get("hgt")
        self.HairColor = data.get("hcl")
        self.EyeColor = data.get("ecl")
        self.PID = data.get("pid")
        self.CID = data.get("cid")
        
        self.rawData = rawData
        
    def heightValid(self):
        if self.Height == None:
            return False
        if self.Height[-2:] == "cm":
            if 150 <= int(self.Height[:-2]) <= 193:
                return True
            else:
                return False
        elif self.Height[-2:] == "in":
            if 59 <= int(self.Height[:-2]) <= 76:
                return True
            else:
                return False
        else:
            return False
        
        
    def hairColorValid(self):
        if self.HairColor == None:
            return False
        if self.HairColor[0] == "#" and len(self.HairColor) == 7:
            for char in self.HairColor[1:]:
                if char not in "0123456789abcdef":
                    return False
            return True
        else:
            return False    
        
        
    def isValid(self):
        
        if (self.BirthYear != None and 1920 <= int(self.BirthYear) <= 2007 and
            self.IssueYear != None and 2013 <= int(self.IssueYear) <= 2023 and
            self.ExpiraionYear != None and 2023 <= int(self.ExpiraionYear) <= 2033 and 
            self.PID != None and len(self.PID) == 9 and self.PID.isdigit() and
            self.CID != None and len(str(int(self.CID))) == 3 and self.CID.isdigit() and
            self.heightValid() and
            self.hairColorValid()):
            return True
        else:
            return False
        
def readPassports(filename, passports):
    file = open(filename, "r")
    lines = file.readlines()
    
    while lines:
        rawData = ""
        dict = {"byr":None,"iyr":None,"eyr":None,"hgt":None,"hcl":None,"ecl":None,"pid":None,"cid":None}
        currentLine = lines.pop(0)
        rawData += currentLine
        while currentLine != "\n":
            currentLine = currentLine.strip()
            currentLine = currentLine.split(" ")
            
            for item in currentLine:
                item = item.split(":")
                dict.update({item[0]: item[1]})
                
            try:
                currentLine = lines.pop(0)
                rawData += currentLine
            except:
                break
            
        
        tempPassport = Passport(dict, rawData)
        passports.append(tempPassport)
    file.close()
        
def printValidPassports(passports):
    output = ""
    validPassports = 0
    for passport in passports:
        if passport.isValid():
            validPassports += 1
            output += passport.rawData
            
    file = open("valid_passports2.txt", "w")
    file.write(output)
    print(f"There are {validPassports} valid passports")
    
    
fileName = input("Enter the name of the file: ")
Passports = []

readPassports(fileName, Passports)
printValidPassports(Passports)
    