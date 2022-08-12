import tkinter
from PIL import ImageTk, Image
from functools import partial
from urllib.request import urlopen
import json

def inicio():
    ventana_j = tkinter.Tk()
    ventana_j.resizable()
    ventana_j.title("Test De Equipos del Futbol Argentino")
    
    f1 = tkinter.Frame(ventana_j)
    f2 = tkinter.Frame(ventana_j)
    f3 = tkinter.Frame(ventana_j)
    url = 'https://www.escudosfc.com.br/images/bocc.png'
    u = urlopen(url)
    raw_data = u.read()
    photo = ImageTk.PhotoImage(data=raw_data)
    lbl_img = tkinter.Label (f1, image = photo)
    lbl_img.pack()
    
    nombre = tkinter.Entry(f2, text = "Nombre", bg = "light Blue")
    empezar = tkinter.Button(f3, text = "Confirmar", bg = "white")
    f1.grid(column=0, row=0)
    f2.grid(column=0, row=1)
    f3.grid(column=0, row=2)
    nombre.grid(row=1, column=0)
    empezar.grid(row=2, column=0)
    
    ventana_j.mainloop()