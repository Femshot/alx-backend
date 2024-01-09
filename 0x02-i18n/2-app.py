#!/usr/bin/env python3
""" A simple flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration class for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localselctor
def get_locale():
    """Selecting best lan for locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Index Page Route """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(port="5000", debug=True)
