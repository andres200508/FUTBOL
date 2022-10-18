import tkinter
from functools import partial
from ventana_juego import VentanaJuego
#boton.config(relief=tkinter.RAISED)
#boton.config(relief=tkinter.SUNKEN)


ventana = tkinter.Tk()
ventana.resizable(width=0, height=0)
ventana.title("Test De Equipos del Futbol Argentino")

def elegir_dificultad(boton):
    botones = [boton1, boton2, boton3, boton4]
    for i in botones:
        i.config(relief=tkinter.RAISED)
    botones[boton].config(relief=tkinter.SUNKEN)

def finalizar():
    ventana.destroy()
    vj=VentanaJuego()

f1 = tkinter.Frame(ventana)
f2 = tkinter.Frame(ventana)
f3 = tkinter.Frame(ventana)
f1.grid(column=0, row=0)
f2.grid(column=0, row=1)
f3.grid(column=0, row=2)

boton1 = tkinter.Button(f1, text = "Facil", width = 10, height = 5, command=partial(elegir_dificultad, 0), bg="lawn green")
boton2 = tkinter.Button(f1, text = "Medio", width = 10, height = 5, command=partial(elegir_dificultad, 1), bg="yellow2")
boton3 = tkinter.Button(f1, text = "Dificil", width = 10, height = 5, command=partial(elegir_dificultad, 2), bg="darkgoldenrod1")
boton4 = tkinter.Button(f1, text = "Imposible", width = 10, height = 5, command=partial(elegir_dificultad, 3), bg="orangered2")


#etiqueta.pack(fill = tkinter.BOTH, expand = True)
etiqueta = tkinter.Label(f2, text = "Ingrese un nombre de usuario", bg = "cornflower blue")
nombre = tkinter.Entry(f2, text = "Nombre de usuario", bg = "gray80")
empezar = tkinter.Button(f3, text = "Presione Para Iniciar", bg = "cornflower blue", command=finalizar)


etiqueta.grid(row =0, column = 0)
nombre.grid(row=1, column=0)
empezar.grid(row=0, column=0)

boton1.grid(row = 1, column = 0)
boton2.grid(row = 1, column = 1)
boton3.grid(row = 1, column = 2)
boton4.grid(row = 1, column = 3)

ventana.mainloop()    