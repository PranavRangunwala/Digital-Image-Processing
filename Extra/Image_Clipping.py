# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:20:37 2024

@author: RANGUNWALA
"""

import cv2
import numpy as np

def clip_and_scale_image(image, t0, t1):
    # Find the minimum and maximum intensity values in the image
    a = np.min(image)
    b = np.max(image)
    
    # Define new intensity range (0-255)
    c, d = t0, t1

    # Apply the formula to scale the intensity values
    s = ((d - c) / (b - a) * (image - a) + c).astype(np.uint8)

    # Clip the values to be within 0-255 range
    s_clipped = np.clip(s, 0, 255)
    
    # Convert back to uint8
    output_image = s_clipped.astype(np.uint8)
    
    return output_image

# Load an input image in grayscale
input_image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Picture2.png')

# Clip and scale the image using the minimum and maximum intensity values
output_image = clip_and_scale_image(input_image,0,255)

# Save and display the result
cv2.imwrite('output_image.jpg', output_image)
cv2.imshow('Clipped and Scaled Image update', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
