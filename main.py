import pandas as pd
import numpy as np
from pyscript import PyScript
ps = PyScript()

# Function to convert checkbox values to float
def checkboxToFloat(value):
        return float(value == 'on') if value else 0.0

# Function to convert text values to float, defaulting to 0.0 if empty
def textToFloat(value):
    return float(value) if value else 0.0

def performCalc(event):
    
    
    # Assuming you have HTML elements with the specified IDs
    highBP = checkboxToFloat(ps.get_value("#HighBP"))
    highChol = checkboxToFloat(ps.get_value("#HighChol"))
    cholCheck = checkboxToFloat(ps.get_value("#CholCheck"))
    smoke = checkboxToFloat(ps.get_value("#Smoke"))
    stroke = checkboxToFloat(ps.get_value("#Stroke"))
    heartDiseaseOrAttack = checkboxToFloat(ps.get_value("#HeartDiseaseOrAttack"))
    physAct = checkboxToFloat(ps.get_value("#PhysAct"))
    fruit = checkboxToFloat(ps.get_value("#Fruit"))
    veg = checkboxToFloat(ps.get_value("#Veg"))
    hvyAlcCons = checkboxToFloat(ps.get_value("#HvyAlcCons"))
    healthcare = checkboxToFloat(ps.get_value("#Healthcare"))
    noDocCost = checkboxToFloat(ps.get_value("#NoDocCost"))
    diffWalk = checkboxToFloat(ps.get_value("#DiffWalk"))
    # Construct the enteredData dictionary
    enteredData = {
    'Diabetes_012': 0.0,
    'HighBP': highBP,
    'HighChol': highChol,
    'CholCheck': cholCheck,
    'BMI': textToFloat(ps.get_value("#BMI")),
    'Smoker': smoke,
    'Stroke': stroke,
    'HeartDiseaseOrAttack': heartDiseaseOrAttack,
    'PhysActivity': physAct,
    'Fruits': fruit,
    'Veggies': veg,
    'HvyAlcoholConsump': hvyAlcCons,
    'AnyHealthcare': healthcare,
    'NoDocbcCost': noDocCost,
    'GenHlth': textToFloat(ps.get_value("#genHealth")),
    'MentHlth': textToFloat(ps.get_value("#mentalHealth")),
    'PhysHlth': textToFloat(ps.get_value("#physHealth")),
    'DiffWalk': diffWalk,
    'Sex': textToFloat(ps.get_value("#gender")),
    'Age': textToFloat(ps.get_value("#age")),
    'Education': textToFloat(ps.get_value("#eduLevel")),
    'Income': textToFloat(ps.get_value("#income")),
    }
    csv_file_path = './Type12.csv'
    df = pd.read_csv(csv_file_path)
    enteredDf = pd.DataFrame([enteredData])
    #ensures column names are the same
    dfCols = df.columns
    #Reindexes enteredDf so the data types are the same
    enteredDf = enteredDf.reindex(columns=dfCols, fill_value=None)
    #Resets index
    df = df.reset_index(drop=True)
    enteredDf = enteredDf.reset_index(drop=True)
    #Print functions to check data types and column names are correct
    #print(df.info())
    #print(enteredDf.info())
    #Locks just the first row as a var since thats what needs to be compared
    firstRowEnteredDf = enteredDf.iloc[0]
    #Does the comparison
    comparisonResult = (df == firstRowEnteredDf)
        
    colMatch = comparisonResult.all()
    rowMatch = comparisonResult.all(axis=1)
    allMatches = comparisonResult.all().all()
    matchingPercent = comparisonResult.mean() * 100
    print(f'column matches: {colMatch}')
    print(f'Row matches: {rowMatch}')
    print(f'All matches: {allMatches}')     
    print(f'Match Percent: \n{matchingPercent}')
    #outputDiv= document.querySelector("#output")
    #outputDiv.innerText = 'processed {lineCount} lines. \n{PercentType0} are not diabetic. \n{PercentType1} Have are type 1 \n{PercentType2} Have are type 2'
######################################MAIN#######################################
performCalc()