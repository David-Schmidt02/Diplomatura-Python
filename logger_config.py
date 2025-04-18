import logging
import os
import datetime
# Crear la carpeta "logs" si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuración del primer logger: registra todas las acciones y las muestra por consola
logger_main = logging.getLogger('logger_main')
logger_main.setLevel(logging.DEBUG)

# Añadir un FileHandler para logger_main
file_handler_main = logging.FileHandler('logs/main.log')  # Ruta modificada
file_handler_main.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato para ambos handlers
formatter_main = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter_main)
file_handler_main.setFormatter(formatter_main)

logger_main.addHandler(file_handler_main)
logger_main.addHandler(console_handler)

# Configuración del segundo logger: registra solo acciones relacionadas con el CRUD de la base de datos
logger_bd = logging.getLogger('logger_bd')
logger_bd.setLevel(logging.INFO)

file_handler = logging.FileHandler('logs/logger_bd.log')  # Ruta modificada
file_handler.setLevel(logging.INFO)

formatter_bd = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter_bd)

logger_bd.addHandler(file_handler)

fecha_actual = datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
logger_main.info(f"Se activa el logger del main en la fecha: {fecha_actual}")
logger_bd.info(f"Se activa el logger de la base de datos en la fecha: {fecha_actual}")

# Ejemplo de uso
if __name__ == "__main__":
    logger_main.debug("Este es un mensaje de depuración.")
    logger_main.info("Este es un mensaje informativo.")
