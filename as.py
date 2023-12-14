import pandas as pd
import numpy as np

def performCalc():
# Read data from the CSV file
csv_file_path = 'your_file.csv'
df = pd.read_csv(csv_file_path)

# Assume enteredData is a dictionary
enteredData = {
    'Diabetes_012': 0.0,
    'HighBP': 1,
    'HighChol': 0.0,
    'CholCheck': 1,
    'BMI': 12.0,
    'Smoker': 1.0,
    'Stroke': 1.0,
    'HeartDiseaseorAttack': 0.0,
    'PhysActivity': 1,
    'Fruits': 0,
    'Veggies': 0,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 1,
    'NoDocbcCost': 0.0,
    'GenHlth': 1.0,
    'MentHlth': 1.0,
    'PhysHlth': 1.0,
    'DiffWalk': 0.0,
    'Sex': 1,
    'Age': 20,
    'Education': 5.0,
    'Income': 1.0
}

# Convert enteredData into a DataFrame
enteredDf = pd.DataFrame([enteredData])

# Ensure columns in both DataFrames match
df_columns = df.columns
enteredDf = enteredDf.reindex(columns=df_columns, fill_value=None)

# Reset index for both DataFrames
df = df.reset_index(drop=True)
enteredDf = enteredDf.reset_index(drop=True)

# Convert enteredDf to match the data types of df
enteredDf = enteredDf.astype(df.dtypes)

# Convert DataFrames to NumPy arrays and exclude the first column
df_array = df.iloc[:, 1:].to_numpy()
enteredDf_array = enteredDf.iloc[:, 1:].to_numpy()

# Perform element-wise comparison
comparisonResult = np.equal(df_array, enteredDf_array)

# Summary results
columnMatches = np.all(comparisonResult, axis=0)
rowMatches = np.all(comparisonResult, axis=1)
allMatches = np.all(comparisonResult)

# Print the results
print("\nColumn Matches:")
print(pd.Series(columnMatches, index=df.columns[1:]))  # Printing with column names

print("\nRow Matches:")
print(pd.Series(rowMatches, index=df.index))  # Printing with row indices

print("\nAll Matches:")
print(allMatches)
