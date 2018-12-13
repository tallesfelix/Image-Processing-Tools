#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:50:27 2018

@author: talles
"""

import numpy as np
import cv2 as cv
import math as math

def filtroContraHarmonica(img, q):
    s = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    listaDenominador = np.zeros((9,), dtype=int)
    listaDivisor = np.zeros((9,), dtype=int)
    for i in range(1,img.shape[0]-1):     #Loop sobre cada pixel da imagem 
        for j in range(1,img.shape[1]-1):
            lista = [img.item(i-1,j-1)**(q+1), img.item(i-1,j)**(q+1), img.item(i-1,j+1)**(q+1),img.item(i,j-1)**(q+1), img.item(i, j)**(q+1), img.item(i, j+1)**(q+1), img.item(i+1, j-1)**(q+1), img.item(i+1, j)**(q+1), img.item(i+1, j+1)**(q+1)] 
            lista2 = [img.item(i-1,j-1)**(q), img.item(i-1,j)**(q), img.item(i-1,j+1)**(q),img.item(i,j-1)**(q), img.item(i, j)**(q), img.item(i, j+1)**(q), img.item(i+1, j-1)**(q), img.item(i+1, j)**(q), img.item(i+1, j+1)**(q)]
            sumDenominador = np.sum(lista)
            sumDivisor = np.sum(lista2)
            valor = sumDenominador / sumDivisor
            s[i][j] = valor 
    return s

def Conv(img, c, q):
    vetor = np.zeros((img.shape[0], img.shape[1]), dtype=np.int)
    if (q < 0):
        k = -q
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            if( q >= 0 ):
                sumDenominador = (img.item(i-1, j-1)*c[0][0])**(q+1) + (img.item(i-1, j)*c[0][1])**(q+1) + (img.item(i-1, j+1)*c[0][2])**(q+1) + (img.item(i,j-1)*c[1][0])**(q+1) + (img.item(i, j)*c[1][1])**(q+1) + (img.item(i,j+1)*c[1][2])**(q+1) + (img.item(i+1,j-1)*c[2][0])**(q+1) + (img.item(i+1,j)*c[2][1])**(q+1) + (img.item(i+1, j+1)+c[2][2])**(q+1)
                sumDivisor = ((img.item(i-1, j-1)*c[0][0])**(q)) + ((img.item(i-1, j)*c[0][1])**(q)) + ((img.item(i-1, j+1)*c[0][2])**(q)) + ((img.item(i,j-1)*c[1][0])**(q)) + ((img.item(i, j)*c[1][1])**(q)) + ((img.item(i,j+1)*c[1][2])**(q)) + ((img.item(i+1,j-1)*c[2][0])**(q)) + ((img.item(i+1,j)*c[2][1])**(q)) + ((img.item(i+1, j+1)+c[2][2])**(q))
            if( q < 0 ):
                sumDenominador = (img.item(i-1, j-1)*c[0][0])**(k+1) + (img.item(i-1, j)*c[0][1])**(k+1) + (img.item(i-1, j+1)*c[0][2])**(k+1) + (img.item(i,j-1)*c[1][0])**(k+1) + (img.item(i, j)*c[1][1])**(k+1) + (img.item(i,j+1)*c[1][2])**(k+1) + (img.item(i+1,j-1)*c[2][0])**(k+1) + (img.item(i+1,j)*c[2][1])**(k+1) + (img.item(i+1, j+1)+c[2][2])**(k+1)
                sumDivisor = ((img.item(i-1, j-1)*c[0][0])**(k)) + ((img.item(i-1, j)*c[0][1])**(k)) + ((img.item(i-1, j+1)*c[0][2])**(k)) + ((img.item(i,j-1)*c[1][0])**(k)) + ((img.item(i, j)*c[1][1])**(k)) + ((img.item(i,j+1)*c[1][2])**(k)) + ((img.item(i+1,j-1)*c[2][0])**(k)) + ((img.item(i+1,j)*c[2][1])**(k)) + ((img.item(i+1, j+1)+c[2][2])**(k))           
                sumDenominador = 1 / sumDenominador
                sumDivisor = 1 / sumDivisor
            sum = int(sumDenominador / sumDivisor)
            if sum > 255:
                sum =255
            if sum <= 0 :
                sum = 0
            vetor.itemset((i,j), sum)
    return vetor

img = cv.imread("Fig0508(a)(circuit-board-pepper-prob-pt1).tif", 0)
Kernel = np.array(([1,1,1],[1,1,1],[1,1,1]), dtype="int")
q = 1
cv.imwrite("contraHamornica2.png", Conv(img, Kernel, q))
