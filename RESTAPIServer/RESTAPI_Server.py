import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/v1/ressources/calculator/add', methods=['POST'])
def add():
    t = request.json
    print(t)
    sum = int(t['x']) + int(t['y'])
    print(str(sum))
    result = {'Summe' : str(sum)}
    print(result)
    return json.dumps(result)

@app.route('/v1/ressources/calculator/sub', methods=['POST'])
def sub():
    t = request.json
    print(t)
    diff = int(t['x']) - int(t['y'])
    print(str(diff))
    result = {'Differenz' : str(diff)}
    print(result)
    return json.dumps(result)



app.run()