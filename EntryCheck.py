import csv
import math
with open('Type12.csv') as csvFile:
    csvReader= csv.reader(csvFile,delimiter=',')
    lineCount=0
    for row in csvReader:
        if lineCount == 0:
            print(f'Col names are{",".join(row)}')
            lineCount+=1
        else:
            print(f'\t{row[0]}{row[1]}')
            lineCount +=1
    print(f'processed {lineCount} lines.')