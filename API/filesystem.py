import os
import json


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
    dir = os.path.dirname(__file__) + '/presets/'
    imgDir = 'presets/presetImgs/'
    presetList = []

    for dirName, _, fileNames in os.walk(dir):
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


def createPreset(name, list):

    newPreset = {
        "name": "{}".format(name),
        "pixels": []
        }

    newPreset["pixels"].append(
        {
            "name": "pix[{}]".format(name),
            "value": "{}".format(list)
        }
    )
    p = open('presets/{}.json'.format(name), "w")
    p.write(json.dumps(newPreset))
    p.close()

    # parse the json to get the name and pixel values
    # make the file with the name
    # insert in a dummy image file path
    # insert the pixel value list into the file