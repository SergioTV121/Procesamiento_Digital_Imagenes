from asyncio.windows_events import NULL
import imutils
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np

def Mostrar(imagen,root):
    if(np.all(imagen==NULL)):
        return
    fig,ax=plt.subplots()
    plt.imshow(imutils.opencv2matplotlib(imagen))
    plt.title('Imagen')
    plt.axis("off")

    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()

    canvas.get_tk_widget().pack()