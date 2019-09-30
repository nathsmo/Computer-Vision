import cv2 as cv

cap = cv.VideoCapture(0)
#set video capture properties

# hardware specific
#cap.set(cv.CAP_)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()
	thresh, result = cv.threshold(frame[:,:,0], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
	#result = cv.merge([result, result, result])
	result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
	cv.putText(result, str(thresh), (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
	#result = cv.GaussianBlur(frame, (0,0), 15)

	window_name = 'Original'
	window_name2 = 'Blur'

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
	cv.imshow(window_name2, result)

	#align windows
	cv.moveWindow(window_name, 0, 0)
	cv.moveWindow(window_name2, C, 0)

	#show frame
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

#When everythins done, release the capture
cap.release()
cv.destroyAllWindows()