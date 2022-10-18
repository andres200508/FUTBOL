import tkinter
from PIL import ImageTk, Image
from functools import partial
from urllib.request import urlopen
import sqlite3
import random

class VentanaJuego:
    
    def __init__(self):
        ventana_j = tkinter.Tk()
        ventana_j.resizable()
        ventana_j.title("¿Cual Es El Nombre Del Siguiente Equipo?")
        self.nombre = ""
        self.nombre2 = ""
        self.nombre3 = ""
        self.nombre4 = ""
        self.url = ""
        self.equiposbd()
        puntF = tkinter.Frame(ventana_j)
        escudoF = tkinter.Frame(ventana_j)
        botonesF = tkinter.Frame(ventana_j)
        confirmarF = tkinter.Frame(ventana_j)
        puntF.grid(column=0,row=0)
        escudoF.grid(column=0,row=1)
        botonesF.grid(column=0,row=2)
        confirmarF.grid(column=0,row=3)
        
        
        u = urlopen(self.url)
        raw_data = u.read()
        photo = ImageTk.PhotoImage(data=raw_data)
        lbl_img = tkinter.Label (escudoF, image = photo)
        lbl_img.pack()
        
        puntuacion = tkinter.Label(puntF, text = "Puntuacion:", bg = "light blue")
        confirmar = tkinter.Button(confirmarF, text = "Confirmar", bg = "green4")
        puntuacion.pack()
        confirmar.pack()
        
        boton1 = tkinter.Button(botonesF, text=self.nombre, bg="Paleturquoise4", width=35, height=2, command=partial(self.opciones, 0))
        boton2 = tkinter.Button(botonesF, text =self.nombre2, bg = "Paleturquoise4",  width = 35, height = 2, command=partial(self.opciones, 1))
        boton3 = tkinter.Button(botonesF, text =self.nombre3, bg = "Paleturquoise4", width = 35, height = 2, command=partial(self.opciones, 2))
        boton4 = tkinter.Button(botonesF, text =self.nombre4, bg = "Paleturquoise4", width = 35, height = 2, command=partial(self.opciones, 3))
        
        boton1.grid(column=0,row=0)
        boton2.grid(column=1,row=0)
        boton3.grid(column=0,row=1)
        boton4.grid(column=1,row=1)
        
        
        ventana_j.mainloop()
    
    def equiposbd(self):
        db = sqlite3.connect("futbol_bd")
        c = db.cursor()
        c.execute('SELECT Nombre,Url from Equipos order by random() limit 4')
        resp = c.fetchall()
        print(resp)
        self.nombre = resp[0][0]
        self.nombre2 = resp[1][0]
        self.nombre3 = resp[2][0]
        self.nombre4 = resp[3][0]
        self.url = resp[3][1]
        db.close()
            
    def opciones(self,indice):
        botones = [boton1, boton2, boton3, boton4]

    
       