import csv

# Specify the file name
file_name = 'Type12.csv'

# Reading from CSV file and printing the first 10 rows
with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Print header
    header = next(csv_reader)
    print(header)

    # Print the first 10 rows
    row_count = 0
    for row in csv_reader:
        print(row)
        row_count += 1
        if row_count >= 10:
            break
