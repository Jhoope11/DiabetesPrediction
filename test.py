import csv
import math
import pandas as pd
#from pyscript import document

def sameDataType():
    df = pd.read_csv('Type12 copy.csv')
    df['Diabetes_012'] = pd.to_numeric(df['Diabetes_012'])
    



def performCalc():
    HighBP = 1
    HighChol = 1
    CholCheck = 1
    smoke = 1
    stroke = 1
    heartIssue = 0
    physAct = 1
    fruit = 0
    veg = 0
    hvyDrinker = 0
    healthCare = 1
    noDocBcCost = 0
    diffWalk = 0
    bmi = 12
    genHealth = 1
    mentalHealth = 1
    physHealth = 1
    gender = 1
    age = 20
    eduLevel = 5
    income = 1
    EnteredInfo = [HighBP, HighChol, CholCheck, bmi, smoke, stroke, heartIssue, physAct, fruit, veg, hvyDrinker, healthCare, noDocBcCost, genHealth, mentalHealth, physHealth, diffWalk, gender, age, eduLevel, income]
    csvFile = open('./Type12.csv')
    with open('./Type12.csv') as csvFile:
        csvReader= csv.reader(csvFile,delimiter=',')
        lineCount=0
        PercentType1 = 0
        PercentType2 = 0
        PercentType0 = 0
        matchedCol = 0
        matchedRow = 0
        for row in csvReader:
            if lineCount == 0:
                print(f'Col names are {", ".join(row)} ')
                print(EnteredInfo)
                lineCount+=1
            else:
                y = float(row[0])
                if y == 1.0:
                    PercentType1 += 1
                elif y == 2.0:
                    PercentType2 += 1
                else:
                    PercentType0 += 1
                lineCount +=1
                rowInfo = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21]] 
                for i in EnteredInfo:
                    result1 = type(EnteredInfo[i])
                    result2 = type(rowInfo[i])
                    print(result1,result2)
                    if EnteredInfo[i] == rowInfo[i]:
                        #print(EnteredInfo[i], rowInfo[i])
                        matchedCol += 1
                        #print(f"col match")
                        if matchedCol == 21:
                            print(f"RowMatch")
                            matchedRow += 1

            
        x = lineCount - 1
        print(f'This has {matchedRow} rows That are the same')
        print(f'{PercentType0} Are not diabetic \n{PercentType1} Have Type 1 \n{PercentType2} Have Type 2')
        PercentType0 = PercentType0 / x * 100
        PercentType1 = PercentType1 / x * 100
        PercentType2 = PercentType2 / x * 100
        print(f'processed {lineCount} lines. \n{PercentType0} are not diabetic. \n{PercentType1} Have are type 1 \n{PercentType2} Have are type 2')
        #outputDiv= document.querySelector("#output")
        #outputDiv.innerText = 'processed {lineCount} lines. \n{PercentType0} are not diabetic. \n{PercentType1} Have are type 1 \n{PercentType2} Have are type 2'
######################################MAIN#######################################
sameDataType()