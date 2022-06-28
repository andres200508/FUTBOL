import tkinter
from PIL import ImageTk, Image
from functools import partial
from urllib.request import urlopen

def inicio():
    ventana_j = tkinter.Tk()
    ventana_j.resizable()
    ventana_j.title("Test De Equipos del Futbol Argentino")
    
    f1 = tkinter.Frame(ventana_j)
    f2 = tkinter.Frame(ventana_j)
    f3 = tkinter.Frame(ventana_j)
    
    imageUrl = "https://www.escudosfc.com.br/images/rosarioc.png"
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()
    
    img = ImageTk.Photoimage(data=raw_data)
    label = tkinter.Label(f1, image = img)
    label.image = img
    label.pack()
    
    nombre = tkinter.Entry(f2, text = "Nombre", bg = "light Blue")
    empezar = tkinter.Button(f3, text = "Confirmar", bg = "white")
    
    f1.grid(column=0, row=0)
    f2.grid(column=0, row=1)
    f3.grid(column=0, row=2)
    l1.grid(column=0, row=0)
    nombre.grid()
    empezar.grid()
    
    
    ventana_j.mainloop()