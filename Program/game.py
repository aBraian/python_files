class Game:
    
    class_type = "Game"
    
    def __init__(self, id_game:int, name:str, platform:str, mode:str, company:str, year:int, country:str, gender:str) -> None:
        """
        Constructor de la clase Game.

        Args:
            id_game (int): Identificador del juego.
            name (str): Nombre del juego.
            platform (str): Plataforma del juego.
            mode (str): Modo de juego del juego.
            company (str): Compañía desarrolladora del juego.
            year (int): Año de lanzamiento del juego.
            country (str): País de origen del juego.
            gender (str): Género del juego.
        """
        self.id_game = id_game
        self.name = name
        self.platform = platform
        self.mode = mode
        self.company = company
        self.year = year
        self.country = country
        self.gender = gender