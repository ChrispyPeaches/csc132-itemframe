from time import sleep
import board
import neopixel
import json
import sys


#PLUG DIN WIRE INTO PIN M18 ON PI BREAKOUT BOARD

# li = [ board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19]
# for i in li:
#     print(i)


pixels = neopixel.NeoPixel(board.D18, 256)
sleep(1)
#converts Hex values into rgb values function
def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i+2],16)for i in (0,2,4))

#uses the functionfrom above to return the pixel and hex value of the json
def lightupMatrix(data):
    for x in data['pixels'] :
        pixel=int(x['name'])
        pixels[pixel] = hex_to_rgb(x['value'])

 

data = '{"pixels":[{"name":"1","value":"#FFFFFF"},{"name":"4","value":"#B12345"},{"name":"22","value":"#FFFFFF"},{"name":"23","value":"#FFFFFF"},{"name":"34","value":"#FFFFFF"}]}'
Loaddata=json.loads(data)
lightupMatrix(Loaddata)
