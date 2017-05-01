from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import json

print('app.py working')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/enviropi_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine('postgres://localhost:5432/envirorpi_db')


import models


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    print('hitting index route')
    return "Hello World"


@app.route('/environment', methods=['GET', 'POST'])
def environment():
    return "All Environment Data"


@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    return "Temperature Data"


@app.route('/lighting', methods=['GET', 'POST'])
def lighting():
    return "Lighting Data"


if __name__ == '__main__':
    app.debug = True
    app.run()
