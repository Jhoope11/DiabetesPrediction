import csv
import math

def performCalc(event):
    with open('./Type12.csv') as csvFile:
        csvReader= csv.reader(csvFile,delimiter=',')
        lineCount=0
        PercentType1 = 0
        PercentType2 = 0
        PercentType0 = 0
        for row in csvReader:
            if lineCount == 0:
                print(f'Col names are {", ".join(row)} ')
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
        x = lineCount - 1
        print(f'{PercentType0} Are not diabetic \n{PercentType1} Have Type 1 \n{PercentType2} Have Type 2')
        PercentType0 = PercentType0 / x * 100
        PercentType1 = PercentType1 / x * 100
        PercentType2 = PercentType2 / x * 100
        print(f'processed {lineCount} lines. \n{PercentType0} are not diabetic. \n{PercentType1} Have are type 1 \n{PercentType2} Have are type 2')
        
######################################MAIN#######################################
#performCalc()