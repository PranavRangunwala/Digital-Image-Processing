# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt

# Read the image using cv2
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg')

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

# Set the figure size to match the image dimensions
plt.figure(figsize=(width / 100, height / 100), dpi=100)

# Display the image using matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Hide axis
plt.show()
