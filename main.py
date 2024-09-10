import cv2 as cv

def showImage(path):
    img = cv.imread(path, cv.COLOR_BGR2GRAY)
    cv.namedWindow("Display window", cv.WINDOW_KEEPRATIO)
    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def showVideo(path):
    cap = cv.VideoCapture(path, cv.CAP_ANY)
    while True:
        ret, frame = cap.read()
        if not(ret):
            break
        cv.imshow('frame', frame)
        if (cv.waitKey(1)&0xFF == 27):
            break
    cap.release()
    cv.destroyAllWindows()

def writeVideo(path_from, path_to):
    cap = cv.VideoCapture(path_from, cv.CAP_ANY)
    ret, frame = cap.read()
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter.fourcc(*"XVID")
    video_writer = cv.VideoWriter(path_to, fourcc, 25, (w, h))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow('frame', frame)
        video_writer.write(frame)

        if cv.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()