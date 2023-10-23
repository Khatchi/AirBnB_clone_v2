#!/usr/bin/python3
""" Starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__, template_folder="templates")
file = "10-hbnb_filters.html"


@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at the end of the request. """
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    cities = storage.all(City)
    cities = dict(sorted(cities.items(), key=lambda item: item[1].name))
    amenities = storage.all(Amenity)
    amenities = dict(sorted(amenities.items(), key=lambda item: item[1].name))
    return render_template(file, states=states, cities=cities, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
