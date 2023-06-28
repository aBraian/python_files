import json
import re
from games_catalog import *

def read_json(file_name:str) -> list:
    """
    Lee y analiza un archivo JSON que contiene una lista de juegos.
    
    Args:
        file_name (str): El nombre del archivo JSON.
    
    Returns:
        list: Una lista de juegos extraída del archivo JSON.
    """
    if re.search("\.json$", file_name) != None:
        with open(file_name, "r") as file:
            json_file = json.load(file)
            list_games = json_file["games"]
        return list_games

def parser_csv(games:GameCatalog) -> str:
    """
    Genera una representación en formato CSV de los juegos en el catálogo.

    Args:
        games (GameCatalog): El catálogo de juegos.

    Returns:
        str: Una cadena de texto en formato CSV que representa los juegos en el catálogo.
    """
    header = "id, name, platform, mode, company, year, country, gender"
    list_aux = [header]
    for game in games.list_games:
        row = f"{str(game.id_game)}, {game.name}, {game.platform}, {game.mode}, {game.company}, {str(game.year)}, {game.country}, {game.gender}"
        list_aux.append(row)
    file_rows = "\n".join(list_aux)
    return file_rows

def write_csv(file_name:str, games:GameCatalog) -> None:
    """
    Escribe los juegos del catálogo en formato CSV en un archivo.

    Args:
        file_name (str): El nombre del archivo CSV.
        games (GameCatalog): El catálogo de juegos.
    """
    if len(games.list_games) > 0:
        if re.search("\.csv$", file_name):
            with open(file_name, "w") as file:
                file_rows = parser_csv(games)
                file.write(file_rows)
                print("Se creó el archivo:", file.name)