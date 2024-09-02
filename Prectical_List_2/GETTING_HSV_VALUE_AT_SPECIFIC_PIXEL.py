import cv2
import numpy as np

# Function to get HSV values from a clicked pixel
def get_hsv_values(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsv[y, x]
        print('HSV values at (',x,', ',y,'): H=',pixel[0],'S=',pixel[1],', V=',pixel[2])

# Load the image
img = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Bumble_Bee.jpg')

# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a window and set a mouse callback to get HSV values
cv2.imshow('HSV Image', hsv)
cv2.setMouseCallback('HSV Image', get_hsv_values)

cv2.waitKey(0)
cv2.destroyAllWindows()
