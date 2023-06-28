import re
from constants import *

def input_int(message:str) -> int:
    """
    Función para ingresar un número entero desde la consola.

    Args:
        message (str): Mensaje que indica la acción a realizar.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    while True:
        answer = input(message)
        if re.match(r"\d+$", str(answer)) != None:
            answer = int(answer)
            break
        else:
            print("ERROR. Ingresar un numero entero")
    return answer

def choose_sorted() -> bool:
    """
    Permite al usuario elegir el modo de ordenamiento.

    Returns:
        bool: True si se elige el modo de ordenamiento descendente (mayor a menor), False si se elige el modo de ordenamiento ascendente (menor a mayor).
    """
    running = True
    return_value = True
    while running:
        running = False
        mode = input_int(MESSAGE_SORT)
        if mode == 1:
            return_value = False
        elif mode == 2:
            pass
        else:
            running = True
            print("OPCION NO VALIDA")
    return return_value