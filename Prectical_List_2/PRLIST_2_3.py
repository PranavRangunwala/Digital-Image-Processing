# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:48:57 2024

@author: RANGUNWALA
"""

import cv2 as cv
import numpy as np

A = cv.imread(r"C:\Users\RANGUNWALA\Downloads\AAA.jpg")
B = cv.imread(r"C:\Users\RANGUNWALA\Downloads\BBB.jpg")

A_resized = cv.resize(A, (B.shape[1], B.shape[0]))

SUMM = cv.add(A_resized, B)
SUBB = cv.subtract(A_resized, B)
MULL = cv.multiply(A_resized, B,scale=1)
DIVV = cv.divide(A_resized, B,scale=1)

cv.imshow("Addition", SUMM)
cv.imshow("Subtraction", SUBB)
cv.imshow("Multiplication", MULL)
cv.imshow("Division", DIVV)

cv.waitKey(0)
cv.destroyAllWindows()