from input_data import *

def choose_sorted() -> bool:
    """
    Permite al usuario elegir el modo de ordenamiento.

    Returns:
        bool: True si se elige el modo de ordenamiento descendente (mayor a menor), False si se elige el modo de ordenamiento ascendente (menor a mayor).
    """
    running = True
    return_value = True
    message = (
            "SELECCIONAR MODO DE ORDENAMIENTO\n"
            "1. Ascendente (Menor a mayor)\n"
            "2. Descendente (Mayor a menor\n"
            "OPCION: "
        )
    while running:
        running = False
        mode = input_int(message)
        if mode == 1:
            return_value = False
        elif mode == 2:
            pass
        else:
            running = True
            print("OPCION NO VALIDA")
    return return_value