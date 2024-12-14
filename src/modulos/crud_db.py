import sqlite3 as sql
from colorama import init, Fore, Style
init()

#? ------------------- Crea la base de datos 'inventario.db' si no existe. ---------------------------------
def createDB(): #? se crea la DB
    try:
        conn = sql.connect("inventario.db")
        print("Base de datos 'inventario.db' ha sido creada con éxito.")
    except sql.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if conn:
            conn.close()

#? ------------------- Crea la tabla 'productos' en la base de datos 'inventario.db' si no existe. --------------------------------
def create_table():
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conn.commit()
        print("Tabla 'productos' ha sido creada con éxito.")
    except sql.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        if conn:
            conn.close()

#? --------------------------------- REGISTRAR PRODUCTO EN LA DB ------------------------------------------
def registrar_producto(nombre, descripcion, categoria, cantidad, precio):
    try:
        conn = sql.connect("inventario.db")
        instruccion = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)"
        c = conn.cursor()
        c.execute(instruccion, (nombre, descripcion, categoria, cantidad, precio))
        conn.commit()
    except sql.Error as e:
        print(f"Error al registrar el producto: {e}")
    finally:
        if conn:
            conn.close()


#? --------------------------------- BUSCAR UN PRODUCTO POR ID, DEVUELVE UNA LISTA DE UN SOLO PRODUCTO ------------------------------------------

def buscar_producto_por_id(id):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = """
            SELECT *
            FROM productos
            WHERE id = ?
        """
        c.execute(consulta, (id,))
        producto = c.fetchone() #? fetchone() devuelve un producto
        return producto
    except sql.Error as e:
        print(f"Error al buscar el producto: {e }")
    finally:
        if conn:
            conn.close()

#? --------------------------------- BUSCAR UN PRODUCTO POR NOMBRE, DEVUELVE UNA LISTA DE UN SOLO PRODUCTO ------------------------------------------

def buscar_producto_por_nombre(nombre):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = """
            SELECT *
            FROM productos
            WHERE nombre LIKE ?
            ORDER BY nombre, cantidad
        """
        c.execute(consulta, (nombre,))
        producto = c.fetchone() #? fetchone() devuelve un producto
        return producto
    except sql.Error as e:
        print(f"Error al buscar el producto: {e }")
    finally:
        if conn:
            conn.close()

#? --------------------------------- BUSCAR VARIOS PRODUCTOS POR  NOMBRE, DEVUELVE UNA LISTA DE LOS PRODUCTOS ------------------------------------------

def filtrar_productos_por_nombre(nombre):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = """
            SELECT *
            FROM productos
            WHERE nombre LIKE ?
            ORDER BY nombre, cantidad
        """
        c.execute(consulta, (f"%{nombre}%",))
        productos = c.fetchall() #? fetchall() devuelve todos los resultados en una lista.
        return productos
    except sql.Error as e:
        print(f"Error al buscar el producto: {e }")
    finally:
        if conn:
            conn.close()

#? ----------------  FILTRAR PRODUCTOS POR CATEGORIA ------------------------------------------
def filtrar_por_categoria(categoria):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = """
                SELECT *
                FROM productos
                WHERE categoria LIKE ?
                ORDER BY nombre, cantidad
            """
        c.execute(consulta, (f"{categoria}%",))
        productos = c.fetchall()
        return productos
    except sql.Error as e:
        print(f"Error al filtrar productos por categoría: {e}")
        return []
    finally:
        if conn:
            conn.close()

#? --------------------  MOSTRAR TODOS LOS PRODUCTOS ------------------------------------------
def filtrar_todos_los_productos():
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "SELECT * FROM productos"
        c.execute(consulta)
        productos = c.fetchall()
        return productos
    except sql.Error as e:
        print(f"Error al mostrar los productos: {e}")
    finally:
        if conn:
            conn.close()

#? ----------------  MOSTRAR PRODUCTOS CON STOCK BAJO  ------------------------------------------

def mostrar_productos_con_stock_bajo():
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "SELECT * FROM productos WHERE cantidad < 25 ORDER BY cantidad, nombre"
        c.execute(consulta)
        productos = c.fetchall()
        return productos
    except sql.Error as e:
        print(f"Error al mostrar los productos con stock bajo mínimo: {e}")
        return []
    finally:
        if conn:
            conn.close()

#? ----------------  MOSTRAR PRODUCTOS CON STOCK MEDIO ------------------------------------------

def mostrar_productos_con_stock_medio():
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "SELECT * FROM productos WHERE cantidad BETWEEN 25 and 50 ORDER BY cantidad, nombre"
        c.execute(consulta)
        productos = c.fetchall()
        return productos
    except sql.Error as e:
        print(f"Error al mostrar los productos con stock bajo mínimo: {e}")
        return []
    finally:
        if conn:
            conn.close()

#? ----------------  MOSTRAR PRODUCTOS CON STOCK ALTO ------------------------------------------

