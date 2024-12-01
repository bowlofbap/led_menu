from enum import Enum

class Options(Enum):
    SNAKE = "Snake"
    TETRIS = "Tetris"
    GIFS = "Gifs"

    @property
    def selection(self):
        return self.value[0]