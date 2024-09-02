# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:16:21 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

imagee = cv.imread(r"C:\Users\RANGUNWALA\Downloads\Screenshot 2024-06-08 190631.jpg")
image = cv.cvtColor(imagee, cv.COLOR_BGR2GRAY)
Avgg = np.mean(image)

Below_Avg = np.sum(image < Avgg)
Above_Avg = np.sum(image > Avgg)

Total_Number_Of_Pixels = image.shape[0] * image.shape[1]

print("Average : ",Avgg)
print("Below Average Pixel Total: ",Below_Avg)
print("Above Average Pixel Total: ",Above_Avg)
print("Total Number Of Pixels: ",Total_Number_Of_Pixels)

print("Below Average Pixels Percentage Is : ",(Below_Avg*100)/Total_Number_Of_Pixels)
print("Above Average Pixels Percentage Is : ",(Above_Avg*100)/Total_Number_Of_Pixels)