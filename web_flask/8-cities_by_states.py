#!/usr/bin/python3
""" starts a Flask web application with 7 routes and templates
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# It's executed every time the application context tears down
@app.teardown_appcontext
def bye(error):
    """ Close the SQLAlquemy session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def render_cities_by_states():
    """returns a web page with a cities_by_states list

    Returns:
        web_page: states list
    """
    st = storage.all(State).values()
    ci = storage.all(City).values()
    return render_template("8-cities_by_states.html", states=st, cities=ci)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
