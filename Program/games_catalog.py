import re
from game import *
from input_data import *
        
class GameCatalog:
    
    class_type = "GameCatalog"
    
    def __init__(self) -> None:
        """
        Constructor de la clase Games. 
        """
        self.list_games = []
        
    def load(self, list_games:list) -> None:
        """
        Carga juegos en la lista de juegos existente.

        Args:
            list_games (list): Una lista de juegos en formato de diccionario.
        """
        for game in list_games:
            game_add = Game(game["id"], game["name"], game["platform"], game["mode"], game["company"], game["year"], game["country"], game["gender"])
            self.list_games.append(game_add)

    def filter_gender(self, pattern:str) -> class_type:
        """
        Filtra los juegos que contengan en su genero el patron especificado.  

        Args:
            pattern (str): Patron para excluir los juegos.

        Returns:
            GameCatalog: Objeto del tipo Games que contiene los juegos filtrados por genero.
        """
        games_filter = GameCatalog()
        for game in self.list_games:
            if re.search(pattern, game.gender, re.IGNORECASE) == None:
                games_filter.list_games.append(game)
        return games_filter   
            
    def print(self) -> None:
        """
        Imprime los atributos de los juegos.
        """
        if len(self.list_games) > 0:
            for game in self.list_games:
                message = (f"ID: {str(game.id_game).zfill(4)} | NOMBRE: {game.name} | PLATAFORMA: {game.platform} | MODO: {game.mode} | COMPANIA: {game.company} | ANIO: {game.year} | PAIS: {game.country} | GENERO: {game.gender}")
                print(message)
    
    def find_decade(self, message:str) -> class_type:
        """
        Busca los juegos según una década específica.

        Args:
            message (str): Mensaje que indica las decadas.

        Returns:
            GameCatalog: Objeto del tipo Games que contiene los juegos filtrados por decada.
        """
        games = GameCatalog()
        running = True
        while running:
            running = False
            print(message)
            decade = input_int("Ingresar una decada: ")
            if decade % 10 == 0:
                for game in self.list_games:
                    if int(game.year) >= decade and int(game.year) < decade + 10:
                        games.list_games.append(game)
            if len(games.list_games) == 0:
                print("No se encontraron juegos de esa decada")
                running = True
        return games