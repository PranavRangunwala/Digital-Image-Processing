# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:22:36 2024

@author: RANGUNWALA
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image in grayscale
img = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Picture8.png', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equ = cv2.equalizeHist(img)

# Stack images side-by-side
res = np.hstack((img, equ))

# Display the original and equalized images
cv2.imshow('Image Comparison', res)

# Compute histograms
hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(12, 6))

# Original image histogram
plt.subplot(1, 2, 1)
plt.plot(hist_img, color='black')
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Equalized image histogram
plt.subplot(1, 2, 2)
plt.plot(hist_equ, color='black')
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
