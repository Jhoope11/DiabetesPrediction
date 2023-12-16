from flask import Flask, render_template

app = Flask(__name__)

# Load CSV file into a dictionary for quick lookup
csv_data = {}
with open('Type12.csv', 'r') as csv_file:
    headers = csv_file.readline().strip().split(',')
    for line in csv_file:
        values = line.strip().split(',')
        key = values[0]  # Assuming the first column is the key
        csv_data[key] = {header: value for header, value in zip(headers, values)}


@app.route('/', methods=['GET'])
def index():
    # Use the first row as the form values
    first_row_key = list(csv_data.keys())[0]
    form_values = csv_data[first_row_key].copy()

    # Convert checkbox values to 1 or 0
    convert_checkbox_values(form_values)

    # Check if the values are in the CSV file
    result = check_values_in_csv(static_values)
    
    return render_template('result.html', result=result)

def convert_checkbox_values(form_values):
    checkbox_fields = [
        'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke', 
        'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 
        'AnyHealthcare', 'NoDocbcCost', 'DiffWalk'
    ]

    for field in checkbox_fields:
        # Check if the checkbox is present in form data
        form_values[field] = 1 if field in form_values and form_values[field] == 'on' else 0

    # Handle empty values in text boxes and replace with 0
    text_fields = ['BMI', 'GenHlth', 'MentHlth', 'PhysHlth', 'Sex', 'Age', 'EduLevel', 'Money', 'Type012']
    for field in text_fields:
        if field in form_values and not form_values[field].strip():
            form_values[field] = 0
            
def check_values_in_csv(static_values):
    result = {}

    # Get the keys from the second row of the CSV file (assuming it contains the type information)
    csv_keys = list(csv_data.keys())
    csv_values = list(csv_data.values())[1]  # Assuming the second row contains the example values

    for key, value in static_values.items():
        if key in csv_data:
            # Get the corresponding row values based on the key
            row_values = csv_data[key]

            # Print the comparison details
            print(f"Key: {key}, Form value: {value}, CSV values: {row_values[1:]}")

            # Compare the form value with the CSV values
            match_count = sum(1 for v, csv_value in zip(row_values[1:], csv_values[1:]) if str(value) == csv_value)  # Skip the first column (key) in CSV data
            
            # Print the match count
            print(f"Match count for {key}: {match_count}")

            result[key] = match_count
        else:
            result[key] = 0  # Default value if key is not found in CSV

    return result


# Assuming csv_data is defined and available in the scope
static_values = {
    'Type012': 0,
    'HighBP': 0,
    'HighChol': 1,
    'CholCheck': 1,
    'BMI': 15.0,
    'Smoker': 1,
    'Stroke': 0,
    'HeartDiseaseorAttack': 0,
    'PhysActivity': 0,
    'Fruits': 1,
    'Veggies': 1,
    'HvyAlcoholConsump': 0,
    'AnyHealthcare': 1,
    'NoDocbcCost': 0,
    'GenHlth': 5.0,
    'MentHlth': 10.0,
    'PhysHlth': 20.0,
    'DiffWalk': 0.0,
    'Sex': 0,
    'Age': 11,
    'Education': 4.0,
    'Money': 5.0
    # Add more key-value pairs for the remaining columns if needed
}


if __name__ == '__main__':
    app.run(debug=True)
