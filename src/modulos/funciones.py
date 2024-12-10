import os
import re
from . import crud_db
# import crud_db
from colorama import init, Fore, Style
init()

nombre_regex = r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ][a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ\s\W]*$'     # Expresión Regugal para validar nombres
categoria_regex = r"^[a-zA-Z\s]{3,50}$"
descripcion_regex = r"^(|[a-zA-Z0-9\s\.,\-']{1,100})$"


#? ########################## VARIABLES GLOBALES ##############################################################
lista_productos = []


#? ########################## FUNCTION LIMPIAR CONSOLA #########################################################
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#? ########################## FUNCTION VALIDAR NOMBRE #########################################################
def validar_nombre(nombre):        # Valida que el nombre comience en una letra y tenga entre 2 y 50 caracteres, acepta números y acentos
    if len(nombre) < 2 or len(nombre) >= 50:
        return False
    else:
        if re.match(nombre_regex, nombre):
            return True
        else:
            return False

#? ########################## FUNCTION VALIDAR DESCRIPCION #####################################################
def validar_descripcion(descripcion):      # Valida que la descripción tenga entre 10 y 200 caracteres, acepta letras, números, espacios, puntos, comas, guiones medios, y apostrofes
    if len(descripcion) >= 200:
        return False
    else:
        if re.match(descripcion_regex, descripcion):
            return True
        else:
            return False

#? ########################## FUNCTION VALIDAR CATEGORIA #######################################################
def validar_categoria(categoria):      # Valida que la categoría tenga entre 3 y 50 caracteres, acepta letras y espacios
    if len(categoria) < 3 or len(categoria) >= 50:
        return False
    else:
        if re.match(categoria_regex, categoria):
            return True
        else:
            return False

#? ########################## FUNCTION VALIDAR CANTIDAD #######################################################
def validar_cantidad(cantidad):      # Valída que la cantidad ingresada sea mayor a cero
    if cantidad <= 0 :
        print(Fore.RED + "\nLa cantidad debe ser mayor a cero")
        return False
    else:
        return True

#? ########################## FUNCTION VALIDAR PRECIO #######################################################
def validar_precio(precio):      # Valída que la cantidad ingresada sea mayor a cero
    if precio <= 0 :
        print(Fore.RED + "\nEL precio debe ser mayor a cero")
        return False
    else:
        return True

#? ########################## FUNCTION MOSTRAR MENU ###########################################################
def mostrar_menu():
    print( "\n" + Fore.YELLOW +  Style.BRIGHT + " -- Menú de Gestión de Productos --- \n" + Style.RESET_ALL)
    print("1- Registro: " + Fore.LIGHTBLUE_EX + "Alta de productos nuevos" + Style.RESET_ALL)
    print("2- Visualización: " + Fore.LIGHTBLUE_EX + "Consultar datos de todos productos" + Style.RESET_ALL)
    print("3- Actualización: " + Fore.LIGHTBLUE_EX + "Modificar cantidad de stock del producto" + Style.RESET_ALL)
    print("4- Elimininación: " + Fore.LIGHTBLUE_EX + "Dar de baja productos" + Style.RESET_ALL)
    print("5- Listado: " + Fore.LIGHTBLUE_EX + "Listado por Nombre ó Categoria de Productos" + Style.RESET_ALL)
    print("6- Reporte de Stock: " + Fore.LIGHTBLUE_EX + "Lista de productos con cantidad Bajo, Medio, Alto" + Style.RESET_ALL)
    print("7- Salir\n")


#? ########################## FUNCTION BUSCAR PRODUCTO #######################################################
def buscar_producto(nombre):
    producto = crud_db.buscar_producto_por_nombre(nombre)
    if producto is None:
        return False
    else:
        return producto


#? ##########################  OPCION 1 - Registro: Alta de productos nuevos ###################################

