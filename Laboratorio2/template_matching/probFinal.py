# Nathalia Morales y Yuri Kaffaty

import cv2 as cv
import numpy as np
import time

def resize(image, width = None, height = None, inter = cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv.resize(image, dim, interpolation = inter)
    return resized

if __name__ == '__main__' :
    cap = cv.VideoCapture(0)
    start = time.time()
    window_name ="Reconocimiento de Logo UFM"

    template = cv.imread("logo.png", cv.IMREAD_GRAYSCALE)
    edge_img = cv.Canny(template, 50, 200)

    (h, w) = template.shape[:2]

    while True:
        lis=[]
        start = time.time()
        good, frame = cap.read()
        lis.append(good)

        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        found = None
        r,c = frame.shape[0:2]
        k = 2
        R = int(r/k)
        C = int(c/k)    
        cv.namedWindow(window_name, cv.WINDOW_NORMAL)
        cv.resizeWindow(window_name, (C,R))
        cv.moveWindow(window_name, 0, 0)

        for scale in np.linspace(0.2, 1.0, 20)[::-1]:

            resized = resize(gray_frame, width = int(gray_frame.shape[1] * scale))
            r = gray_frame.shape[1] / float(resized.shape[1])

            if resized.shape[0] < h or resized.shape[1] < w:
                break

            edge = cv.Canny(resized, 50, 200)
            result = cv.matchTemplate(edge, edge_img, cv.TM_CCOEFF)
            (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + w) * r), int((maxLoc[1] + h) * r))

        seconds = time.time() - start
        num_frames = len(lis)
        fps  = num_frames/seconds

        cv.putText(frame, str("FPS: {0}".format(fps)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0))
        cv.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv.imshow(window_name, frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()