#!/usr/bin/env python3
"""creating a flask app instance with configurations for i18n
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Dict, Union, Optional


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary from users if login_as is passed as
    query string
    """
    user_id = request.args.get('login_as')
    user_id = int(user_id)
    if user_id and user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user and set it as a global on flask.g.user
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    function to determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def index_route():
    """
    an index page for testing i18n
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=1)
