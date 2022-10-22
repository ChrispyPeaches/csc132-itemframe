import os
import json


def takeValues(name):
    dir = 'presets/'
    for dirName, _, fileNames in os.walk(dir):
        for fileName in fileNames:
            if fileName == '{}.json'.format(name):
                break
    return fileName
    # create takeValues function
    # take preset name as a parameter
    # find the corresponding json file
    # retrieve values
    # return values in specific format (in main)


def retrievePresetLists():
    dir = 'presets/'
    imgDir = 'presets/presetImgs/'
    presetList = {
        "names":
        [

        ]
    }

    for dirName, _, fileNames in os.walk(dir):
        for fileName in fileNames:
            if fileName.endswith('.json'):
                for iDirName, _, iFileNames in os.walk(imgDir):
                    for iFileName in iFileNames:
                        if iFileName.endswith('.png') or iFileName.endswith('.jpg'):
                            if((os.path.splitext(fileName)[0]) == (os.path.splitext(iFileName)[0])):
                                presetList["names"].append(
                                    {
                                        "presetName": "{}".format((os.path.splitext(fileName)[0])),
                                        "presetImageFile": "presets/presetImgs/{}".format(iFileName)
                                    }
                                )
    finalList = json.dumps(presetList)
    return finalList
    # get names of each file in presets folder
    # send list of names back
    # have the function look directly in the presets folder
    # no file extensions
    # format as list of strings in json
    # name: preset name
    # imagefile: later
