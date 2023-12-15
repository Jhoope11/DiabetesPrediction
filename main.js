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
        HighBP: document.getElementById('HighBP').checked,
        HighChol: document.getElementById('HighChol').checked,
        BMI: parseFloat(document.getElementById('BMI').value) || 0,
        Smoker: document.getElementById('Smoke').checked,
        Stroke: document.getElementById('Stroke').checked,
        HeartDiseaseorAttack: document.getElementById('HeartDiseaseOrAttack').checked,
        PhysActivity: document.getElementById('PhysAct').checked,
        Fruits: document.getElementById('Fruit').checked,
        Veggies: document.getElementById('Veg').checked,
        HvyAlchoholConsumption: document.getElementById('HvyAlcCons').checked,
        AnyHealthcare: document.getElementById('Healthcare').checked,
        GenHlth: parseInt(document.getElementById('genHealth').value) || 0,
        MentHlth: parseInt(document.getElementById('mentalHealth').value) || 0,
        PhysHlth: parseInt(document.getElementById('physHealth').value) || 0,
        DiffWalk: document.getElementById('DiffWalk').checked,
        Sex: document.getElementById('gender').value || 0,
        Age: parseInt(document.getElementById('age').value) || 0,
        Education: parseInt(document.getElementById('eduLevel').value) || 0,
        Income: parseInt(document.getElementById('income').value) || 0,
      };
    const percentage = calculatePrediction(userValues, parsedData);
    document.getElementById('output').innerText = `Prediction Result: ${percentage}%`;
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
    // Count the number of times an entered value is within 10 of a value in the CSV file
    let countWithin10 = 0;
  
    // Define a function to check if a user-entered value is within 10 of a CSV value
    function isWithin5(userValue, csvValue) {
      return Math.abs(userValue - csvValue) <= 5;
    }
    function isTheSame(userValue, csvValue){
        console.log('isTheSame(userValues.highBP, row.feature1) ')
        return Math.abs(userValue - csvValue) = 0;
    }
  
    // Loop through each row in the CSV data and compare values
    parsedData.forEach(row => {
        if (
          isWithin5(userValues.HighBP, row.HighBP) &&
          isWithin5(userValues.HighChol, row.HighChol) &&
          isWithin5(userValues.BMI, row.BMI) &&
          isWithin5(userValues.Smoker, row.Smoker) &&
          isWithin5(userValues.Stroke, row.Stroke) &&
          isWithin5(userValues.HeartDiseaseorAttack, row.HeartDiseaseorAttack) &&
          isWithin5(userValues.PhysActivity, row.PhysActivity) &&
          isWithin5(userValues.Fruits, row.Fruits) &&
          isWithin5(userValues.Veggies, row.Veggies) &&
          isWithin5(userValues.HvyAlchoholConsumption, row.HvyAlchoholConsumption) &&
          isWithin5(userValues.AnyHealthcare, row.AnyHealthcare) &&
          isWithin5(userValues.GenHlth, row.GenHlth) &&
          isWithin5(userValues.MentHlth, row.MentHlth) &&
          isWithin5(userValues.PhysHlth, row.PhysHlth) &&
          isWithin5(userValues.DiffWalk, row.DiffWalk) &&
          isTheSame(userValues.Sex, row.Sex) &&
          isWithin5(userValues.Age, row.Age) &&
          isWithin5(userValues.Education, row.Education) &&
          isWithin5(userValues.Income, row.Income)
        ) {
          countWithin10++;
        }
      });
  
    // Calculate the percentage
    const percentage = (countWithin10 / parsedData.length) * 100;
  
    // Return the calculated percentage
    return percentage;
  }