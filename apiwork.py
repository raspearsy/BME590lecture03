from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return "Hello World {0}".format(name)


@app.route("/api/data")
def api():
    x = {"temp": [20, 21, 21], "time": [10, 20, 30], "unit": "s"}
    return jsonify(x)


@app.route("/api/add", methods=['POST'])
def add():
    x = request.json['a'] + request.json['b']
    return jsonify(x)
