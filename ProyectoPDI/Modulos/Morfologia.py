from asyncio.windows_events import NULL
from tkinter import Frame
import cv2
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

def AplicarMorfologia(imagen,kernel,fig,ax,canvas,frame,root,toolBarFrame,operacion):        
        plt.clf()
        plt.close('all')
        fig.clear(False)
        toolBarFrame.pack_forget()
        toolBarFrame.grid_forget()
                
        if(operacion==1):  #Dilatar
                imagen = cv2.dilate(imagen, kernel, iterations=1)
        elif(operacion==2):           #Erosionar
                imagen = cv2.erode(imagen, kernel, iterations=1)
        elif(operacion==3):           #Apertura
                imagen = cv2.erode(imagen, kernel, iterations=1)
                imagen = cv2.dilate(imagen, kernel, iterations=1)
        elif(operacion==4):           #Clausura
                imagen = cv2.dilate(imagen, kernel, iterations=2)
                imagen = cv2.erode(imagen, kernel, iterations=1)
                
     
        fig,ax=plt.subplots()
        plt.imshow(imagen,cmap='gray')
        plt.title('Imagen')
        plt.axis("off")  
       
        canvas = FigureCanvasTkAgg(fig,master = frame)          
        canvas.draw()
        canvas.get_tk_widget().grid(row=0,column=2,rowspan=4)

        toolbarFrame = Frame(master=root)
        toolbarFrame.grid(row=1,column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

        return [imagen,toolbar]
        