from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load CSV file into a list of dictionaries for quick lookup
csv_data = []
with open('Type12.csv', 'r') as csv_file:
    # Read headers from the first row
    headers = csv_file.readline().strip().split(',')

    # Iterate through the remaining lines
    for line in csv_file:
        values = line.strip().split(',')

        # Create a dictionary using headers as keys and values as values
        data_row = {header: value for header, value in zip(headers, values)}

        # Add the data row to the csv_data list
        csv_data.append(data_row)

# Convert checkbox values to 1 or 0
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

# Check if the static values are in the CSV file
def check_values_in_csv(static_values):
    result = {}
    total_rows = len(csv_data[1:])
    
    # Initialize lists for scatter plot
    x_values = []
    y_values = []

    # Iterate through each header
    for header in headers:
        # Compare the form value with the column values for each row
        match_count = sum(1 for data_row in csv_data[1:] if str(static_values[header]) == data_row[header])

        # Calculate percentage
        percentage = (match_count / total_rows) * 100 if total_rows > 0 else 0

        # Store the match count and percentage for the header
        result[header] = {'match_count': match_count, 'percentage': percentage}

        # Append values for scatter plot
        x_values.append(header)
        y_values.append(percentage)

    # Create a scatter plot
    scatter_plot = create_scatter_plot(x_values, y_values)

    # Encode the scatter plot image as Base64
    scatter_plot_base64 = base64.b64encode(scatter_plot).decode('utf-8')

    result['scatter_plot'] = scatter_plot_base64

    return result

def create_scatter_plot(x_values, y_values):
    # Create a scatter plot for user-entered values
    plt.scatter(x_values, y_values, color='blue', label='User Entered Values')

    plt.xlabel('Column')
    plt.ylabel('Percentage of Matches')
    plt.title('Proximity of Static Values to CSV Data')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return buffer.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle user-submitted form data
        form_values = request.form.to_dict()
        print(form_values)

        # Convert checkbox values to 1 or 0
        convert_checkbox_values(form_values)

        # Check if the values are in the CSV file
        result = check_values_in_csv(form_values)

        return render_template('result.html', result=result)
    else:
        # Use the first row as the form values
        form_values = csv_data[0].copy()

        return render_template('index.html', form_values=form_values)

if __name__ == '__main__':
    app.run(debug=True)
