#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:05:15 2018

@author: talles
"""

import cv2 as cv
import math as math
import numpy as np
from PIL import Image
from scipy.ndimage import imread



# Read image in BGR
img = Image.open("guy.jpeg")
output = Image.new("RGBA", img.size)

for i in range(img.size[1]):     #Loop sobre cada pixel da imagem 
        for j in range(img.size[0]):
            p = img.getpixel((j,i))
            d = math.sqrt(math.pow(p[0], 2) + math.pow((p[1] - 255), 2) + math.pow(p[2], 2))
            g = p[1]
            if d > 200:
                d = 255
            if d < 255:
                g = min(p[2],p[1])
            output.putpixel((j,i),(p[0],g,p[2], int(d)))
output.save("guy_sem_fundo.png", "PNG" )
img2 = cv.imread("guy_sem_fundo.png",1)
background = cv.imread("background2.png",1)
for i in range(background.shape[0]):
        for j in range(background.shape[1]):
            if img2[i][j][2] > 9:
                background[i][j] = img2[i][j]


cv.imwrite("chroma.png", background)