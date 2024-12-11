from .constants import BLUETOOTH_DIRECTIONS
from .Direction import Direction
from .ControllerMap import ControllerMap
from .BoardHandler import BoardHandler
from .DisplayHandler import DisplayHandler
from .Options import Options
from .Menu import Menu
import pygame
import math
import sys

class ControllerHandler:
    #abstraction to handle inputs andpo0-gameloop and wraps around the game itself

    def __init__(self):
        self._joystick_connected = False
        self._running = True
        self._clock = pygame.time.Clock()
        self._menu = Menu(list(Options), BoardHandler(), DisplayHandler())

    #called externally to kick off listening for inputs
    def start(self):
        pygame.init()
        pygame.joystick.init()
        joystick_detected = False
        while joystick_detected==False:
            print("Waiting for controller...")
            pygame.joystick.quit()
            pygame.joystick.init()
            try:
                joystick = pygame.joystick.Joystick(0) # create a joystick instance
                joystick.init() # init instance
                self._joystick_connected = True
                joystick_detected = True
                print("controller found")

            except pygame.error:
                print("not enough joystick found.")
                joystick_detected = False
                self._menu._display_handler.scroll_text("Waiting for controller...")
        self.loop()

    def loop(self):
        self._menu.update()
        while self._running:
            if not self.is_controller_connected():
                self.clear_screen()
                continue
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    axis = event.axis         # Axis number (0 for horizontal, 1 for vertical)                     
                    position = event.value    # Position on the axis (-1.0 to 1.0)
                    direction, motion = self._convert_bt_to_direction_and_motion(axis, position)
                    if motion == "press":
                        self._process_direction_down(direction)
                elif event.type == pygame.JOYBUTTONDOWN:
                    controller_button = ControllerMap(event.button)
                    self._process_button_down(controller_button)
            self._clock.tick(30)
        self.clear_screen()
        pygame.quit()
        sys.exit()

    def is_controller_connected(self):
        joystick_count = pygame.joystick.get_count()
        if joystick_count > 0 and self._joystick_connected:
            #joystick exists and connected
            return True
        elif joystick_count > 0 and not self._joystick_connected:
            #joystick is exists but currently not connected
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            self._joystick_connected = True
            return True
        elif joystick_count == 0 and self._joystick_connected:
            self._joystick_connected = False
            return False

    def _process_direction_down(self, direction):
        self._menu.navigate(direction)

    def _process_button_down(self, controller_button):
        if controller_button == ControllerMap.A:
            self._running = False
            self._menu.select_option()

    def clear_screen(self):
        self._menu.clear()

    def _convert_bt_to_direction_and_motion(self, raw_input_x, raw_input_y):
        # Handle release state
        if abs(raw_input_y) <= 0.1:
            return None, "release"

        # Calculate which direction matches the input for button down presses
        closest_direction = None
        smallest_distance = float('inf')
        
        for direction, vector in BLUETOOTH_DIRECTIONS.items():
            # Calculate Euclidean distance between input and direction vector
            distance = math.sqrt((raw_input_x - vector['x']) ** 2 + (raw_input_y - vector['y']) ** 2)
            
            if distance < smallest_distance and distance <= 0.1:
                closest_direction = direction
                smallest_distance = distance

        return Direction[closest_direction], "press"
