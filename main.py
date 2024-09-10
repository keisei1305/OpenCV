import cv2 as cv

def showImage(path, image_color, window_method):
    img = cv.imread(path, image_color)
    cv.namedWindow("Display window", window_method)
    cv.imshow("Display window", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def showVideo(path, color_converter, window_method):
    cap = cv.VideoCapture(path, cv.CAP_ANY)
    cv.namedWindow("Display window", window_method)
    while True:
        ret, frame = cap.read()
        if not(ret):
            break
        converted_frame = cv.cvtColor(frame, color_converter)
        cv.imshow('Display window', converted_frame)
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

showVideo("media/earth.webm", cv.COLOR_BGR2RGB, cv.WINDOW_FULLSCREEN)