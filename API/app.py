from cgitb import text
import json
from flask import Flask, jsonify, request, json, send_file
from flask.wrappers import Response

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
        f"presetName": f"itemframe",
        f"presetImgFile": f"presets/presetImgs/itemframe.png"
    },
    {
        f"presetName": f"sword",
        f"presetImgFile": f"presets/presetImgs/sword.png"
    },
    {
        f"presetName": f"pickaxe",
        f"presetImgFile": f"presets/presetImgs/pickaxe.png"

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


@app.route("/", methods=['POST'])
def maxtrixInput():
    postData.append(request.get_json())
    # Just adds data sent to the list. 204 code response
    return "", 204


@app.route("/presetlist", methods=['GET'])
def getPresetsList():
    # Check filesystem for presets
    # return list of all presets
    return jsonify(testPresetList)


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
        return Response(status=400, mimetype="application/json")


@app.route("/preset", methods=['GET'])
def getPreset():
    # Find preset file
    # convert it if needed
    # send back the matrix values
    # For testing
    return jsonify(testPreset["pixels"])
