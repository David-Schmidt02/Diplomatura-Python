"""
modelo.py:
    El script almacena toda la lógica relacionada con la interacción con la **base de datos**.
"""
from misRegex import patron_producto, patron_cantidad
import datetime
import re
from peewee import * 
from logger_config import logger_main

"""
Se utiliza el ORM *Peewee*, se especifica como 'default' una base de datos 'SQLite3'.
"""

db = SqliteDatabase("base_productos_sqlite.db")

class BaseModel(Model):
    class Meta:
        database = db

class Producto(BaseModel):
    """
    La clase *Producto* permite crear las instancias de los productos que se almacenarán en la tabla del mismo nombre.
    """
    id = AutoField()
    nombre = CharField()
    cantidad = IntegerField()
    laboratorio = CharField()
    fecha = CharField()

class InteraccionBD():
    """
    La clase *InteraccionBD* permite crear un **objeto** con el cual podemos relacionarnos con la *base de datos*.
    """
    def __init__(self):
        """
        El *constructor*, genera un **objeto** para *conectarse* con la *base de datos* y otro para actualizar el *treeview*.
        """
        self.actualizarTv = Abcm()

    def conectar_base(self,tv):
        """
        Es un botón meramente interactivo, permite conectarnos con la *base de datos* antes de proceder con el *ABCM*.
        """
        try:
            self.actualizarTv.actualizar_treeview(tv)
            return "Se conectó a la base"
        except:
            return "Debe crear la tabla 'Productos'"


    def crear_tabla(self):
        """
        Permite crear la *tabla Productos*, en el caso de que ya esté creada se maneja como una **excepción**.
        """
        if not(Producto.table_exists()):
            db.create_tables([Producto])
            logger_main.info("Se creó la tabla 'Productos'")
            return "Se creó la tabla 'Productos'"
        else:
            return "La tabla 'Productos' ya fue creada"

    def seleccionar_base(self, seleccion):
        """
        Con esta función deberías de poder crear las bases de datos de MySQL y Postgres y a partir de un servidor de estos manipularlas.
        """
        global db
        if seleccion =="SQLite3 (default)":
            db = SqliteDatabase("base_productos_sqlite.db")
        elif seleccion == "MySQL":
            db = MySQLDatabase("base_productos_mysql.db")
        elif seleccion == "Postgres":
            db = PostgresqlDatabase("base_productos_postgres.db")

        print(f"Objeto de la base de datos ubicado en: {db}")
        return f"Se selecciono la base {seleccion}"
            
    
