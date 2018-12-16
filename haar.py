# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:49:11 2018

@author: Talles
"""

import cv2 as cv
import numpy as np


def haar_vetor(dado):
    z=0
    temp = np.zeros(dado.shape[0], dtype=np.float)
    for i in range(0,512,2):
        temp[z] = dado[i]*0.5 + dado[i+1]*0.5
        temp[z+256] = (dado[i]*0.5+dado[i+1]*(-0.5))+127
        if(z != 255):
            z = z+1
    for i in range(0,dado.shape[0]):
        dado[i] = temp[i]
        
def haar(img,it):
    linha = np.zeros(img.shape[0])
    for h in range(it):
        for i in range (0, img.shape[0]):
            for j in range (0, img.shape[0]):
                linha[j] = img[i][j]
            haar_vetor(linha)
            for j in range(0, linha.shape[0]):
                img[i][j] = linha[j]
        coluna = np.zeros(img.shape[0])
        for j in range(0, img.shape[0]):
            for i in range(0, img.shape[0]):
                coluna[i] = img[i][j]
            haar_vetor(coluna)
            for i in range(0, coluna.shape[0]):
                img[i][j] = coluna[i]

def haar_rgb(img, it):
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    
    haar(b,it)
    haar(g,it)
    haar(r,it)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i][j][0] = b[i][j]
                img[i][j][1] = g[i][j]
                img[i][j][2] = r[i][j]


def haar_inverse(img,it):
    coluna = np.zeros(img.shape[0])
    for h in range(it -1, -1, -1):
        for j in range(img.shape[0]):
            for i in range(img.shape[0]):
                coluna[i] = img[i][j]
            inverse(coluna)
            
            for i in range(img.shape[0]):
                img[i][j] = coluna[i]
        linha = np.zeros(img.shape[0])
        for i in range(img.shape[0]):
            for j in range(img.shape[0]):
                linha = img[i][j]
            inverse(linha)
            for j in range(img.shape[0]):
                img[i][j] = linha[j]

def inverse(data):
    w0 = 0.5
    w1 = -0.5
    s0 = 0.5
    s1 = 0.5

    temp = np.zeros(data.shape, dtype=np.float)

    h = data.shape[0] >> 1
    for i in range(h):
        k = i << 1
        b = (data[i] * s0 + (data[i + h] - 127) * w0) / w0
        if b < 0:
            b = 0

        temp[k] = b

        b = (data[i] * s1 + (data[i + h] - 127) * w1) / s0
        if b < 0:
            b = 0

        temp[k + 1] = b

    for i in range(data.shape[0]):
        data[i] = temp[i]
        
image = cv.imread("lena (1).bmp")
haar_rgb(image, 1)
cv.imwrite("teste.bmp", image)