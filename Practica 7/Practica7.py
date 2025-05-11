import cv2
import numpy as np

from matplotlib import pyplot as plt
imagen=cv2.imread("./Imagenes/huella-dactilar.jpg")    #Carga la magen
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)  #Convierte la imagen a niveles de gris

kernel1=np.ones((5,5),np.uint8)
kernel2=np.array(
        [[0,0,0,0,0],
         [0,0,1,0,0],
         [0,1,1,1,0],
         [0,0,1,0,0],
         [0,0,0,0,0]],np.uint8)
kernel3=np.array(
        [[1,1,1],
         [1,1,1],
         [1,1,1]],np.uint8)

print(kernel2)



 
cv2.imshow('Original', imagen)

imagenErosionada = cv2.erode(imagen, kernel1, iterations=1)
cv2.imshow('Erosion 1', imagenErosionada)
cv2.waitKey(0)
imagenErosionada = cv2.erode(imagen, kernel2, iterations=1)
cv2.imshow('Erosion 2', imagenErosionada)
cv2.waitKey(0)
imagenErosionada = cv2.erode(imagen, kernel3, iterations=1)
cv2.imshow('Erosion 3', imagenErosionada)
cv2.waitKey(0)

imagenDilatada = cv2.dilate(imagen, kernel1, iterations=1)
cv2.imshow('Dilatacion 1', imagenDilatada) 
cv2.waitKey(0)
imagenDilatada = cv2.dilate(imagen, kernel2, iterations=1)
cv2.imshow('Dilatacion 2', imagenDilatada) 
cv2.waitKey(0)
imagenDilatada = cv2.dilate(imagen, kernel3, iterations=1)
cv2.imshow('Dilatacion 3', imagenDilatada) 
cv2.waitKey(0)

imagenApertura = cv2.dilate(imagen, kernel1, iterations=1)
imagenApertura = cv2.erode(imagenApertura, kernel1, iterations=1)
cv2.imshow('Apertura', imagenApertura) 
cv2.waitKey(0)

imagenClausura = cv2.erode(imagen, kernel1, iterations=1)
imagenClausura = cv2.dilate(imagenClausura, kernel1, iterations=1)
cv2.imshow('Clausura', imagenClausura) 
cv2.waitKey(0)
