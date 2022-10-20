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
for j in range(128):
    pixels[j] = (0, 255, 0)
for i in range(128, 256, 1):
    pixels[i] = (255, 0, 0)
sleep(2)
pixels.deinit()