def mostrar_productos_con_stock_alto():
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "SELECT * FROM productos WHERE cantidad > 50 ORDER BY cantidad, nombre"
        c.execute(consulta)
        productos = c.fetchall()
        return productos
    except sql.Error as e:
        print(f"Error al mostrar los productos con stock bajo mínimo: {e}")
        return []
    finally:
        if conn:
            conn.close()


#? ----------------  ACTUALIZAR CANTIDAD DE STOCK DE UN PRODUCTO ------------------------------------------

def actualizar_stock(id_producto, nueva_cantidad):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "UPDATE productos SET cantidad =? WHERE id =?"
        c.execute(consulta, (nueva_cantidad, id_producto))
        conn.commit()
        print(f"El stock del producto con ID {id_producto} ha sido actualizado a {nueva_cantidad}.")
        return True
    except sql.Error as e:
        print(f"Error al actualizar el stock del producto: {e}")
        return False
    finally:
        if conn:
            conn.close()

#? ----------------  ELIMINAR UN PRODUCTO DE LA BASE DE DATOS ------------------------------------------

def eliminar_producto(id_producto):
    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        consulta = "DELETE FROM productos WHERE id =?"
        c.execute(consulta, (id_producto,))
        conn.commit()
        print(f"El producto con ID {id_producto} ha sido eliminado de la base de datos.")
        return True
    except sql.Error as e:
        print(f"Error al eliminar el producto: {e}")
        return False
    finally:
        if conn:
            conn.close()


#? ---------------- MODIFICAR EL INVENTARIO ------------------------------------------
def modificar_stock_inventario(id_producto, cantidad, transaccion):
    def verificar_stock_bajo(stock_actual):
        """Alertas si el stock es bajo o agotado."""
        if stock_actual == 0:
            print(Fore.RED + Style.BRIGHT + "El producto con ID: " + Fore.WHITE + Style.BRIGHT + f"{id_producto} " + Fore.RED + Style.BRIGHT + "está agotado.")
        elif stock_actual <= 25:
            print(Fore.RED + Style.BRIGHT + f"El producto con ID: " + Fore.WHITE + Style.BRIGHT + f"{id_producto} " + Fore.RED + Style.BRIGHT + "está en stock bajo.")

    if transaccion not in ["entrada", "salida"]:
        print(Fore.RED + Style.BRIGHT + "Transacción inválida. Debe ser 'entrada' o 'salida'.")
        return False
    # Se valida que la cantidad sea positiva
    if cantidad <= 0:
        print(Fore.RED + Style.BRIGHT + "La cantidad debe ser mayor a cero.")
        return False

    try:
        conn = sql.connect("inventario.db")
        c = conn.cursor()
        c.execute("SELECT cantidad FROM productos WHERE id = ?", (id_producto,))
        cantidad_actual = c.fetchone()

        if not cantidad_actual:
            print(Fore.RED + Style.BRIGHT + f"El producto con ID: " + Fore.WHITE + Style.BRIGHT + f"{id_producto} " + Fore.RED + Style.BRIGHT + "no existe.")
            return False

        stock_actual = cantidad_actual[0]

        if transaccion == "entrada":
            nueva_cantidad = stock_actual + cantidad
            consulta = "UPDATE productos SET cantidad = ? WHERE id = ?"
            c.execute(consulta, (nueva_cantidad, id_producto))
            print(Fore.GREEN + Style.BRIGHT + "Se ha registrado una entrada para el producto con ID: " + Fore.WHITE + Style.BRIGHT + f"{id_producto}, " + Fore.GREEN + Style.BRIGHT + "y de Cantidad: " + Fore.WHITE + Style.BRIGHT + f"{cantidad}.")

        elif transaccion == "salida":
            if cantidad > stock_actual:
                print(Fore.RED + Style.BRIGHT + "No se puede realizar la venta del producto. El Stock actual: " + Fore.WHITE + Style.BRIGHT + f"({stock_actual}), " + Fore.RED + Style.BRIGHT + "es insuficiente.")
                return False

            nueva_cantidad = stock_actual - cantidad
            consulta = "UPDATE productos SET cantidad = ? WHERE id = ?"
            c.execute(consulta, (nueva_cantidad, id_producto))
            print(Fore.RED + Style.BRIGHT + f"Se ha registrado una salida para el producto con ID: " + Fore.WHITE + Style.BRIGHT + f"{id_producto}, " + Fore.RED + Style.BRIGHT + "con una Cantidad de: " + Fore.WHITE + Style.BRIGHT + f"{cantidad}." + Style.RESET_ALL)

        # Se Verifica el estado del Stock
        verificar_stock_bajo(nueva_cantidad)

        conn.commit()
        return True

    except sql.Error as e:
        print(Fore.RED + f"Error al registrar la transacción: {e}")
        return False

    finally:
        if conn:
            conn.close()



# createDB()
# create_table()