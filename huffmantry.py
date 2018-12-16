#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:26:14 2018

@author: talles
"""
import heapq
import cv2 as cv
import numpy as np
#node: [value, childL, childR]
def haar_vetor(dado):
    z=0
    temp = np.zeros(dado.shape[0], dtype=np.float)
    for i in range(0,dado.shape[0],2):
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

def printTree(tree, depth=0):
    value = tree[0]
    child0 = tree[1] if (len(tree)>=2) else None
    child1 = tree[2] if (len(tree)>=3) else None
    print('   '*depth, value)
    if(child0 != None): printTree(child0, depth+1)
    if(child1 != None):printTree(child1, depth+1)

def makeTree(letterFrequencies):
    heap = []
    for lf in letterFrequencies: heapq.heappush(heap, [lf])
    while (len(heap) > 1):
        child0 = heapq.heappop(heap)
        child1 = heapq.heappop(heap)
        freq0, label0 = child0[0]
        freq1, label1 = child1[0]
        freq = freq0 + freq1
        label = ''.join(sorted(label0 + label1))
        node = [(freq, label), child0, child1]
        heapq.heappush(heap, node)
    return heap.pop()

def testMakeTree():
    print('Testing makeTree()', end='')
    tree= makeTree([(45,'a'), (13, 'b'), (12,'c'), (16, 'd'), (9, 'e'), (5, 'f')])
    assert(tree == [(100, 'abcdef'),
                        [(45,'a')],
                        [(55,'bcdef'),
                         [(25, 'bc'),
                              [(12,'c')],
                              [(13,'b')]],
                          [(30, 'def'),
                               [(14,'ef'),
                                    [(5, 'f')],
                                    [(9, 'e')]],
                                [(16,'d')]]]])
    print('Passed!')

def walkTree(codeTree, codeMap, codePrefix):
    if(len(codeTree) == 1):
        frequency, label = codeTree[0]
        codeMap[label] = codePrefix
    else:
        value, child0, child1 = codeTree
        walkTree(child0, codeMap, codePrefix + '0')
        walkTree(child1, codeMap, codePrefix + '1')
def makeCodeMap(codeTree):
    codeMap = dict()
    walkTree(codeTree, codeMap, '')
    return codeMap
def testMakeCodeMap():
    print('Testing makeCodeMap()', end='')
    tree= makeTree([(45,'a'), (13, 'b'), (12,'c'), (16, 'd'), (9, 'e'), (5, 'f')])
    codeMap = makeCodeMap(tree)
    assert(codeMap == { 'a' : '0',
                        'b' : '101',
                        'c' : '100',
                        'd' : '111',
                        'e' : '1101',
                        'f' : '1100'
                        })
    print('Passed')
def encode(message, frequencies):
    codeMap = makeCodeMap(makeTree(frequencies))
    return ''.join([ codeMap[letter] for letter in message])

def testEncode():
    print('Testing encode()', end='')
    frequencies = [(0, '\x00'), (1, '\x01'), (2, '\x02'), (3, '\x03'), (4, '\x04'), (5, '\x05'), (6, '\x06'), (7, '\x07'), (8, '\x08'), (9, '\t'), (10, '\n'), (11, '\x0b'), (12, '\x0c'), (13, '\r'), (14, '\x0e'), (15, '\x0f'), (16, '\x10'), (17, '\x11'), (18, '\x12'), (19, '\x13'), (20, '\x14'), (21, '\x15'), (22, '\x16'), (23, '\x17'), (24, '\x18'), (25, '\x19'), (26, '\x1a'), (27, '\x1b'), (28, '\x1c'), (29, '\x1d'), (30, '\x1e'), (31, '\x1f'), (32, ' '), (33, '!'), (34, '"'), (35, '#'), (36, '$'), (37, '%'), (38, '&'), (39, "'"), (40, '('), (41, ')'), (42, '*'), (43, '+'), (44, ','), (45, '-'), (46, '.'), (47, '/'), (48, '0'), (49, '1'), (51, '2'), (51, '3'), (52, '4'), (53, '5'), (54, '6'), (56, '7'), (56, '8'), (57, '9'), (58, ':'), (60, ';'), (60, '<'), (61, '='), (62, '>'), (63, '?'), (64, '@'), (65, 'A'), (66, 'B'), (67, 'C'), (68, 'D'), (69, 'E'), (70, 'F'), (73, 'G'), (72, 'H'), (73, 'I'), (74, 'J'), (75, 'K'), (76, 'L'), (78, 'M'), (78, 'N'), (79, 'O'), (80, 'P'), (81, 'Q'), (82, 'R'), (83, 'S'), (84, 'T'), (85, 'U'), (86, 'V'), (87, 'W'), (88, 'X'), (89, 'Y'), (92, 'Z'), (91, '['), (92, '\\'), (93, ']'), (94, '^'), (95, '_'), (97, '`'), (97, 'a'), (98, 'b'), (99, 'c'), (100, 'd'), (101, 'e'), (102, 'f'), (103, 'g'), (104, 'h'), (105, 'i'), (107, 'j'), (107, 'k'), (108, 'l'), (109, 'm'), (111, 'n'), (113, 'o'), (112, 'p'), (113, 'q'), (114, 'r'), (117, 's'), (117, 't'), (119, 'u'), (122, 'v'), (124, 'w'), (131, 'x'), (145, 'y'), (150, 'z'), (170, '{'), (459, '|'), (4326, '}'), (250755, '~'), (530118, '\x7f'), (942, '\x80'), (290, '\x81'), (178, '\x82'), (164, '\x83'), (158, '\x84'), (147, '\x85'), (142, '\x86'), (142, '\x87'), (141, '\x88'), (138, '\x89'), (142, '\x8a'), (142, '\x8b'), (143, '\x8c'), (143, '\x8d'), (143, '\x8e'), (145, '\x8f'), (146, '\x90'), (145, '\x91'), (147, '\x92'), (147, '\x93'), (149, '\x94'), (149, '\x95'), (151, '\x96'), (152, '\x97'), (152, '\x98'), (153, '\x99'), (154, '\x9a'), (155, '\x9b'), (156, '\x9c'), (157, '\x9d'), (159, '\x9e'), (159, '\x9f'), (160, '\xa0'), (161, '¡'), (162, '¢'), (163, '£'), (164, '¤'), (165, '¥'), (166, '¦'), (167, '§'), (168, '¨'), (169, '©'), (170, 'ª'), (171, '«'), (172, '¬'), (173, '\xad'), (174, '®'), (175, '¯'), (176, '°'), (177, '±'), (178, '²'), (179, '³'), (180, '´'), (181, 'µ'), (182, '¶'), (183, '·'), (184, '¸'), (185, '¹'), (186, 'º'), (187, '»'), (188, '¼'), (189, '½'), (190, '¾'), (191, '¿'), (192, 'À'), (193, 'Á'), (194, 'Â'), (195, 'Ã'), (196, 'Ä'), (197, 'Å'), (198, 'Æ'), (199, 'Ç'), (200, 'È'), (201, 'É'), (202, 'Ê'), (203, 'Ë'), (204, 'Ì'), (205, 'Í'), (206, 'Î'), (207, 'Ï'), (208, 'Ð'), (209, 'Ñ'), (210, 'Ò'), (211, 'Ó'), (212, 'Ô'), (213, 'Õ'), (214, 'Ö'), (215, '×'), (216, 'Ø'), (217, 'Ù'), (218, 'Ú'), (219, 'Û'), (220, 'Ü'), (221, 'Ý'), (222, 'Þ'), (223, 'ß'), (224, 'à'), (225, 'á'), (226, 'â'), (227, 'ã'), (228, 'ä'), (229, 'å'), (230, 'æ'), (231, 'ç'), (232, 'è'), (233, 'é'), (234, 'ê'), (235, 'ë'), (236, 'ì'), (237, 'í'), (238, 'î'), (239, 'ï'), (240, 'ð'), (241, 'ñ'), (242, 'ò'), (243, 'ó'), (244, 'ô'), (245, 'õ'), (246, 'ö'), (247, '÷'), (248, 'ø'), (249, 'ù'), (250, 'ú'), (251, 'û'), (252, 'ü'), (253, 'ý'), (254, 'þ'), (255, 'ÿ')]
    message = 'abacdaebfa'
    encoded = encode(message, frequencies)
    assert(encoded == '010101001110110110111000')
    print("Passed!!")
    
def decode(encodedMessage, frequencies):
    codeTree = entireTree = makeTree(frequencies)
    decodedLetters = []
    for digit in encodedMessage:
        if(digit == '0'): codeTree = codeTree[1]
        else: codeTree = codeTree[2]
        if (len(codeTree) == 1):
            frequency, label = codeTree[0]
            decodedLetters.append(label)
            codeTree = entireTree
    return ''.join(decodedLetters)
def testDecode(vetor):
    print('Testing decode()', end='')
    frequencies = [(0, '\x00'), (1, '\x01'), (2, '\x02'), (3, '\x03'), (4, '\x04'), (5, '\x05'), (6, '\x06'), (7, '\x07'), (8, '\x08'), (9, '\t'), (10, '\n'), (11, '\x0b'), (12, '\x0c'), (13, '\r'), (14, '\x0e'), (15, '\x0f'), (16, '\x10'), (17, '\x11'), (18, '\x12'), (19, '\x13'), (20, '\x14'), (21, '\x15'), (22, '\x16'), (23, '\x17'), (24, '\x18'), (25, '\x19'), (26, '\x1a'), (27, '\x1b'), (28, '\x1c'), (29, '\x1d'), (30, '\x1e'), (31, '\x1f'), (32, ' '), (33, '!'), (34, '"'), (35, '#'), (36, '$'), (37, '%'), (38, '&'), (39, "'"), (40, '('), (41, ')'), (42, '*'), (43, '+'), (44, ','), (45, '-'), (46, '.'), (47, '/'), (48, '0'), (49, '1'), (51, '2'), (51, '3'), (52, '4'), (53, '5'), (54, '6'), (56, '7'), (56, '8'), (57, '9'), (58, ':'), (60, ';'), (60, '<'), (61, '='), (62, '>'), (63, '?'), (64, '@'), (65, 'A'), (66, 'B'), (67, 'C'), (68, 'D'), (69, 'E'), (70, 'F'), (73, 'G'), (72, 'H'), (73, 'I'), (74, 'J'), (75, 'K'), (76, 'L'), (78, 'M'), (78, 'N'), (79, 'O'), (80, 'P'), (81, 'Q'), (82, 'R'), (83, 'S'), (84, 'T'), (85, 'U'), (86, 'V'), (87, 'W'), (88, 'X'), (89, 'Y'), (92, 'Z'), (91, '['), (92, '\\'), (93, ']'), (94, '^'), (95, '_'), (97, '`'), (97, 'a'), (98, 'b'), (99, 'c'), (100, 'd'), (101, 'e'), (102, 'f'), (103, 'g'), (104, 'h'), (105, 'i'), (107, 'j'), (107, 'k'), (108, 'l'), (109, 'm'), (111, 'n'), (113, 'o'), (112, 'p'), (113, 'q'), (114, 'r'), (117, 's'), (117, 't'), (119, 'u'), (122, 'v'), (124, 'w'), (131, 'x'), (145, 'y'), (150, 'z'), (170, '{'), (459, '|'), (4326, '}'), (250755, '~'), (530118, '\x7f'), (942, '\x80'), (290, '\x81'), (178, '\x82'), (164, '\x83'), (158, '\x84'), (147, '\x85'), (142, '\x86'), (142, '\x87'), (141, '\x88'), (138, '\x89'), (142, '\x8a'), (142, '\x8b'), (143, '\x8c'), (143, '\x8d'), (143, '\x8e'), (145, '\x8f'), (146, '\x90'), (145, '\x91'), (147, '\x92'), (147, '\x93'), (149, '\x94'), (149, '\x95'), (151, '\x96'), (152, '\x97'), (152, '\x98'), (153, '\x99'), (154, '\x9a'), (155, '\x9b'), (156, '\x9c'), (157, '\x9d'), (159, '\x9e'), (159, '\x9f'), (160, '\xa0'), (161, '¡'), (162, '¢'), (163, '£'), (164, '¤'), (165, '¥'), (166, '¦'), (167, '§'), (168, '¨'), (169, '©'), (170, 'ª'), (171, '«'), (172, '¬'), (173, '\xad'), (174, '®'), (175, '¯'), (176, '°'), (177, '±'), (178, '²'), (179, '³'), (180, '´'), (181, 'µ'), (182, '¶'), (183, '·'), (184, '¸'), (185, '¹'), (186, 'º'), (187, '»'), (188, '¼'), (189, '½'), (190, '¾'), (191, '¿'), (192, 'À'), (193, 'Á'), (194, 'Â'), (195, 'Ã'), (196, 'Ä'), (197, 'Å'), (198, 'Æ'), (199, 'Ç'), (200, 'È'), (201, 'É'), (202, 'Ê'), (203, 'Ë'), (204, 'Ì'), (205, 'Í'), (206, 'Î'), (207, 'Ï'), (208, 'Ð'), (209, 'Ñ'), (210, 'Ò'), (211, 'Ó'), (212, 'Ô'), (213, 'Õ'), (214, 'Ö'), (215, '×'), (216, 'Ø'), (217, 'Ù'), (218, 'Ú'), (219, 'Û'), (220, 'Ü'), (221, 'Ý'), (222, 'Þ'), (223, 'ß'), (224, 'à'), (225, 'á'), (226, 'â'), (227, 'ã'), (228, 'ä'), (229, 'å'), (230, 'æ'), (231, 'ç'), (232, 'è'), (233, 'é'), (234, 'ê'), (235, 'ë'), (236, 'ì'), (237, 'í'), (238, 'î'), (239, 'ï'), (240, 'ð'), (241, 'ñ'), (242, 'ò'), (243, 'ó'), (244, 'ô'), (245, 'õ'), (246, 'ö'), (247, '÷'), (248, 'ø'), (249, 'ù'), (250, 'ú'), (251, 'û'), (252, 'ü'), (253, 'ý'), (254, 'þ'), (255, 'ÿ')]
    encoded = '010101001110110110111000'
    decoded = decode(encoded, frequencies)
    assert(decoded == 'abacdaebfa')
    print("Passed!")



img = cv.imread("lena.bmp")
img_vetor = [] #aqui vai ser a string com todas a intensidades de pixels da imagem
histograma = np.arange(256, dtype=int) #histograma de 0 a 255 pra guardar as intensidades
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]): #lendo cada pixel na imagem
            subpixel = img[i][j][k] #cada subpixel
            histograma[subpixel] += 1 #determina a frequencia de cada subpixel somando 1 no histograma
            img_vetor.append(chr(subpixel)) #concatena a intensidade do subpixel
    freq = []
    for i in range(256):
        freq.append((histograma[i], chr(i))) #cria tuplas com a frequencia e a intensidade ex: [(33,'0'), (23,'1')] 
img_vetor = ''.join(img_vetor)
#ATE aqui ta certo


encoded = encode(img_vetor, freq)
b = encoded
array = bytearray(int(b[x:x+8], 2) for x in range(0, len(b), 8))
with open('binass', 'wb') as f:
    f.write(array)
    f.close()
with open('binass', 'rb') as f:
    file = f.read()
imageUnpack = np.unpackbits(bytearray(file))

imageFile = ' '.join(str(x) for x in imageUnpack)
image = decode(encoded, freq)


img_vetor = list(img_vetor)
h=0
print(img[0][0][2])
print(ord(img_vetor[2]))
for i in range(img.shape[0]):
    for j in range(0,img.shape[1]):
        for k in range(img.shape[2]): #lendo cada pixel na imagem
            img[i][j][k] = ord(img_vetor[h]) #cada subpixel
            h += 1
cv.imwrite('decompress.bmp', img)



