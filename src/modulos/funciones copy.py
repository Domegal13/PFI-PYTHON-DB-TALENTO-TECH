import os
import re
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
    nombre_producto = nombre_producto.upper().strip()   # Se pasa el nombre a mayúsculas y se eliminan los espacios adelante y atrás
    nombre_validado = validar_nombre(nombre_producto)
    if nombre_validado :
            for producto in lista_productos:
                if nombre_producto == producto[0]:
                    print(Fore.YELLOW + f"El producto {producto[0]} ya existe...")
                    break
            else:
                try:
                    cantidad_producto = int(input("introduzca la cantidad: "))
                    cantidad_validada = validar_cantidad(cantidad_producto)
                    if cantidad_validada :
                        lista_productos.append([nombre_producto, cantidad_producto])
                        print(Fore.GREEN + Style.BRIGHT + "\nProducto agregado exitosamente...")
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "\nLa cantidad debe ser numérica")
    else:
        print(Fore.RED + Style.BRIGHT + "\nIntroduzca un nombre de producto correcto\n")
        agregar_producto()


#? ##########################  OPCION 2 - Visualización: Consulta datos de productos ###################################
def mostrar_un_producto():
    nombre_producto = input(Fore.YELLOW + "\nIntroduzca el nombre del producto a buscar: ")
    nombre_producto = nombre_producto.upper()
    for producto in lista_productos:       
        if nombre_producto == producto[0]:
            print(Fore.YELLOW + "\n-----------------------------------\n")
            print(Fore.LIGHTGREEN_EX + f"{producto[0]}" + Fore.YELLOW + " --Stock:" + Fore.GREEN +  f"  {producto[1]}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n-----------------------------------")
            break
    else:
        print(Fore.RED + Style.BRIGHT + f"El producto {nombre_producto}, no existe...")


            
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
    nombre_producto = input(Fore.YELLOW + "\n Introduzca el Producto a eliminar: " + Style.RESET_ALL)
    nombre_producto = nombre_producto.upper()
    validar_nombre(nombre_producto)
    if validar_nombre:
        for producto in lista_productos:           
            if nombre_producto == producto[0]:
                resp = input(Fore.LIGHTMAGENTA_EX + "\nEstá seguro de elimiar el producto: " + Fore.BLUE + Style.BRIGHT + f"{nombre_producto}" + Fore.LIGHTMAGENTA_EX  + " - S/N:")
                if resp == "S" or resp == "s":
                    # producto_eliminado = lista_productos.remove(producto)
                    print(Fore.WHITE + "\nEl Producto " + Fore.GREEN + f"{nombre_producto}" + Fore.WHITE  + " ha sido eliminado...\n" + Style.RESET_ALL )
                    break
                else:
                    break
        else:
            print(Fore.RED + Style.BRIGHT + "\nProducto no encontrado..." + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "\nIntroduzca un valor correcto..." + Style.RESET_ALL)



#? ##########################  OPCION 5 - Listado: Listado completo de los productos en la base de datos ###################################

#! ####################################### MOSTRAR MENU ORDENAR STOTK ######################################################
def mostrar_menu_ordenar_stock(): 
        print(Fore.YELLOW + Style.BRIGHT + "\n--- Menú Ordenar Stock ---")  
        print(Fore.YELLOW +  Style.BRIGHT + "\n1- Ordenar por nombre")
        print("2- Ordenar por cantidad")
        print("3- Salir" + Style.RESET_ALL)

#! ####################################### ORDENAR STOTK POR NOMBRE ######################################################
def ordenar_por_nombre():
        if len(lista_productos) > 0:
            lista_productos.sort()
            print(Fore.YELLOW + "\n-----------------------------------")
            print(Fore.YELLOW + "\nLista de Productos por Nombre")
            for nombre in lista_productos:
                print(Fore.LIGHTGREEN_EX + f"{nombre[0]}" + Fore.YELLOW + " --Stock:" + Fore.GREEN +  f"  {nombre[1]}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n-----------------------------------")
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar") 

#! ####################################### ORDENAR STOTK POR CANTIDAD ######################################################
def ordenar_por_cantidad():
        if len(lista_productos) > 0:
            lista_productos.sort(key=lambda prod: prod[1])
            print(Fore.YELLOW + "\n-----------------------------------")
            print(Fore.YELLOW + "\nLista de Productos por Cantidad")
            for nombre in lista_productos:
                print(Fore.LIGHTGREEN_EX + f"{nombre[0]}" + Fore.YELLOW + " --Stock:" + Fore.GREEN +  f"  {nombre[1]}" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n-----------------------------------")
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar") 

#! ####################################### SWITCH MENU ORDENAR STOTK ######################################################
def switch_menu_ordenar_stock(opcion):
        match(opcion):
            case 1:
                limpiar_consola()
                ordenar_por_nombre()
            case 2:
                limpiar_consola()
                ordenar_por_cantidad()
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
    print(Fore.YELLOW +  Style.BRIGHT + "\n1- Stock Alto")
    print("2- Stock Medio")
    print("3- Stock Bajo")
    print("4- Salir" +  Style.RESET_ALL)

#! ######################################### REPORTE DE STOCK ####################################################
def reporte_stock(opc): 
    lista_stock_alto = []
    lista_stock_medio = []
    lista_stock_bajo = []
    if len(lista_productos) > 0:
        for producto in lista_productos:
            if producto[1] >= 20:
                lista_stock_alto.append([producto[0], producto[1]])
            elif 10 <= producto[1] < 20:
                lista_stock_medio.append([producto[0], producto[1]])
            elif producto[1] < 10:
                lista_stock_bajo.append([producto[0], producto[1]])
    else:
        print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")  

    if opc == 1:
        limpiar_consola()
        print(Fore.YELLOW + "\n-----------------------------------")          
        print(Fore.YELLOW + "\nLista de Productos\n")
        if len(lista_stock_alto) > 0:
            for alto in lista_stock_alto:
                print(Fore.LIGHTGREEN_EX + f"{alto[0]}" + Fore.WHITE + f" Stock: {alto[1]}" + Fore.LIGHTBLUE_EX + "  -- Stock Alto" + Style.RESET_ALL)   
            print(Fore.YELLOW + "\n-----------------------------------")   
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")  
    elif opc == 2:
        limpiar_consola()    
        print(Fore.YELLOW + "\n-----------------------------------")
        print(Fore.YELLOW + "\nLista de Productos\n")
        if len(lista_stock_medio) > 0:
            for medio in lista_stock_medio:
                print(Fore.LIGHTGREEN_EX + f"{medio[0]}" + Fore.WHITE+ f" Stock: {medio[1]}" + Fore.YELLOW + "  -- Stock Medio" + Style.RESET_ALL)   
            print(Fore.YELLOW + "\n-----------------------------------")   
        else:
            print(Fore.RED + Style.BRIGHT + "\nNo hay productos para mostrar")   
    elif opc == 3:
        limpiar_consola()
        print(Fore.YELLOW + "\n-----------------------------------")
        print(Fore.YELLOW + "\nLista de Productos\n")
        if len(lista_stock_bajo) > 0:
            for bajo in lista_stock_bajo:        
                print(Fore.LIGHTGREEN_EX + f"{bajo[0]}" + Fore.WHITE + f" Stock: {bajo[1]}" + Fore.RED + "  -- Stock Bajo" + Style.RESET_ALL)
            print(Fore.YELLOW + "\n-----------------------------------")
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
                mostrar_un_producto()
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
