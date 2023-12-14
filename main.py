import pandas as pd
import numpy as np
from pyscript import PyScript

def performCalc(event):
    ps = PyScript()
    
    
    HighBP = ps.get_value("#HighBP")
    HighChol = ps.get_value("#HighChol")
    CholCheck = ps.get_value("#CholCheck")
    Smoke = ps.get_value("#Smoke")
    Stroke = ps.get_value("#Stroke")
    HeartDiseaseOrAttack = ps.get_value("#HeartDiseaseOrAttack")
    PhysAct = ps.get_value("#PhysAct")
    Fruit = ps.get_value("#Fruit")
    Veg = ps.get_value("#Veg")
    HvyAlcCons = ps.get_value("#HvyAlcCons")
    Healthcare = ps.get_value("#Healthcare")
    NoDocCost = ps.get_value("#NoDocCost")
    DiffWalk = ps.get_value("#DiffWalk")

    # Convert checkbox values to float
    HighBP = float(HighBP == 'on')
    HighChol = float(HighChol == 'on')
    CholCheck = float(CholCheck == 'on')
    Smoke = float(Smoke == 'on')
    Stroke = float(Stroke == 'on')
    HeartDiseaseOrAttack = float(HeartDiseaseOrAttack == 'on')
    PhysAct = float(PhysAct == 'on')
    Fruit = float(Fruit == 'on')
    Veg = float(Veg == 'on')
    HvyAlcCons = float(HvyAlcCons == 'on')
    Healthcare = float(Healthcare == 'on')
    NoDocCost = float(NoDocCost == 'on')
    DiffWalk = float(DiffWalk == 'on')
    # Construct the enteredData dictionary
    enteredData = {
    'Diabetes_012': 0.0,
    'HighBP': HighBP,
    'HighChol': HighChol,
    'CholCheck': CholCheck,
    'BMI': float(ps.get_value("#BMI")),
    'Smoker': Smoke,
    'Stroke': Stroke,
    'HeartDiseaseorAttack': HeartDiseaseOrAttack,
    'PhysActivity': PhysAct,
    'Fruits': Fruit,
    'Veggies': Veg,
    'HvyAlcoholConsump': HvyAlcCons,
    'AnyHealthcare': Healthcare,
    'NoDocbcCost': NoDocCost,
    'GenHlth': float(ps.get_value("#genHealth")),
    'MentHlth': float(ps.get_value("#mentalHealth")),
    'PhysHlth': float(ps.get_value("#physHealth")),
    'DiffWalk': DiffWalk,
    'Sex': float(ps.get_value("#gender")),
    'Age': float(ps.get_value("#age")),
    'Education': float(ps.get_value("#eduLevel")),
    'Income': float(ps.get_value("#income")),
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