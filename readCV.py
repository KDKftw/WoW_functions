import cv2 as cv

img = cv.imread(r"C:\Users\KDK\Desktop\wow_scs.jpg")

print(img)
cv.imshow("Scs", img)

cv.waitKey(0)