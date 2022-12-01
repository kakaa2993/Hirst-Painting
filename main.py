from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.secret_key = "Kakaa2993@t"
Bootstrap(app=app)


class Form(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(label="Cafe Location on Google Maps(URL)",
                           validators=[DataRequired(), URL(message="Invalid URL")])
    open = StringField(label="Opening Time e.g. 8AM ",
                       validators=[DataRequired()])
    close = StringField(label="Closing Time e.g. 5:30PM ",
                        validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating",
                         choices=[(1, "☕"), (2, "☕☕"), (3, "☕☕☕"), (4, "☕☕☕☕"), (5, "☕☕☕☕☕")],
                         validators=[])
    wifi = SelectField(label="Wifi Strength Rating ",
                       choices=[(0, "✘"), (1, "💪"), (2, "💪💪"), (3, "💪💪💪"), (4, "💪💪💪💪"), (5, "💪💪💪💪💪")])
    power = SelectField(label="Power Socket Availability",
                        choices=[(0, "✘"), (1, "🔌"), (2, "🔌🔌"), (3, "🔌🔌🔌"), (4, "🔌🔌🔌🔌"), (5, "🔌🔌🔌🔌🔌")])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    list_ = []
    with open(file="cafe-data.csv", encoding="utf-8") as file:
        csv_data = csv.reader(file)
        for row in csv_data:
            list_.append(row)
    return render_template("cafes.html", rows=list_)


def add_data_to_database(detail):
    with open("cafe-data.csv", "a") as csv_data:
        writer = csv.writer(csvfile=csv_data)
        writer.writerow(detail)


@app.route("/add", methods=['POST', 'GET'])
def add():
    order_form = Form()
    if order_form.validate_on_submit():
        print("success")
        data = [order_form.cafe_name.data, order_form.location.data,order_form.open.data, order_form.close.data, order_form.coffee.data, order_form.wifi.data, order_form.power.data]
        add_data_to_database(data)
        return render_template("cafe.html")
    return render_template("add.html", form=order_form)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
