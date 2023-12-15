from flask import Flask, render_template, request

app = Flask(__name__)

# Load CSV file into a dictionary for quick lookup
csv_data = {}
with open('Type12.csv', 'r') as csv_file:
    headers = csv_file.readline().strip().split(',')
    for line in csv_file:
        values = line.strip().split(',')
        key = values[0]  # Assuming the first column is the key
        csv_data[key] = values

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get values from HTML form
        form_values = request.form.to_dict()
        
        # Convert checkbox values to 1 or 0
        convert_checkbox_values(form_values)

        # Check if the values are in the CSV file
        result = check_values_in_csv(form_values)
        
        return render_template('result.html', result=result)

    return render_template('index.html')

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


def check_values_in_csv(form_values):
    result = {}
    
    # Get the keys from the first row of the CSV file
    csv_keys = list(csv_data.keys())

    for key, value in form_values.items():
        if key in csv_data:
            # Get the corresponding row values based on the key
            row_values = csv_data[key]
            
            # Get the index of the key in the CSV file
            key_index = csv_keys.index(key)
            
            # Get the values from the first row for the corresponding key
            csv_values = [csv_data[k][key_index] for k in csv_keys]

            # Compare the form value with the CSV values
            match_count = sum(1 for v in csv_values if str(value) == v)
            result[key] = match_count
        else:
            result[key] = 0  # Default value if key is not found in CSV

    return result






if __name__ == '__main__':
    app.run(debug=True)
