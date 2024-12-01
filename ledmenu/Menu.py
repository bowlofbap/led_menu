from .DisplayHandler import DisplayHandler
from .Direction import Direction
from .Options import Options

class Menu:
    def __init__(self, options):
        self._options = list(Options)
        self._current_index = 0
        self._display_handler = DisplayHandler()

    def show_menu(self):
        # Display_handler the current menu option
        self._display_handler.clear()
        self._display_handler.write(self._options[self._current_index].selection)

    def navigate(self, direction):
        # Update the current selection index
        if direction == Direction.LEFT.name:
            self._current_index = (self._current_index - 1) % len(self._options)
        elif direction == Direction.RIGHT.name:
            self._current_index = (self._current_index + 1) % len(self._options)
        self.show_menu()

    def start_selection(self, selection=None):
        current_selection = self._options[self._current_index] if selection is None else selection
        if current_selection == Options.SNAKE:
            #TODO: play snake
        elif current_selection == Options.TETRIS:
            #TODO: play tetris
        elif current_selection == Options.GIFS:
            #TODO: play gifs

    def get_current_option(self):
        # Return the currently selected option
        return self._options[self._current_index]