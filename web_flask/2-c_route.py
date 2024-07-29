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


web_app.run(host='0.0.0.0', port=5000)

