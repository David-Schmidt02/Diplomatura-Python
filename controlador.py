"""
controlador.py:
    Si se ejecuta directamente ('__name__ == "__main__"') permite lanzar la aplicación.
"""
from tkinter import Tk
from vista import Vista

class Controlador:
    def __init__(self, root, gestor_tema):
        self.root = root
        self.vista = Vista(self.root, gestor_tema)

class GestorTema:
    def __init__(self):
        self.observadores = []
        self.tema = "Light"

    def agregar_observador(self, obs):
        self.observadores.append(obs)

    def cambiar_tema(self, nuevo_tema):
        self.tema = nuevo_tema
        self.notificar()

    def notificar(self):
        for obs in self.observadores:
            obs.update_tema(self.tema)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Aquí están los parámetros: ", args)      

if __name__ == "__main__":
    root = Tk()
    gestor_tema = GestorTema()
    aplicacion = Controlador(root, gestor_tema)
    root.mainloop()


