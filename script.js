// Parse CSV data into an object with headers and data
async function parseCSV(csvFile) {
    const response = await fetch(csvFile);
    const csvData = await response.text();

    const lines = csvData.trim().split('\n');
    const headers = lines[0].split(',').map(header => header.trim());
    const data = lines.slice(1).map(line => {
        const values = line.split(',').map(value => parseFloat(value.trim()));
        return Object.fromEntries(headers.map((header, index) => [header, values[index]]));
    });

    return { headers, data };
}

// Plot a bar chart using Plotly
function plotBarChart(barChart, data, xAxisValues, yAxisColumn) {
    const headers = Object.keys(data[0]);

    // Filter out rows with negative values in the specified columns
    function filterData(column) {
        return data.filter(entry => entry[column] >= 0);
    }

    // Count occurrences of user input in each column
    const userCounts = headers.map(column => {
        const count = filterData(column).filter(entry => {
            const entryValue = entry[yAxisColumn];
            return xAxisValues.includes(entryValue);
        }).length;
        return count;
    });

    // Create bars for CSV data
    const csvBars = headers.flatMap((column, index) => {
        const csvData = filterData(column);
        return [
            {
                x: xAxisValues,
                y: Array(xAxisValues.length).fill(0), // All bars for CSV data have y=0
                type: 'bar',
                name: `${column} (CSV Data)`,
                showlegend: false,
                marker: { color: 'blue' },
            }
        ];
    });

    // Create bars for user input counts
    const userInputBars = headers.map((column, index) => {
        return {
            x: xAxisValues,
            y: userCounts,
            type: 'bar',
            name: `${column} (User Input)`,
            showlegend: false,
            marker: { color: 'red' },
        };
    });

    // Plotly Bar Chart
    Plotly.newPlot(barChart, csvBars.concat(userInputBars), {
        barmode: 'group',
        margin: { t: 40, r: 10, b: 80, l: 60 },
        xaxis: {
            title: 'User Input',
            ticktext: headers,
            tickmode: 'array',
            tickvals: headers.map((_, index) => index),
        },
        yaxis: { title: 'Number of Matches' }, // Update Y-axis label
    });
}

// Function to submit the form and process user input
async function submitForm(event) {
    event.preventDefault();

    // Get user input values from the form
    const formData = {
        HighBP: document.getElementById('HighBP').checked,
        HighChol: document.getElementById('HighChol').checked,
        CholCheck: document.getElementById('CholCheck').checked,
        Smoke: document.getElementById('Smoke').checked,
        Stroke: document.getElementById('Stroke').checked,
        HeartDiseaseOrAttack: document.getElementById('HeartDiseaseOrAttack').checked,
        PhysAct: document.getElementById('PhysAct').checked,
        Fruit: document.getElementById('Fruit').checked,
        Veg: document.getElementById('Veg').checked,
        HvyAlcCons: document.getElementById('HvyAlcCons').checked,
        Healthcare: document.getElementById('Healthcare').checked,
        NoDocCost: document.getElementById('NoDocCost').checked,
        DiffWalk: document.getElementById('DiffWalk').checked,
        BMI: document.getElementById('BMI').value,
        genHealth: document.getElementById('genHealth').value,
        mentalHealth: document.getElementById('mentalHealth').value,
        physHealth: document.getElementById('physHealth').value,
        gender: document.getElementById('gender').value,
        age: document.getElementById('age').value,
        eduLevel: document.getElementById('eduLevel').value,
        income: document.getElementById('income').value,
    };

    // Parse CSV data from the external file
    const csvFile = 'Type12.csv'; // Replace with the actual path to your CSV file
    const parsedData = await parseCSV(csvFile);

    // Extract X-axis values from the user input
    const xAxisValues = Object.entries(formData)
        .filter(([key, value]) => key !== 'BMI' && key !== 'genHealth' && key !== 'mentalHealth' && key !== 'physHealth')
        .filter(([key, value]) => value)
        .map(([key, value]) => value);

    // Plot the bar chart
    plotBarChart('barChart', parsedData.data, xAxisValues, 'BMI'); // 'BMI' is the Y-axis column
}
