from time import sleep
import board
import neopixel
import json
import sys

data = json.loads('{"#FFFFFF":3, "#B12345":78}')

#PLUG DIN WIRE INTO PIN M18 ON PI BREAKOUT BOARD
MATRIX_PIN = board.D12 

# li = [ board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19]
# for i in li:
#     print(i)


pixels = neopixel.NeoPixel(board.D12, 256)
sleep(1)
#converts Hex values into rgb values function
def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i+2],16)for i in (0,2,4))

#uses the functionfrom above to return the pixel and hex value of the json
def lightupMatrix(data):
    for key, value in data.items():
        pixels[value] = hex_to_rgb(key)

 

 
lightupMatrix(data)
