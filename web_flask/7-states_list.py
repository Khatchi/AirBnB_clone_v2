#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at the end of the request. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a list of states from the database """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
