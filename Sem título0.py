#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:51:23 2018

@author: talles
"""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from math import log, ceil
from matplotlib.colors import LogNorm
from cmath import exp, pi

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + \
           [even[k] - T[k] for k in range(N//2)]

def fft2(f):
    return np.transpose(fft(np.transpose(fft(f))))

def ifft2(fourier, row, column):
    f = fft2(np.conj(fourier))
    f = np.matrix(np.real(np.conj(f)))/(row*column)
    return f

def plot_spec(im_fft):
    plt.imshow(np.abs(np.fft.fftshift(im_fft)), norm=LogNorm(vmin=5), cmap=plt.cm.gray)

def fourier_filter(im_fft, col1, col2):
    im_fft = np.fft.fftshift(im_fft)
    middle = im_fft.shape[0]/2
    for i in range(im_fft.shape[0]):
        for j in range(col1, col2):
            im_fft[i][col1] = im_fft[i][col1] - im_fft[i][col1]
    plt.imshow(np.abs((im_fft)), norm=LogNorm(vmin=5), cmap=plt.cm.gray)

    return np.fft.ifftshift(im_fft)

img = cv.imread('palhaco.jpg',0)
fourier = fft2(img)
#plot_spec(fourier)
fourier = fourier_filter(fourier,120, 138)
i_fourier = ifft2(fourier, img.shape[0], img.shape[0])
cv.imwrite('window.bmp', i_fourier)

