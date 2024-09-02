# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:37:43 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Calculate the standard deviation of pixel intensities
contrast = np.std(gray_image)

# Print the contrast value
print(f"Contrast of the image: {contrast}")

# Display the original image
cv.imshow('Original Image', image)
cv.waitKey(0)
cv.destroyAllWindows()