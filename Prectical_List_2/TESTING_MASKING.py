import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Bumble_Bee.jpg')

# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range for the specific color (replace with your values)
lower_bound = np.array([15, 100, 139])
upper_bound = np.array([25, 255, 255])

# Create the mask
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img, img, mask=mask)

# Display the original image, mask, and masked image
cv2.imshow('Original Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
