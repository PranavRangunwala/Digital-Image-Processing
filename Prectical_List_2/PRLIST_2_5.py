import cv2 as cv

# Load images
A = cv.imread(r"C:\Users\RANGUNWALA\Downloads\AAA.jpg")
B = cv.imread(r"C:\Users\RANGUNWALA\Downloads\BBB.jpg")

A_resized = cv.resize(A, (B.shape[1], B.shape[0]))

AND = cv.bitwise_and(A_resized, B)
OR = cv.bitwise_or(A_resized, B)
XOR = cv.bitwise_xor(A_resized, B)
NOT_A = cv.bitwise_not(A_resized)
NOT_B = cv.bitwise_not(B)

cv.imshow("AND", AND)
cv.imshow("OR", OR)
cv.imshow("XOR", XOR)
cv.imshow("NOT A", NOT_A)
cv.imshow("NOT B", NOT_B)

cv.waitKey(0)
cv.destroyAllWindows()
