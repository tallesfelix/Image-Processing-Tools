#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:20:56 2018

@author: talles
"""

import cv2 as cv
import numpy as np

#def convolucao(img, c):
#    aux = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
#    for i in range (1, img.shape[0]-1):
#        for j in range (1, img.shape[1]-1):
#            valor = img.item(i-1,j-1)*c[0][0]+img.item(i-1, j)*c[0][1]+img.item(i-1,j+1)*c[0][2]+img.item(i,j-1)*c[1][0]+omh.item(i,j)*c[1][1]+img.item(i,j+1)*c[1][2]+img.item(i+1,j-1)*c[2][0]+img.item(i+1,j)*c[2][1]+img.item(i+1,j+1)*c[2][2]
#            if (valor > 255):
#                valor = 255
#            elif(valor < 0):
#                valor = 0
#            aux.itemset((i,j), valor)
#    return aux

img = cv.imread("Fig0417(a)(barbara).tif",0)
print(img[0][0])
kernel = np.array(([1,1,1],[0,0,0],[-1,-1,-1]), dtype="int")
(ih, iw) = img.shape[:2]
(kh, kw) = kernel.shape[:2]
pad = (kw - 1) // 2
img = cv.copyMakeBorder(img, pad, pad, pad, pad, cv.BORDER_CONSTANT, 0)
output = np.zeros((ih, iw), dtype="int")
for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			# extract the ROI of the image by extracting the
			# *center* region of the current (x, y)-coordinates
			# dimensions
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
 
			# perform the actual convolution by taking the
			# element-wise multiplicate between the ROI and
			# the kernel, then summing the matrix
			k = (roi * kernel).sum()
 
			# store the convolved value in the output (x,y)-
			# coordinate of the output image
			output[y - pad, x - pad] = k

print(img[2][1])
#imgR = convolucao(img,matriz)
#cv.imwrite("convolucao.png", imgR)
                
                
                