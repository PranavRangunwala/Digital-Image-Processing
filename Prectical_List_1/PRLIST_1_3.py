# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:26:56 2024

@author: RANGUNWALA
"""

import cv2 as cv

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg");

image[100:500,100:300] = (0,0,0)

cv.imshow("IMAGEE",image)
cv.waitKey(0)
cv.destroyAllWindows()