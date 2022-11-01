from distutils.command.config import config
import json
from operator import and_
from flask import Flask, jsonify, request, json, send_file
from flask.wrappers import Response
import filesystem
from flask_cors import CORS
import LTUmatrix
import os

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run

# Initialize flask app
app = Flask(__name__)
# Enable CORS security for flask app
CORS(app)

configFile = os.path.dirname(__file__) + 'Config/'
File = configFile + 'config.json'

def storeLast(data):
    file = open('Config/config.json',"w")
    a = json.dump(data , file , indent = 2)
    return (a)
    

def startupPixels():
    file = open('Config/config.json','r')
    x = json.load(file)
    LTUmatrix.lightupMatrix(x)
    file.close

startupPixels()
    

@app.route("/", methods=['POST'])
def maxtrixInput():
    # Receive pixel data from website and send to LED matrix
    try:
        # If the program successfully lights up the LED matrix with the
        # pixel data, return a success response, if unsuccessful, return
        # a internal server error response.
        LTUmatrix.lightupMatrix(request.get_json()) or storeLast(request.get_json())
        return "", 200
    except:
        # If for any reason the program fails, return an internal
        # server error response.
        return "", 500


@app.route("/presetlist", methods=['GET'])
def getPresetsList():
    # Get and return a list of existing presets in the filesystem
    try:
        return jsonify(filesystem.retrievePresetLists())
    except:
        # If for any reason the program fails, return an internal
        # server error response.
        return Response(status=500, mimetype="application/json")


@app.route("/presetimg", methods=['GET'])
def getPresetImg():
    # Given a preset name, read the preset's file to find its associated image,
    # then return the image file.

    # Retrieve the name of the preset from the request
    reqArgs = request.args.to_dict()
    try:
        # Open the JSON file of the requested image's assocaited preset
        f = json.loads(
            open(f"{app.root_path}/presets/{reqArgs['presetName']}.json", "r").read())
        # Retrieve the image file path from preset file and send back the file it referenced
        return send_file(f['imgFile'])
    except:
        # If for any reason the program fails, return an internal
        # server error response.
        return Response(status=500, mimetype="application/json")


@app.route("/preset", methods=['GET'])
def getPreset():
    # When a preset is clicked on the website's preset list, the clicked
    # preset's name is sent and the pixel values of that preset are returned
    # and assigned to the pixel grid on the website.

    # Retrieve the name of the preset from the request
    reqArgs = request.args.to_dict()
    try:
        # Return the pixel values of the requested preset
        return jsonify(filesystem.takeValues(reqArgs['presetName'])['pixels'])
    except:
        # If for any reason the program fails, return an internal
        # server error response.
        return Response(status=500, mimetype="application/json")


@app.route("/preset", methods=['POST'])
def createPreset():
    # Send recieved pixel data to function that creates preset
    filesystem.createPreset(request.get_json())
    filesystem.presetImg(request.get_json())
    return "", 200
    # given a preset name and list of pixels in json
    # make a file with the filename being the preset name if the file doesn't already exist
    # if the file already exists, overwrite the data
    # in the file match the preset format in itemframe.json (need image file path and pixels)

@app.route("/presetimg", methods=['POST'])
def uploadImage():
    file = request.files.get('uploadImage')
    presetName = request.form.get('uploadImageName')

    conFile, nConFile = filesystem.createDict(presetName, file)
    lConFile = json.loads(conFile)
    lConFile2 = json.loads(nConFile)

    filesystem.createPreset(lConFile)
    filesystem.uploadedPresetImg(lConFile2)
    # Send recieved pixel data to function that creates preset
    return "", 200
    # given a preset name and list of pixels in json
    # make a file with the filename being the preset name if the file doesn't already exist
    # if the file already exists, overwrite the data
    # in the file match the preset format in itemframe.json (need image file path and pixels)

@app.route("/quit", methods=['POST'])
def shutdown():
    LTUmatrix.turnOff(request.get_json())
    return "",204
