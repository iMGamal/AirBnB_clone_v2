#!/usr/bin/python3
"""Module for flask server."""


from flask import Flask

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def welcome():
    """Handle the initial route."""
    return "Hello HBNB!"


web_app.run(host='0.0.0.0', port=5000)

