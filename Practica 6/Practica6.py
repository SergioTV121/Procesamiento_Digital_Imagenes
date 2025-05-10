#Autor: Tinoco Videgaray Sergio Ernesto
#Grupo: 4BV1 IIA
#Fecha 12/05/22


from __future__ import print_function
from cmath import sqrt
import math
from PIL import Image               
import numpy as np                  
from matplotlib import pyplot as plt 

def convertirCMY(r,g,b,alto,ancho):    
    i=0    
    while(i<alto):
        j=0
        while(j<ancho):
            r[i][j]=255-(r[i][j])
            g[i][j]=255-(g[i][j])
            b[i][j]=255-(b[i][j])
            j+=1
        i+=1
    return r,g,b

def convertirHSI(r,g,b,alto,ancho):
    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            R=r[i][j]
            G=g[i][j]
            B=b[i][j]

            arg=((1/2)*((R-G)+(R-B)))/(sqrt((pow((R-G),2))+(R-B)*(G-B))) 
            theta=math.acos(arg)
            theta*=(180/math.pi)        #Conversion Radianes a Grados
            if(B<=G):
                r[i][j]=theta/360       #Matiz
            else:
                r[i][j]=(360-theta)/360
            
            g[i][j]=1-((3/(R+G+B)))*(min([R,G,B]))   #Saturacion

            b[i][j]=(R+G+B)/3   #Intensidad

            j+=1
        i+=1
    return np.trunc(r*255),np.trunc(g*255),np.trunc(b*255)


img=Image.open("peces.jpg")   #Se carga la imagen original
imgGray=img.convert("L")    #Se convierte a escala de grises
gray=np.asarray(imgGray)    #Se genera una matriz con la imagen en niveles de gris

r,g,b=img.split()    #Guardo los 3 canales RGB en 3 variables distintas

#Convierto las imagenes en matrices
r=np.asarray(r)
g=np.asarray(g)
b=np.asarray(b)

alto=r.shape[0]
ancho=r.shape[1]


c,m,y=convertirCMY(np.copy(r),np.copy(g),np.copy(b),alto,ancho)  #Invoco a la funcion para convertir a CMY

#Declaro un objeto de tipo figure para el grafico
fig=plt.figure(figsize=(15,18))  #Tamaño de cada subgrafica
fig.set_size_inches(12, 8)  #Tamaño de la grafica en pulgadas

#Añado el subgrafo del canal Cian
fig.add_subplot(2,2,1)
plt.imshow(c,cmap="gray") 
plt.title("Cian")    
plt.axis("off")

#Añado el subgrafo del canal Magenta
fig.add_subplot(2,2,2)
plt.imshow(m,cmap="gray")
plt.title("Magenta")
plt.axis("off")

#Añado el subgrafo del canal Amarillo
fig.add_subplot(2,2,3)
plt.imshow(y,cmap="gray")
plt.title("Amarillo")
plt.axis("off")

#Añado el subgrafo del canal Gray
fig.add_subplot(2,2,4)
plt.imshow(gray,cmap="gray")
plt.title("Gris")
plt.axis("off")

plt.show()  #Muestro el Grafico Final


h,s,i=convertirHSI(np.copy(r)/255,np.copy(g)/255,np.copy(b)/255,alto,ancho)  #Invoco a la funcion para convertir a HSI

#Declaro un objeto de tipo figure para el grafico
fig=plt.figure(figsize=(15,18))  #Tamaño de cada subgrafica
fig.set_size_inches(12, 8)  #Tamaño de la grafica en pulgadas

#Añado el subgrafo del canal Red
fig.add_subplot(2,2,1)
plt.imshow(h,cmap="gray")
plt.title("Matiz")    
plt.axis("off")

#Añado el subgrafo del canal Green
fig.add_subplot(2,2,2)
plt.imshow(s,cmap="gray")
plt.title("Saturacion")
plt.axis("off")

#Añado el subgrafo del canal Blue
fig.add_subplot(2,2,3)
plt.imshow(i,cmap="gray")
plt.title("Intensidad")
plt.axis("off")

#Añado el subgrafo del canal Gray
fig.add_subplot(2,2,4)
plt.imshow(gray,cmap="gray")
plt.title("Gris")
plt.axis("off")

plt.show()  #Muestro el Grafico Final