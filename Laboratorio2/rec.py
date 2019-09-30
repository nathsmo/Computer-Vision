import cv2 as cv
import numpy as np

img = cv.imread("testing_img.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread("ufm_logo.png", cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv.matchTemplate(gray_img, template, cv.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.8)

for pt in zip(*loc[::-1]):
	cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 3)

scale=0.5
img = cv.resize(img, None, fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)

cv.imshow("img", img)
cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()
