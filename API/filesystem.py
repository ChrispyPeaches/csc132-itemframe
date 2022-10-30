import os
import json
from PIL import Image


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
def createPreset(values):
    print(values)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def createDict(image):
    raw_image = Image.open(image)
    raw_image = raw_image.convert('RGB')
    pix_val = list(raw_image.getdata())
    pixels = []
    for index, val in enumerate(pix_val):
        t = {
            f"name": f"pix[{index}]",
            f"value" : f"{rgb_to_hex((val))}"
        }
        pixels.append(t)
        jsonPix = json.dumps(pixels)
    return(jsonPix)