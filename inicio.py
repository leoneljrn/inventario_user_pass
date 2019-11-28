
from tkinter import *

from menu import menu3

class Ventana_login:
    #Constructor
    def __init__(self, window):
        self.window = window 
        frm_login(self)
            
    #Atributos

    #Métodos
    

def frm_login(self):

        self.window.title("Inventario Usuario") 

        #creamos un contenedor para la ventana login
        frame = LabelFrame(self.window, text = "Ingrese un Usuario")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        frame.pack() # Empaqueta el frame en la raíz
        #frame.pack(fill="x") #Ocupa el ancho de la ventana
        frame.pack(fill="both", expand=1) #Ocupa todo el espacio de la ventana
        #frame.pack(fill="y")  #Ocupa el alto de la ventana (por verificar)
        #frame.pack(side=RIGHT) 
        frame.config(bg="lightgreen")

        #creamos un imput con su label
        Label(frame, text = "Usuario:").grid(row = 1, column = 0, sticky = W)
        
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)
        

        Label(frame, text = "Clave:").grid(row = 2, column = 0, sticky = W)
        self.clave = Entry(frame)
        self.clave.grid(row = 2, column = 1) 

        #Buton
        Button(frame, text = "Enviar", command = menu3).grid(row = 3, columnspan = 2, pady = 5 )

def ingresar():
    print('Bienvenido..')

if __name__ == '__main__':
    v_login = Tk()
    v_login.geometry('300x100')
    v_login.config(bg="blue") 
    vent_login = Ventana_login(v_login)
    v_login.mainloop()



