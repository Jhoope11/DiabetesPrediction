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
    console.log(headers, data);
    return { headers, data };
}

// Function to filter data based on user input
function filterData(data, headers, formData) {
    return data.filter(entry => {
        return headers.filter(header => {
            const userInputValue = formData[header];
            const entryValue = entry[header];
            //console.log('Header:', header, 'User Input Value:', userInputValue, 'Entry Value:', entryValue);
            if (typeof userInputValue === 'boolean') {
                // For checkboxes
                return userInputValue ? entryValue === 1.0 : entryValue === 0.0;
            } else {
                // For text entries (convert empty to 0.0)
                const numericUserInput = parseFloat(userInputValue);
                return (
                    entryValue !== undefined &&
                    !isNaN(numericUserInput) &&
                    entryValue === (userInputValue === '' ? 0.0 : numericUserInput)
                );
            }
        });
    });
}


// Plot a bar chart using Plotly
function plotBarChart(barChart, data, formData) {
    const headers = Object.keys(data[0]);

    // Filter data based on user input
    const filteredData = filterData(data, headers, formData);

    // Create a map to store match counts for each header
    const userCounts = new Map();

    // Iterate through the filtered data to count matches and create bars
    const userInputBars = filteredData.reduce((bars, entry) => {
        headers.forEach(header => {
            const userInputValue = parseFloat(formData[header]);
            const entryValue = entry[header];
            // For numeric values
            if (entryValue === userInputValue) {
                // Increment the match count for the current header
                userCounts.set(header, (userCounts.get(header) || 0) + 1);
                // Create a new bar for the current match
                const matchCount = userCounts.get(header);
                const yValue = matchCount;
                bars.push({
                    x: [header],
                    y: [yValue],
                    type: 'bar',
                    name: `${header} (User Input)`,
                    showlegend: false,
                    marker: { color: 'red' },
                });
            }
        });
        return bars;
    }, []);
    // Plotly Bar Chart
    Plotly.newPlot(barChart, userInputBars, {
        barmode: 'group',
        margin: { t: 40, r: 10, b: 80, l: 60 },
        xaxis: { title: 'User Input' },
        yaxis: { title: 'Incrementing Count' },
    });
}
// Function to submit the form and process user input
async function submitForm(event) {
    event.preventDefault();

    // Get user input values from the form
    const formData = {
        HighBP: document.getElementById('HighBP').checked ? 1 : 0,
        HighChol: document.getElementById('HighChol').checked ? 1.0 : 0.0,
        CholCheck: document.getElementById('CholCheck').checked ? 1.0 : 0.0,
        Smoker: document.getElementById('Smoke').checked ? 1.0 : 0.0,
        Stroke: document.getElementById('Stroke').checked ? 0.0 : 1.0,
        HeartDiseaseorAttack: document.getElementById('HeartDiseaseOrAttack').checked ? 1.0 : 0.0,
        PhysActivity: document.getElementById('PhysAct').checked ? 1 : 0,
        Fruits: document.getElementById('Fruit').checked ? 1 : 0,
        Veggies: document.getElementById('Veg').checked ? 1 : 0,
        HvyAlcoholConsump: document.getElementById('HvyAlcCons').checked ? 1 : 0,
        AnyHealthcare: document.getElementById('Healthcare').checked ? 1 : 0,
        NoDocbcCost: document.getElementById('NoDocCost').checked ? 1.0 : 0.0,
        DiffWalk: document.getElementById('DiffWalk').checked ? 1.0 : 0.0,
        BMI: document.getElementById('BMI').value || 0.0,
        genHealth: document.getElementById('genHealth').value || 0.0,
        mentalHealth: document.getElementById('mentalHealth').value || 0.0,
        physHealth: document.getElementById('physHealth').value || 0.0,
        gender: document.getElementById('gender').value || 0.0,
        age: document.getElementById('age').value || 0.0,
        eduLevel: document.getElementById('eduLevel').value || 0.0,
        income: document.getElementById('income').value || 0.0,
    };

    // Parse CSV data from the external file
    const csvFile = 'Type12.csv'; // Replace with the actual path to your CSV file
    const parsedData = await parseCSV(csvFile);

    // Plot the bar chart
    plotBarChart('barChart', parsedData.data, formData);
}

// Initial plot when the page loads
submitForm({ preventDefault: () => {} });
