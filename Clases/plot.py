import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv
import numpy as np
from matplotlib.pyplot import figure

def imgview(img, title=None, filename=None):
    figure(num=None, figsize=(10, 10), dpi=80)

    goc = (len(img.shape))
    img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.axis('off')
    plt.title(title, fontsize=16)
    if goc == 2:
        plt.imshow(img2, vmin=0, vmax=255)
    else:
        plt.imshow(img2)
    if filename != None:
        plt.savefig(filename)
    plt.show()
    
def imgcmp(img1, img2, title=None,filename=None):
    if title == None:
        title = ['','']
    goc = (len(img1.shape))
    goc2 = (len(img2.shape))
    
    img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
    
    f, ax = plt.subplots(1, 2)
    ax[0].axis('off')
    ax[1].axis('off')

    ax[0].imshow(img1)
    ax[1].imshow(img2)
    
    ax[0].set_title(title[0])
    
    if goc == 2:
        ax[0].imshow(img1, vmin=0, vmax=255)
    else:
        ax[0].imshow(img1)
            
    ax[1].set_title(title[1])
    if goc2 == 2:
        ax[1].imshow(img2, vmin=0, vmax=255)
    else:
        ax[1].imshow(img2)
    
    if filename != None:
        f.savefig(filename)
        
    plt.show(block=True)
