# 🐱‍💻 Gestor de Productos Cosméticos con Tkinter, PeeWee y Patrón Observador

¡Bienvenido/a a este proyecto de gestión y análisis de productos cosméticos desarrollado en Python!  
Esta aplicación permite administrar productos, gestionar temas visuales, registrar acciones y trabajar con diferentes motores de base de datos, todo bajo una arquitectura robusta y buenas prácticas de desarrollo.

---

## 🚀 Tecnologías y librerías utilizadas

- **Tkinter** 🖥️ – Framework estándar para crear interfaces gráficas en Python.
- **PeeWee** 🗄️ – ORM ligero para interactuar con bases de datos relacionales (SQLite, MySQL, PostgreSQL).
- **logging** 📋 – Registro y manejo de logs para auditoría y depuración.
- **re** 🔎 – Manejo de expresiones regulares para validación y procesamiento de datos.
- **os** 📁 – Gestión de archivos y directorios.
- **Programación Orientada a Objetos (POO)** 🧩 – Modularización y reutilización de código.
- **Descriptores** 🛠️ – Gestión avanzada de atributos en clases.
- **Patrones de diseño**: Observador 👀 – Notificación automática de cambios de estado entre componentes.

---

## 🧠 Conocimientos aplicados

- **Patrón Observador:** Implementación para que los widgets de la interfaz reaccionen automáticamente a los cambios de tema.
- **Descriptores:** Uso para control avanzado de atributos y validaciones en los modelos.
- **Manejo de bases de datos relacionales:** Conexión, creación de tablas y operaciones CRUD usando PeeWee.
- **Validación de datos:** Aplicación de expresiones regulares para asegurar la integridad de los datos ingresados.
- **Registro de eventos:** Uso de logging para auditar acciones y facilitar la depuración.
- **Diseño modular:** Separación clara entre lógica de negocio, interfaz y acceso a datos.

---

## 🏗️ Arquitectura y patrón de diseño

El proyecto sigue una arquitectura inspirada en **Modelo-Vista-Controlador (MVC)** y aplica el **Patrón Observador**:

- **Controlador:**  
  `controlador.py` – Orquesta la aplicación, inicializa la interfaz y gestiona el ciclo de vida.
- **Vista:**  
  `vista.py` – Maneja la interfaz gráfica, los widgets y la interacción con el usuario.
- **Modelo:**  
  `modelo.py` – Gestiona la lógica de negocio, la validación y el acceso a la base de datos.
- **Observador:**  
  `observador.py` – Implementa el patrón para notificar a los widgets sobre cambios de tema.
- **Utilidades:**  
  `misRegex.py`, `logger_config.py`, `widgets.py` – Validaciones, configuración de logs y componentes personalizados.

---
## ✨ Funcionalidades principales

- **Gestión de productos:** Alta, baja y modificación de productos cosméticos.
- **Selección de laboratorio y cantidad:** Validación de datos mediante regex.
- **Cambio de temas visuales:** Los widgets y la interfaz se actualizan automáticamente usando el patrón Observador.
- **Soporte multi-base de datos:** Selección dinámica entre SQLite, MySQL y PostgreSQL.
- **Registro de acciones:** Todas las operaciones relevantes quedan registradas en archivos de log y en archivos de texto.
- **Interfaz intuitiva:** Uso de Tkinter y widgets personalizados para una experiencia de usuario amigable.
---
**⚡ David Schmidt ⚡**  
*Desarrollador Python | Explorador de datos | Apasionado por los Pokémon*

