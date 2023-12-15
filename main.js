// Assuming your CSV file is named 'data.csv' and is in the same directory as your HTML and JS files
const csvFilePath = 'Type12.csv';
let parsedData;
// Read the CSV file using the Fetch API or other suitable methods
fetch(csvFilePath)
  .then(response => response.text())
  .then(csvData => {
    // Parse CSV data
    parsedData = parseCSV(csvData);

    // Now you can use the parsedData for further processing
    document.getElementById('output').innerText = 'CSV Loaded';
  })
  .catch(error => console.error('Error fetching CSV:', error));


function submitForm(event) {
    event.preventDefault();
    // Get boolean values from checkboxes
    if(!parsedData){ 
        console.error('CSV Not loaded');
        return;
    }
    const userValues = {
        HighBP: document.getElementById('HighBP').checked ? 1 : 0,
        HighChol: document.getElementById('HighChol').checked ? 1.0 : 0.0,
        CholCheck: document.getElementById('CholCheck').checked ? 1 : 0,
        Smoker: document.getElementById('Smoke').checked ? 1.0 : 0.0,
        Stroke: document.getElementById('Stroke').checked ? 1.0 : 0.0,
        HeartDiseaseorAttack: document.getElementById('HeartDiseaseOrAttack').checked ? 1.0 : 0.0,
        PhysActivity: document.getElementById('PhysAct').checked ? 1 : 0,
        Fruits: document.getElementById('Fruit').checked ? 1 : 0,
        Veggies: document.getElementById('Veg').checked ? 1 : 0,
        HvyAlcoholConsump: document.getElementById('HvyAlcCons').checked ? 1 : 0,
        AnyHealthcare: document.getElementById('Healthcare').checked ? 1 : 0,
        NoDocbcCost: document.getElementById('NoDocCost').checked ? 1.0 : 0.0,
        DiffWalk: document.getElementById('DiffWalk').checked ? 1.0 : 0.0,
        BMI: parseFloat(document.getElementById('BMI').value) || 0.0,
        GenHlth: parseFloat(document.getElementById('genHealth').value) || 0.0,
        MentHlth: parseFloat(document.getElementById('mentalHealth').value) || 0.0,
        PhysHlth: parseFloat(document.getElementById('physHealth').value) || 0.0,
        Sex: parseInt(document.getElementById('gender').value) || 0.0,
        Age: parseInt(document.getElementById('age').value) || 0.0,
        Education: parseFloat(document.getElementById('eduLevel').value) || 0.0,
        Money: parseFloat(document.getElementById('income').value) || 0.0,
    };
    const percentage = calculatePrediction(userValues, parsedData);
    document.getElementById('output').innerText = `Prediction Result: \n${percentage}%`;
  }

function parseCSV(csvData) {
    // Split the CSV data into rows
    const rows = csvData.split('\n');
  
    // Get the headers from the first row
    const headers = rows[0].split(',');
  
    // Initialize an array to store the parsed data
    const parsedData = [];
  
    // Loop through the remaining rows
    for (let i = 1; i < rows.length; i++) {
      // Split each row into values
      const values = rows[i].split(',');
  
      // Create an object with key-value pairs for each header and value
      const rowObject = {};
      for (let j = 0; j < headers.length; j++) {
        rowObject[headers[j]] = parseFloat(values[j]);
      }
  
      // Add the row object to the parsed data array
      parsedData.push(rowObject);
    }
  
    return parsedData;
  }
  
  function calculatePrediction(userValues, parsedData) {
    // Loop through each row in the CSV data and compare values
    const columnCounts = Array(Object.keys(parsedData[0]).length).fill(0);
    let matchingRowsCount = 0;
    let matchingValue = false;
    let firstLoop = false;
    let secLoop = false;
    let x = 0;
    let y = 0;
    let z = 0;
    // Loop through each row in the CSV data
    parsedData.forEach(row => {
  
        // Loop through each column in the row
        Object.keys(row).forEach((key, index) => {
        const csvValue = row[key];
        const userValue = userValues[key];
        
        // Check the condition based on the column name

        if (key === 'BMI') {
            // Check if the user-entered value is within 5 of the CSV value
            if (Math.abs(userValue - csvValue) <= 5) {
                // Increment the count for the current column
                columnCounts[index]++;
                matchingValue = true;
                //secLoop = true;
                }
        } else {
            // Check if the user-entered value is the same as the CSV value
            if (userValue === csvValue) {
                //console.log(key, userValue, csvValue);
                // Increment the count for the current column
                columnCounts[index]++;
                matchingValue = true;
                //firstLoop = true;
            }
        }
        if(matchingValue){
            console.log(matchingValue);
            /*
            if(firstLoop){
                x += 1;
                firstLoop = false;
            }
            if(secLoop){
                y += 1;
                secLoop = false;
            } 
            */
            key = 'Diabetes_012';
            if(csvValue == 2.0){
                console.log(key, userValue, csvValue, x, y ,z);
                matchingRowsCount++;
                //z += 1;
            }  
            matchingValue = false;
            //console.log(matchingValue);
        }
        });
    });
    //console.log(x,y,z);
    // Calculate the percentage
    const percentages = columnCounts.map(count => (count / parsedData.length) * 100);
    const matchingRowsPercentage = (matchingRowsCount / parsedData.length) * 100;
    console.log(userValues)
    console.log('Keys:', Object.keys(parsedData[0]));
    console.log('Percentages:', percentages);
    // Format the output
    formattedOutput = Object.keys(parsedData[0])
    .map((key, index) => {
        const trimmedKey = key.trim();
        return `${trimmedKey}: ${percentages[index].toFixed(2)}%`;
    })
    .join('\n');
    // Add information about matching rows with diabetes_012 equal to 2.0
    formattedOutput += `\nPercentage of similarity with the same entries that had type 2 Diabetes: ${matchingRowsPercentage.toFixed(2)}`;
    return formattedOutput;
  }