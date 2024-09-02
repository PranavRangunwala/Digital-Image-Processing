# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:41:37 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg");

min_value = np.min(image)
max_value = np.max(image)

print("Smallest Pixel = ",min_value)
print("Largest Pixel = ",max_value)

cv.imshow("IMAGEE",image)
cv.waitKey(0)
cv.destroyAllWindows()