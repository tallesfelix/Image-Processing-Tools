#metodo novo para plotação do gráfico
#convolução
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy as signal

def convol2d(img, k):
        # Esta função que leva uma imagem e um kernel 
    # e retorna a convolução deles
    # Args:
    # image: um array numpy de tamanho [image_height, image_width].
    # k: uma matriz numérica de tamanho [kernel_height, kernel_width].
    # Retorna:
    # uma matriz numérica de tamanho [image_height, image_width] (saída de convolução).
    k = np.flipud(np.fliplr(k))# Virar o kernel
    saida = np.zeros_like(img) # saída de convolução
    # Adicionar zero preenchimento à imagem de entrada
    img_padded = np.zeros((img.shape[0] + 2, img.shape[1] + 2), dtype=np.int)   
    img_padded[1:-1, 1:-1] = img
    for x in range(1,img.shape[1]-1):     #Loop sobre cada pixel da imagem 
        for y in range(1,img.shape[0]-1):
            # multiplicação elemental do kernel e da imagem
            saida[y,x]=(k*img_padded[y:y+3,x:x+3]).sum()
    return saida

def cmatri(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            v = int(input("Digite o elemento [" + str(i) + "][" + str(j) +"]"))
            linha.append(v)
        matriz.append(linha)
    return matriz
def lmatri():
    lin = int(input("Insira o número de linhas: "))
    col = int(input("Insira o número de colunas: "))
    return cmatri(lin, col)

img = cv.imread('Fig0417(a)(barbara).tif', 0)# Carrega a imagem   
cv.imshow('imagem original', img)
# Convolve o kernel de nitidez e a imagem
k = np.array([lmatri()])
imgc = convol2d(img, k)

cv.imsave('com filtro', imgc)
