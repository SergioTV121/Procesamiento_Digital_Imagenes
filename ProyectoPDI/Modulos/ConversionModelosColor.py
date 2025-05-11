
from __future__ import print_function
from asyncio.windows_events import NULL
from cmath import sqrt
import math
import cv2               
import numpy as np                  
from matplotlib import pyplot as plt 
import imutils
import cv2
from pyparsing import alphas
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

def convertirCMY(imagen,root):  
    if (np.all(imagen==NULL)):
        return
    
    b,g,r=cv2.split(imagen)    #Guardo los 3 canales RGB en 3 variables distintas

    #Convierto las imagenes en matrices
    c=np.asarray(r)
    m=np.asarray(g)
    y=np.asarray(b)

    alto=c.shape[0]
    ancho=c.shape[1]
    i=0    
    while(i<alto):
        j=0
        while(j<ancho):
            c[i][j]=255-(c[i][j])
            m[i][j]=255-(m[i][j])
            y[i][j]=255-(y[i][j])
            j+=1
        i+=1

    #Declaro un objeto de tipo figure para el grafico
    fig=plt.figure(figsize=(16,8))        
    fig.add_subplot(232), plt.imshow(imutils.opencv2matplotlib(imagen)),plt.title('Imagen Original')
    plt.axis("off")
    fig.add_subplot(234), plt.imshow(c, cmap='gray'),plt.title('Cian')
    plt.axis("off")
    fig.add_subplot(235), plt.imshow(m, cmap='gray'),plt.title('Magenta')
    plt.axis("off")
    fig.add_subplot(236), plt.imshow(y, cmap='gray'),plt.title('Amarillo')
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()



def convertirHSI(imagen,root):
    if (np.all(imagen==NULL)):
        return
    b,g,r=cv2.split(imagen) #Guardo los 3 canales RGB en 3 variables distintas

    #Convierto las imagenes en matrices
    h=np.asarray(r)/255
    s=np.asarray(g)/255
    i=np.asarray(b)/255

    alto=h.shape[0]
    ancho=h.shape[1]

    j=0
    while(j<alto):
        k=0
        while(k<ancho):
            R=h[j][k]
            G=s[j][k]
            B=i[j][k]

            arg=((1/2)*((R-G)+(R-B)))/(sqrt((pow((R-G),2))+(R-B)*(G-B))) 
            theta=math.acos(arg)
            theta*=(180/math.pi)        #Conversion Radianes a Grados
            if(B<=G):
                h[j][k]=theta/360       #Matiz
            else:
                h[j][k]=(360-theta)/360
            
            s[j][k]=1-((3/(R+G+B)))*(min([R,G,B]))   #Saturacion

            i[j][k]=(R+G+B)/3   #Intensidad

            k+=1
        j+=1
    h=np.trunc(h*255)
    s=np.trunc(s*255)
    i=np.trunc(i*255)

    #Declaro un objeto de tipo figure para el grafico
    fig=plt.figure(figsize=(16,8))        
    fig.add_subplot(232), plt.imshow(imutils.opencv2matplotlib(imagen)),plt.title('Imagen Original')
    plt.axis("off")
    fig.add_subplot(234), plt.imshow(h, cmap='gray'),plt.title('Matiz')
    plt.axis("off")
    fig.add_subplot(235), plt.imshow(s, cmap='gray'),plt.title('Saturacion')
    plt.axis("off")
    fig.add_subplot(236), plt.imshow(i, cmap='gray'),plt.title('Intensidad')
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()