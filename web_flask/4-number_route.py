#!/usr/bin/python3
""" starts a Flask web application with 5 routes
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """returns Hello HBNB!

    Returns:
        str: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    """returns HBNB

    Returns:
        str: HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_C(text=None):
    """returns a string

    Args:
        text (str, optional): text. Defaults to None.

    Returns:
        str: holberton output
    """
    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """returns a string

    Args:
        text (str, optional): text. Defaults to "is cool".

    Returns:
        str: holberton output
    """
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """returns the number if is int

    Args:
        n (int): a number

    Returns:
        string: holberton output
    """
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
