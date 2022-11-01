import os
import json
import numpy as np
from itertools import chain
from PIL import Image as im

presetsDir = os.path.join(os.path.dirname(__file__), "presets/")
presetImgsDir = os.path.join(presetsDir, "presetImgs/")


def hex_to_rgb(value):
    value = value.lstrip('#')
    rgbList = []
    for i in (0, 2, 4):
        rgbList.append(int(value[i:i + 2], 16))
    return np.array(rgbList)

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

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def createDict(name, image):
    raw_image = im.open(image)
    raw_image = raw_image.convert('RGB')
    pix_val = list(raw_image.getdata())
    preset = {
        "presetName": "{}".format(name.replace(' ', '_')),
        "pixels": []
    }

    preset2 = {
        "presetName": "{}".format(name.replace(' ', '_')),
        "pixels": []
    }

    row = []
    start = 0
    end = 256
    step = 16

    for i in range(start, end, step):
        x = i
        row.append((pix_val[x:x + step]))

    row[0].reverse()
    row[2].reverse()
    row[4].reverse()
    row[6].reverse()
    row[8].reverse()
    row[10].reverse()
    row[12].reverse()
    row[14].reverse()

    finVal = list(chain.from_iterable(row))
    for index, val in enumerate(finVal):
        t = {
            f"name": f"pix[{index}]",
            f"value": f"{rgb_to_hex((val))}"
        }
        preset['pixels'].append(t)
    jsonPix = json.dumps(preset)

    for index, val in enumerate(pix_val):
        t = {
            f"name": f"pix[{index}]",
            f"value": f"{rgb_to_hex(val)}"
        }
        preset2['pixels'].append(t)
    jsonPix2 = json.dumps(preset2)
    return(jsonPix, jsonPix2)


def createPreset(values):
    newPreset = {
        "imgFile": presetImgsDir + "{}.png".format(values['presetName'].replace(' ', '_')),
        "pixels": values['pixels']
    }
    p = open(presetsDir + '{}.json'.format(values['presetName'].replace(' ', '_')), "w")
    p.write(json.dumps(newPreset))
    p.close()


    # parse the json to get the name and pixel values
    # make the file with the name
    # insert in a dummy image file path
    # insert the pixel value list into the file

def presetImg(values):
    colors = np.empty((16, 16, 3), dtype=np.uint8)

    # int(len(values['pixels']) ** (1/2))
    for i in range(16):
        for j in range(16):
            colors[i, j] = (hex_to_rgb(values['pixels'][16 * i + j]['value']))

    image = im.fromarray(colors, "RGB")
    # for i in range(16):
    # for j in range(16):
    # print(image.getpixel((i, j)))
    image.save(presetImgsDir + '{}.png'.format(values['presetName'].replace(' ', '_')), 'PNG')


def uploadedPresetImg(values):
    colors = np.empty((16, 16, 3), dtype=np.uint8)

    # int(len(values['pixels']) ** (1/2))
    for i in range(16):
        for j in range(16):
            colors[i, j] = (hex_to_rgb(values['pixels'][16 * i + j]['value']))

    image = im.fromarray(colors, "RGB")
    # for i in range(16):
    # for j in range(16):
    # print(image.getpixel((i, j)))
    image.save(presetImgsDir + '{}.png'.format(values['presetName'].replace(' ', '_')), 'PNG')

    # parse the json to get the name and pixel values
    # make the file with the name
    # insert in a dummy image file path
    # insert the pixel value list into the file
