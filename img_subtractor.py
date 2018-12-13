#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:39:27 2018

@author: talles
"""
import cv2 as cv
import numpy as np
img1 = cv.imread("Fig0648(a)(lenna-noise-R-gauss-mean0-var800).tif")
img2 = cv.imread("Fig0648(b)(lenna-noise-G-gauss-mean0-var800).tif")	
img = np.subtract(img1, img2)
cv.imwrite("subtracted_img.png", img)