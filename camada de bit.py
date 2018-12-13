#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:10:28 2018

@author: talles
"""


import cv2 as cv
image = cv.imread("Fig0314(a)(100-dollars).tif",0)

for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
        bits = bin(image[i][j])[2:].zfill(8)
        if(bits[3] == "1"):
            image[i][j]= image[i][j]
        else:
            image [i][j] = 0           
cv.imwrite("invertedcamadadebit.png",image)