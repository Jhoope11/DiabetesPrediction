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
    # Convert DataFrames to NumPy arrays and exclude the first column
    df_array = df.iloc[:, 1:].to_numpy()
    enteredDf_array = enteredDf.iloc[:, 1:].to_numpy()

    comparisonResult = np.equal(df_array, enteredDf_array)
    # Summary results
    columnMatches = np.all(comparisonResult, axis=0)
    rowMatches = np.all(comparisonResult, axis=1)
    allMatches = np.all(comparisonResult)
    matchingPercent = comparisonResult.mean(axis=0) * 100
    matchingPercentColumns = (comparisonResult.mean(axis=0) * 100).round(2)
    matchingPercentRows = (comparisonResult.mean(axis=1) * 100).round(2)

    # Print the results
    print("\nColumn Matches:")
    print(pd.Series(columnMatches, index=df.columns[1:]))  # Printing with column names

    print("\nRow Matches:")
    print(pd.Series(rowMatches, index=df.index))  # Printing with row indices

    print("\nAll Matches:")
    print(allMatches)

    print("\nMatching Percent (Columns):")
    print(pd.Series(matchingPercentColumns, index=df.columns[1:]))

    print("\nMatching Percent (Rows):")
    print(pd.Series(matchingPercentRows, index=df.index))
    
    print("\nMatching Percent:")
    print(pd.Series(matchingPercent, index=df.columns[1:]))
    #outputDiv= document.querySelector("#output")
    #outputDiv.innerText = 'processed {lineCount} lines. \n{PercentType0} are not diabetic. \n{PercentType1} Have are type 1 \n{PercentType2} Have are type 2'
######################################MAIN#######################################
performCalc()