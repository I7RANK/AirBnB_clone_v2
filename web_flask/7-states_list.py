#!/usr/bin/python3
""" starts a Flask web application with 7 routes and templates
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


data = storage.all(State).values()


@app.route('/states_list', strict_slashes=False)
def render_states_list():
    """returns a web page with a states list

    Returns:
        web_page: states list
    """
    return render_template("7-states_list.html", data=data)


# It's executed every time the application context tears down
@app.teardown_appcontext
def bye(error):
    """ Close the SQLAlquemy session """
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
