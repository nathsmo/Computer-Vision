import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while(True):
	#Capture frame-by-frame

	_, frame = video.read()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

	lower_red = np.array([30,150,50])
	upper_red = np.array([255,255,180])

	mask = cv.inRange(hsv, lower_red, upper_red)
	res = cv.bitwise_and(frame,frame, mask= mask)	

	edges = cv.Canny(frame,100,200)

	# Find OpenCV version (para que funcione en cualquier computadora el FPS)
	(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')
     
	if int(major_ver)  < 3:
		fps = video.get(cv.cv.CV_CAP_PROP_FPS)
		#print("Frames per second using video.get(cv.cv.CV_CAP_PROP_FPS): {0}".format(fps))
	else:
		fps = video.get(cv.CAP_PROP_FPS)
		#print("Frames per second using video.get(cv.CAP_PROP_FPS) : {0}".format(fps))
	
	cv.putText(edges, str("FPS {0}".format(fps)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))

	window_name = 'Original'
	window_name2 = 'Edges'

	cv.namedWindow(window_name, cv.WINDOW_NORMAL)
	cv.namedWindow(window_name2, cv.WINDOW_NORMAL)

	r,c = frame.shape[0:2]
	k = 2
	R = int(r/k)
	C = int(c/k)

	#print("these are the dimensions", C, R)
	cv.resizeWindow(window_name, (int(C/2), int(C/2)))
	cv.resizeWindow(window_name2, (C,R))

	cv.imshow(window_name, frame)
	cv.imshow(window_name2, edges)

	#align windows
	cv.moveWindow(window_name, 0, 0)
	cv.moveWindow(window_name2, C, 0)

	#show frame
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv.destroyAllWindows()