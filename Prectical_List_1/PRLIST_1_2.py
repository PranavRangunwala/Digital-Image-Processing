# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:21:05 2024

@author: RANGUNWALA
"""

import cv2 as cv

image = cv.imread(r'C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg')
height,width = image.shape[0:2]
cv.imshow("IMAGE", image)
print("Height = ",height)
print("Width = ",width)
cv.waitKey(0)

