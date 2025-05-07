#Autor Tinoco Videgaray Sergio Ernesto
#Fecha: 12/03/22

#Ordenamiento por insercion
def OrdenarLista(Lista):
    n=len(Lista)
    j=1
    while(j<n):
        i=j-1
        x=Lista[j]
        while(Lista[i]>x and i>=0):
            Lista[i+1]=Lista[i]
            i-=1
        Lista[i+1]=x  
        j+=1
    return Lista

from traceback import print_tb
from PIL import Image
import numpy as np
from matplotlib import pyplot
from pyparsing import alphas
import statistics as stat

img=Image.open("./gato.jpg").convert("L")
matriz=np.asanyarray(img)
arregloGrises=[]

#Obtener dimensiones de la imagen
alto=matriz.shape[0]
ancho=matriz.shape[1]

#Inicializar el arreglo de niveles de grises
i=0
while(i<=255):
    arregloGrises.append(0)
    i+=1

#Contar cada nivel de gris en la imagen
i=0
while(i<alto):
    j=0
    while(j<ancho):
        r=matriz[i][j]
        arregloGrises[r]+=1
        j+=1
    i+=1

#Calcular la media
i=0
media=0
while(i<=255):
    media+=arregloGrises[r]
    i+=1
media/=256
print("Media: ",media)

arregloGrises=OrdenarLista(arregloGrises)

#Calcular la mediana
mediana=(arregloGrises[128]+arregloGrises[129])/2
print("Mediana: ",mediana)

#Calcular la moda
moda=stat.mode(arregloGrises)
print("Moda: ",moda)

#Calcular la varianza
varianza=0
i=0
while(i<=255):
    varianza+=pow((arregloGrises[i]-media),2)
    i+=1
varianza/=255
print("Varianza: ",varianza)

#Calcular la desviacion estandar
desvEstandar=pow(varianza,(1/2))
print("Desviacion estandar: ",desvEstandar)


#Generar el histograma
pyplot.hist(arregloGrises,255,facecolor='green')
pyplot.title("Histograma")
#Mostrar el histograma
pyplot.show()