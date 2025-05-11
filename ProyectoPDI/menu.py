from glob import glob
from tkinter import Button, Label, Menu, PhotoImage, Tk
from tkinter.filedialog import askopenfilename,asksaveasfile

from numpy import imag
from Modulos.Estadistica import*
from Modulos.TransformacionesBasica import *
from Modulos.AritmeticoLogicas import *
from Modulos.ConversionModelosColor import *
from Modulos.Filtros import *
from Modulos.Morfologia import *
from Modulos.MostrarImagen import *

kernel1=np.array(
                [[0,1,0],
                [1,1,1],
                [0,1,0]],np.uint8)
kernel2=np.ones((3,3),np.uint8)
kernel3=np.array(
                [[0,0,1,0,0],
                [0,1,1,1,0],
                [1,1,1,1,1],
                [0,1,1,1,0],
                [0,0,1,0,0]],np.uint8)



imagen=NULL
imagenM=NULL
toolbarF=NULL
                

def abrirArchivo():
    #Limpiar la Ventana del Menu
    for widgets in root.winfo_children():
        if(str(widgets)!=".!menu"):
            widgets.destroy()
    #Cargar Imagen
    global imagen,imagenM
    if(np.all(imagen==NULL)):   #Si no hay una imagen previamente cargada
        nombreArchivo=askopenfilename(initialdir='./Imagenes/',title = "Selecciona el archivo",filetypes = (("jpg png Files","*.*"),("all files","*.*")))
        if(nombreArchivo):
            imagen=cv2.imread(nombreArchivo)
            imagenM=imagen
            return imagen
        else:
            return NULL
    else:
        return imagen


def ValidarImagenes(imagenA,imagenB):
    while(1):   
        if(imagenA.shape!=imagenB.shape): #Si las imagenes no coinciden en el tamaño
            messagebox.showwarning("Tamaños Incompatibles","Por favor seleccione una imagen de tamaño "+str(imagenA.shape[0])+"x"+str(imagenA.shape[1]))
            nombreArchivo=askopenfilename(initialdir='./Imagenes/Imagenes BN',title = "Selecciona el archivo",filetypes = (("jpg png Files","*.*"),("all files","*.*")))
            if not(nombreArchivo):
                return NULL
            else:
                imagenB=cv2.imread(nombreArchivo)
        else:
            return imagenB

def AbrirAB():
    #Limpiar la Ventana del Menu
    for widgets in root.winfo_children():
        if(str(widgets)!=".!menu"):
            widgets.destroy()
    #Cargar Imagen
    dirImagenA=askopenfilename(initialdir='./Imagenes/',title = "Selecciona la Imagen A",filetypes = (("jpg png Files","*.*"),("all files","*.*")))
    dirImagenB=askopenfilename(initialdir='./Imagenes/',title = "Selecciona la Imagen B",filetypes = (("jpg png Files","*.*"),("all files","*.*")))
    if(dirImagenA and dirImagenB):
        imagenA=cv2.imread(dirImagenA)
        imagenB=cv2.imread(dirImagenB)
        if(np.any(ValidarImagenes(imagenA,imagenB)!=NULL)):
            imagenB=ValidarImagenes(imagenA,imagenB)
            global imagen
            imagen=NULL
            return [imagenA,imagenB]
        else:
            return NULL
    else:
        return NULL


