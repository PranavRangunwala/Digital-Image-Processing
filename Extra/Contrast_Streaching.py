import cv2
import numpy as np

# Load the image (grayscale)
image = cv2.imread(r'C:\Users\RANGUNWALA\Downloads\Picture2.png', cv2.IMREAD_GRAYSCALE)

# Define the range for contrast stretching
r1, c1 = 90, 40
r2, c2 = 160, 200

# Define the contrast stretching function
def contrast_stretch(image, r1, c1, r2, c2):
    stretched_image = np.zeros_like(image)

    # Apply the first stretching
    mask1 = (image <= r1)
    stretched_image[mask1] = ((c1 - 0) / (r1 - 0)) * image[mask1] + 0

    # Apply the second stretching
    mask2 = (image > r1) & (image <= r2)
    stretched_image[mask2] = ((c2 - c1) / (r2 - r1)) * (image[mask2] - r1) + c1

    # Apply the third stretching
    mask3 = (image > r2)
    stretched_image[mask3] = ((255 - c2) / (255 - r2)) * (image[mask3] - r2) + c2

    return stretched_image

# Perform contrast stretching
stretched_image = contrast_stretch(image, r1, c1, r2, c2)

# Show the result
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
