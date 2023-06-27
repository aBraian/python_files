import re

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