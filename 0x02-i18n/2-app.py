#!/usr/bin/env python3
"""
creating a flask app instance
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    class to configure Babel for i18n
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    function to determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', methods=['GET'])
def index_route():
    """
    an index page for testing i18n
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=1)




