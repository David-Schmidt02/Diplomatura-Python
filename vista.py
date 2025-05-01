"""
vista.py:
    El script almacena todo lo relacionado con la interfaz gráfica Tkinter.
"""
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox

from modelo import Abcm
from modelo import InteraccionBD

from widgets import MiBoton, MiEntry, MiLabel

from observador import Subject

objeto = Abcm()
objetoBase = InteraccionBD()

from logger_config import logger_main, logger_bd

class Vista():
    def __init__(self,window, gestor_tema):
        self.widgets = []
        """
        El constructor inicializa el *root* de tkinter y lo configuro, con su *título*, *background*, *buttons*, *treeview*, *labels*, una *combobox* y los *entrys*.
        """
        self.root = window
        self.root.title("PS COSMÉTICA")
        self.root.resizable(0, 0)
        self.root.config(bg="#F0C266")
        self.gestor_tema = gestor_tema
        
        # BASE DE DATOS Y TABLA----------------------------------------------------------------
        """
        El botón: *boton_db* permite conectarse a la *base de datos* previamente a realizar cualquier acción.
        """
        self.boton_db = MiBoton(
            self.root,
            text="Conectarse a la Base de Datos",
            command=lambda:self.conectar_base(),
            gestor_tema=self.gestor_tema,
        )
        self.boton_db.grid(column=1, row=1)
        self.widgets.append(self.boton_db)
        """
        El boton: *boton_table* permite crear la tabla *Productos* en la *base de datos*.
        """
        self.boton_table = MiBoton(
            self.root,
            text="Crear Tabla Productos",
            command=lambda:self.crear_tabla(),
            gestor_tema=gestor_tema,
        )
        self.boton_table.grid(column=2, row=1)
        self.widgets.append(self.boton_table)

        # INGRESO DE DATOS------------------------------------------------------------------------
        self.labe1_p = MiLabel(self.root, text="Producto:", gestor_tema=self.gestor_tema)
        self.labe1_p.grid(row=2)
        self.widgets.append(self.labe1_p)
        self.combo = ttk.Combobox(
            state="readonly",
            values=[
                "LIDHERMA",
                "EXEL",
                "IDRAET",
                "AP",
                "COLONY",
                "ZINE",
            ],
        )
        self.combo.grid(column=2, row=3, padx=5, pady=5, sticky="w")
        self.labe1_l = MiLabel(self.root, text="Laboratorio:", gestor_tema=self.gestor_tema)
        self.labe1_l.grid(row=3)
        self.widgets.append(self.labe1_l)

        self.labe1_c = MiLabel(self.root, text="Cantidad:", gestor_tema=self.gestor_tema)
        self.labe1_c.grid(row=4)
        self.widgets.append(self.labe1_c)

        self.producto = StringVar()
        self.laboratorio = StringVar()
        self.cantidad = StringVar()

        self.producto_e = MiEntry(self.root, textvariable=self.producto, gestor_tema=self.gestor_tema)
        self.producto_e.grid(column=2, row=2)
        self.widgets.append(self.producto_e)

        self.cantidad_e = MiEntry(self.root, textvariable=self.cantidad, gestor_tema=self.gestor_tema)
        self.cantidad_e.grid(column=2, row=4)
        self.widgets.append(self.cantidad_e)
        # TREEVIEW------------------------------------------------------------------------
        """
        Se configura el *treeview*, especificando su número de *columnas* (y el nombre de estas) así como sus *títulos*
        """
        self.tv = ttk.Treeview(self.root, columns=("col1", "col2", "col3", "col4"))
        self.tv.column("#0", anchor="w", width=80, minwidth=80)
        self.tv.heading("#0", text="id")
        self.tv.column("col1", anchor="w", width=80, minwidth=80)
        self.tv.heading("col1", text="Producto")
        self.tv.column("col2", anchor="w", width=80, minwidth=80)
        self.tv.heading("col2", text="Laboratorio")
        self.tv.column("col3", anchor="w", width=80, minwidth=80)
        self.tv.heading("col3", text="Cantidad")
        self.tv.column("col4", anchor="w", width=80, minwidth=80)
        self.tv.heading("col4", text="Fecha")
        self.tv.grid(column=0, row=6, columnspan=5)

        #Se activa la funcion seleccion cada vez que se selecciona en el tv 
        self.tv.bind("<<TreeviewSelect>>", self.seleccion) 
        
        """
        El boton: *boton1* permite realizar el *alta* de productos.
        """
        self.boton1 = MiBoton(
            self.root, 
            text="Alta",
            command=lambda: self.alta(),
            gestor_tema=self.gestor_tema)
        self.boton1.grid(column=0,row=2)
        self.widgets.append(self.boton1)
        """
        El boton: *boton2* permite realizar la *baja* de productos.
        """
        self.boton2 = MiBoton(
            self.root,
            text="Baja",
            command=lambda: self.baja(),
            gestor_tema=self.gestor_tema
        )
        self.boton2.grid(column=0,row=3)
        self.widgets.append(self.boton2)
        """
        El boton: *boton3* permite realizar la *modificación* de productos.
        """
        self.boton3 = MiBoton(
            self.root,
            text="Modificación",
            command=lambda: self.modificacion(),
            gestor_tema=self.gestor_tema
        )
        self.boton3.grid(column=0,row=4,)
        self.widgets.append(self.boton3)
        """
        La combobox: *combo_temas* permite seleccionar los *temas* de la aplicación.
        """
        #Combobox para modificar los temas:
        self.combo_temas = ttk.Combobox(
            state="readonly",
            values=[
                "Crema (default)",
                "Light",
                "Black",
            ],
        )
        self.combo_temas.bind("<<ComboboxSelected>>", self.cambiar_tema)
        self.combo_temas.grid(column=0, row=1, padx=5, pady=5, sticky="w")

        """
        La combobox: *combo_bases* permite seleccionar la *base de datos* a utilizar.
        """
        #Combobox para modificar las bases:
        self.combo_bases = ttk.Combobox(
            state="readonly",
            values=[
                "SQLite3 (default)",
                "MySQL",
                "Postgres"
            ],
        )
        self.combo_bases.bind("<<ComboboxSelected>>", self.cambiar_base)
        self.combo_bases.grid(column=0, row=5, padx=5, pady=5, sticky="w")

    def loggear_en_bd(funcion):
        def envoltura(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            logger_bd.info(f"Acción: {funcion.__name__} ejecutada por el usuario")
            if funcion.__name__=="alta" or funcion.__name__=="baja"or funcion.__name__=="modificacion":
                logger_bd.info(f"Producto: {resultado[0]}")
                logger_bd.info(f"Laboratorio: {resultado[1]}")
                logger_bd.info(f"Cantidad: {resultado[2]}")
            elif funcion.__name__=="conectar_base":
                logger_bd.info(f"Conexión a la base de datos")
            elif funcion.__name__=="crear_tabla":
                logger_bd.info(f"Creación de la tabla 'Productos'")
            return resultado
        
        return envoltura
    
    @loggear_en_bd
    def cambiar_base(self, event=None):
        seleccion = self.combo_bases.get()
        retorno = objetoBase.seleccionar_base(seleccion)
        logger_main.info(f"Se seleccionó la base: {seleccion}")
        messagebox.showinfo("Base de datos", retorno)
    # ------------------------------------------------------------------------

    def cambiar_tema(self, event=None):
        """
        La función *cambiar_tema* permite que, utilizando **polimorfismo** en los distintos *widgets*, los modifiquemos según el *tema* seleccionado.
        """
        seleccion = self.combo_temas.get()
        logger_main.info(f"Se seleccionó el tema: {seleccion}")
        self.modificar_root(seleccion)
        # Se le pasa el tema al gestor de temas para que lo modifique en todos los widgets 
        self.gestor_tema.cambiar_tema(seleccion)
        """for x in self.widgets:
            x.modificar(seleccion)
        """
    def modificar_root(self, seleccion):
        if seleccion == "Crema (default)":
            self.root.config(bg="#F0C266",)
        elif seleccion == "Light":
            self.root.config(bg="#B7EEE3")
        elif seleccion == "Black":
            self.root.config(bg="#1A1E48")
        
    def seleccion(self, event):
        """
        La funcion *seleccion* permite que los *entrys* se rellenen con la información de la *base de datos* correspondiente al elemento seleccionado del *treeview*.
        """    
        valor = self.tv.selection()
        item = self.tv.item(valor)
        id = item["text"]
        objeto.cargar_entrys(self.producto,self.combo,self.cantidad,id)


    # ABCM------------------------------------------------------------------------
    @loggear_en_bd
    def alta(self):
        """
        La función "alta" de "vista.py" invoca a la funcion "alta" del **objeto** creado previamente, y espera su retorno para mostrarlo en un *messagebox*.
        """
        retorno = objeto.alta(self.tv, self.producto, self.combo, self.cantidad)
        messagebox.showinfo("Alta", retorno)
        return (self.producto.get(), self.combo.get(), self.cantidad.get())
    @loggear_en_bd
    def baja(self):
        """
        La función "baja" de "vista.py" invoca a la funcion "baja" del **objeto** creado previamente, y espera su retorno para mostrarlo en un *messagebox*.
        """
        valor = self.tv.selection()  
        if valor: 
            resultado = messagebox.askquestion("Baja", "¿Estas seguro de querer eliminar este producto?")
            if resultado == "yes":
                retorno = objeto.baja(self.tv, valor)
                messagebox.showinfo("Baja", retorno[0])
            else:
                messagebox.showinfo("Acción cancelada", "No se eliminó el producto")
        else:
            messagebox.showinfo("Acción cancelada", "Debe seleccionar un producto a eliminar")
        return retorno[1], retorno[2], retorno[3]
    @loggear_en_bd
    def modificacion(self):
        """
        La función "modificacion" de "vista.py" invoca a la funcion "modificacion" del **objeto** creado previamente, y espera su retorno para mostrarlo en un *messagebox*.
        """
        valor = self.tv.selection()
        if valor:
            resultado = messagebox.askquestion("Modificación", "¿Estas seguro de querer modificar este producto?")
            if resultado == "yes":
                retorno = objeto.modificacion(self.tv, self.producto, self.combo, self.cantidad,valor)
                messagebox.showinfo("Modificación", retorno[0])
            else:
                messagebox.showinfo("Acción cancelada", "No se modificó el producto")
        else:
            messagebox.showinfo("Acción cancelada", "Debe seleccionar un producto a modificar")
        return retorno[1], retorno[2], retorno[3]
    # ------------------------------------------------------------------------
    @loggear_en_bd    
    def conectar_base(self):
        """
        La función "conectar_base" de "vista.py" invoca a la funcion "conectar_base" del **objeto** creado previamente, y espera su retorno para mostrarlo en un *messagebox*.
        """
        retorno = objetoBase.conectar_base(self.tv) 
        messagebox.showinfo("Base de Datos", retorno)
    @loggear_en_bd
    def crear_tabla(self):
        """
        La función "crear_tabla" de "vista.py" invoca a la funcion "crear_tabla" del **objeto** creado previamente, y espera su retorno para mostrarlo en un *messagebox*.
        """
        retorno = objetoBase.crear_tabla()
        messagebox.showinfo("Tabla 'Productos'", retorno)


