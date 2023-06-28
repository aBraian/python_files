from constants import *
from file_control import *
from games_catalog import *
from input_data import *
from menu import *

file = read_json(JSON_PATH)
games = GameCatalog()
games.load(file)

main_menu(games)