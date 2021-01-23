#!/usr/bin/python3
""" starts a Flask web application with 7 routes and templates
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# It's executed every time the application context tears down
@app.teardown_appcontext
def bye(error):
    """ Close the SQLAlquemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def render_cities_by_states():
    """returns a web page with a cities_by_states list

    Returns:
        web_page: states list
    """
    st = storage.all(State).values()
    ci = storage.all(City).values()
    am = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html", states=st,
        cities=ci, amenitys=am
    )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
