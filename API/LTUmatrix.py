from time import sleep
from unicodedata import name
import board
import neopixel



#PLUG DIN WIRE INTO PIN M18 ON PI BREAKOUT BOARD

# li = [ board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19]
# for i in li:
#     print(i)

pixels = neopixel.NeoPixel(board.D18, 256)
#converts Hex values into rgb values function
def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i+2],16)for i in (0,2,4))

#uses the functionfrom above to return the pixel and hex value of the json
def lightupMatrix(data):
    try:
        pixels = neopixel.NeoPixel(board.D18, 256)
    except:
        pixels = neopixel.NeoPixel(board.D12, 256)
    for x in data:
        num = ""
        for y in x["name"]:
            if y.isdigit():
                num = num + y
                pixel = int(num)
        pixels[pixel] = hex_to_rgb(x['value'])

def turnOff(data):
    for x in data:
        pixels.deinit(x)

 


