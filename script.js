function calculateBMI() {
    let height = document.getElementById("height").value;
    let weight = document.getElementById("weight").value;
    let result = document.getElementById("result");

    if (height === "" || weight === "" || height <= 0 || weight <= 0) {
        result.innerHTML = "Please enter valid values";
        return;
    }

    let bmi = (weight / (height * height)).toFixed(2);

    let category = "";
    if (bmi < 18.5) {
        category = "Underweight";
    } else if (bmi < 24.9) {
        category = "Normal weight";
    } else if (bmi < 29.9) {
        category = "Overweight";
    } else {
        category = "Obese";
    }

    result.innerHTML = `Your BMI is ${bmi} (${category})`;
}
