import cv2 as cv

img1 = cv.imread("sea.jpeg")
cv.imshow('Sea',img1)
cv.waitKey(2000)
cv.destroyAllWindows()

img2 = cv.imread("fish.jpeg")
cv.imshow('Fish',img2)
cv.waitKey(2000)
cv.destroyAllWindows()

img2 = cv.resize(img2, (3000,4000))

result = cv.addWeighted(img1, 0.3, img2, 0.7, 0)
cv.imwrite('result.jpeg', result)

cv.imshow('Result',result)
cv.waitKey(2000)
cv.destroyAllWindows()