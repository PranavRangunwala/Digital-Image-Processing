# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:51:20 2024

@author: RANGUNWALA
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Opening_2.jpg')

imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imggg = cv2.GaussianBlur(imgg,(3, 3), 0)

_, binary_image = cv2.threshold(imggg, 127, 255, cv2.THRESH_BINARY)

# Define the structuring element (SE)
structuring_element = np.array([
                   [0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], np.uint8)

# OR
structuring_element2 = np.ones((3, 3), np.uint8)  # 5x5 square SE


# Perform erosion on the binary image
eroded_image = cv2.erode(binary_image, structuring_element, iterations=5)
dileted_image = cv2.dilate(binary_image, structuring_element2, iterations=1)

internal_boundry = cv2.subtract(imggg,eroded_image)
external_boundry = cv2.subtract(dileted_image, imggg)

cv2.imshow("Internal Boundry", internal_boundry)
cv2.imshow("External Boundry", external_boundry)
cv2.waitKey(0)
cv2.destroyAllWindows()