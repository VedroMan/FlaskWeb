from flask import Flask, jsonify 
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*" : {'origins' : "*"} })


@app.route("/")
def hello_world():
    return "<h1>Hello!</h1>"
