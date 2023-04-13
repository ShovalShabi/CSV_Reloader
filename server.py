import csv
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    This function renders the index page of the Flask application. It reads data from a CSV file
    and returns it in a dictionary that is then rendered using a template.

    :return: HTML template containing data from the CSV file
    """
    page_title = "CSV Reloader"
    fields = read_csv(filename='data/data.csv')
    data = json.dumps(fields)
    return render_template('index.html', page_title=page_title, fields=fields, reader=data)


@app.route('/Data', methods=['POST'])
def button_action():
    """
    This function is executed when a button is pressed on the index page. It currently only prints
    a message to the console.

    :return: None
    """
    print("Playing music")


def read_csv(filename):
    """
    This function reads a CSV file and returns its contents in a dictionary.

    :param filename: The name of the CSV file
    :return: A dictionary containing the data from the CSV file
    """
    with open(filename, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        data_dict = {}

        # Creating a dictionary of sets for the data
        for col in reader.fieldnames:
            data_dict[col] = []

        # Putting the data in the dictionary
        for row in reader:
            for key in data_dict.keys():
                data_dict[key].append(row[key])
        return data_dict
