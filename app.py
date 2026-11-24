import inspect

from flask import Flask, jsonify, redirect, render_template, request, url_for

import api

app = Flask(__name__)

# Every public function defined in api.py, by name
FUNCTIONS = {
    name: func
    for name, func in inspect.getmembers(api, inspect.isfunction)
    if func.__module__ == api.__name__ and not name.startswith("_")
}


@app.route("/")
def index():
    functions = {
        name: list(inspect.signature(func).parameters)
        for name, func in FUNCTIONS.items()
    }
    return render_template("index.html", functions=functions)


@app.route("/docs")
def docs():
    return redirect(url_for("static", filename="docs.html"))


@app.route("/api/<name>")
def call(name):
    if name not in FUNCTIONS:
        return jsonify(error=f"no function named '{name}'"), 404

    func = FUNCTIONS[name]
    args = request.args.to_dict()
    try:
        inspect.signature(func).bind(**args)
    except TypeError as e:
        return jsonify(error=str(e)), 400

    try:
        return jsonify(result=func(**args))
    except ValueError as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(debug=True)
