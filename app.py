from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius=0):
    celsius_temperature = float(celsius)
    fahrenheit = celsius_temperature * 9 / 5 + 32
    return f"{celsius} C is {fahrenheit} F"


if __name__ == '__main__':
    app.run()
