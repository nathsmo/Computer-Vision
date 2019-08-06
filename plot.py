import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv
import numpy as np
from matplotlib.pyplot import figure

def imgview(img, title=None, filename=None):
    """Muestra la imagen img
    
    Args:
    img (numpy array): imagen conformada por el array en formato de numpy
    title (string): titulo opcional de la imagen
    filename (string): titulo opcional de la imagen una vez se descargue
    Returns:
    result (img): presentacion de la imagen asi tambien como la 
    opcion de diplay con su titulo y/o descarga en el folder local
    """
    figure(num=None, figsize=(10, 10), dpi=80)

    goc = (len(img.shape))
    plt.axis('off')
    plt.title(title, fontsize=16)
    if goc == 2:
        plt.imshow(img, vmin=0, vmax=255, cmap='gray')
    else:
        plt.imshow(img)
    if filename != None:
        plt.savefig(filename)
    plt.show()
            
def imgcmp(img1, img2, title=None, filename=None):
    """Presentacion de dos imagenes paralelas una al lado de otra
    Args:
    img1 (numpy array, imagen): Primera imagen ingresada
    img2 (numpy array, imagen): Segunda imagen ingresada
    title (lista de strings): lista con dos elementos de tipo string 
     para los titulos de las imagenes
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion de dos imagenes lado a lado
    con el titulo opcional y con la descarga opcional de ambas en un solo formato.
    """    
    if title == None:
        title = ['','']
    goc = (len(img1.shape))
    goc2 = (len(img2.shape))
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    if goc == 2:
        ax1.imshow(img1, vmin=0, vmax=255, cmap='gray')
    else:
        ax1.imshow(img1)
    ax1.set_title(title[0])
    plt.axis('off')
    ax2 = fig.add_subplot(222)
    if goc2 == 2:
        ax2.imshow(img2, vmin=0, vmax=255, cmap='gray')
    else:
        ax2.imshow(img2)
    ax2.set_title(title[1])
    plt.axis('off')

    if filename != None:
        plt.savefig(filename)

    plt.show()


def split_rgb(img, filename=None):
    """Presentacion de cuatro imagenes con la tonalidad respectiva de RGB
    Args:
    img (numpy array, imagen): imagen ingresada a presentar
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion de cuatro imagenes.
    Primero se presenta la imagen original, seguida por las tonalidades de Rojo, Verde y Azul.
    Tiene la descarga opcional.
    """ 
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    ax1.imshow(img)
    ax1.set_title('RGB')
    plt.axis('off')
    ax2 = fig.add_subplot(222)
    ax2.imshow(img[:,:,0], cmap='gray', vmin=0, vmax=255)
    ax2.set_title('RED')
    plt.axis('off')
    ax3 = fig.add_subplot(223)
    ax3.imshow(img[:,:,1], cmap='gray', vmin=0, vmax=255)
    ax3.set_title('GREEN')
    plt.axis('off')
    ax4 = fig.add_subplot(224)
    ax4.imshow(img[:,:,2], cmap='gray', vmin=0, vmax=255)
    ax4.set_title('BLUE')
    plt.axis('off')
    
    if filename != None:
        plt.savefig(filename)
    plt.show()

def hist(img, filename=None):
    """ Presentacion del histograma de colores dentro de la imagen
    Args:
    img (numpy array, imagen): imagen ingresada a presentar
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion del histrograma con la frecuencia de los colores y su 
    intensidad dentro de la imagen ingresada.
    Tiene la descarga opcional.
    """ 
    fig = plt.figure(figsize=(30,10))
    ax1 = fig.add_subplot(111)
    colors = ['r','g','b']
    for i, color in enumerate(colors):
        histr = cv.calcHist([img],[i],None,[256],[0,256])
        ax1.plot(histr, c=color)
    
    if filename != None:
        plt.savefig(filename)
    plt.show


def imgnorm(img):
    """Nomralize an image using min - max values to [0,255]
    Args:
        img (numpy array): Source image
    Returns:
        normalized (numpy array): Nomalized image
    """
    vmin, vmax = img.min(), img.max()
    normalized = []
    delta = vmax-vmin
    for p in img.ravel():
        normalized.append(255*(p-vmin)/delta)
    img_normalized = np.array(normalized).astype(np.uint8).reshape(img.shape[0], -1)
    return img_normalized
