from asyncio.windows_events import NULL
from operator import indexOf
import imutils
import numpy as np
import cv2
from matplotlib import pyplot as plt
from operator import indexOf
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)


def HistogramaGrises(imagen,root):
    if (np.all(imagen==NULL)):
        return
    h,w,c=imagen.shape
    imagenG=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagenG=np.asarray(imagenG)

    fig = plt.figure(constrained_layout=True,figsize=(16,5))
    ax = fig.add_gridspec(1, 4)

    ax1 = fig.add_subplot(ax[0,0])
    ax1.axis("off")      
    ax1.set_title("Imagen")
    ax1.imshow(imutils.opencv2matplotlib(imagenG))

    hist = cv2.calcHist([imagenG], [0], None, [256], [0, 256])  
    
    ax1 = fig.add_subplot(ax[0, 1:3])
    plt.xlabel("Niveles de Gris",fontsize=10)
    plt.ylabel("Numero de Pixeles",fontsize=10)
    plt.xlim([0, 256]) #Rango de valores
    ax1.set_title("Histograma ")
    ax1.plot(hist, color="black")

    #Datos estadisticos
    ax1 = fig.add_subplot(ax[0, 3:4])
    ax1.axis("off")      
    prom,med,mod,var,desv=EstadisticasImagen(imagenG,hist,w*h)
    datos="\nMedia: "+str("{:.2f}".format(prom))+"\nMediana: "+str(med)+"\nModa: "+str(mod)+"\nVarianza: "+str("{:.3f}".format(var))+"\nDesviacion Estandar: "+str("{:.3f}".format(desv))

    ax1.text(0.1, 0.4, 
        datos,
        style = 'normal',
        fontsize = 16,
        color = "black")

        
    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    canvas.get_tk_widget().pack()






def HistogramaRGB(imagen,root):
    if(np.all(imagen==NULL)):
        return
    h,w,c=imagen.shape
    chans = cv2.split(imagen)
    colors = ('b','g','r')

    fig = plt.figure(constrained_layout=True,figsize=(15,8))
    ax = fig.add_gridspec(6, 7)


    ax1 = fig.add_subplot(ax[0:6, 0:2])
    ax1.axis("off")      
    ax1.set_title("Imagen")
    ax1.imshow(imutils.opencv2matplotlib(imagen))
    
    i=4
    for (chan, color) in zip(chans, colors):    #Recorre los canales
        #Crea un histograma con el canal en la iteracion actual
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        ax1 = fig.add_subplot(ax[i:i+2, 2:6])
        #Grafico del Hisograma
        plt.xlabel("Niveles de Gris",fontsize=10)
        plt.ylabel("Numero de Pixeles",fontsize=10)
        plt.xlim([0, 255]) #Rango de valores
        ax1.set_title("Histograma "+color.upper(),fontsize=14)
        ax1.plot(hist, color=color)

        #Datos estadisticos
        ax1 = fig.add_subplot(ax[i:i+2, 6:7])
        ax1.axis("off")      
        prom,med,mod,var,desv=EstadisticasImagen([chan],hist,w*h)
        datos="\nMedia: "+str("{:.2f}".format(prom))+"\nMediana: "+str(med)+"\nModa: "+str(mod)+"\nVarianza: "+str("{:.3f}".format(var))+"\nDesviacion Estandar: "+str("{:.3f}".format(desv))


        ax1.text(0.1, 0.2, 
         datos,
         style = 'normal',
         fontsize = 16,
         color = "black")

        i-=2
    
    
    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()



def EstadisticasImagen(imagen,hist,tam):
    media=(np.sum(imagen))/tam   #Media aritmetica

    m=tam//2     #Posicion intermedia

    k=0

    #Calcular la mediana
    for i in range(len(hist)):  #Recorre los valores del histograma
        k+=int(hist[i]) #Acumula los niveles de gris
        if(k>=m):   #Si la cantidad de pixeles supera la mitad del total
            mediana=i   #Se asigna el indice de los niveles de gris
            break   

    #Varianza
    moda=indexOf(hist,max(hist))    #Obtiene el indice del valor mas alto
    
    #Varianza
    var=0
    i=0
    while(i<=255):
        var+=pow((int(hist[i])-media),2)
        i+=1
    var/=255

    #Calcular la desviacion estandar
    desv=pow(var,(1/2))

    return media,mediana,moda,var,desv
