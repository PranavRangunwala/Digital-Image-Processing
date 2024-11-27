# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 05:39:53 2024

@author: RANGUNWALA
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\blur.jpg')
gimage = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\gblur.jpg')

# Apply a 5x5 averaging filter
blurred_image = cv2.blur(image, (5, 5))
#cv2.blur(src, ksize)

# Apply a Gaussian filter with a 5x5 kernel
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
#cv2.GaussianBlur(src, ksize, sigmaX)

# Apply a Median filter with a 5x5 kernel
median_blur = cv2.medianBlur(gimage, 5)
#cv2.medianBlur(src, ksize)

# Define a sharpening kernel
sharpening_kernel = np.array([[-1, -1, -1], 
                              [-1, 9, -1], 
                              [-1, -1, -1]])

# Apply the sharpening filter
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
#cv2.filter2D(src, ddepth, kernel)

# Display the original and blurred images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Blurred Image (5x5)')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.show()

# Display the Gaussian blurred image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Gaussian Blurred Image')
plt.imshow(cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))
plt.show()

# Display the median blurred image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(gimage, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Median Blurred Image')
plt.imshow(cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB))
plt.show()

# Display the sharpened image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Sharpened Image')
plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.show()
