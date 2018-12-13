#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:43:42 2018

@author: talles
"""

import cv2 as cv
import numpy as np

    
image = cv.imread("Fig0305(a)(DFT_no_log).tif",0)
print(np.max(image))
c = 30
for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
            pixel = c*np.log(1+image[i][j])
            image[i][j] = pixel
cv.imwrite("invertedlogaritmoconstante.png",image)
print (image)