def CargarFrame(operacion,root):
        global imagen,imagenM
        if(np.all(imagen==NULL)):
            return
       
        frame=Frame(root)
        frame.pack()
        frame.config(bg="white")
        frame.grid(padx=20, pady=20)
        
        imagenM=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

        fig,ax=plt.subplots()
        plt.imshow(imagen,cmap='gray')
        plt.title('Imagen')
        plt.axis("off")  
       
        canvas = FigureCanvasTkAgg(fig,master = frame)          
        canvas.get_tk_widget().grid(row=0,column=2,rowspan=4)
        canvas.draw()

        toolbarFrame = Frame(master=root)
        toolbarFrame.grid(row=1,column=0)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        

        #Imagenes
        imgK1=PhotoImage(file="./Imagenes/Kernel/kernel1.gif")
        imgK2=PhotoImage(file="./Imagenes/Kernel/kernel2.gif")
        imgK3=PhotoImage(file="./Imagenes/Kernel/kernel3.gif")
        lblImg1 = Label(frame,image=imgK1)  #Añade la Imagen
        lblImg1.image = imgK1   #Muestra la Imagen
        lblImg2 = Label(frame,image=imgK2)  #Añade la Imagen
        lblImg2.image = imgK2   #Muestra la Imagen
        lblImg3 = Label(frame,image=imgK3)  #Añade la Imagen
        lblImg3.image = imgK3   #Muestra la Imagen

        lblImg1.grid(row=0,column=0)
        lblImg2.grid(row=1,column=0)
        lblImg3.grid(row=2,column=0)

        
        #Botones
        btn1=Button(frame,text="Aplicar Kernel",command=lambda:ActualizarComponentes(AplicarMorfologia(imagenM,kernel1,fig,ax,canvas,frame,root,toolbar,operacion)))
        btn2=Button(frame,text="Aplicar Kernel",command=lambda:ActualizarComponentes(AplicarMorfologia(imagenM,kernel2,fig,ax,canvas,frame,root,toolbar,operacion)))
        btn3=Button(frame,text="Aplicar Kernel",command=lambda:ActualizarComponentes(AplicarMorfologia(imagenM,kernel3,fig,ax,canvas,frame,root,toolbar,operacion)))
        btn4=Button(frame,text="Reiniciar",command=lambda:ReiniciarImagen(fig,canvas,frame,toolbar))
        btn1.grid(row=0,column=1)
        btn2.grid(row=1,column=1)
        btn3.grid(row=2,column=1)
        btn4.grid(row=3,column=1)

def ActualizarComponentes(componentes):
    global imagenM,toolbarF
    imagenM=componentes[0]
    toolbarF=componentes[1]

def setImagenBase():
    global imagen,imagenM
    imagen=imagenM

def NuevaImagen(root):
    global imagen
    imagen=NULL
    Mostrar(abrirArchivo(),root)

def setImagenModificada(img):
    global imagenM
    imagenM=img

def GuardarImagen():
    global imagenM
    if(np.all(imagenM==NULL)):
        messagebox.showwarning("Faltan recursos","No hay ninguna imagen cargada")
        return
    files = [('JPG', '*.jpg'),
             ('PNG', '*.png'),
             ('All Files', '*.*')]
    imgDir = asksaveasfile(mode='w',filetypes=files, defaultextension=files,initialfile="imagen-pdi")
    if imgDir is None:
        return
    cv2.imwrite(imgDir.name,imagenM)
   
    

def CerrarImagen(root):
    #Limpiar la Ventana del Menu
    for widgets in root.winfo_children():
        if(str(widgets)!=".!menu"):
            widgets.destroy()
    global imagen
    imagen=NULL


def ReiniciarImagen(fig,canvas,frame,tbFrame):
    plt.clf()
    plt.close('all')
    fig.clear(False)

    global toolbarF,imagenM,imagen
    imagenM=imagen

    tbFrame.pack_forget()
    tbFrame.grid_forget()

    fig,ax=plt.subplots()
    plt.imshow(imagenM,cmap='gray')
    plt.title('Imagen')
    plt.axis("off")  

    canvas = FigureCanvasTkAgg(fig,master = frame)          
    canvas.draw()

    toolbarF = Frame(master=root)
    toolbarF.grid(row=1,column=0)
    toolbar = NavigationToolbar2Tk(canvas, toolbarF)
    
    canvas.get_tk_widget().grid(row=0,column=2,rowspan=4)




def AcercaDe():
    messagebox.showinfo("Acerca de","Programado por Sergio Tinoco Videgaray\nProcesamiento Digital de Imagenes - 4BV1\nIngenieria en IA ESCOM-IPN")

def Salir():
    opcion=messagebox.askokcancel("Salir","¿Seguro que deseas salir del programa?")
    if(opcion):
        root.destroy()

root=Tk()
root.title("Procesamiento de Imagenes")
root.iconbitmap("./icono.ico")

barraMenu=Menu(root)
root.config(menu=barraMenu,width=820,height=200,bg="white")

#Pestañas Menu

menuArchivo=Menu(barraMenu,tearoff=0)
menuArchivo.add_command(label="Cargar Imagen",command=lambda:NuevaImagen(root))
menuArchivo.add_command(label="Guardar Imagen",command=lambda:GuardarImagen())
menuArchivo.add_separator()
menuArchivo.add_command(label="Usar Imagen Resultante",command=lambda:setImagenBase())
menuArchivo.add_command(label="Cerrar Imagen",command=lambda:CerrarImagen(root))
menuArchivo.add_command(label="Salir",command=Salir)

#Menu de Operaciones Basicas
menuOpBasicas=Menu(barraMenu,tearoff=0)

