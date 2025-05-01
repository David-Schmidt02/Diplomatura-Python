"""
El patrón observador es un patrón de diseño que permite a un objeto (el sujeto) notificar a otros objetos (los observadores) sobre cambios en su estado. En este caso, el sujeto es la clase `Vista` y los observadores son los widgets de la interfaz gráfica.
La clase `Vista` mantiene una lista de observadores y proporciona el método para agregarlos y para notificarles los cambios. Los widgets de la interfaz gráfica  se registran como observadores y actualizan su apariencia en función de la configuración de vista.
"""
class Subject:
    observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, seleccion):
        for observador in self.observadores:
            observador.update_tema(seleccion)

class Observador:
    def update_Tema(self, seleccion):
        raise NotImplementedError("El método 'update_tema' debe ser implementado por los widgets.")



