#Autor: Tinoco Videgaray Sergio Ernesto
#Grupo: 4BV1 IIA
#Fecha 08/04/22

from PIL import Image               
import numpy as np                  
from matplotlib import pyplot as plt 


#Opreaciones aritmeticas

imgA=Image.open("P5/imgA.jpg").convert("L")
imgB=Image.open("P5/imgB.jpg").convert("L")

matrizA=np.asarray(imgA)      
matrizB=np.asarray(imgB)    

alto=matrizA.shape[0]
ancho=matrizA.shape[1]

matrizC = [ [ 0 for i in range(ancho) ] for j in range(alto) ]

#Suma
i=0
while(i<alto):
    j=0
    while(j<ancho):
        matrizC[i][j]=(matrizA[i][j]+matrizB[i][j])//2
        j+=1
    i+=1

plt.imshow(matrizC,cmap="gray")
plt.title("Suma")
plt.show()

#Resta
i=0
while(i<alto):
    j=0
    while(j<ancho):
        matrizC[i][j]=(matrizA[i][j]-matrizB[i][j])
        if(matrizC[i][j]<0):
            matrizC[i][j]=0
        j+=1
    i+=1

plt.imshow(matrizC,cmap="gray")
plt.title("Resta")
plt.show()



#Opreaciones logicas
imgA=Image.open("P5/cA.jpg").convert("L")
imgB=Image.open("P5/cB.jpg").convert("L")

matrizA=np.asarray(imgA)      
matrizB=np.asarray(imgB)    

alto=matrizA.shape[0]
ancho=matrizA.shape[1]

matrizC = [ [ 0 for i in range(ancho) ] for j in range(alto) ]

#AND
i=0
while(i<alto):
    j=0
    while(j<ancho):
        matrizC[i][j]=matrizA[i][j]&matrizB[i][j]
        j+=1
    i+=1

plt.imshow(matrizC,cmap="gray")
plt.title("AND")
plt.show()



#OR
imgA=Image.open("P5/gA.jpg").convert("L")
imgB=Image.open("P5/gB.jpg").convert("L")

matrizA=np.asarray(imgA)      
matrizB=np.asarray(imgB)    

alto=matrizA.shape[0]
ancho=matrizA.shape[1]

matrizC = [ [ 0 for i in range(ancho) ] for j in range(alto) ]

i=0
while(i<alto):
    j=0
    while(j<ancho):
        matrizC[i][j]=matrizA[i][j]|matrizB[i][j]
        j+=1
    i+=1

plt.imshow(matrizC,cmap="gray")
plt.title("OR")
plt.show()

#XOR
i=0
while(i<alto):
    j=0
    while(j<ancho):
        matrizC[i][j]=matrizA[i][j]^matrizB[i][j]
        j+=1
    i+=1

plt.imshow(matrizC,cmap="gray")
plt.title("XOR")
plt.show()