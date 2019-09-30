import numpy as np 
import cv2 as cv
import time

min_match = 30
num_frames = 120

detector = cv.xfeatures2d.SIFT_create()
flan = 0

fparam = dict(algorithm=flan, trees=5)
flann=cv.FlannBasedMatcher(fparam,{})

trainImg = cv.imread("logo.png", 0)
trankp, trandecs = detector.detectAndCompute(trainImg, None)

video = cv.VideoCapture(0)

while True:
	ret, querybgr = video.read()

	qimg = cv.cvtColor(querybgr, cv.COLOR_BGR2GRAY)
	qkp, qdesc = detector.detectAndCompute(qimg, None)
	matches = flann.knnMatch(qdesc,trandecs,k=2)

	

	good = []
	start = time.time()
	for m,n in matches:

		if (m.distance<0.75*n.distance):
			good.append(m)

	if(len(good)>min_match):
		tp=[]
		qp=[]

		for m in good:
			tp.append(trankp[m.trainIdx].pt)
			qp.append(qkp[m.queryIdx].pt)

		tp, qp=np.float32((tp, qp))
		H,status=cv.findHomography(tp,qp,cv.RANSAC,3.0)
		h, w = trainImg.shape
		traingBorder=np.float32([[[0,0],[0,h-1],[w-1, h-1], [w-1, 0]]])
		qBorder = cv.perspectiveTransform(traingBorder, H)
		cv.polylines(querybgr, np.int32([qBorder]), True, (0, 255, 0), 5)

	#else:
		#print("Not enough matches - %d/%d"%(len(good), min_match))
	
    # Grab a few frames
	#for i in xrange(0, num_frames):
	#	ret, frame = video.read()
    # End time
	end = time.time()
 
    # Time elapsed
	seconds = end - start
	#print("Time taken : {0} seconds".format(seconds))
 
    # Calculate frames per second
	fps  = num_frames / seconds
	#print("Estimated frames per second : {0}".format(fps))

	cv.putText(querybgr, str("FPS {0}".format(fps)), (50,50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))
	
	cv.imshow('Result', querybgr)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break

#video.release()
#cv.destroyAllWindows()