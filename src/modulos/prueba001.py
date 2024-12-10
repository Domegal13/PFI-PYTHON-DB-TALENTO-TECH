
import os
import re
import crud_db 
from colorama import init, Fore, Style
init()

regex_nombre = r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ][a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ\s\W]*$'     # Expresión Regugal para validar nombres 
lista_productos = []


#? ########################## FUNCTION LIMPIAR CONSOLA #########################################################
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#? ########################## FUNCTION VALIDAR NOMBRE #########################################################
def validar_nombre(nombre):        # Valida que el nombre comience en una letra y tenga entre 2 y 50 caracteres, acepta números y acentos
    
    if len(nombre) < 2 or len(nombre) >= 50:
        return False
    else:
        if re.match(regex_nombre, nombre):
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
    print("1- Registro: Alta de productos nuevos")
    print("2- Visualización: Consulta datos de productos")
    print("3- Actualización: Modificar cantidad de stock del producto")
    print("4- Elimininación: Dar de baja productos")
    print("5- Listado: Listado completo de los productos en la base de datos")
    print("6- Reporte de bajo stock: Lista de productos con cantidad bajo mínimo")
    print("7- Salir\n")


#? ##########################  OPCION 1 - Registro: Alta de productos nuevos ###################################

def agregar_producto():
    nombre_producto = input(Style.RESET_ALL + "\nIntroduzca el nombre del producto: ")
    producto = buscar_producto(nombre_producto)
    if producto:
        print(Fore.RED + "\nEl producto ya existe en la base de datos\n")
        mostrar_menu()
        # return
    else:

        descripción_producto = input(Style.RESET_ALL + "\nIntroduzca la descripción del producto: ")
        cantidad_producto = int(input(Style.RESET_ALL + "\nIntroduzca la cantidad del producto: "))
        precio_producto = float(input(Style.RESET_ALL + "\nIntroduzca el precio del producto: "))

        crud_db.registrar_producto(nombre_producto, descripción_producto, cantidad_producto, precio_producto)


def buscar_producto(nombre):
    producto = crud_db.buscar_producto_por_nombre(nombre) 
    # print(producto)
    if producto is None:
        # print("No se encontró el producto en la base de datos\n")
        return False
    else: 
        return producto  



# prod = buscar_producto("AAsA")
# print(type(prod)) 
# if len(prod) > 0:
#     print(f"{prod}")
# else:
    # print("No hay productos en la base de datos")

# buscar_producto("bbb")
# buscar_producto("ava")
agregar_producto()