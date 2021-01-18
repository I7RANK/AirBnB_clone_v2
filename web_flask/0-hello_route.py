#!/usr/bin/python3
""" starts a Flask web application
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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
