import random

sex = ["F", "M"]
ageList = [22, 36, 41, 47, 52,57,62,67,72,77]
def age():
    return random.choice(ageList)
choList = [158, 173, 203,264,294]
def cho():
    return random.choice(choList)  
smo = ["Y", "N"]
hdlList = [61,54,44, 34]
def hdl():
    return random.choice(hdlList)
sbpList = [118, 125,135,145,165]
def sbp():
    return random.choice(sbpList)
med = ["Y", "N"]



pointTotal = 0






fileRead = open("test_cases.py", "r")
file = open("test_cases.py", "a")
wantedScores = [1, 9, 10, 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
index = 0
for i in range(250):
    existingOutputs = fileRead.read().split("\n")
    
    sexChoice = random.choice(sex)
    ageChoice = random.choice(ageList)
    choChoice = random.choice(choList)
    smoChoice = random.choice(smo)
    hdlChoice = random.choice(hdlList)
    sbpChoice = random.choice(sbpList)
    medChoice = random.choice(med)
    
    pointTotal=0
    risk = 0
    
    if sexChoice == "M":
        if ageChoice < 35:
            pointTotal -= 9
        elif ageChoice < 40:
            pointTotal -= 4
        elif ageChoice < 45:
            pointTotal += 0
        elif ageChoice < 50:
            pointTotal += 3
        elif ageChoice < 55:
            pointTotal += 6
        elif ageChoice < 60:
            pointTotal += 8
        elif ageChoice < 65:
            pointTotal += 10
        elif ageChoice < 70:
            pointTotal += 11
        elif ageChoice < 75:
            pointTotal += 12
        elif ageChoice < 80:
            pointTotal += 13
            
        if ageChoice < 40:            
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 4
            elif choChoice < 240:
                pointTotal += 7
            elif choChoice < 280:
                pointTotal += 9
            else:
                pointTotal += 11
                
            if smoChoice == "Y":
                pointTotal += 8
                
        elif ageChoice < 50:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 3
            elif choChoice < 240:
                pointTotal += 5
            elif choChoice < 280:
                pointTotal += 6
            else:
                pointTotal += 8
                
            if smoChoice == "Y":
                pointTotal += 5
        elif ageChoice < 60:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 2
            elif choChoice < 240:
                pointTotal += 3
            elif choChoice < 280:
                pointTotal += 4
            else:
                pointTotal += 5
                
            if smoChoice == "Y":
                pointTotal += 3
        elif ageChoice < 70:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 1
            elif choChoice < 240:
                pointTotal += 1
            elif choChoice < 280:
                pointTotal += 2
            else:
                pointTotal += 3
                
            if smoChoice == "Y":
                pointTotal += 1
        elif ageChoice < 80:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 0
            elif choChoice < 240:
                pointTotal += 0
            elif choChoice < 280:
                pointTotal += 1
            else:
                pointTotal += 1
                
            if smoChoice == "Y":
                pointTotal += 1
                
        if hdlChoice < 40:
            pointTotal += 2
        elif hdlChoice < 50:
            pointTotal += 1
        elif hdlChoice < 60:
            pointTotal += 0
        else:
            pointTotal -= 1
            
            
        if medChoice == "Y":
            if sbpChoice < 120:
                pointTotal += 0
            elif sbpChoice < 130:
                pointTotal += 1
            elif sbpChoice < 140:
                pointTotal += 2
            elif sbpChoice < 160:
                pointTotal += 2
            else:
                pointTotal += 3
        else:
            if sbpChoice < 120:
                pointTotal += 0
            elif sbpChoice < 130:
                pointTotal += 0
            elif sbpChoice < 140:
                pointTotal += 1
            elif sbpChoice < 160:
                pointTotal += 1
            else:
                pointTotal += 2
                
        if pointTotal < 0:
            risk = "<1"
        elif pointTotal < 5:
            risk = "1"
        elif pointTotal < 7:
            risk = "2"
        elif pointTotal == 7:
            risk = "3"
        elif pointTotal == 8:
            risk = "4"
        elif pointTotal == 9:
            risk = "5"
        elif pointTotal == 10:
            risk = "6"
        elif pointTotal == 11:
            risk = "8"
        elif pointTotal == 12:
            risk = "10"
        elif pointTotal == 13:
            risk = "12"
        elif pointTotal == 14:
            risk = "16"
        elif pointTotal == 15:
            risk = "20"
        elif pointTotal == 16:
            risk = "25"
        else:
            risk = ">30"
    #Female
    else:
        if ageChoice < 35:
            pointTotal -= 7
        elif ageChoice < 40:
            pointTotal -= 3
        elif ageChoice < 45:
            pointTotal += 0
        elif ageChoice < 50:
            pointTotal += 3
        elif ageChoice < 55:
            pointTotal += 6
        elif ageChoice < 60:
            pointTotal += 8
        elif ageChoice < 65:
            pointTotal += 10
        elif ageChoice < 70:
            pointTotal += 12
        elif ageChoice < 75:
            pointTotal += 14
        elif ageChoice < 80:
            pointTotal += 16
            
        if ageChoice < 40:            
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 4
            elif choChoice < 240:
                pointTotal += 8
            elif choChoice < 280:
                pointTotal += 11
            else:
                pointTotal += 13
                
            if smoChoice == "Y":
                pointTotal += 9
                
        elif ageChoice < 50:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 3
            elif choChoice < 240:
                pointTotal += 6
            elif choChoice < 280:
                pointTotal += 8
            else:
                pointTotal += 10
                
            if smoChoice == "Y":
                pointTotal += 7
        elif ageChoice < 60:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 2
            elif choChoice < 240:
                pointTotal += 4
            elif choChoice< 280:
                pointTotal += 5
            else:
                pointTotal += 7
                
            if smoChoice == "Y":
                pointTotal += 4
        elif ageChoice < 70:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 1
            elif choChoice < 240:
                pointTotal += 2
            elif choChoice < 280:
                pointTotal += 3
            else:
                pointTotal += 4
                
            if smoChoice == "Y":
                pointTotal += 2
        elif ageChoice < 80:
            if choChoice < 161:
                pointTotal += 0
            elif choChoice < 200:
                pointTotal += 1
            elif choChoice < 240:
                pointTotal += 1
            elif choChoice < 280:
                pointTotal += 2
            else:
                pointTotal += 2
                
            if smoChoice == "Y":
                pointTotal += 1
                
        if hdlChoice < 40:
            pointTotal += 2
        elif hdlChoice < 50:
            pointTotal += 1
        elif hdlChoice < 60:
            pointTotal += 0
        else:
            pointTotal -= 1
            
            
        if medChoice == "Y":
            if sbpChoice < 120:
                pointTotal += 0
            elif sbpChoice < 130:
                pointTotal += 3
            elif sbpChoice < 140:
                pointTotal += 4
            elif sbpChoice < 160:
                pointTotal += 5
            else:
                pointTotal += 6
        else:
            if sbpChoice < 120:
                pointTotal += 0
            elif sbpChoice < 130:
                pointTotal += 1
            elif sbpChoice < 140:
                pointTotal += 2
            elif sbpChoice < 160:
                pointTotal += 3
            else:
                pointTotal += 4
                
        if pointTotal < 9:
            risk = "<1"
        elif pointTotal == 9:
            risk = "1"
        elif pointTotal == 10:
            risk = "1"
        elif pointTotal == 11:
            risk = "1"
        elif pointTotal == 12:
            risk = "1"
        elif pointTotal == 13:
            risk = "2"
        elif pointTotal == 14:
            risk = "2"
        elif pointTotal == 15:
            risk = "3"
        elif pointTotal == 16:
            risk = "4"
        elif pointTotal == 17:
            risk = "5"
        elif pointTotal == 18:
            risk = "6"
        elif pointTotal == 19:
            risk = "8"
        elif pointTotal == 20:
            risk = "11"
        elif pointTotal == 21:
            risk = "14"
        elif pointTotal == 22:
            risk = "17"
        elif pointTotal == 23:
            risk = "22"
        elif pointTotal == 24:
            risk = "27"
        else:
            risk = ">30"
    strOut = (f'sex:{sexChoice} age:{ageChoice} cho:{choChoice} smo:{smoChoice} hdl:{hdlChoice} sbp:{sbpChoice} med:{medChoice} out:{risk}')
    if (strOut not in existingOutputs):
        file.write("\n" + strOut)
    
    #if pointTotal == wantedScores[index]:
    #if strOut[-3:] == wantedScore:
        #index += 1
    