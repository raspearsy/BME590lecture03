from flask import Flask, request, jsonify
from SummingFunctionL03 import summer
app = Flask(__name__)

request_counter = 0


@app.route("/hello/<name>")
def hello(name):
    return "Hello World {0}".format(name)


@app.route("/api/data")
def api():
    x = {"temp": [20, 21, 21], "time": [10, 20, 30], "unit": "s"}
    return jsonify(x)


@app.route("/api/add", methods=['POST'])
def add():
    global request_counter
    request_counter = request_counter + 1
    # x = request.json['a'] + request.json['b']
    x = summer(request.json['a'], request.json['b'])
    return jsonify(x)


@app.route("/api/requests")
def requests():
    return jsonify(request_counter)
