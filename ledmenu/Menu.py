from typing import List, Optional
from .BoardHandler import BoardHandler
from .DisplayHandler import DisplayHandler
from ._Options import Options
from .Direction import Direction
from .SnakeWebHandler import SnakeWebHandler
from .TetrisWebHandler import TetrisWebHandler
from .ProcessHandler import ProcessHandler

class Menu:

    def __init__(self, options: List[Options], board_handler: BoardHandler, _display_handler: DisplayHandler):
        self._options = options
        self._current_index = 0 #for left/right
        self._option_setting_index = 0 #for up/down
        self._option_settings = self._options[0].option_settings
        self._display_handler = _display_handler
        self._board_handler = board_handler
        processHandler = ProcessHandler()
        self._snakeWebHandler = SnakeWebHandler(processHandler)
        self._tetrisWebHandler = TetrisWebHandler(processHandler)

    def navigate(self, direction):
        # Update the current selection index
        if direction == Direction.RIGHT:
            self._current_index = (self._current_index - 1) % len(self._options)
            self._option_settings = self._options[0].option_settings
            self._option_setting_index = 0
        elif direction == Direction.LEFT:
            self._current_index = (self._current_index + 1) % len(self._options)
            self._option_settings = self._options[0].option_settings
            self._option_setting_index = 0
        elif direction == Direction.UP:
            self._option_setting_index = (self._option_setting_index + 1) % len(self._option_settings)
        elif direction == Direction.Down:
            self._option_setting_index = (self._option_setting_index - 1) % len(self._option_settings)
        self.update()

    def select_option(self):
        # Return the currently selected option
        current_option = self._options[self._current_index]
        current_option_setting = current_option.option_settings[self._option_setting_index]
        self._reset_visuals()
        self._display_handler.write_text(current_option.value)
        #self._board_handler.show_graphic(current_option)
        if current_option == Options.TETRIS:
            self._tetrisWebHandler.play_tetris_game()
        elif current_option == Options.SNAKE:
            self._snakeWebHandler.play_snake_game(current_option_setting["AI"], current_option_setting["Multiplayer"])
        elif current_option == Options.GIFS:
            print("GIFS")
        print("Selected option")

    def _reset_visuals(self):
        self._board_handler.clear()
        self._display_handler.clear()

    def update(self):
        current_option = self._options[self._current_index]
        self._board_handler.update(current_option) #TODO: handle this
        self._display_handler.write_text(current_option.option_name + "(" + current_option.option_settings[self._option_setting_index]["Name"] + ")")

    def clear(self):
        self._board_handler.turn_off()
        self._display_handler.clear()
