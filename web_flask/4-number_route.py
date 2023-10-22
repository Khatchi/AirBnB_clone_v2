#!/usr/bin/python3
"""
This is a script that starts flask web app.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB! using / root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays HBNB using /hbnb path"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Defines a dynamic path /c/text """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """ Defines a dynamic path /python/<text>"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_int_route(n):
    """ Defines a dynamic path /number/<int:n>"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
