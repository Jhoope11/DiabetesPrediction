function submitForm(event) {
    event.preventDefault();

    // Fetch user inputs
    const userValues = {
        HighBP: document.getElementById('HighBP').checked ? 1 : 0,
        HighChol: document.getElementById('HighChol').checked ? 1.0 : 0.0,
        CholCheck: document.getElementById('CholCheck').checked ? 1 : 0,
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
        BMI: parseFloat(document.getElementById('BMI').value) || -1,
        GenHlth: parseFloat(document.getElementById('genHealth').value) || -1,
        MentHlth: parseFloat(document.getElementById('mentalHealth').value) || -1,
        PhysHlth: parseFloat(document.getElementById('physHealth').value) || -1,
        Sex: parseInt(document.getElementById('gender').value) || -1,
        Age: parseInt(document.getElementById('age').value) || -1,
        Education: parseFloat(document.getElementById('eduLevel').value) || -1,
        Money: parseFloat(document.getElementById('income').value) || -1,
    };

    // Load CSV file asynchronously
    fetch('path/to/your/csvfile.csv') // Update with the actual path to your CSV file
        .then(response => response.text())
        .then(csvData => {
            // Parse CSV data
            const parsedData = parseCSV(csvData);

            // Extract x and y values for the scatter plot
            const xValues = parsedData.map(entry => entry.x);
            const yValues = parsedData.map(entry => entry.y);

            // Add user-inputted data to the scatter plot
            const userInputX = userValues.Age; // Replace with the appropriate user input property
            const userInputY = userValues.BMI; // Replace with the appropriate user input property
            xValues.push(userInputX);
            yValues.push(userInputY);

            // Plotly Scatter Plot
            const scatterPlot = document.getElementById('scatterPlot');
            Plotly.newPlot(scatterPlot, [{
                x: xValues,
                y: yValues,
                mode: 'markers',
                type: 'scatter'
            }]);

            // Display output or perform further analysis based on user inputs
            const outputDiv = document.getElementById('output');
            outputDiv.innerHTML = `User inputs: ${JSON.stringify(userValues)}`;
        })
        .catch(error => console.error('Error fetching CSV file:', error));
}

// Helper function to parse CSV data
function parseCSV(csvData) {
    // Implement your CSV parsing logic here
    // For simplicity, assuming CSV has "x" and "y" columns
    const lines = csvData.split('\n');
    const parsedData = lines.map(line => {
        const [x, y] = line.split(',').map(Number);
        return { x, y };
    });

    return parsedData;
}
