# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 22:51:45 2018

@author: Talles
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 00:49:11 2018

@author: Talles
"""

import cv2 as cv
import numpy as np

    
image = cv.imread("Fig0305(a)(DFT_no_log).tif",0)
print(np.max(image))
c = (255/np.log(np.max(image)))
for i in range (0, image.shape[0]):
    for j in range (0, image.shape[1]):
            pixel = c*np.log(1+image[i][j])
            image[i][j] = pixel
cv.imwrite("invertedlogaritmo.png",image)