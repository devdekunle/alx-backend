#!/usr/bin/env python3
"""
creating a flask app instance
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_route():
    """
    an index page for testing i18n
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=1)
