import cv2
import numpy as np

# Load the image (grayscale)
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Picture2.png', cv2.IMREAD_GRAYSCALE)

# Find the minimum and maximum pixel intensity values in the image
minI = np.min(image)
maxI = np.max(image)

# Perform contrast stretching
stretched = ((image - minI) / (maxI - minI) * 255).astype(np.uint8)

# Save or display the result
cv2.imshow('input Image', image)
cv2.imshow('Stretched Image', stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()
