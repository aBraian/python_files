from constants import *
from file_control import *
from games_catalog import *
from input_data import *
from menu import *

file = read_json(JSON_PATH)

games = GameCatalog()
games.load(file)
list_gender = games.filter_gender("pelea")
list_gender.print()

decade = games.find_decade(MESSAGE_DECADE)

decade.print()

mode = choose_sorted()
order = games.bubble_sort(mode)
order.print()   

print("")
mode_search = games.search_mode("multijugador", "cooperativo")
mode_search.print()

write_csv(CSV_PATH, list_gender)