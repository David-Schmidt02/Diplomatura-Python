"""
controlador.py:
    Si se ejecuta directamente ('__name__ == "__main__"') permite lanzar la aplicación.
"""
from tkinter import Tk
from vista import Vista

if __name__ == "__main__":
    root = Tk()
    objeto = Vista(root)
    root.mainloop()
