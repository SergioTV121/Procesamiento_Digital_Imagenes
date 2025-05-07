#Autor: Tinoco Videgaray Sergio Ernesto
#Grupo: 4BV1 IIA
#Fecha 09/03/22

from PIL import Image                #Biblioteca PIL para trabajar con imagenes
import numpy as np                   #Biblioteca Numpy para trabajar con matrices
from matplotlib import pyplot as plt #Biblioteca MatPlot para trabajar con graficos
img=Image.open("Documents/ProgramasPython/Practicas/PDI/RM/RM-A.jpg")
img=img.convert("L")         #Convierte la imagen en escala de grises para eliminar las capas de color
matriz=np.asarray(img)        #Crea la matriz de la imagen en escala de grises


matrizInv = [ [ 0 for i in range(matriz.shape[1]) ] for j in range(matriz.shape[0]) ]

i=0
while(i<357):
    j=0
    while(j<344):
        matrizInv[i][j]=255-matriz[i][j]     #Restar (L-r)
        j+=1
    i+=1

plt.imshow(matriz,cmap="gray") #Carga los datos de la matriz normal en pyplot
plt.title("Imagen original")
plt.show()#Muestra la imagen original

plt.imshow(matrizInv,cmap="gray") #Carga los datos de la matriz invertida en pyplot
plt.title("Imagen invertida")
plt.show()#Muestra la imagen resultante
