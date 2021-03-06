#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    import numpy
except ImportError:
    exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

from rgbmatrix5x5 import RGBMatrix5x5

print("""
RGBMatrix5x5 - Random Blinky!

Displays random warm colours across the matrix.

Press Ctrl+C to exit!
""")

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.8)

height = rgbmatrix5x5.height
width = rgbmatrix5x5.width

while True:
    rand_mat = numpy.random.rand(width, height)
    for y in range(height):
        for x in range(width):
            h = 0.1 * rand_mat[x, y]
            s = 0.8
            v = rand_mat[x, y]
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
            rgbmatrix5x5.set_pixel(x, y, r, g, b)
    rgbmatrix5x5.show()
    time.sleep(0.01)
