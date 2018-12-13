#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:19:29 2018

@author: talles
"""

import cv2 as cv
import numpy as np
from math import *

def rgbTocmy(r,g,b):
    c = 1-r
    m = 1-g
    y = 1-b
    return c,m,y

def cmyTorgb(c,m,y):
    r = 1-c
    g = 1-m
    b = 1-y
    return r,g,b

def rgb2hsi(r,g,b):
     R = r
     G = g
     B = b  
     r = r/255
     b = g/255
     g = b/255           
     i = (R+G+B)/(3*255)
     s = 1 - ((3*min(R,G,B)/(R+G+B)))
     num = (((r-g) + (r - b))/2)
     den = ((((r - g) ** 2) + ((r - b) * (g - b))) ** 0.5)
     theta = np.degrees(np.arccos(num/den))
     if (b <= g):
         h = theta
     else:
         h = 360 - theta     
     H = h
     S = s
     I = i
     print(B,"b")
     print(G,"g")
     print(R,"r")
     print(H,"h")
     print(S,"s")
     print(I,"i")
     return H,S,I


             

img = cv.imread("Fig0638(a)(lenna_RGB).tif",1)
cv.imwrite('rgb2hsi.png',rgb2hsi(194,123,78))