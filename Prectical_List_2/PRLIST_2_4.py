import cv2 as cv

image1 = cv.imread(r"C:\Users\RANGUNWALA\Downloads\IMGG1.jpeg")
image2 = cv.imread(r"C:\Users\RANGUNWALA\Downloads\IMGG2.jpeg")
a = 0.4
image2_resized = cv.resize(image2, (image1.shape[1], image1.shape[0]))
BLEND_IMAGE = cv.addWeighted(image1, a, image2_resized, 1 - a,0) #for blending

cv.imshow("Blend Image", BLEND_IMAGE)
cv.waitKey(0)
cv.destroyAllWindows()
