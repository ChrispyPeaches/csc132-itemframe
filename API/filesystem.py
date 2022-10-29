import os
import json
import numpy as np
from PIL import Image as im

presetsDir = os.path.dirname(__file__) + '/presets/'
presetImgsDir = presetsDir + '/presetImgs/'


def hex_to_rgb(value):
    value = value.lstrip('#')
    rgbList = []
    for i in (0, 2, 4):
        rgbList.append(int(value[i:i + 2], 16))
    return np.array(rgbList)


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
        "pixels": values['pixels']
    }
    p = open(presetsDir + '{}.json'.format(newPreset["name"]), "w")
    p.write(json.dumps(newPreset))
    p.close()

    colors = np.empty((16, 16,3), dtype=np.uint8)

    # int(len(values['pixels']) ** (1/2))
    for i in range(16):
        for j in range(16):
            colors[i,j] = (hex_to_rgb(values['pixels'][i + j]['value']))
    #colors = np.array(colors, dt)
    #colors.reshape((16,16,3))
    print(colors)
    image = im.fromarray(colors, "RGB")
    for i in range(16):
        for j in range(16):
            print(image.getpixel((i, j)))
    image.save(presetImgsDir + '{}.png'.format(values['presetName']), 'PNG')

    #array = im.fromarray(data)
    # print(data)
    #array = np.array(values['value'])
    #narray = np.array(values['pixels'])
    #array = np.arange(0, 256, 1, np.uint8)
    #array = np.reshape(array, (16, 16))
    #data = im.fromarray(array)
    # parse the json to get the name and pixel values
    # make the file with the name
    # insert in a dummy image file path
    # insert the pixel value list into the file
