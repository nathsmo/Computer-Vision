# Nathalia Morales carnet 20160295
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import sys

kx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
ky = np.array([[-1, -2, -1],
               [ 0, 0,  0],
               [ 1, 2, 1]])

def pad(img, r, v, dtype=np.uint8):
    """Hace un padding de valor v de r pixeles alrededor de una imagen binaria img 
    y devuelva dicha imagen. Si el valor v es -1, el valor a tomar para el padding 
    es una copia de los bordes de la imagen original.
    
    Args:
        img (numpy array): imagen conformada por el array en formato de numpy
        r (int): cantidad de pixeles de padding que se quieren
        v (int): valor si quiere los pixeles de afuera o 0 como padding
        
    Returns:
        padded (numpy array): presentacion de la imagen con el padding agregado
    """
    rows, columns = img.shape
    R = img.shape[0] + 2*r
    C = img.shape[1] + 2*r
    if v != -1:
        padded = np.zeros((R,C),dtype=np.uint8)
        padded[r:rows+r, r:columns+r] = img
    else:
        padded = np.zeros((R,C),dtype=np.uint8)
        padded[r:rows+r, 0] = img[:, 0]
        padded[r:rows+r, columns+r] = img[:, img.shape[1]-1]
        padded[0, r:columns+r] = img[0, :]
        padded[rows+r, r:columns+r] = img[img.shape[0]-1, :]
        
        padded[rows+r, columns+r] = img[rows-1, columns-1]
        padded[0, columns+r] = img[0, columns-1]
        padded[rows+r, 0] = img[rows-1, 0]
        padded[0, 0] = img[0,0]

        padded[r:rows+r, r:columns+r] = img
        
    return padded

def convolve(img, kernel, dtype=np.float64):
    """Efectua una convolución del kernel con la imagen. Por medio de:
    i. Validar que la imagen a procesar es en tonalidades de gris y que el kernel es cuadrado.
    ii. Realiza un padding de radio 1 con copia de los bordes.
    iii. Aplica la convolución de la imagen con padding y el kernel, 
    utilizando el padding para que la operación no se salga de los bordes de la imagen.
    iv. Devuelve la imagen convolucionada sin los valores generados en el borde del padding 
    
    Args:
        img (numpy array): imagen conformada por el array en formato de numpy
        kernel (int): matris de valores conformada por el array en formato de numpy
        
    Returns:
        padded (numpy array): presentacion de la imagen convolucionada por los pasos previamente descritos.
    """
    filas = img.shape[0]
    columnas = img.shape[1]    
    sim = kernel.shape[0]-kernel.shape[1]
    kernel = np.matrix(kernel)

    if np.amin(img) > -1 and sim == 0 and np.amax(img) < 256 and len(img.shape) == 2:
        img = pad(img, 1, -1)
        padded = np.zeros((filas,columnas),dtype=np.float64)
        for i in range(1, filas+1):
            for j in range(1, columnas+1):
                matrix = np.matrix(img[i-1:i+2, j-1:j+2]) 
                res_list = np.multiply(kernel,matrix)
                suma = np.sum(res_list)/9
                padded[i-1][j-1] = suma
        return padded
    else:
        print("La imagen debe de estar en tonalidades de gris. Solo un canal se debe de ingresar a la funcion a la vez.")
        return

def float64_to_uint8(img):
    """Convierte una imagen de tipo float64 a tipo uint8.
    
    Args:
        img (numpy array): imagen conformada por el array en formato de numpy
        
    Returns:
        img (numpy array): presentacion de la imagen con la normalizacion aplicada
    """
    mini = np.min(img)
    maxi = np.max(img)
    img = ((img-mini)/(maxi-mini))*255
    return np.uint8(img)

def gradient2magnitude(gx, gy):
    """ Genera una imagen que representa la magnitud del gradiente calculada a partir 
    de un par de imágenes que representan gradiente horizontal y vertical. 
    
    Args:
        gx (numpy array): imagen conformada por el array con la convolucion en x en formato de numpy
        gy (numpy array): imagen conformada por el array con la convolucion en y en formato de numpy
        
    Returns:
        img (numpy array): imagen con la magnitud entre ambos gradientes
    """
    return np.sqrt((np.square(gx))+(np.square(gy)))

def gradient2angle(gx, gy):
    """ Genera una imagen que representa el ángulo del gradiente calculado 
    a partir de un par de imágenes que representan gradiente horizontal y vertical.
    
    Args:
        gx (numpy array): imagen conformada por el array con la convolucion en x en formato de numpy
        gy (numpy array): imagen conformada por el array con la convolucion en y en formato de numpy
        
    Returns:
        img (numpy array): imagen que contiene los ángulos del gradiente entre pi y menos pi
    """
    return  np.arctan2(gy,gx)

def rgbs(img, kx, ky):
    """ Genera una imagen que 
    
    Args:
        img (numpy array): imagen conformada por el array de numpy
        kx (numpy array): matriz para hacer el gradiente en x
        ky (numpy array): matriz para hacer el gradiente en y
        
    Returns:
        img (numpy array): imagen rgb_magnitudes.png (tipo uint8)
    """
    grad2angle = [[],[],[]]
    grad2mag = [[],[],[]]

    for i in range(0,3):
        gx = convolve(img[:,:,i],kx)
        gy = convolve(img[:,:,i],ky)
        grad2mag[i] = float64_to_uint8(gradient2magnitude(gx, gy))
        grad2angle[i] = float64_to_uint8(gradient2angle(gx, gy))
    grad2mag_img = cv.merge(grad2mag)
    grad2angle_img = cv.merge(grad2angle)
    
    img_save(grad2mag_img, "Color gradient", "rgb_magnitudes.png")
    img_save(grad2angle_img, "Angle", "rgb_angles.png")
    return

def img_save(img, title=None, filename=None):
    """Presenta y guarda la imagen con el titulo
    Args:
    img (numpy array, imagen): imagen 
    title (lista de strings): lista con dos elementos de tipo string 
     para los titulos de las imagenes
    filename (string): titulo de la imagen a descargar en el folder local 
    
    Returns:
        result (img): Presentacion de tres imagenes lado a lado
        con el titulo opcional y con la descarga opcional de ambas en un solo formato.
    """ 
    fig = plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')

    plt.savefig(filename)
    return

def main():
    img = sys.argv[1]
    img = cv.imread(img, cv.IMREAD_COLOR)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    rgbs(img, kx, ky)
    return

if __name__ == '__main__':
   main()