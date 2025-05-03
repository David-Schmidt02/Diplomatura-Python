"""
El patrón observador es un patrón de diseño que permite a un objeto (el sujeto) notificar a otros objetos (los observadores) sobre cambios en su estado. En este caso, el sujeto es la clase `Vista` y los observadores son los widgets de la interfaz gráfica.
La clase `Vista` mantiene una lista de observadores y proporciona el método para agregarlos y para notificarles los cambios. Los widgets de la interfaz gráfica  se registran como observadores y actualizan su apariencia en función de la configuración de vista.
"""
import os

ruta_txts = os.path.join(os.path.dirname(__file__), 'txts')
os.makedirs(ruta_txts, exist_ok=True) 
archivo_registro = os.path.join(ruta_txts, 'registro_cambio_de_temas.txt')

def registrar_cambio(widget, tema):
    """
    Registra el cambio de tema de un widget en un archivo de texto.
    
    :param widget: Nombre del widget que cambió de tema.
    :param tema: Tema seleccionado.
    """
    with open(archivo_registro, 'a') as archivo:
        archivo.write(f"Widget: {widget}, Tema: {tema}\n")

class Subject:
    observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, seleccion):
        for observador in self.observadores:
            observador.update_tema(seleccion)
            registrar_cambio(observador.__class__.__name__, seleccion)

class Observador:
    def update_Tema(self, seleccion):
        raise NotImplementedError("El método 'update_tema' debe ser implementado por los widgets.")
