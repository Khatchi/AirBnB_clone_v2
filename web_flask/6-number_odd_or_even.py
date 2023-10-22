#!/usr/bin/python3
"""
This is a script that starts flask web app.
"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>')
def num_template_route(n):
    """Defines a dynamic path /number_template/<int:n>.
    Displays contents of html file, if n=int.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even_route(n):
    """Defines a dynamice path /number_even_or_odd/<int:n>.
    Display contents if odd/even: n=int.
    """
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
