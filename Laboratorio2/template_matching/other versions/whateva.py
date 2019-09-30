import cv2 as cv
import numpy as np

#Captura de video por OpenCv
cap = cv.VideoCapture(0)
#Imagen a usar para buscar


#Nombres de las ventanas
window_name ="Resultado Final"
window_name2 = "Gris"
window_name3 = "Edges"

#Tomar la imagen y volverla a gris y hacerle edges
template = cv.imread("logo.png", cv.IMREAD_GRAYSCALE)
edge_img = cv.Canny(template, 50, 200)

#tamano de la imagen
(h, w) = template.shape[:2]

while True:
    _, frame = cap.read() #frame momentaneo
    #Frame gris
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Edge sobre el gray frame
    edge = cv.Canny(gray_frame, 50, 200) 

    result = cv.matchTemplate(edge, edge_img, cv.TM_CCOEFF)
    (_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

    #cv.rectangle(frame, (maxLoc2[0], maxLoc2[1]),(maxLoc2[0] + w, maxLoc2[1] + h), (0, 255, 0), 3)
    cv.rectangle(frame, (maxLoc[0], maxLoc[1]), (maxLoc[0] + w, maxLoc[1] + h), (255, 0, 0), 3)

    r,c = frame.shape[0:2]
    k = 2
    R = int(r/k)
    C = int(c/k)

    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
#    cv.namedWindow(window_name2, cv.WINDOW_NORMAL)
#    cv.namedWindow(window_name3, cv.WINDOW_NORMAL)

    cv.resizeWindow(window_name, (C,R))
#    cv.resizeWindow(window_name2, (C,R))
#    cv.resizeWindow(window_name3, (C,R))

    cv.imshow(window_name, frame)
#    cv.imshow(window_name2, gray_frame)
#    cv.imshow(window_name3, edge)

    #align windows
    cv.moveWindow(window_name, 0, 0)
#    cv.moveWindow(window_name2, C, 0)
#    cv.moveWindow(window_name3, C, 0)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()