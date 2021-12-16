"""A simple flask web app"""
from flask import Flask, request, flash
from flask import render_template
import calc.run_csv_operations
import csv
from pathlib import Path
import datetime
import os
import time
from calc.calculator import Calculator

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

root_dir = Path(__file__).parent.parent
input_folder_dir = root_dir / 'input'
output_folder_dir = root_dir / 'output'

@app.route("/")
def index():
    """home page; index route"""
    return render_template('index.html')


@app.route("/calculator/", methods=['GET', 'POST'])
def calculator():
    if request.method == "POST":
        val1 = request.form["val1"]
        val2 = request.form["val2"]
        operation = request.form["operation"]
        if val1 == "" or val2 == "":
            flash("Values cannot be empty!")
            return render_template('calculator.html')
        else:
            now = datetime.datetime.now()
            filename = 'input_'+now.strftime("%m-%d-%Y_%H-%M-%S"+".csv")
            header = ("value_a", "value_b", "operation")
            values = (val1, val2, operation)
            with open(os.path.join(input_folder_dir, filename), 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
                writer.writerow(values)

            calc.run_csv_operations.run_operations()

            return render_template('calculator.html')
    else:
        return render_template('calculator.html')


@app.route("/results/", methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        return render_template('results.html')
    else:
        calculation_results = []
        exceptions = []
        with open(os.path.join(output_folder_dir, 'calculation_results'), mode='r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                calculation_results.append(row)

        with open(os.path.join(output_folder_dir, 'exceptions'), mode='r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                exceptions.append(row)

        return render_template('results.html', calc_results=calculation_results, exceptions=exceptions)


# if __name__ == "__main__":
#     app.run(debug=True)
