from src.modulos.funciones import mostrar_menu, menu_switch_case, limpiar_consola
from src.modulos.crud_db import createDB, create_table
from colorama import init, Fore, Style
init()


createDB()
create_table()

#? ########################################### FUNCTION MAIN ##################################################################
def funcion_main():
    opcion_seleccionada = 1000
    while opcion_seleccionada != 7:
        mostrar_menu()
        try:
            opcion_seleccionada = int(input(Fore.GREEN + Style.BRIGHT + "Por favor, selecciona una opción (1-7): "  ))
            menu_switch_case(opcion_seleccionada)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Opción Inválida...")

#? ########################################### EXECUTE MAIN ##################################################################
if __name__ == "__main__":
    funcion_main()
    limpiar_consola()
    print(Fore.YELLOW + Style.BRIGHT + "Saliendo del programa..." + Style.RESET_ALL)