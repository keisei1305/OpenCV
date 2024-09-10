import cv2 as cv

img = cv.imread("imges/leopard.png")
cv.namedWindow("Display window", cv.WINDOW_FREERATIO)
cv.imshow("Display window", img)
cv.waitKey(0)
cv.destroyAllWindows()