"""
widgets.py:
    El script almacena la configuración compartida entre los distintos *botones*, *labels* y *entrys* utilizados.
"""
from tkinter import *
from observador import Observador

class MiBoton(Observador): #ObservadorConcretoA
    def __init__(self, parent = None, gestor_tema=None, **kwargs):
        self.root = parent
        self.boton = Button(self.root, **kwargs, bg="#F0C266", 
                            activebackground="#BD761A")
        
        self.observado = gestor_tema
        self.observado.agregar_observador(self)

    def grid(self, **kwargs):
        self.boton.grid(**kwargs, sticky="w", padx=5, pady=2)

    def update_tema(self, seleccion):
        if seleccion == "Crema (default)":
            self.boton.config(bg="#F0C266",activebackground="#BD761A")
        elif seleccion == "Light":
            self.boton.config(bg="#B7EEE3",activebackground="#3A6E63",fg="black")
        elif seleccion == "Black":
            self.boton.config(bg="#1A1E48",activebackground="#8487AD",fg="white")

class MiLabel(Observador): #ObservadorConcretoB
    def __init__(self, parent = None, gestor_tema=None, **kwargs):
        self.root = parent
        self.label = Label(self.root, **kwargs, bg="#F9FFDB")

        self.observado = gestor_tema
        self.observado.agregar_observador(self)

    def grid(self, **kwargs):
        self.label.grid(**kwargs, column=1, padx=5, pady=5, sticky="w")

    def update_tema(self, seleccion):
        if seleccion == "Crema (default)":
            self.label.config(bg="#F9FFDB",fg="black")
        elif seleccion == "Light":
            self.label.config(bg="#5EDAF9",fg="black")
        elif seleccion == "Black":
            self.label.config(bg="#8487AD",fg="white")

class MiEntry(Observador): #ObservadorConcretoC
    def __init__(self, parent = None, gestor_tema=None, **kwargs):
        self.root = parent
        self.entry = Entry(self.root, **kwargs, bg="white")

        self.observado = gestor_tema
        self.observado.agregar_observador(self)

    def grid(self, **kwargs):
        self.entry.grid(**kwargs, sticky="w", padx=5, pady=2)
        
    def update_tema(self, seleccion):
        pass



if __name__ == "__main__":
    root = Tk()
    boton = MiBoton(root, text="Alta")
    boton.grid(column=0, row=2)
    root.mainloop()



