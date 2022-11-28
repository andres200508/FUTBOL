import tkinter
from PIL import ImageTk, Image
from functools import partial
from urllib.request import urlopen
import sqlite3
import string, random

contador = 0

class VentanaJuego:
    
    def __init__(self):
        self.ventana_j = tkinter.Tk()
        self.ventana_j.resizable(width=False, height=False)
        self.ventana_j.title("¿Cual Es El Nombre Del Siguiente Equipo?")
        self.nombre = ""
        self.nombre2 = ""
        self.nombre3 = ""
        self.nombre4 = ""
        self.url = ""
        self.L_AZ = ""
        self.mostrar_pantalla()
    
    def mostrar_pantalla(self):
        self.equiposbd()
        puntF = tkinter.Frame(self.ventana_j)
        self.escudoF = tkinter.Frame(self.ventana_j)
        botonesF = tkinter.Frame(self.ventana_j)
        confirmarF = tkinter.Frame(self.ventana_j)
        puntF.grid(column=0,row=0)
        self.escudoF.grid(column=0,row=2)
        botonesF.grid(column=0,row=1)
        confirmarF.grid(column=0,row=3)
        
        
        u = urlopen(self.url)
        raw_data = u.read()
        photo = ImageTk.PhotoImage(data=raw_data)
        self.lbl_img = tkinter.Label (self.escudoF, image = photo)
        self.lbl_img.pack()
        
        puntuacion = tkinter.Label(puntF, text = "Puntuacion:"+ str(contador), bg = "light blue")
        puntuacion.pack()
        
        self.boton1 = tkinter.Button(botonesF, text=self.nombre, bg="Paleturquoise4", width=35, height=2, command=partial(self.opciones, 0))
        self.boton2 = tkinter.Button(botonesF, text =self.nombre2, bg = "Paleturquoise4",  width = 35, height = 2, command=partial(self.opciones, 1))
        self.boton3 = tkinter.Button(botonesF, text =self.nombre3, bg = "Paleturquoise4", width = 35, height = 2, command=partial(self.opciones, 2))
        self.boton4 = tkinter.Button(botonesF, text =self.nombre4, bg = "Paleturquoise4", width = 35, height = 2, command=partial(self.opciones, 3))
        
        self.boton1.grid(column=0,row=0)
        self.boton2.grid(column=1,row=0)
        self.boton3.grid(column=0,row=1)
        self.boton4.grid(column=1,row=1)
        self.ventana_j.mainloop()
        
    def sortearletra(self):        
        self.LAZ = random.choice(string.ascii_letters)
        

    def equiposbd(self):
        db = sqlite3.connect("futbol_bd")
        c = db.cursor()
        c.execute('SELECT Nombre,Url from Equipos as c where c.Nombre like "%" order by random() limit 4')
        resp = c.fetchall()
        print(resp)
        self.correcto = random.randint(0,3)
        self.nombre = resp[0][0]
        self.nombre2 = resp[1][0]
        self.nombre3 = resp[2][0]
        self.nombre4 = resp[3][0]
        self.url = resp[self.correcto][1]
        self.nombres = [self.nombre,self.nombre2,self.nombre3,self.nombre4]
        db.close()
     
    def opciones(self,indice):
        if indice == self.correcto:
            print("***************************************************** CORRECTO ***************************************************")
            global contador
            self.lbl_img.destroy()
            self.mostrar_pantalla()
            contador = contador + 1
            print("Puntuacion: " + str(contador) + " equipo(s) acertado(s)")
        else:
            print("❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎ INCORRECTO ❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎")
            respuesta= self.url
            print(self.url)
            self.ventana_j.destroy()
     
            
'''KÑQWXYZ'''

