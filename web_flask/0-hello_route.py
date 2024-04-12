#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
"""Flask class and render_template method"""
app = Flask(__name__)


""" App route section"""


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
