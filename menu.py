from tkinter import *
 
class Ventana_menu:
    #Constructor
    def __init__(self, window):
        self.menu = window

    #Atributos

    #Métodos



#Creamos la ventana
def menu3():

    v_menu = Tk()
    menubar = Menu(v_menu)
    v_menu.config(menu = menubar)
    datosmenu = Menu(menubar, tearoff=0)
    registrarmenu = Menu(menubar, tearoff=0)

    self.estado = IntVar()
    self.estado.set(1)  # Mostrar Barra de Estado
    menubar.add_cascade(label = "Datos", menu = datosmenu)
    menubar.add_cascade(label = "Registrar", menu = registrarmenu)

    v_menu.mainloop()





