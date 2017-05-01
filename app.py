from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    print('hitting index route')
    return "Hello World"


@app.route('/environment', methods=['GET'])
def environment():
    return "All Environment Data"


@app.route('/temperature', methods=['GET', 'PATCH'])
def temperature():
    return "Temperature Data"


@app.route('/lighting', methods=['GET', 'PATCH'])
def lighting():
    return "Lighting Data"


if __name__ == '__main__':
    app.debug = True
    app.run()
