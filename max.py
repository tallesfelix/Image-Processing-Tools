#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 20:55:14 2018

@author: talles
"""
import cv2 as cv
import numpy as np
def filtroMax(img):
    s = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    for i in range(1,img.shape[0]-1):     #Loop sobre cada pixel da imagem 
        for j in range(1,img.shape[1]-1):
            lista = [img.item(i-1,j-1), img.item(i-1,j), img.item(i-1,j+1),img.item(i,j-1), img.item(i, j), img.item(i, j+1), img.item(i+1, j-1), img.item(i+1, j), img.item(i+1, j+1)] 
            lista.sort()
            valor = lista[8]
            s[i][j] = valor

    return s

img = cv.imread("Fig0512(a)(ckt-uniform-var-800).tif",0)

cv.imwrite('max.png', filtroMax(img))

