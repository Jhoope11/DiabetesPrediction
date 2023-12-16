from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Loads Type12.csv file into a list of dictionaries for quick lookup
csvData = []
with open('Type12.csv', 'r') as csvFile:
    # Reads headers from the first row
    headers = csvFile.readline().strip().split(',')
    # Iterates through the remaining lines
    for line in csvFile:
        values = line.strip().split(',')
        # Creates a dictionary using headers as keys and values as values
        dataRow = {header: value for header, value in zip(headers, values)}
        # Adds the data row to the csvData list
        csvData.append(dataRow)

# Converts and handles inputted values
def convertCheckboxValues(formValues):
    checkboxFieldsFloats = [
        'HighChol',  'Smoker', 'Stroke',
        'HeartDiseaseorAttack', 'NoDocbcCost', 'DiffWalk'
    ]
    checkboxFieldsInts = ['HighBP', 'CholCheck', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump',
        'AnyHealthcare'
    ]
    for field in checkboxFieldsFloats:
        # Checks if the checkbox is present in form data
        formValues[field] = 1.0 if field in formValues and formValues[field] == 'on' else 0.0
    for field in checkboxFieldsInts:
        # Checks if the checkbox is present in form data
        formValues[field] = 1 if field in formValues and formValues[field] == 'on' else 0
    # Handles empty values in text boxes and replace with 0
    textFields = ['BMI', 'GenHlth', 'MentHlth', 'PhysHlth', 'Sex', 'Age', 'Education', 'Money', 'Type012']
    for field in textFields:
        if field in formValues and not formValues[field].strip():
            formValues[field] = 0.0
        else:
            try:
                # Tries to cast the field value to float
                formValues[field] = float(formValues[field])
            except (ValueError, TypeError):
                # Handles the case where casting to float is not possible
                formValues[field] = 0.0
    print(formValues)
    return formValues

# Check if the entered values are in the CSV file
def checkValuesInCsv(enteredValues):
    result = {}
    totalRows = len(csvData[1:])
    # Initialize lists for scatter plot
    xValues = []
    yValues = []
    # Iterate through each header
    for header in headers:
        # Compare the form value with the column values for each row
        matchCount = sum(1 for dataRow in csvData[1:] if str(enteredValues[header]) == dataRow[header])
        # Calculate percentage
        percentage = (matchCount / totalRows) * 100 if totalRows > 0 else 0
        # Store the match count and percentage for the header
        result[header] = {'matchCount': matchCount, 'percentage': percentage}
        xValues.append(header)
        yValues.append(percentage)
        
    scatterPlot = createScatterPlot(xValues, yValues)
    scatterPlotBase64 = base64.b64encode(scatterPlot).decode('utf-8')
    result['scatterPlot'] = scatterPlotBase64
    return result

def createScatterPlot(xValues, yValues):
    plt.scatter(xValues, yValues, color='blue', label='User Entered Values')

    plt.xlabel('Column')
    plt.ylabel('Percentage of Matches')
    plt.title('Proximity of entered Values to CSV Data')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    return buffer.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle user-submitted form data
        formValues = request.form.to_dict()
        print(formValues)
        # handles inputted values
        convertCheckboxValues(formValues)
        # Checks if the values are in the CSV file
        result = checkValuesInCsv(formValues)
        return render_template('result.html', result=result)
    else:
        # Uses the first row as the form values
        formValues = csvData[0].copy()
        return render_template('index.html', formValues=formValues)

if __name__ == '__main__':
    app.run(debug=True)