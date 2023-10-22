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
def c_text(text):
    """ Defines a dynamic path /c/text """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
