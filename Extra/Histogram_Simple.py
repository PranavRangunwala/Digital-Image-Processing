# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:56:00 2024

@author: RANGUNWALA
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\2.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate histogram for the grayscale image
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot the histogram
plt.title("Grayscale Intensity Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Count")
plt.plot(histogram, color='black')  # Use black color for the grayscale histogram
plt.xlim([0, 256])  # Intensity values range from 0 to 255
plt.show()
