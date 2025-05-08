#Autor Tinoco Videgaray Sergio Ernesto
#Fecha: 03/04/22

from PIL import Image
import numpy as np
from matplotlib import pyplot
import math

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


img=Image.open("./mariposas.jpg").convert("L")
matriz=np.asarray(img)

alto=matriz.shape[0]
ancho=matriz.shape[1]

#Logaritmica
print("\nFuncion Logaritmica")
c=int(input("Ingrese el valor de C: "))
if(c==0):
    print("Por favor ingrese un valor distinto de 0")
else:    
    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            matriz[i][j]=SalidaLog(c,matriz[i][j])
            j+=1
        i+=1
    pyplot.imshow(matriz,cmap="gray")
    pyplot.title("Logaritmica")
    pyplot.show()


#Potencia
matriz=np.asarray(img)
print("\nFuncion Potencia")
c=int(input("Ingrese el valor de C: "))
g=float(input("Ingrese el valor de gamma: "))

if(g<=0):
    print("Por favor ingrese un valor de gamma mayor que 0")
else:    
    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            matriz[i][j]=SalidaPot(c,matriz[i][j],g)
            j+=1
        i+=1
    pyplot.imshow(matriz,cmap="gray")
    pyplot.title("Potencia")
    pyplot.show()