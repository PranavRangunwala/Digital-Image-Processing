# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:48:57 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg")
before_brightness = np.mean(image)

brightened_image = cv.subtract(image, 50)
after_brightness = np.mean(brightened_image)

print("Before Adding Scaler Value : ",before_brightness)
print("After Adding Scaler Value : ",after_brightness)

cv.imshow("Before", image)
cv.imshow("After", brightened_image)
cv.waitKey(0)
cv.destroyAllWindows()