from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    print('hitting index route')
    return "Hello World"


if __name__ == '__main__':
    app.debug = True
    app.run()
