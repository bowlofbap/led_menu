from .Color import Color
from .constants import *

class BoardHandler:

    def __init__(self):
        import neopixel, board
        pixel_pin = board.D18
        num_pixels = WIDTH * HEIGHT
        order = neopixel.GRB
        self._pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=LED_BRIGHTNESS, auto_write=False,pixel_order=order)

    def _draw_pixel(self, x, y, color: Color, shadow: bool):
        brightness = 1 if not shadow else 0.1
        if (x>=0 and y>=0):
            r = int(color._value_[0] * brightness)
            g = int(color._value_[1] * brightness)
            b = int(color._value_[2] * brightness)
            self._pixels[self._get_pixel_from_grid(x,y)] = (r, g, b)

    #helper to translate the continuous strip into a grid
    #works for following setup

    # 9  10 11
    # 8  7  6
    # 3  4  5
    # 2  1  0

    def _get_pixel_from_grid(self, x, y):
        if (x%2 == 0):
            y = HEIGHT - y - 1
        return HEIGHT*(WIDTH - x - 1) + y

    #blank the screen
    def clear(self):
        self._pixels.fill((0,0,0))

    #update the leds/pixels
    def _update_screen(self):
        game_nodes = self._game.get_game_nodes().get_nodes()
        for y in range(len(game_nodes)):
            for x in range(len(game_nodes[y])):
                node: Node = game_nodes[y][x]
                node_shape = node.get_shape()
                if node_shape:
                    self._draw_pixel(y, x, node_shape.color, node.get_shadow())
        self._pixels.show()

    def turn_off(self):
        self.clear()
        self._pixels.show()

    #main update that gets called during the loop to update the screen
    def update(self, option):
        self.clear()
        #self._update_screen()
