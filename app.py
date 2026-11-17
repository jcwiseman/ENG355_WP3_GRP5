"""@file app.py
@brief Flask web application entry point.

@details Defines the Flask app and its routes. Imports helper functions
from api.py and serves the HTML templates.
"""

from flask import Flask, render_template, request, jsonify
from api import api_func_one

## @brief The Flask application instance.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """@brief Serves the home page.

    @details Renders index.html and passes the current counter value to it.
    @return The rendered HTML page.
    """
    return render_template("index.html", counter=counter)


@app.route("/print-class", methods=["GET"])
def print_class():
    """@brief Returns the class name from the API helper.

    @details Calls api_func_one() with the course name "English 355".
    @return The course name as the response body.
    """
    return api_func_one("English 355")


if __name__ == "__main__":
    app.run(debug=True)
