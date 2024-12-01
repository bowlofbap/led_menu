from .DisplayHandler import DisplayHandler
from .Options import Options

class Menu:
    def __init__(self, options):
        self._options = options
        self._current_index = 0
        self._display_handler = DisplayHandler()

    def show_menu(self):
        # Display_handler the current menu option
        self._display_handler.clear()
        self._display_handler.write(self._options[self._current_index])

    def navigate(self, direction):
        # Update the current selection index
        if direction == "up":
            self._current_index = (self._current_index - 1) % len(self._options)
        elif direction == "down":
            self._current_index = (self._current_index + 1) % len(self._options)
        self.show_menu()

    def select_option(self):
        # Return the currently selected option
        return self._options[self._current_index]