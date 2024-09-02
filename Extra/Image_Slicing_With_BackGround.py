# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:40:05 2024

@author: RANGUNWALA
"""

import cv2
import numpy as np

def intensity_slicing(image, t1, t2, L=256):
    # Create a copy of the image to avoid modifying the original
    output_image = image.copy()
    
    # Define the new intensity value for the specified range
    max_intensity = L - 1
    
    # Apply the intensity slicing transformation
    # Set pixel values to max_intensity if they are within the range [t1, t2]
    output_image[(image >= t1) & (image <= t2)] = max_intensity
    
    return output_image

# Load an input image in grayscale
input_image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\11zon_cropped.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the intensity range t1 and t2
t1 = 140  # example lower bound of intensity
t2 = 255  # example upper bound of intensity

# Apply the intensity slicing transformation
output_image = intensity_slicing(input_image, t1, t2)

# Save and display the result
cv2.imwrite('output_image.jpg', output_image)
cv2.imshow('Intensity Sliced Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

