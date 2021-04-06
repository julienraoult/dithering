#!/usr/bin/env python

""" Floyd-Steinberg Dithering algorithm, see:
    http://en.wikipedia.org/wiki/Floyd-Steinberg
    https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Steinberg
    https://stackoverflow.com/questions/63074421/what-is-wrong-with-my-floyd-steinberg-dithering-implementation
"""

import cv2 as cv
from matplotlib import pyplot as plt 
import numpy as np

class Dither:
    def __init__(self, src="orange-kitten.jpg"):
        self.image = np.array(cv.cvtColor(cv.imread(src), cv.COLOR_BGR2GRAY))
        self.pixel = []
        self.pixel = np.copy(self.image)
        self.pixel = self.pixel.astype('int') # prevent overflow

    def process(self):
        for y in range(1, self.image.shape[0]-1):
            for x in range(1, self.image.shape[1]-1):

                oldpixel    = self.pixel[y][x]
                newpixel    = np.round(oldpixel/255) * 255 # binary quantization (0 or 255)
                quant_error = oldpixel - newpixel
    
                self.pixel[y][x]      = newpixel
                self.pixel[y][x+1]   += quant_error * 7/16
                self.pixel[y+1][x]   += quant_error * 5/16
                self.pixel[y+1][x-1] += quant_error * 3/16
                self.pixel[y+1][x+1] += quant_error * 1/16
                
    def display(self):
        plt.imshow(self.pixel, cmap="gray")
        plt.show()

def main():
    print("Dithering in python!")
    dither = Dither()
    dither.process()
    dither.display()  

if __name__ == "__main__":
    main()
           
