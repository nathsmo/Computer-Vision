import numpy as np 
import cv2 as cv

def resize(image, width = None, height = None, inter = cv.INTER_AREA):
	# initialize the dimensions of the image to be resized and grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# if both the width and height are None, then return the original image
	if width is None and height is None:
		return image

	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the dimensions
		r = height / float(h)
		dim = (int(w * r), height)

	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the dimensions
		r = width / float(w)
		dim = (width, int(h * r))

	# resize the image
	resized = cv.resize(image, dim, interpolation = inter)

	# return the resized image
	return resized

window_name = 'Original'
window_name2 = 'Logo'

video = cv.VideoCapture(0)
count = 0
template = cv.imread("logo.png")
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

cv.namedWindow(window_name, cv.WINDOW_NORMAL)
cv.namedWindow(window_name2, cv.WINDOW_NORMAL)

while (video.isOpened()):
	ret, frame = video.read()

	r,c = frame.shape[0:2]
	(tH, tW) = template.shape[:2]
	k = 2
	R = int(r/k)
	C = int(c/k)

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	if count == 0:
		count = 1
		#cv.imwrite("image.png", frame)

	for scale in np.linspace(0.2, 1.0, 20)[::-1]:
		# resize the image according to the scale, and keep track of the ratio of the resizing
		resized = resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])

		# if the resized image is smaller than the template, then break from the loop
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break

		# detect edges in the resized, grayscale image and apply template matching to find the template in the image
		edged = cv.Canny(resized, 50, 200)
		result = cv.matchTemplate(edged, template, cv.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv.minMaxLoc(result)

	threshold = 0.6
	loc = np.where(result>=threshold)

	for pt in zip(*loc[::-1]):
		logo_img = frame[pt[1]:pt[1]+tH, pt[0]:pt[0]+tW]
		cv.rectangle(frame, pt, (pt[0]+tW, pt[1]+tH), (0,255,0), 1)

	cv.resizeWindow(window_name, (C,R))

	cv.imshow(window_name, frame)
	cv.imshow(window_name2, logo_img)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break

video.release()
cv.destroyAllWindows()