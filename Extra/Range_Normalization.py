import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Picture2.png', cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_GRAYSCALE <= OPTIONAL

# Get the minimum and maximum pixel values from the image
a, b = np.min(image), np.max(image)

# Target range for normalization
c, d = 50, 210

# Apply the normalization formula
Normalized_Image = ((d-c)/(b-a)*(image-a)+c).astype(np.uint8)

# Clip the values to the range [0, 255] and convert to uint8
Normalized_Image = np.clip(Normalized_Image, 0, 255).astype(np.uint8)

# Display the normalized image
cv2.imshow("Before Image", image)
cv2.imshow("Normalized Image", Normalized_Image)

cv2.waitKey(0)
cv2.destroyAllWindows()
