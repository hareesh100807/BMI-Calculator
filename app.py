from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category ="Underweight 🥺"
            elif bmi < 25:
                category = "Normal 😊"
            elif bmi < 30:
                category = "Overweight 😐"
            elif bmi < 35:
                category = "Obese ⚠️"
            else:
                category = "Clinically Obese 🚨"

        except ValueError:
            bmi = "Invalid Input"
            category = "Please enter numbers only."

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
