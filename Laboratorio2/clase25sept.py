import cv2 as cv
import time

def sliding_window(img, step, window_size):
	""" Apply a sliding window over an image

	Args:
		img(numpy array): Image to apply sliding window
		step (int): Distance in pixels between two windows
		window_size (tuple): Window size in pixels (rows, cols)

	Returns: Generator of corresponding windows
	"""

	r, c = img.shape[0:2]
	for j in range(0, r, step):
		for i in range(0, c, step):
			yield (i, j, img[j:j + window_size[1], i:i + window_size[0]])

	return None


def sliding_window_view(img, step, window_size):
	""" Draw a square over a sliding window

	Args:
		img (numpy array): Image to apply sliding window
		step (int): Distance in pixels between two windows
		windoe_size(tuple): Window size in pixels (rows, cols)

	Returns: None
	"""
	win_r, win_r = window_size

	for (i, j, window) in sliding_window(img, step=step, window_size=window_size):
		if window.shape[0] != win_r or window.shape[1] != win_c:
			continue

		clone = img.copy()
		cv.rectangle(clone, (i,j), (i+win_c, j + win_r), (0, 255, 0), 1)
		cv.imshow("Sliding Window demo", clone)

		#only for visual purposes
		cv.waitKey(1)
		time.sleep(0.01)

	return None

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-path', type=str, help='Path to image', default='../img/cameraman_face.jpg')
	parser.add_argument('-step', type=int, help='Step of windows in rows and cols', default=16)
	args= parser.parse_args()

	img = cv.imread(args.path, cv.IMREAD_UNCHANGED)
	if img.shape != None:
		win_r, win_c = (32,32)
		win_size = (win_r, win_c)
		sliding_window_view(img, args.step, win_size)
	else:
		print('Image not found at {0}'.format(args.pathc))




