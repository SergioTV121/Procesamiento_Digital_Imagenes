from asyncio.windows_events import NULL
from tkinter import messagebox
import numpy as np
import cv2
import imutils
from matplotlib import pyplot as plt
import math
from tkinter.simpledialog import askinteger,askfloat
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


def MaxLog(c):
    return 8*c

def SalidaLog(c,r):
    S=c*(math.log(r+1,2))
    S*=255/(MaxLog(c))
    return S

def MaxPot(c,g):
    return c*(255**g)

def SalidaPot(c,r,g):
    S=c*(r**g)
    S*=255/(MaxPot(c,g))
    return S


def MostrarImagenResultante(imagenO,imagenR,operacion,root):
    fig=plt.figure(figsize=(10,6))        
    fig.add_subplot(121), plt.imshow(imutils.opencv2matplotlib(imagenO)),plt.title('Imagen Original')
    plt.axis("off")
    fig.add_subplot(122), plt.imshow(imutils.opencv2matplotlib(imagenR)),plt.title(operacion)
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    canvas.get_tk_widget().pack()    



def Reversion(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    
    imgT=cv2.bitwise_not(imagen)   #Obtiene el negativo de la imagen

    MostrarImagenResultante(imagen,imgT,"Imagen Invertida",root)
    return imgT

    

def Binarizar(imagen,root):     
    if (np.all(imagen==NULL)):
        return NULL
    m=askinteger("Umbralado","Ingrese un valor para el Umbral",minvalue=0,maxvalue=255)    
    if(m is None):
        return

    img=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    img=np.asarray(img)
    imgT=np.copy(img)

    alto=imgT.shape[0]
    ancho=imgT.shape[1]

    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            if(imgT[i][j]<=m):
                imgT[i][j]=0
            else:
                imgT[i][j]=255
            j+=1
        i+=1

    MostrarImagenResultante(imagen,imgT,"Imagen Binarizada",root)
    return cv2.cvtColor(imgT,cv2.COLOR_GRAY2BGR)



def FuncionLogaritmica(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    c=0
    while(c==0):
        c=askinteger("Logaritmica","Ingrese un valor para el parametro C")
        if(c==0):
            messagebox.showwarning("Dato no valido","Por favor ingrese un valor distinto de 0")
        
    if(c is None):
        return
    img=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    img=np.asarray(img)
    imgT=np.copy(img)

    alto=imgT.shape[0]
    ancho=imgT.shape[1]

    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            imgT[i][j]=SalidaLog(c,imgT[i][j])
            j+=1
        i+=1
    MostrarImagenResultante(imagen,imgT,"Transformacion Logaritmica",root)
    return cv2.cvtColor(imgT,cv2.COLOR_GRAY2BGR)


#Potencia

def FuncionPotencia(imagen,root):
    if (np.all(imagen==NULL)):
        return NULL
    c,g=0,0
    while(c==0):
        c=askinteger("Potencia","Ingrese un valor para el parametro C")
        if(c==0):
            messagebox.showwarning("Dato no valido","Por favor ingrese un valor distinto de 0")

    if(c is None ):
        return

    g=askfloat("Potencia","Ingrese un valor para el parametro Gamma",minvalue=0.01,maxvalue=50)

    if(g is None ):
        return    

    img=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    img=np.asarray(img)
    imgT=np.copy(img)

    alto=imgT.shape[0]
    ancho=imgT.shape[1]

    
    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            imgT[i][j]=SalidaPot(c,imgT[i][j],g)
            j+=1
        i+=1

    MostrarImagenResultante(imagen,imgT,"Transformacion Potencia",root)
    return cv2.cvtColor(imgT,cv2.COLOR_GRAY2BGR)