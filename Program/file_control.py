import json
import re

def read_json(file_name:str) -> list:
    """
    Lee y analiza un archivo JSON que contiene una lista de juegos.
    
    Args:
        file_name (str): El nombre del archivo JSON.
    
    Returns:
        list: Una lista de juegos extraída del archivo JSON.
    """
    if re.search("\.json$", file_name) != None:
        with open(file_name, "r") as archivo:
            json_file = json.load(archivo)
            list_games = json_file["games"]
        return list_games

"""
def write_csv(lista:list, nombre_archivo:str):
    return_value = False
    if re.search("(^.+)\.([a-zA-Z0-9]+$)", nombre_archivo) != None:
        with open(nombre_archivo, "w") as archivo:
            lineas_archivo = "_"
            archivo.write(lineas_archivo)
        if archivo.closed == True:
            print("Se creó el archivo:", archivo.name)
            return_value = True
    if return_value == False: 
        print("Error al crear el archivo:", nombre_archivo)
    return return_value
"""