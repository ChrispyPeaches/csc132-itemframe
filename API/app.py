import json
from flask import Flask, jsonify, request, json, send_file
from flask.wrappers import Response
import filesystem
from flask_cors import CORS
#import LTUmatrix

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run


app = Flask(__name__)
CORS(app)

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


#@app.route("/", methods=['POST'])
#def maxtrixInput():
    #LTUmatrix.lightupMatrix(request.get_json())
    # Just adds data sent to the list. 204 code response
    #return "", 204


@app.route("/presetlist", methods=['GET'])
def getPresetsList():
    # Check filesystem for presets
    # return list of all presets
    return jsonify(filesystem.retrievePresetLists())


@app.route("/presetimg", methods=['GET'])
def getPresetImg():
    # Given a preset name, read the preset's file to find its associated image,
    # then return the image file.
    reqArgs = request.args.to_dict()
    try:
        f = json.loads(
            open(f"{app.root_path}/presets/{reqArgs['presetName']}.json", "r").read())

        return send_file(f"{app.root_path}/{f['imgFile']}")
    except:
        return Response(status=500, mimetype="application/json")


@app.route("/preset", methods=['GET'])
def getPreset():
    reqArgs = request.args.to_dict()
    # Trust me, it works \/
    return jsonify(filesystem.takeValues(reqArgs['presetName'])['pixels'])


@app.route("/preset", methods=['POST'])
def createPreset():
    value = request.get_json()
    # Send recieved pixel data to function that creates preset

    return "", 204
