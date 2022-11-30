from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import csv

app = Flask(__name__)
app.secret_key = "Kakaa2993@t"
Bootstrap(app=app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open(file="cafe-data.csv", encoding="utf-8") as file:
        csv_data = csv.reader(file)
        # for row in csv_data:
        #     print(row)
        # print(csv_data)
        return render_template("cafes.html", rows=csv_data)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
