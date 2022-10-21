from time import sleep
import board
import neopixel

# PLUG DIN WIRE INTO PIN M18 ON PI BREAKOUT BOARD
MATRIX_PIN = board.D12

# li = [ board.D11, board.D12, board.D13, board.D14, board.D15, board.D16, board.D17, board.D18, board.D19]
# for i in li:
#     print(i)
pixels = neopixel.NeoPixel(board.D12, 256)
pixels.deinit()
sleep(1)
pixels = neopixel.NeoPixel(board.D12, 256)
sleep(1)
#converts Hex values into rgb values function
def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i+2],16)for i in (0,2,4))

#uses the functionfrom above to return the pixel and hex value of the json
def lightupMatrix(pixelArr, hex_values):
    i = 0
    for pixel in pixelArr:
        pixels[pixel] = hex_to_rgb(hex_values[i])
        i += 1

 

 
pixel = [1,2]
hex_value = ['#ff0066','FFFFFF']
lightupMatrix(pixel,hex_value)
sleep(2)
pixels.deinit()
