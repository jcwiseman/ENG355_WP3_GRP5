from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

counter = -1


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", counter=counter)


@app.route("/mack-address", methods=["GET"])
def mack():
    return jsonify({"name": "Mack Address Hansen"})


if __name__ == "__main__":
    app.run(debug=True)
