from asyncio.windows_events import NULL
import cv2         
import numpy as np          
import imutils
from tkinter.filedialog import askopenfilename        
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

#Operaciones aritmeticas

def MostrarImagenResultante(imagenA,imgenB,imagenR,operacion,root):
    fig=plt.figure(figsize=(14,6))
    fig.add_subplot(131)
    plt.imshow(imutils.opencv2matplotlib(imagenA))
    plt.title('Imagen A')
    plt.axis("off")

    fig.add_subplot(132)
    plt.imshow(imutils.opencv2matplotlib(imgenB))
    plt.title('Imagen B')
    plt.axis("off")
    
    fig.add_subplot(133)
    plt.imshow(imutils.opencv2matplotlib(imagenR))
    plt.title(operacion)
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    canvas.get_tk_widget().pack()


#Suma
def Suma(imagenes,root):
    if (np.all(imagenes==NULL)):    #Si no se selecciono alguna Imagen
        return NULL

    imagenSuma = cv2.addWeighted(imagenes[0],0.5,imagenes[1],0.5,0)   #Aplica la suma
    MostrarImagenResultante(imagenes[0],imagenes[1],imagenSuma,"Suma",root)
    return imagenSuma
    



#Resta
def Resta(imagenes,root):
    if (np.all(imagenes==NULL)): #Si no se selecciono alguna Imagen
        return NULL

    imagenResta = cv2.subtract(imagenes[0],imagenes[1])   #Aplica la resta    
    MostrarImagenResultante(imagenes[0],imagenes[1],imagenResta,"Resta",root)
    return imagenResta


#Opreaciones logicas
#AND
def AND(imagenes,root):
    if (np.all(imagenes==NULL)):    #Si no se selecciono alguna Imagen
        return NULL

    imgA=cv2.cvtColor(imagenes[0],cv2.COLOR_BGR2GRAY)
    imgB=cv2.cvtColor(imagenes[1],cv2.COLOR_BGR2GRAY)
    imgA=np.asarray(imgA)      
    imgB=np.asarray(imgB)    

    matrizA=np.asarray(np.copy(imgA),np.uint8)      
    matrizB=np.asarray(np.copy(imgB),np.uint8)   

    alto=matrizA.shape[0]
    ancho=matrizA.shape[1]

    matrizC = np.zeros((alto,ancho),np.uint8)

    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            matrizC[i][j]=matrizA[i][j]&matrizB[i][j]
            j+=1
        i+=1

    MostrarImagenResultante(matrizA,matrizB,matrizC,"Operacion AND",root)
    return cv2.cvtColor(matrizC,cv2.COLOR_GRAY2BGR)




#OR
def OR(imagenes,root):
    if (np.all(imagenes==NULL)):    #Si no se selecciono alguna Imagen
        return NULL


    imgA=cv2.cvtColor(imagenes[0],cv2.COLOR_BGR2GRAY)
    imgB=cv2.cvtColor(imagenes[1],cv2.COLOR_BGR2GRAY)
    imgA=np.asarray(imgA)      
    imgB=np.asarray(imgB)    

    matrizA=np.asarray(np.copy(imgA),np.uint8)      
    matrizB=np.asarray(np.copy(imgB),np.uint8)   

    alto=matrizA.shape[0]
    ancho=matrizA.shape[1]

    matrizC = np.zeros((alto,ancho),np.uint8)

    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            matrizC[i][j]=matrizA[i][j]|matrizB[i][j]
            j+=1
        i+=1

    MostrarImagenResultante(matrizA,matrizB,matrizC,"Operacion OR",root)
    return cv2.cvtColor(matrizC,cv2.COLOR_GRAY2BGR)



#XOR
def XOR(imagenes,root):
    if (np.all(imagenes==NULL)):    #Si no se selecciono alguna Imagen
        return NULL

    imgA=cv2.cvtColor(imagenes[0],cv2.COLOR_BGR2GRAY)
    imgB=cv2.cvtColor(imagenes[1],cv2.COLOR_BGR2GRAY)
    imgA=np.asarray(imgA)      
    imgB=np.asarray(imgB)    

    matrizA=np.asarray(np.copy(imgA),np.uint8)      
    matrizB=np.asarray(np.copy(imgB),np.uint8)   

    alto=matrizA.shape[0]
    ancho=matrizA.shape[1]

    matrizC = np.zeros((alto,ancho),np.uint8)

    i=0
    while(i<alto):
        j=0
        while(j<ancho):
            matrizC[i][j]=matrizA[i][j]^matrizB[i][j]
            j+=1
        i+=1

    MostrarImagenResultante(matrizA,matrizB,matrizC,"Operacion XOR",root)
    return cv2.cvtColor(matrizC,cv2.COLOR_GRAY2BGR)