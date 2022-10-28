import os
import json
import numpy as np
from PIL import Image as im


presetsDir = os.path.dirname(__file__) + '/presets/'
presetImgsDir = presetsDir + '/presetImgs/'


def takeValues(name):
    dir = os.path.join(os.path.dirname(__file__), 'presets')
    for dirName, _, fileNames in os.walk(dir):
        for fileName in fileNames:
            if fileName == '{}.json'.format(name):
                with open(os.path.join(dir, fileName)) as jfile:
                    values = json.load(jfile)
                    return values
    # create takeValues function
    # take preset name as a parameter
    # find the corresponding json file
    # retrieve values
    # return values in specific format (in main)


def retrievePresetLists():
    presetList = []
    for dirName, _, fileNames in os.walk(presetsDir):
        for fileName in fileNames:
            if fileName.endswith('.json'):
                presetList.append(
                    {
                        "presetName": "{}".format((os.path.splitext(fileName)[0]))
                    }
                )
    return presetList
    # get names of each file in presets folder
    # send list of names back
    # have the function look directly in the presets folder
    # no file extensions
    # format as list of strings in json
    # name: preset name
    # imagefile: later


def createPreset(values):
    newPreset = {
        "name": "{}".format(values['presetName']),
        "pixels": []
    }
    p = open('presets/{}.json'.format(newPreset["name"]), "w")
    p.write(json.dumps(newPreset))
    p.close()

    array = np.arange(0, 256, 1, np.uint8)
    array = np.reshape(array, (16, 16))
    data = im.fromarray(array)
    data.save(presetImgsDir + 'gfg_dummy_pic.png')

    # parse the json to get the name and pixel values
    # make the file with the name
    # insert in a dummy image file path
    # insert the pixel value list into the file
