import sqlite3
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    print('hitting index route')
    return "Hello World"


@app.route('/environment', methods=['GET'])
def environment():
     with sqlite3.connect('environment.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM environment ORDER BY id desc")
        all_data = cursor.fetchall()
        return all_data


@app.route('/temperature', methods=['GET', 'PATCH'])
def temperature():
    return "Temperature Data"


@app.route('/lighting', methods=['GET', 'PATCH'])
def lighting():
    return "Lighting Data"


if __name__ == '__main__':
    app.debug = True
    app.run()
