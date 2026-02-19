#!/usr/bin/env python3

######### Task 2 ##########
# 1. Create a module that has following methods - convertToGray, threshold, invert_mask
# 2. Import this custom module to use these defined class methods in this file.
# 3. Use Object-Oriented Programming to read frames from the 'test_video.mp4', 
#    extract the red and green beacon placed on the dock.
# 
# Useful Suggestion:
# 1. For initial developement use the 'dock.png'
# 2. Use 0 instaed of 1 in the 'waitKey' function, to play the video frame by frame. Press any key
#    to roll through frames. *Note - Some frames might look frozen, but continue rolling. Its just how I recorded the video.
###########################

import cv2 as cv
from matplotlib import pyplot as plt
import os
from threshold import Threshold
from return_values import pixel_value

cdir = os.getcwd()
print(cdir)

class Docking:
    def __init__(self, file):
        self.file = cdir + file

    def extraction(self):
        img = Threshold(self.file)
        print(img)

        gray_img = img.convertToGray()
        mask = img.thresholding()
        extracted = img.invert_mask()

        # show images
        titles = ['Original Image', 'Grayscale', 'Mask', 'Extracted']
        images = [img.img, gray_img, mask, extracted]

        for i in range(4):
            plt.subplot(2,2,i+1) 
            plt.imshow(images[i], 'gray', vmin=0, vmax=255)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

            # print the color of the pixel located at [43, 268]
            px_value = pixel_value(images[i], [43, 268])
            print(px_value)
        
        plt.show()

def main():
    file = "/src/task2/dock.png"
    frame_reader = Docking(file)

    # currently only printing red beacon from dock.png
    beacon_extraction = frame_reader.extraction()

if "__main__" == __name__:
    main()