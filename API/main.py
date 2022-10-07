import json
from flask import Flask, jsonify, request
from keyboard import wait

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run

app = Flask(__name__)

data = [{'example': 'data', 'sample': 'amount'}]


@app.route("/", methods=['GET'])
def hello_world():
    # Sends the data in the list as a response
    return jsonify(data)


@app.route("/", methods=['POST'])
def matrix_input():
    # Just adds data sent to the list. 204 code response
    data.append(request.get_json())
    return '', 204
