"""
misRegex.py:
    El script almacena las *expresiones regulares* utilizadas para **validar** los *entrys*.
    *patron_producto* se utiliza para validar el nombre de los productos.
    *patron_cantidad* se utiliza para validar la cantidad de los productos.
"""
import re
# regex para el campo cadena
patron_producto = "^[A-Za-záéíóú]+$"
# regex para la cantidad
patron_cantidad = "^[1-9]\d*$"