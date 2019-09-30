import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

PATH = '../img/'
img = cv.imread(PATH+'cameraman.tif', cv.IMREAD_GRAYSCALE)
img2 = img.copy()
template = cv.imread(PATH+'cameraman_face.jpg', cv.IMREAD_GRAYSCALE)

scale = 0.2
template = cv.resize(template, None,fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)
w, h = template.shape[::-1]

def imgpyramid(img, scale=0.5, min_size=(32, 32)):
    """ Build a pyramid for an image until min_size
        dimensions are reached.
    Args:
        img (numpy array): Source image
        scale (float): scaling factor
        min_size(tuple): size of pyramid top level.
    Returns:
        Pyramid generator
    """
    yield img
    
    while True:
        img = cv.resize(img, None, fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)
        if (img.shape[0]<min_size[0]) or (img.shape[1]<min_size[1]):
            break
        yield img
        
def pyramidview(img):
    for (i, resized) in enumerate(imgpyramid(img)):
        cv.imshow("Layer {}".format(i+1))
        cv.waitkey(0)
        
pyramidview(img)     