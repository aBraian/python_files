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
            class_type: Objeto del tipo GameCatalog que contiene los juegos filtrados por genero.
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
            class_type: Objeto del tipo GameCatalog que contiene los juegos filtrados por decada.
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
    
    def copy(self) -> class_type:
        """
        Crea una copia del objeto GameCatalog.

        Returns:
            class_type: Un nuevo objeto GameCatalog que contiene una copia de los juegos.
        """
        copy = GameCatalog()
        if len(self.list_games) > 0:
            for game in self.list_games:
                game_copy = Game(game.id_game, game.name, game.platform, game.mode, game.company, game.year, game.country, game.gender)
                copy.list_games.append(game_copy)
        return copy
    
    def bubble_sort(self, mode:bool) -> class_type:
        """
        Ordena los juegos en el objeto GameCatalog utilizando el algoritmo Bubble Sort.

        Args:
            mode (bool): Determina el modo de ordenamiento. True para orden descendente, False para orden ascendente.

        Returns:
            class_type: Un nuevo objeto GameCatalog que contiene los juegos ordenados.
        """
        swap = True
        copy = self.copy()
        if len(copy.list_games) > 0:
            while swap:
                swap = False
                for i in range(len(copy.list_games) - 1):
                    if mode:
                        if copy.list_games[i].company < copy.list_games[i + 1].company:
                            aux = copy.list_games[i]
                            copy.list_games[i] = copy.list_games[i + 1]
                            copy.list_games[i + 1] = aux
                            swap = True
                    else:   
                        if copy.list_games[i].company > copy.list_games[i + 1].company:
                            aux = copy.list_games[i]
                            copy.list_games[i] = copy.list_games[i + 1]
                            copy.list_games[i + 1] = aux
                            swap = True
        return copy
    
    def search_mode(self, *args) -> class_type:
        """
        Filtra los juegos según los modos de juego especificados.

        Args:
            *args: Argumentos variables que contienen los modos de juego en formato de cadena.

        Returns:
            class_type: Un objeto del tipo GameCatalog que contiene los juegos filtrados por modos de juego.
        """
        games = GameCatalog()
        for mode in args:
            for game in self.list_games:
                if re.search(mode, game.mode, re.IGNORECASE) != None:
                    if game not in games.list_games:
                        games.list_games.append(game)
        return games