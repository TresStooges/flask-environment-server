from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import json
import os

print('app.py working')
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/enviropi_db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# engine = create_engine('postgres://localhost:5432/envirorpi_db')

port = int(os.environ.get('PORT', 5000))
import models


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    print('hitting index route')
    return "Hello World"


@app.route('/environment', methods=['GET', 'POST'])
def environment():
    if request.method == 'GET':
        all_environment_data = []
        properties = models.Property.query.all()
        for property in properties:
            all_environment_data.append({
                'id': property.id,
                'location': property.location,
                'name': property.name,
                'temperature': property.temperature,
                'timestamp': property.timestamp,
                'image': property.image,
                'date': property.date,
                'time': property.time

                # 'imageb': property.imageb
            })
        return jsonify(all_environment_data)
    elif request.method == 'POST':
        new_property_data = json.loads(request.data)
        new_property = models.Property(
            new_property_data["location"],
            new_property_data["name"],
            new_property_data["temperature"],
            new_property_data["image"],
            new_property_data["date"],
            new_property_data["time"]
            # new_property_data["imageb"]
        )
        db.session.add(new_property)
        db.session.commit()
        return request.data


@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    return "Temperature Data"


@app.route('/lighting', methods=['GET', 'POST'])
def lighting():
    return "Lighting Data"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=port)
