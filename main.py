import cv2 as cv

def showImage(path):
    img = cv.imread(path, cv.COLOR_BGR2GRAY)
    cv.namedWindow("Display window", cv.WINDOW_KEEPRATIO)
    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def showMp4(path):
    cap = cv.VideoCapture(path, cv.CAP_ANY)
    while True:
        ret, frame = cap.read()
        if not(ret):
            break
        cv.imshow('frame', frame)
        if (cv.waitKey(1)&0xFF == 27):
            break

showMp4(0)