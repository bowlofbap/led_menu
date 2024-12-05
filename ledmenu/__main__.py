from .ControllerHandler import ControllerHandler

#  Main program logic follows:
if __name__ == '__main__':
    controllerHandler = ControllerHandler()
    try:
        controllerHandler.start()
    except KeyboardInterrupt:
        controllerHandler.clear_screen()