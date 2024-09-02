# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:12:59 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg")

Averagee = np.mean(image)

print("Averge Is : ",Averagee)
