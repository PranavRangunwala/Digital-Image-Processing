import cv2
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import NoNorm

# Read an image 
image = cv2.imread( r'C:\Users\RANGUNWALA\Downloads\2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Apply log transformation method 
c = 255 / np.log(1 + np.max(image)) # c = 255 / np.log(1 + 255)
log_image = c * (np.log(image + 1)) 

# Specify the data type so that 
# float value will be converted to int 
log_image = np.array(log_image,dtype="uint8")

# Display both images 
plt.imshow(image)
plt.show()
plt.imshow(log_image)
plt.show() 

