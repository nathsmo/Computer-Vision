# USAGE
# python match.py --template cod_logo.png --images images

# import the necessary packages
import numpy as np
import argparse
import glob
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

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True, help="Path to template image")
ap.add_argument("-i", "--images", required=True,
	help="Path to images where template will be matched")
ap.add_argument("-v", "--visualize",
	help="Flag indicating whether or not to visualize each iteration")
args = vars(ap.parse_args())

# load the image image, convert it to grayscale, and detect edges
template = cv.imread(args["template"])
template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
template = cv.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv.imshow("Template", template)

# loop over the images to find the template in
for imagePath in glob.glob(args["images"] + "/*.jpg"):
	# load the image, convert it to grayscale, and initialize the bookkeeping variable to keep track of the matched region
	image = cv.imread(imagePath)
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	found = None

	# loop over the scales of the image
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

		# check to see if the iteration should be visualized
		if args.get("visualize", False):
			# draw a bounding box around the detected region
			clone = np.dstack([edged, edged, edged])
			cv.rectangle(clone, (maxLoc[0], maxLoc[1]),
				(maxLoc[0] + tW, maxLoc[1] + tH), (0, 255, 0), 2)
			cv.imshow("Visualize", clone)
			cv.waitKey(0)

		# if we have found a new maximum correlation value, then update the bookkeeping variable
		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)

	# unpack the bookkeeping variable and compute the (x, y) coordinates of the bounding box based on the resized ratio
	(_, maxLoc, r) = found
	(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
	(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

	# draw a bounding box around the detected result and display the image
	cv.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
	cv.imshow("Image", image)
	cv.waitKey(0)