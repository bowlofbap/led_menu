from ledsnake.ControllerHandler import ControllerHandler
from .constants import *

class SnakeWebHandler:
    processHandler = None
    
    def __new__(cls, processHandler):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SnakeWebHandler, cls).__new__(cls)
            cls.instance.processHandler = processHandler
        return cls.instance

    def play_snake_game(self, ai, multiplayer):
        self.processHandler.kill_process()
        controller_handler = ControllerHandler(WIDTH, HEIGHT, ai = ai, multiplayer = multiplayer, debug = False)
        self.processHandler.start_process(lambda: controller_handler.startGame(), {})
