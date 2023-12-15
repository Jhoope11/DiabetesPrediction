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
        
        # Check if the values are in the CSV file
        result = check_values_in_csv(form_values)
        
        return render_template('result.html', result=result)

    return render_template('index.html')

def check_values_in_csv(form_values):
    result = {}
    for key, value in form_values.items():
        if key in csv_data:
            if value == csv_data[key][1]:  # Assuming you want to check the second column
                result[key] = True
            else:
                result[key] = False
        else:
            result[key] = False
    return result

if __name__ == '__main__':
    app.run(debug=True)
