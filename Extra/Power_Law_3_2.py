import cv2
import numpy as np

# Read an image 
img = cv2.imread(r'C:\Users\RANGUNWALA\Pictures\Picture1.png')  
#img = cv2.imread( r'C:\Users\RANGUNWALA\Downloads\graylevel6.jpg') 

# Convert the image to float for gamma correction
img_float = img.astype(np.float32) / 255

# Trying 4 gamma values. 
for gamma in [0.1, 0.4, 1.2, 2.2]:
    # Apply gamma correction
    gamma_corrected = np.array(255 * (img_float ** gamma), dtype='uint8')
        
    # Display the gamma-corrected image
    cv2.imshow(f'Gamma {gamma}', gamma_corrected)

    # Wait for a key press
    cv2.waitKey(0)  # Wait indefinitely for a key press

# Destroy all windows after exiting the loop
cv2.destroyAllWindows()