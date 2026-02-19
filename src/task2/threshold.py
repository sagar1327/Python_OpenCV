#!/usr/bin/env python3

# imported important modules
import cv2 as cv
from matplotlib import pyplot as plt
import os
from return_values import pixel_value

cdir = os.getcwd()

class Threshold:

    def __init__(self, file_path):
        self.img = cv.imread(file_path, cv.IMREAD_COLOR_RGB)
        # check if can read the image or not
        assert self.img is not None, "file could not be read, check with os.path.exists()"

    def convertToGray(self):
        # reads an image/video, and converts it into gray-scale
        self.gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

        return self.gray_img

    def thresholding(self):
        # for red
        ret,self.mask = cv.threshold(self.gray_img,88,255,cv.THRESH_BINARY)
        
        return self.mask

    def invert_mask(self):
        mask_inv = cv.bitwise_not(self.mask)
        mask_img = cv.bitwise_and(self.img,self.img,mask = mask_inv)

        return mask_img