def agregar_producto():
    # Pedir y validar el nombre del producto
    nombre_producto = input(Style.RESET_ALL + "\nIntroduzca el nombre del producto: ").upper().strip()
    nombre_validado = validar_nombre(nombre_producto)
    if not nombre_validado:
        print(Fore.RED + "\nEl nombre del producto debe ser una cadena de caracteres válida\n")
        return

    # Comprobar si el producto ya existe en la DB
    producto = buscar_producto(nombre_producto)
    if producto:
        print(Fore.RED + "\nEl producto ya existe en la base de datos\n")
        return

    # Pedir y validar la descripción del producto
    while True:
        descripcion_producto = input(Style.RESET_ALL + "\nIntroduzca la descripción del producto: ").upper().strip()
        descripcion_validada = validar_descripcion(descripcion_producto)
        if descripcion_validada:
            break
        print(Fore.RED + "\nLa descripción debe ser una cadena de caracteres válida\n")

    # Pedir y validar la categoría del producto
    while True:
        categoria_producto = input(Style.RESET_ALL + "\nIntroduzca la categoría del producto: ").upper().strip()
        categoria_validada = validar_categoria(categoria_producto)
        if categoria_validada:
            break
        print(Fore.RED + "\nLa categoría debe ser una cadena de caracteres válida\n")

    # Pedir y validar la cantidad del producto
    while True:
            cantidad_producto = int(input(Style.RESET_ALL + "\nIntroduzca la cantidad del producto: "))
            cantidad_validada = validar_cantidad(cantidad_producto)
            if cantidad_validada:
                break
            else:
                print(Fore.RED + "\nLa cantidad debe ser un número entero mayor a cero\n")

    # Pedir y validar el precio del producto
    while True:
            precio_producto = float(input(Style.RESET_ALL + "\nIntroduzca el precio del producto: "))
            precio_validado = validar_precio(precio_producto)
            if precio_validado:
                break
            else:
                print(Fore.RED + "\nEl precio debe ser mayor a cero\n")

    # Registrar el producto
    crud_db.registrar_producto(nombre_producto, descripcion_producto, categoria_producto, cantidad_producto, precio_producto)
    print(Fore.GREEN + "\nProducto registrado correctamente\n")



#? ##########################  OPCION 2 - Visualización: Consulta datos de productos ###################################

def filtar_productos():
    productos = crud_db.filtrar_todos_los_productos()
    if len(productos) < 1:
        print(Fore.RED + "\nNo hay productos registrados en la base de datos\n ")
        return
    print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS -----------------------\n")
    print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
    print(Fore.YELLOW + "-------------------------------------------------")
    for producto in productos:
        print(Fore.YELLOW + f"{producto[0]}  | " + Fore.WHITE + f"{producto[1]}" + Fore.WHITE + " | " + Fore.MAGENTA + f"{producto[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{producto[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{producto[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{producto[5]}")
        print(Fore.YELLOW + "-------------------------------------------------")


#? ##########################  OPCION 3 - Actualización: Modificar cantidad de stock del producto ###################################

#! ####################################### MENU STOTK ######################################################
def mostrar_menu_stock():
    print(Fore.YELLOW + Style.BRIGHT + "\n--- Menú Modificar Stock ---")
    print(Fore.YELLOW +  Style.BRIGHT + "\n1- Aumentar Stock")
    print("2- Disminuir Stock")
    print("3- Salir")

