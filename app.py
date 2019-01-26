from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hello, World!')

@app.route("/foo/<someId>")
def foo_url_arg(someId):
    return jsonify({"echo": someId})