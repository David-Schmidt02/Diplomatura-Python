"""
controlador.py:
    Si se ejecuta directamente ('__name__ == "__main__"') permite lanzar la aplicación.
"""
from tkinter import Tk
from vista import Vista
from observador import Subject

class Controlador:
    def __init__(self, root, gestor_tema):
        self.root = root
        self.vista = Vista(self.root, gestor_tema)

class GestorTema (Subject):
    def __init__(self):
        self.tema = "Light"

    def cambiar_tema(self, nuevo_tema):
        self.tema = nuevo_tema
        self.notificar_observadores(self.tema)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Aquí están los parámetros: ", args)      

if __name__ == "__main__":
    root = Tk()
    gestor_tema = GestorTema()
    aplicacion = Controlador(root, gestor_tema)
    root.mainloop()