#Submenu Obtener Histograma
menuOpBasicas.add_command(label="Histograma Grises",command=lambda:HistogramaGrises(abrirArchivo(),root))
menuOpBasicas.add_command(label="Histograma RGB",command=lambda:HistogramaRGB(abrirArchivo(),root))

menuTransformaciones=Menu(barraMenu,tearoff=0)

#Submenu Obtener Imagen Invertida
menuTransformaciones.add_command(label="Invertir Imagen",command=lambda:setImagenModificada(Reversion(abrirArchivo(),root)))

#Submenu Binarizar
menuTransformaciones.add_command(label="Binarizacion",command=lambda:setImagenModificada(Binarizar(abrirArchivo(),root)))

#Submenu Transformacion Logaritmica
menuTransformaciones.add_command(label="Logaritmo",command=lambda:setImagenModificada(FuncionLogaritmica(abrirArchivo(),root)))

#Submenu Transformacion Potencia
menuTransformaciones.add_command(label="Potencia",command=lambda:setImagenModificada(FuncionPotencia(abrirArchivo(),root)))

#Menu Aritmetico Logicas
menuAritmeticoLogicas=Menu(barraMenu,tearoff=0)
#Submenu Operacion Suma
menuAritmeticoLogicas.add_command(label="Suma",command=lambda:setImagenModificada(Suma(AbrirAB(),root)))
#Submenu Operacion Resta
menuAritmeticoLogicas.add_command(label="Resta",command=lambda:setImagenModificada(Resta(AbrirAB(),root)))
menuAritmeticoLogicas.add_separator()
#Submenu Operacion AND
menuAritmeticoLogicas.add_command(label="AND",command=lambda:setImagenModificada(AND(AbrirAB(),root)))
#Submenu Operacion OR
menuAritmeticoLogicas.add_command(label="OR",command=lambda:setImagenModificada(OR(AbrirAB(),root)))
#Submenu Operacion XOR
menuAritmeticoLogicas.add_command(label="XOR",command=lambda:setImagenModificada(XOR(AbrirAB(),root)))

#Menu Conversion
menuConversion=Menu(barraMenu,tearoff=0)
#Submenu Conversion CMY
menuConversion.add_command(label="CMY",command=lambda:convertirCMY(abrirArchivo(),root))
#Submenu Conversion HSI
menuConversion.add_command(label="HSI",command=lambda:convertirHSI(abrirArchivo(),root))

#Menu de Filtros
menuFiltros=Menu(barraMenu,tearoff=0)
#Submenu Filtro Promedio
menuFiltros.add_command(label="Promedio",command=lambda:setImagenModificada(Promedio(abrirArchivo(),root)))
#Submenu Filtro Media
menuFiltros.add_command(label="Mediana",command=lambda:setImagenModificada(Mediana(abrirArchivo(),root)))
#Submenu Filtro Laplaciano
menuFiltros.add_command(label="Laplaciano",command=lambda:setImagenModificada(Laplaciano(abrirArchivo(),root)))
#Submenu Filtro Sobel
menuFiltros.add_command(label="Sobel",command=lambda:setImagenModificada(Sobel(abrirArchivo(),root)))

#Menu de Morfologia
menuMorfologia=Menu(barraMenu,tearoff=0)
#Submenu Diltacion
menuMorfologia.add_command(label="Diltacion",command=lambda:[abrirArchivo(),CargarFrame(1,root)])
#Submenu Erosion
menuMorfologia.add_command(label="Erosion",command=lambda:[abrirArchivo(),CargarFrame(2,root)])
menuMorfologia.add_separator()
#Submenu Apertura
menuMorfologia.add_command(label="Apertura",command=lambda:[abrirArchivo(),CargarFrame(3,root)])
#Submenu Clausura
menuMorfologia.add_command(label="Clausura",command=lambda:[abrirArchivo(),CargarFrame(4,root)])


#Ayuda
menuAcercaDe=Menu(barraMenu,tearoff=0)
#Submenu ayuda
menuAcercaDe.add_command(label="Acerca de",command=AcercaDe)

#Agregar Pestañas Menu
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
barraMenu.add_cascade(label="Operaciones Basicas",menu=menuOpBasicas)
barraMenu.add_cascade(label="Transformaciones",menu=menuTransformaciones)
barraMenu.add_cascade(label="Aritmetico Logicas",menu=menuAritmeticoLogicas)
barraMenu.add_cascade(label="Conversion",menu=menuConversion)
barraMenu.add_cascade(label="Filtros",menu=menuFiltros)
barraMenu.add_cascade(label="Morfologia",menu=menuMorfologia)
barraMenu.add_cascade(label="Ayuda",menu=menuAcercaDe)


root.mainloop()