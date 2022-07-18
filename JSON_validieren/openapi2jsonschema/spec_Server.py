import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open("./spec.yaml") as fobj:
    spec = fobj.read()

@app.route('/spec', methods=['GET'])
def add():

    return spec




app.run()