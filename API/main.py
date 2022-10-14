import json
from flask import Flask, jsonify, request

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run

app = Flask(__name__)

testPixValues = []


def createTestPixValues():
    for i in range(256):
        testPixValues.append({
            f"name": f"pix[{i}]",
            f"value": "#FFFFFF"
        })


postData = []


createTestPixValues()


@app.route("/", methods=['GET'])
def hello_world():
    # Sends the data in the list as a response
    return jsonify(postData)


@app.route("/", methods=['POST'])
def maxtrixInput():
    postData.append(request.get_json())
    # Just adds data sent to the list. 204 code response
    return "", 204


@app.route("/presetlist", methods=['GET'])
def getPresetsList():
    # Check filesystem for presets
    # return list of all presets
    pass


@app.route("/preset", methods=['GET'])
def getPreset():
    # Find preset file
    # convert it if needed
    # send back the matrix values

    # For testing
    return jsonify(testPixValues)
