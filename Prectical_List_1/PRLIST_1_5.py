# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:57:53 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

image = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg");
new_width = 540
new_height = 960
Resized_Image = cv.resize(image, (new_height,new_width))

#Getting Image Dimentions of Original and resized Image
height,width,_ = image.shape;
height1,width1,_1 = Resized_Image.shape;
cv.imshow('Original Image', image)
#Old Image Dimentions
print("Height = ",height)
print("Width = ",width)
print()
#New Image Dimentions
print("New Height = ",height1)
print("New Width = ",width1)
cv.imshow('Resized Image', Resized_Image)

#PRECTICAL LIST 1 - 6th

cv.imwrite(r"C:\Users\RANGUNWALA\Downloads\Resized_Image.jpg", Resized_Image)
print("Resized image saved successfully")

cv.waitKey(0)
cv.destroyAllWindows()