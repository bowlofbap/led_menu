from typing import List, Optional
from .BoardHandler import BoardHandler
from .DisplayHandler import DisplayHandler
from .Options import Options
from .Direction import Direction
from .SnakeWebHandler import SnakeWebHandler
from .TetrisWebHandler import TetrisWebHandler
from .ProcessHandler import ProcessHandler

class Menu:

    def __init__(self, options: List[Options], board_handler: BoardHandler, _display_handler: DisplayHandler):
        self.options = options
        self.current_index = 0
        self._display_handler = _display_handler
        self._board_handler = board_handler
        processHandler = ProcessHandler()
        self._snakeWebHandler = SnakeWebHandler(processHandler)
        self._tetrisWebHandler = TetrisWebHandler(processHandler)

    def navigate(self, direction):
        # Update the current selection index
        if direction == Direction.RIGHT:
            self.current_index = (self.current_index - 1) % len(self.options)
        elif direction == Direction.LEFT:
            self.current_index = (self.current_index + 1) % len(self.options)
        self.show_menu()

    def select_option(self):
        # Return the currently selected option
        current_option = self.options[self.current_index]
        self._reset_visuals()
        self._display_handler.write_text(current_option.value)
        #self._board_handler.show_graphic(current_option)
        if current_option == Options.TETRIS:
            self._tetrisWebHandler.play_tetris_game()
        elif current_option == Options.SNAKE:
            self._snakeWebHandler.play_snake_game(True, False)
        elif current_option == Options.GIFS:
            print("GIFS")

    def _reset_visuals(self):
        self._board_handler.clear()
        self._display_handler.clear()

    def update(self):
        current_option = self.options[self.current_index]
        self._board_handler.update(current_option)
        self._display_handler.scroll_text(current_option.value)

    def clear(self):
        self._board_handler.clear()
        self._display_handler.clear()
