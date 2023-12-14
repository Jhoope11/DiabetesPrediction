// Function to convert checkbox values to float
function checkboxToFloat(value) {
  return value === 'on' ? 1.0 : 0.0;
}

// Function to convert text values to float, defaulting to 0.0 if empty
function textToFloat(value) {
  return value ? parseFloat(value) : 0.0;
}

// Function to perform the calculation
function performCalc() {
  // Read data from the CSV file (replace 'your_file.csv' with the actual path)
  const csvFilePath = 'your_file.csv';

  // Assuming you have HTML elements with the specified IDs
  var highBP = checkboxToFloat(document.getElementById('HighBP'));
  var highChol = checkboxToFloat(document.getElementById('HighChol'));
  var cholCheck = checkboxToFloat(document.getElementById('CholCheck'));
  var smoke = checkboxToFloat(document.getElementById('Smoke'));
  var stroke = checkboxToFloat(document.getElementById('Stroke'));
  var heartDiseaseOrAttack = checkboxToFloat(document.getElementById('HeartDiseaseOrAttack'));
  var physAct = checkboxToFloat(document.getElementById('PhysAct'));
  var fruit = checkboxToFloat(document.getElementById('Fruit'));
  var veg = checkboxToFloat(document.getElementById('Veg'));
  var hvyAlcCons = checkboxToFloat(document.getElementById('HvyAlcCons'));
  var healthcare = checkboxToFloat(document.getElementById('Healthcare'));
  var noDocCost = checkboxToFloat(document.getElementById('NoDocCost'));
  var diffWalk = checkboxToFloat(document.getElementById('DiffWalk'));
  var BMI = textToFloat(document.getElementById('BMI').value);
  var genHealth = textToFloat(document.getElementById('genHealth').value);
  var mentalHealth = textToFloat(document.getElementById('mentalHealth').value);
  var physHealth = textToFloat(document.getElementById('physHealth').value);
  var gender = textToFloat(document.getElementById('gender').value);
  var age = textToFloat(document.getElementById('age').value);
  var eduLevel = textToFloat(document.getElementById('eduLevel').value);
  var income = textToFloat(document.getElementById('income').value);

  // Create a DataFrame from the entered data
  const enteredData = {
    'Diabetes_012': 0.0,
    'HighBP': highBP,
    'HighChol': highChol,
    'CholCheck': cholCheck,
    'BMI': BMI,
    'Smoker': smoke,
    'Stroke': stroke,
    'HeartDiseaseOrAttack': heartDiseaseOrAttack,
    'PhysActivity': physAct,
    'Fruits': fruit,
    'Veggies': veg,
    'HvyAlcoholConsump': hvyAlcCons,
    'AnyHealthcare': healthcare,
    'NoDocbcCost': noDocCost,
    'GenHlth': genHealth,
    'MentHlth': mentalHealth,
    'PhysHlth': physHealth,
    'DiffWalk': diffWalk,
    'Sex': gender,
    'Age': age,
    'Education': eduLevel,
    'Income': income
  };
  const enteredDf = new DataFrame([enteredData]);

  // Assuming you have loaded the CSV data into df using pandas-js
  const df = DataFrame.fromCSV(csvFilePath);

  // Ensure columns in both DataFrames match
  const dfColumns = df.columns;
  const enteredDfMatched = enteredDf.reindex(dfColumns, null);

  // Perform element-wise comparison
  const comparisonResult = enteredDfMatched.values.eq(df.values);

  // Summary results
  const columnMatches = comparisonResult.all(0).toArray();
  const rowMatches = comparisonResult.all(1).toArray();
  const allMatches = comparisonResult.all().get();

  // Print the results (you may want to use console.log instead of print in JavaScript)
  console.log("\nColumn Matches:");
  console.log(columnMatches);

  console.log("\nRow Matches:");
  console.log(rowMatches);

  console.log("\nAll Matches:");
  console.log(allMatches);
}

// Call the function when the button is clicked
document.getElementById('submitBtn').addEventListener('click', performCalc);
