import tkinter
from PIL import ImageTk, Image
from functools import partial
from urllib.request import urlopen
import json
import sqlite3

def Equiposbd(self):
        self.db = sqlite3.connect("futbol_bd")
        self.c = self.db.cursor()
        
def opciones(nombres):
    botones = [boton1, boton2, boton3, boton4]
    for i in botones:
        i.config(relief=tkinter.RAISED)
    botones[boton].config(relief=tkinter.SUNKEN)

def inicio():
    ventana_j = tkinter.Tk()
    ventana_j.resizable()
    ventana_j.title("Test De Equipos del Futbol Argentino")
    
    puntF = tkinter.Frame(ventana_j)
    escudoF = tkinter.Frame(ventana_j)
    botonesF = tkinter.Frame(ventana_j)
    confirmarF = tkinter.Frame(ventana_j)
    puntF.grid(column=0,row=0)
    escudoF.grid(column=0,row=1)
    botonesF.grid(column=0,row=2)
    confirmarF.grid(column=0,row=3)
    
    url = 'https://www.escudosfc.com.br/images/san_loc.png'
    u = urlopen(url)
    raw_data = u.read()
    photo = ImageTk.PhotoImage(data=raw_data)
    lbl_img = tkinter.Label (escudoF, image = photo)
    lbl_img.pack()
    
    puntuacion = tkinter.Label(puntF, text = "Puntuacion:", bg = "light blue")
    confirmar = tkinter.Button(confirmarF, text = "Confirmar", bg = "cornflower blue")
    puntuacion.pack()
    confirmar.pack()
    
    boton1 = tkinter.Button(botonesF, text = "name", width = 20, height = 2, command=partial(opciones, 0))
    boton2 = tkinter.Button(botonesF, text = "name2", width = 20, height = 2, command=partial(opciones, 1))
    boton3 = tkinter.Button(botonesF, text = "name3", width = 20, height = 2, command=partial(opciones, 2))
    boton4 = tkinter.Button(botonesF, text = "name4", width = 20, height = 2, command=partial(opciones, 3))
    
    boton1.grid(column=0,row=0)
    boton2.grid(column=1,row=0)
    boton3.grid(column=0,row=1)
    boton4.grid(column=1,row=1)

    ventana_j.mainloop()