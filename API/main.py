from cgitb import text
import json
from flask import Flask, jsonify, request
import API.LTUmatrix as LTUmatrix

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run

app = Flask(__name__)

testPreset = {
    "imgFile": "presets/presetImgs/itemframe.png",
    "pixels":
    [
        {
            f"name": f"pix[0]",
            f"value": "#FFFFFF"
        },
        {
            f"name": f"pix[1]",
            f"value": f"#FFFFFF"
        },
        {
            f"name": f"pix[2]",
            f"value": f"#FFFFFF"
        }
    ]
}

testPresetList = [
    {
        f"presetName": f"itemframe"
    },
    {
        f"presetName": f"sword"
    },
    {
        f"presetName": f"pickaxe"
    }
]


def createTestPixValues():
    for i in range(256):
        testPreset["pixels"].append(
            {
                f"name": f"pix[{i}]",
                f"value": "#FFFFFF"
            }
        )


postData = []


createTestPixValues()


@app.route("/", methods=['GET'])
def hello_world():
    # Sends the data in the list as a response
    return jsonify(postData)


@app.route("/", methods=['POST'])
def maxtrixInput():
    LTUmatrix.lightupMatrix(request.get_json())
    # Just adds data sent to the list. 204 code response
    return "", 204


@app.route("/presetlist", methods=['GET'])
def getPresetsList():
    # Check filesystem for presets
    # return list of all presets
    return jsonify(testPresetList)


@app.route("/preset", methods=['GET'])
def getPreset():
    # Find preset file
    # convert it if needed
    # send back the matrix values
    # For testing
    return jsonify(testPreset["pixels"])
