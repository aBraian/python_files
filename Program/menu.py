from constants import *
from file_control import *
from games_catalog import *
from input_data import *

def show_options(list_options:list, header:str = "") -> None:
    """
    Muestra las opciones disponibles

    Args:
        list_options (list): Una lista de opciones.
        header (str, optional): Encabezado opcional que se mostrará antes de las opciones. 
            Por defecto, es una cadena vacía.
    """
    if header != "":
        print(header)
    for index, value in enumerate(list_options):
        print(f"{str(index + 1).zfill(2)}. {value}")

def main_menu(games:GameCatalog) -> None:
    """
    Muestra el menú principal y permite interactuar con las opciones.

    Args:
        games (GameCatalog): El catálogo de juegos.
    """
    file_print = GameCatalog()
    while True:
        show_options(MENU_OPTIONS, MENU_HEADER)
        option = input_int("OPCION: ")
        if option == 1:
            print("")
            file_print = games.filter_gender("pelea")
            file_print.print()
            print("")
        elif option == 2:
            print("")
            file_print = games.find_decade(MESSAGE_DECADE)
            file_print.print()
            print("")
        elif option == 3:
            print("")
            mode = choose_sorted()
            file_print = games.bubble_sort(mode)
            file_print.print()
            print("")
        elif option == 4:
            print("")
            file_print = games.search_mode("multijugador", "cooperativo")
            file_print.print()
            print("")
        elif option == 5:
            print("")
            write_csv(CSV_PATH, file_print)
            file_print = GameCatalog()
            print("")
        elif option == 6:
            print("")
            print("Programa cerrado correctamente.")
            break
        else:
            print("")
            print("ERROR. Opcion NO valida.")
            print("")