# ABCM------------------------------------------------------------------------
class Abcm():
    def __init__(self):
        pass
    
    def loggear_en_main(function):
        def wrapper(*args, **kwargs):
            logger_main.info(f"Ejecutando la función {function.__name__}")
            return function(*args, **kwargs)
        return wrapper

    @loggear_en_main
    def alta(self, tree, p1, l1, c1):
        """
        **Permite agregar un elemento** luego de rellenar los *entrys*.
        :param tree: Es el *treeview* que contiene todos sus *items*, que luego se **actualizará**. 
        :param valor: Identifica el *item* del *treeview* que deseamos **modificar**.
        """
        self.producto = p1.get()
        self.cantidad = c1.get()
        self.laboratorio = l1.get()
        if re.match(patron_producto, self.producto):
            if re.match(patron_cantidad,self.cantidad):
                self.crear_producto(p1, l1, c1)
                try:
                    self.actualizar_treeview(tree)
                    self.limpiar_datos(p1, l1, c1)
                    return "Se ha agregado: \nProducto: "+ self.producto +"\nLaboratorio:"+ self.laboratorio +"\nCantidad:" + self.cantidad
                except:
                    logger_main.error("Se intentó cargar un producto cuando la tabla no existía")
                    return "La tabla 'Productos' no fue creada"
            else:
                self.limpiar_cantidad(c1)
                logger_main.error("Error en el campo 'Cantidad'")
                return "Error en el campo 'Cantidad'"   
        else:
            self.limpiar_producto(p1)
            logger_main.error("Error en el campo 'Producto'")
            return "Error en el campo 'Producto'" 
        
    def crear_producto(self, p1, l1, c1):
        self.producto = p1.get()
        self.cantidad = c1.get()
        self.laboratorio = l1.get()
        fecha = str(datetime.datetime.today().strftime("%d/%m/%y"))
        alta = Producto()
        alta.nombre = p1.get()
        alta.cantidad = c1.get()
        alta.laboratorio = l1.get()
        alta.fecha = fecha
        alta.save()
        logger_main.info(f"Se agregó el producto {self.producto} a la base de datos")  

    @loggear_en_main
    def baja(self, tree, valor):
        """
        **Elimina un elemento** seleccionado del *treeview*.
        :param tree: Es el *treeview* que contiene todos sus *items*, que luego se **actualizará**. 
        :param valor: Identifica el *item* del *treeview* que deseamos **eliminar**.
        """
        self.item = tree.item(valor)
        self.id_delete = self.item["text"]
        self.producto = self.item['values'][0]
        self.laboratorio = self.item['values'][1]
        self.cantidad = str(self.item['values'][2])
        self.baja = Producto.get(Producto.id == self.id_delete)
        self.baja.delete_instance()
        tree.delete(valor)
        try:
            self.actualizar_treeview(tree)
            logger_main.info(f"Se eliminó el producto {self.producto} de la base de datos")  
            return "Se ha modificado: \nProducto: "+ str(self.producto) +"\nLaboratorio:"+ str(self.laboratorio) +"\nCantidad:" + str(self.cantidad)
        except:
            logger_main.error("Se intentó cargar un producto cuando la tabla no existía")
            return "La tabla 'Productos' no fue creada"
        
    @loggear_en_main
    def modificacion(self,tree, p1, l1, c1, valor):
        """
        **Modifica un elemento** seleccionado del *treeview*.
        :param tree: Es el *treeview* que contiene todos sus *items*, que luego se **actualizará**. 
        :param valor: Identifica el *item* del *treeview* que deseamos **modificar**.
        """
        self.producto = p1.get()
        self.cantidad = c1.get()
        self.laboratorio = l1.get()
        if re.match(patron_producto, self.producto):
            if re.match(patron_cantidad,self.cantidad):
                item = tree.item(valor)
                id_update = item["text"]
                fecha2 = str(datetime.datetime.today().strftime("%d/%m/%y"))
                actualizar = Producto.update(nombre = p1.get(),cantidad = c1.get(),laboratorio = l1.get(), fecha = fecha2).where(Producto.id == id_update)
                actualizar.execute()
                try:
                    self.actualizar_treeview(tree)
                    self.limpiar_datos(p1, l1, c1)
                    logger_main.info(f"Se modificó el producto {self.producto} en la base de datos")
                    return "Se ha modificado: \nProducto: "+ self.producto +"\nLaboratorio:"+ self.laboratorio +"\nCantidad:" + self.cantidad
                except:
                    logger_main.error("Se intentó cargar un producto cuando la tabla no existía")
                    return "La tabla 'Productos' no fue creada"
                
            else:
                self.limpiar_cantidad(c1)
                logger_main.error("Error en el campo 'Cantidad'")
                return "Error en el campo 'Cantidad'"   
        else:
            self.limpiar_producto(p1)
            logger_main.error("Error en el campo 'Producto'")
            return "Error en el campo 'Producto'"
        
    @loggear_en_main    
    def actualizar_treeview(self, tree):
        """
        Elimina todos los elementos del *treeview*, para luego rellenarlo con los elementos de la *base de datos*.
        """
        self.records = tree.get_children()
        try:
            for x in self.records:
                tree.delete(x)
        finally:
            for x in Producto.select():
                tree.insert("", 0, text=x.id, values=(x.nombre, x.cantidad, x.laboratorio,
                                                    x.fecha))  

    @loggear_en_main            
    def cargar_entrys(self, producto, laboratorio, cantidad, id):
        """
        Cuando se selecciona un elemento del *treeview*, se toma su información de la *base de datos* y se rellenan los *entrys* con la misma.
        """
        con = self.conector.conexion()
        cursor = con.cursor()
        data = (id,)
        sql = "SELECT Producto, Laboratorio, Cantidad FROM Productos WHERE id = ?"
        cursor.execute(sql, data)
        resultado = cursor.fetchone()
        con.close()
        if resultado:
            producto.set(resultado[0])
            laboratorio.set(resultado[1])
            cantidad.set(str(resultado[2]))    
        logger_main.info(f"Se cargaron los entrys con el producto {resultado[0]} id {id} de la base de datos")

    @loggear_en_main
    def limpiar_datos(self, producto, combo_laboratorio, cantidad):
        """
        Recibe el contenido de todos los *entry* y el de la *combobox* y los setea en un valor **predeterminado**.
        """
        producto.set("")
        combo_laboratorio.set("")
        cantidad.set("")
        logger_main.info(f"Se limpiaron los entrys")

    @loggear_en_main
    def limpiar_producto(self,producto):
        """
        En el caso de que el nombre del producto no cumpla con la *expresión regular*, se limpiará su *entry*.
        """
        producto.set("")

    @loggear_en_main
    def limpiar_cantidad(self,cantidad):
        """
        En el caso de que la cantidad del producto no cumpla con la *expresión regular*, se limpiará su *entry*.
        """
        cantidad.set("")
