import cv2 as cv
import numpy as np 


img_bgr = cv.imread('testing_img.jpg')
img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

template = cv.imread('ufm_logo.png', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)

cv.imshow('detected', img_bgr)
cv.waitKey(0)
cv.destroyAllWindows()