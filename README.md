# Computer-Vision

All the functions created during the second semester 2019 on the class of Computer Vision

Functions created in plot.py module:

### To import the module do:
`import plot`

### Functions created inside the plot.py file:

* `imgview(img, title=None, filename=None):`
    * Muestra la imagen img. 
    Args:
    img (numpy array): imagen conformada por el array en formato de numpy
    title (string): titulo opcional de la imagen
    filename (string): titulo opcional de la imagen una vez se descargue
    Returns:
    result (img): presentacion de la imagen asi tambien como la 
    opcion de diplay con su titulo y/o descarga en el folder local

* `imgcmp(img1, img2, title=None, filename=None):`
   * Presentacion de dos imagenes paralelas una al lado de otra
    Args:
    img1 (numpy array, imagen): Primera imagen ingresada
    img2 (numpy array, imagen): Segunda imagen ingresada
    title (lista de strings): lista con dos elementos de tipo string 
     para los titulos de las imagenes
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion de dos imagenes lado a lado
    con el titulo opcional y con la descarga opcional de ambas en un solo formato.
    
* `split_rgb(img, filename=None):`
    * Presentacion de cuatro imagenes con la tonalidad respectiva de RGB
    Args:
    img (numpy array, imagen): imagen ingresada a presentar
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion de cuatro imagenes.
    Primero se presenta la imagen original, seguida por las tonalidades de Rojo, Verde y Azul.
    Tiene la descarga opcional.

* `hist(img, filename=None):`
    * Presentacion del histograma de colores dentro de la imagen
    Args:
    img (numpy array, imagen): imagen ingresada a presentar
    filename (string): titulo de la imagen a descargar en el folder local 
    Returns:
    result (img): Presentacion del histrograma con la frecuencia de los colores y su 
    intensidad dentro de la imagen ingresada.
    Tiene la descarga opcional.
   
* `imgnorm(img):`
    *  Normalize an image using min - max values to [0,255]
    Args:
        img (numpy array): Source image
    Returns:
        normalized (numpy array): Nomalized image


