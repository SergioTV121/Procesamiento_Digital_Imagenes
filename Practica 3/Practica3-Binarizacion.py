#Autor Tinoco Videgaray Sergio Ernesto
#Fecha: 01/04/22


from PIL import Image
import numpy as np
from matplotlib import pyplot

img=Image.open("./ajedrez.png").convert("L")
matriz=np.asarray(img)

alto=matriz.shape[0]
ancho=matriz.shape[1]

m=int(input("Ingrese el valor del umbral: "))

i=0
while(i<alto):
    j=0
    while(j<ancho):
        if(matriz[i][j]<=m):
           matriz[i][j]=0
        else:
            matriz[i][j]=255
        j+=1
    i+=1


pyplot.imshow(matriz,cmap="gray")
pyplot.title("Umbralado")
pyplot.show()

