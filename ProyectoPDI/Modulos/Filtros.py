from asyncio.windows_events import NULL
import cv2
from cv2 import blur
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


def MostrarImagenResultante(imagenO,imagenR,operacion,root):
    fig=plt.figure(figsize=(10,6))        
    fig.add_subplot(121), plt.imshow(imagenO,cmap='gray'),plt.title('Imagen Original')
    plt.axis("off")
    fig.add_subplot(122), plt.imshow(imagenR, cmap='gray'),plt.title(operacion)
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    canvas.get_tk_widget().pack()


def Promedio(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    figure_size = 5
    imagenFiltrada = cv2.blur(imagen,(figure_size, figure_size))
    MostrarImagenResultante(imagen,imagenFiltrada,"Filtro Promedio",root)
    return cv2.cvtColor(imagenFiltrada,cv2.COLOR_GRAY2BGR)

def Mediana(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    figure_size = 5
    imagenFiltrada = cv2.medianBlur(imagen, figure_size)
    MostrarImagenResultante(imagen,imagenFiltrada,"Filtro de Mediana",root)
    return cv2.cvtColor(imagenFiltrada,cv2.COLOR_GRAY2BGR)


def Laplaciano(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    blr=cv2.GaussianBlur(imagen,(3,3),0)
    imagenFiltrada = cv2.Laplacian(blr,cv2.CV_16S,ksize=3)
    imagenFiltrada=cv2.subtract(imagen,imagenFiltrada,dtype=cv2.CV_16S)
    MostrarImagenResultante(imagen,imagenFiltrada,"Filtro Laplaciano",root)
    norm = cv2.normalize(imagenFiltrada, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return cv2.cvtColor(norm,cv2.COLOR_GRAY2BGR)
    

def Sobel(imagen,root):  
    if (np.all(imagen==NULL)):
        return NULL
        
    x = cv2.Sobel(imagen,cv2.CV_16S,1,0)  
    y = cv2.Sobel(imagen,cv2.CV_16S,0,1)  
    
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)  
    
    imagenFiltrada = cv2.addWeighted(absX,0.5,absY,0.5,0)  
    
    MostrarImagenResultante(imagen,imagenFiltrada,"Filtro de Sobel",root)
    return imagenFiltrada