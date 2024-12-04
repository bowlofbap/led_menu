from ledtetris.ControllerHandler import ControllerHandler
from ledtetris.TetrisGame import TetrisGame


class TetrisWebHandler:
    processHandler = None
    
    def __new__(cls, processHandler):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TetrisWebHandler, cls).__new__(cls)
            cls.instance.processHandler = processHandler
        return cls.instance

    def play_tetris_game(self):
        self.processHandler.kill_process()
        tetrisGame = TetrisGame() 
        controllerHandler = ControllerHandler(tetrisGame, debug = False)
        self.processHandler.start_process(lambda: controllerHandler.start(), {})
