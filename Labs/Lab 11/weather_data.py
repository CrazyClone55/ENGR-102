# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Shaan Patel
#
# Section: 527
# Assignment: Lab 11
# Date: 15 November 2023
import copy

file = open("WeatherDataCLL.csv", "r")
uniqueYears = []
dict = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
          "Nov", "Dec"]
monthDict = {}

for month in months:
    monthDict[month] = []
    
YearDict = {}

lines = file.readlines()


for line in lines:
    line = line.strip()
    line = line.split(",")
    date = line[0].split("/")
    
    if date[0] == "Date":
        continue
    
    if date[2] not in uniqueYears:
        uniqueYears.append(date[2])
    
    
for year in uniqueYears:
    #regular copy wasnt enough as it only copied the reference for the lists, and didnt create new lists within the dictionary
    YearDict[year] = copy.deepcopy(monthDict)

for line in lines:
    line = line.strip()
    line = line.split(",")
    
    if line[0] == "Date":
        continue
    date = line[0].split("/")
    
    YearDict[date[2]][dict[int(date[0])]].append(line[1:])


outFile = open("WeatherDataCLL.txt", "w")
outFile.write(str(YearDict))

maxTemps = []
minTemps = []
for year in uniqueYears:
    for month in months:
        for item in YearDict[year][month]:
            try:
                maxTemps.append(int(item[4]))
                minTemps.append(int(item[5]))
            except:
                continue
            
print(f"10-year maximum temperature: {max(maxTemps)} F")
print(f"10-year minimum temperature: {min(minTemps)} F")

inputMonth = input("Please enter a month: ")
inputYear = input("Please enter a year: ")

print(f"For {inputMonth} {inputYear}:")
inputMonth = inputMonth[:3]

data = YearDict[inputYear][inputMonth].copy()

averageTemps = []
relativeHumidity = []
windSpeed = []
precipitation = []

for line in data:
    try:
        averageTemps.append(int(line[3]))
    except:
        continue
    
for line in data:
    try:
        relativeHumidity.append(int(line[2]))
    except:
        relativeHumidity.append(0)
    
for line in data:
    try:
        windSpeed.append(float(line[0]))
    except:
        windSpeed.append(0)
    
for line in data:
    try:
        precipitation.append(float(line[1]))
    except:
        precipitation.append(0)
    
count = 0
for day in precipitation:
    if day > 0:
        count += 1 
    
print(f"Mean average daily temperature: {sum(averageTemps)/len(averageTemps):.1f} F")
print(f"Mean relative humidity: {sum(relativeHumidity)/len(relativeHumidity):.1f} %")
print(f"Mean daily wind speed: {sum(windSpeed)/len(windSpeed):.2f} mph")
print(f"Percentage of days with precipitation: {count/len(precipitation)*100:.1f} %")