#! #######################################  AUMENTAR EL STOCK ##############################################
def aumentar_stock():
    try:
        nombre_producto = input(Style.RESET_ALL + "\nIntrozca el nombre del producto: ")
        nombre_producto = nombre_producto.upper().strip()
        nombre_validado = validar_nombre(nombre_producto)
        if nombre_validado :
            bandera=True
            for producto in lista_productos:
                if nombre_producto == producto[0]:
                    bandera=False
                    cantidad_producto = int(input("intruduzca la cantidad a ingresar: "))
                    cantidad_validada = validar_cantidad(cantidad_producto)
                    if cantidad_validada:
                        producto[1] += cantidad_producto
                        break
            if bandera:        # Verifica que el nombre ingresado no se encuentre en la lista_productos
                print(Fore.RED + Style.BRIGHT + "\nEl producto: " + Fore.WHITE + f"{nombre_producto}" + Fore.RED + Style.BRIGHT +  " no existe..." + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "\nIntroduzca un nombre de producto correcto" + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nLa cantidad debe ser numérica" + Style.RESET_ALL)

#! ####################################### DISMINUIR EL STOCK ##############################################
def disminuir_stock():
    try:
        nombre_producto = input(Style.RESET_ALL + "\nIntroduzca el nombre del producto: ")
        nombre_producto = nombre_producto.upper().strip()
        nombre_validado = validar_nombre(nombre_producto)
        if nombre_validado :
            bandera=True
            for producto in lista_productos:
                if nombre_producto == producto[0]:
                    bandera=False
                    cantidad_producto = int(input("Introduzca la cantidad a disminuir: "))
                    cantidad_validada = validar_cantidad(cantidad_producto)
                    if cantidad_validada:
                        if cantidad_producto > producto[1]:
                            print(Fore.RED + "\nLa cantidad debe ser menor que la cantidad del Stock" + Style.RESET_ALL)
                            break
                        else:
                            producto[1] -= cantidad_producto
                            break
            if bandera:   # Verifica que el nombre ingresado no se encuentre en la lista_productos
                print(Fore.RED + Style.BRIGHT + "\nEl producto: " + Fore.WHITE + f"{nombre_producto}" + Fore.RED + Style.BRIGHT +  " no existe..." + Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "\nIntroduzca un nombre de producto correcto")
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nLa cantidad debe ser numérica")

#! ####################################### SWITCH CASE MODIFICAR STOCK #####################################
def switch_case_stock(opc):
    match(opc):
        case 1:
            aumentar_stock()
        case 2:
            disminuir_stock()
        case 3:
            print(Fore.YELLOW + Style.BRIGHT + "\nSaliendo de Modificar Stock" + Style.RESET_ALL)
        case _:
            print(Fore.RED + Style.BRIGHT + "\nOpción inválida..." + Style.RESET_ALL)

#! ####################################### FUNCTION MODIFICAR STOCK ########################################
def modificar_stock():
    opc = 0
    while opc != 3:
        mostrar_menu_stock()
        try:
            opc = int(input(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una opción 1-3: "))
            switch_case_stock(opc)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nOpción Inválida...")

    limpiar_consola()



#? ##########################  OPCION 4 -  Elimininación: Dar de baja productos #########################################################
def eliminar_producto():
    try:
        producto_id = int(input(Fore.YELLOW + "\n Introduzca el Id del Producto a eliminar: " + Style.RESET_ALL))
        filtrar_x_id = crud_db.buscar_producto_por_id(producto_id)
        print(filtrar_x_id)
        if filtrar_x_id == None:
            print(Fore.RED + Style.BRIGHT + "\nProducto no encontrado..." + Style.RESET_ALL)
            return
        id_producto = filtrar_x_id[0]
        nombre_producto = filtrar_x_id[1]
        resp = input(Fore.LIGHTMAGENTA_EX + "\nEstá seguro de elimiar el producto con " + Fore.BLUE + Style.BRIGHT + f"Id: {id_producto} Nombre: {nombre_producto}" + Fore.LIGHTMAGENTA_EX  + " - S/N:") 
        if resp == "S" or resp == "s":
            producto_a_eliminar = crud_db.eliminar_producto(producto_id)
            if producto_a_eliminar:
                print(Fore.WHITE + "\nEl Producto " + Fore.GREEN + f"Id: {id_producto} Nombre: {nombre_producto}" + Fore.WHITE  + " ha sido eliminado...\n" + Style.RESET_ALL )
        else:
            print(Fore.RED + Style.BRIGHT + "\nEliminación cancelada..." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nLa cantidad debe ser numérica")




#? ##########################  OPCION 5 - Listado: Listado completo de los productos en la base de datos ###################################

#! ####################################### MOSTRAR MENU FILTRAR STOTK ######################################################
def mostrar_menu_ordenar_stock():
        print(Fore.YELLOW + Style.BRIGHT + "\n--- Menú Filtrar Stock ---")
        print(Fore.YELLOW +  Style.BRIGHT + "\n1- Filtrar por nombre")
        print("2- Filtrar por Categoria")
        print("3- Salir" + Style.RESET_ALL)

#! ####################################### FILTRAR STOTK POR NOMBRE ######################################################

def mostrar_un_producto():
    nombre_producto = input(Fore.YELLOW + "\nIntroduzca el nombre del producto a buscar: ")
    nombre_producto = nombre_producto.upper().strip()
    productos = crud_db.filtrar_productos_por_nombre(nombre_producto)
    if len(productos) < 1:
        print(Fore.RED + "\nNo se encontró el producto en la base de datos\n ")
    else:
        print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS POR NOMBRE -----------------------\n")
        print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
        print(Fore.YELLOW + "----------------------------------------------------------------")
        for producto in productos:
            print(Fore.YELLOW + f"{producto[0]}  | " + Fore.WHITE + f"{producto[1]}" + Fore.WHITE + " | " + Fore.MAGENTA + f"{producto[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{producto[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{producto[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{producto[5]}")
            print(Fore.YELLOW + "----------------------------------------------------------------")


#! ####################################### ORDENAR STOTK POR CATEGORIA ######################################################
def ordenar_por_categoria():
    categoria = input(Fore.YELLOW + "\nIntroduzca la Categoría a buscar: " + Style.RESET_ALL)
    categoria = categoria.upper().strip()
    productos_x_categoria = crud_db.filtrar_por_categoria(categoria)
    if len(productos_x_categoria) > 0:
        print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS POR CATEGORIA -----------------------\n")
        print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
        print(Fore.YELLOW + "----------------------------------------------------------------")
        for producto in productos_x_categoria:
            print(Fore.YELLOW + f"{producto[0]}  | " + Fore.WHITE + f"{producto[1]}" + Fore.YELLOW + " | " + Fore.MAGENTA + f"{producto[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{producto[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{producto[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{producto[5]}")
            print(Fore.YELLOW + "----------------------------------------------------------------")
    else:
        print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")

#! ####################################### SWITCH MENU ORDENAR STOTK ######################################################
def switch_menu_ordenar_stock(opcion):
        match(opcion):
            case 1:
                limpiar_consola()
                mostrar_un_producto()
            case 2:
                limpiar_consola()
                ordenar_por_categoria()
            case 3:
                print(Fore.WHITE + "\nSaliendo de ordenar Stock" + Style.RESET_ALL)
            case _:
                print(Fore.RED + Style.BRIGHT + "\nOpción inválida..." + Style.RESET_ALL)

#! ####################################### FUNCTION MOSTRAR PRODUCTOS ######################################################
def mostrar_productos():
    opc = 1000
    while opc != 3:
        mostrar_menu_ordenar_stock()
        try:
            opc = int(input(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una opción 1-3: "))
            switch_menu_ordenar_stock(opc)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nOpción Inválida...")



#? ##########################  OPCION 6 - Reporte de bajo stock: Lista de productos con cantidad bajo mínimo ###################################

#! ######################################### MOSTRAR MENU DE REPORTE DE STOCK ####################################################
def mostrar_menu_reporte_stock():
    print(Fore.YELLOW +  Style.BRIGHT + "\n1- Stock Bajo")
    print("2- Stock Medio")
    print("3- Stock Alto")
    print("4- Salir" +  Style.RESET_ALL)

#! ######################################### REPORTE DE STOCK ####################################################
def reporte_stock(opc):
    if opc == 1:
        limpiar_consola()
        lista_stock_bajo = crud_db.mostrar_productos_con_stock_bajo()
        if len(lista_stock_bajo) > 0:
            print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS STOCK BAJO -----------------------\n")
            print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
            print(Fore.YELLOW + "----------------------------------------------------------------")
            for bajo in lista_stock_bajo:
                print(Fore.YELLOW + f"{bajo[0]}  | " + Fore.WHITE + f"{bajo[1]}" + Fore.WHITE + " | " + Fore.MAGENTA + f"{bajo[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{bajo[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{bajo[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{bajo[5]}")
            print(Fore.YELLOW + "\n----------------------------------------------------------------")
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")
    elif opc == 2:
        limpiar_consola()
        lista_stock_medio = crud_db.mostrar_productos_con_stock_medio()
        if len(lista_stock_medio) > 0:
            print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS STOCK MEDIO -----------------------\n")
            print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
            print(Fore.YELLOW + "----------------------------------------------------------------")
            for medio in lista_stock_medio:
                print(Fore.YELLOW + f"{medio[0]}  | " + Fore.WHITE + f"{medio[1]}" + Fore.WHITE + " | " + Fore.MAGENTA + f"{medio[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{medio[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{medio[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{medio[5]}")
            print(Fore.YELLOW + "\n----------------------------------------------------------------")
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")
    elif opc == 3:
        limpiar_consola()
        lista_stock_alto = crud_db.mostrar_productos_con_stock_alto()
        if len(lista_stock_alto) > 0:
            print(Fore.YELLOW + "\n----------------------- LISTADO DE PRODUCTOS STOCK ALTO-----------------------\n")
            print(Fore.YELLOW + "ID | " + Fore.WHITE + " Producto " + Fore.YELLOW + " | " + Fore.MAGENTA + " Descripción " + Fore.YELLOW + " | " + Fore.WHITE + " Categoría " + Fore.YELLOW + " | " + Fore.BLUE + " Stock " + Fore.YELLOW + " | " + Fore.GREEN + " Precio \n")
            print(Fore.YELLOW + "----------------------------------------------------------------")
            for alto in lista_stock_alto:
                print(Fore.YELLOW + f"{alto[0]}  | " + Fore.WHITE + f"{alto[1]}" + Fore.WHITE + " | " + Fore.MAGENTA + f"{alto[2]}" + Fore.YELLOW + " | " + Fore.WHITE + f"{alto[3]}" + Fore.YELLOW + " | " + Fore.BLUE + f"{alto[4]}" + Fore.YELLOW + " | " + Fore.GREEN + f"{alto[5]}")
            print(Fore.YELLOW + "----------------------------------------------------------------")
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")
    elif opc == 4:
        print(Fore.YELLOW + Style.BRIGHT + "\nSaliendo del Reporte de Stock..." + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "\nOpción inválida..." + Style.RESET_ALL)

#! ######################################### REPORTE DE PRODUCTOS ####################################################
def mostrar_reporte_productos():
    opc = 0
    while opc != 4:
        print(Fore.YELLOW + Style.BRIGHT + "\nMostrar Stock")
        mostrar_menu_reporte_stock()
        try:
            opc = int(input(Fore.YELLOW + Style.BRIGHT + "\nSeleccione una opción 1-4: "))
            reporte_stock(opc)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nOpción Inválida...")

    limpiar_consola()



#? ##########################   SWITCH CASE OPTIONS MAIN ######################################################################
def menu_switch_case(opcion_seleccionada):
        match opcion_seleccionada:
            case 1:
                limpiar_consola()
                agregar_producto()
            case 2:
                limpiar_consola()
                filtar_productos()
            case 3:
                limpiar_consola()
                modificar_stock()
            case 4:
                limpiar_consola()
                eliminar_producto()
            case 5:
                limpiar_consola()
                mostrar_productos()
            case 6:
                limpiar_consola()
                mostrar_reporte_productos()
            case 7:
                print(Style.RESET_ALL + "Saliendo del Sistema, gracias... \n")
            case _:
                print(Fore.RED + Style.BRIGHT + "La opcion seleccionada es inválida: \n")


#? --------------------------------------------------------------------

if __name__ == "__main__":
    limpiar_consola()