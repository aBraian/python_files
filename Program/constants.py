import os
import re

main_path = os.path.dirname(__file__)

JSON_PATH = os.path.join(main_path, "games_catalog.json")
CSV_PATH = re.sub("\.json$", ".csv", JSON_PATH)

MESSAGE_DECADE = (
    "DECADAS\n"
    "Decada de 1970\n"
    "Decada de 1980\n"
    "Decada de 2000\n"
    "Decada de 2010\n"
    "Decada de 2020"
)

MESSAGE_SORT = (
    "SELECCIONAR MODO DE ORDENAMIENTO\n"
    "1. Ascendente (Menor a mayor)\n"
    "2. Descendente (Mayor a menor)\n"
    "OPCION: "
)

MENU_OPTIONS = [
    'Listar juegos cuyo género no es "Pelea"',
    'Listar juegos por década',
    'Listar juegos ordenados por "empresa"',
    'Listar juegos modo "COOPERATIVO" - "MULTIJUGADOR"',
    'Exportar a CSV la lista de juegos generada',
    'Salir'
]

MENU_HEADER = "MENU VIDEOJUEGOS"