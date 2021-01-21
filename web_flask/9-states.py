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


@app.route('/states', strict_slashes=False)
def render_states_list():
    """returns a web page with a states list

    Returns:
        web_page: states list
    """
    data = storage.all(State).values()
    return render_template("7-states_list.html", data=data)


@app.route('/states/<id>', strict_slashes=False)
def render_cities_by_states(id):
    """returns a web page with a cities_by_states list

    Returns:
        web_page: states list
    """
    st = storage.all(State).values()
    ci = storage.all(City).values()

    list_city = []
    for i in st:
        if i.id == id:
            for j in ci:
                if j.state_id == i.id:
                    list_city.append(j)
            return render_template("9-states.html", state=i, cities=list_city)
    return render_template("9-states.html", state=0)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")

