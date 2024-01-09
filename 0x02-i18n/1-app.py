#!/usr/bin/env python3
""" A simple flask app """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration class for languages """
    LANGUAGES = ["en", "fr"]


@app.route('/')
def index():
    """ Index Page Route """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
