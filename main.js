// Function to convert checkbox values to float
function checkboxToFloat(value) {
    return value === 'on' ? 1.0 : 0.0;
}

// Function to convert text values to float, defaulting to 0.0 if empty
function textToFloat(value) {
    return value ? parseFloat(value) : 0.0;
}

// Assuming you have loaded the necessary libraries for data manipulation in JavaScript
function performCalc() {

    const csvFilePath = 'Type12.csv';

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

    // Construct the enteredData dictionary
    var enteredData = {
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

    // Convert enteredData into an array of objects
    const enteredDf = [enteredData];

    // Ensure columns in both arrays match
    const dfColumns = ['column1', 'column2', 'column3', /* Add all column names */];
    const enteredDfArray = enteredDf.map(obj => {
        const newObj = {};
        dfColumns.forEach(col => newObj[col] = obj[col] !== undefined ? obj[col] : null);
        return newObj;
    });

    // Convert enteredDf to match the data types of df (assuming dfTypes is an array of data types)
    const dfTypes = ['number', 'number', 'number', /* Add all data types */];
    const enteredDfTypedArray = enteredDfArray.map(obj => {
        const newObj = {};
        dfColumns.forEach((col, index) => newObj[col] = typeof obj[col] === dfTypes[index] ? obj[col] : null);
        return newObj;
    });

    // Perform element-wise comparison
    const comparisonResult = enteredDfTypedArray.map(obj => {
        const newObj = {};
        dfColumns.forEach(col => newObj[col] = obj[col] !== null && dfArray[0][col] === obj[col]);
        return newObj;
    });

    // Summary results
    const columnMatches = dfColumns.map(col => comparisonResult.every(obj => obj[col]));
    const rowMatches = comparisonResult.map(obj => Object.values(obj).every(val => val));
    const allMatches = columnMatches.every(match => match) && rowMatches.every(match => match);

    // Display the results in the 'output' div
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = "<h2>Results:</h2>";

    // Display Column Matches
    outputDiv.innerHTML += "<p><strong>Column Matches:</strong></p>";
    columnMatches.forEach((match, index) => {
        outputDiv.innerHTML += `<p>${dfColumns[index]}: ${match}</p>`;
    });

    // Display Row Matches
    outputDiv.innerHTML += "<p><strong>Row Matches:</strong></p>";
    rowMatches.forEach((match, index) => {
        outputDiv.innerHTML += `<p>Row ${index + 1}: ${match}</p>`;
    });

    // Display All Matches
    outputDiv.innerHTML += `<p><strong>All Matches:</strong> ${allMatches}</p>`;
}
