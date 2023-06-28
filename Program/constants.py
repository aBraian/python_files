import os
import re

main_path = os.path.dirname(__file__)

JSON_PATH = os.path.join(main_path, "games_catalog.json")
CSV_PATH = re.sub("\.json$", ".csv", JSON_PATH)

MESSAGE_DECADE = (
    "Decada de 1970\n"
    "Decada de 1980\n"
    "Decada de 2000\n"
    "Decada de 2010\n"
    "Decada de 2020"
)