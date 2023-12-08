import pandas as pd
import numpy as np
#from pyscript import document

def performCalc():
    enteredData = {
    'Diabetes_012': 0.0,  # Assuming a default value of 0.0 for Diabetes_012
    'HighBP': 1,
    'HighChol': 0.0,  # Assuming a default value of 0.0 for HighChol
    'CholCheck': 1,
    'BMI': 12.0,  # Assuming a default value of 12.0 for BMI
    'Smoker': 1.0,  # Assuming a default value of 1.0 for Smoker
    'Stroke': 1.0,  # Assuming a default value of 1.0 for Stroke
    'HeartDiseaseorAttack': 0.0,  # Assuming a default value of 0.0 for HeartDiseaseorAttack
    'PhysActivity': 1,
    'Fruits': 0,
    'Veggies': 0,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 1,
    'NoDocbcCost': 0.0,  # Assuming a default value of 0.0 for NoDocbcCost
    'GenHlth': 1.0,  # Assuming a default value of 1.0 for GenHlth
    'MentHlth': 1.0,  # Assuming a default value of 1.0 for MentHlth
    'PhysHlth': 1.0,  # Assuming a default value of 1.0 for PhysHlth
    'DiffWalk': 0.0,  # Assuming a default value of 0.0 for DiffWalk
    'Sex': 1,
    'Age': 20,
    'Education': 5.0,  # Assuming a default value of 5.0 for Education
    'Income': 1.0  # Assuming a default value of 1.0 for Income
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