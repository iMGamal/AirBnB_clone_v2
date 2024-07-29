#!/usr/bin/python3
"""Module for flask server."""


from flask import Flask

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def welcome():
    """Handle initial route."""
    return "Hello HBNB!"


@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handle second route."""
    return "HBNB"


@web_app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Handle third route."""
    formatted = text.replace('_', ' ')
    return f"C {formatted}"


@web_app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    formatted = text.replace('_', ' ')
    return f"Python {formatted}"


@web_app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return f"{n} is a number"
    return "NULL"


web_app.run(host='0.0.0.0', port=5000)

