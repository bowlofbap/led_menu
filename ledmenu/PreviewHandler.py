from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from typing import List, Optional

class PreviewHandler:

    def __init__(self, ):
        self._tetris_game = game
        serial = spi(port=0, device=0, gpio_noop=True)
        self._device = max7219(serial, cascaded=4, blocks_arranged_in_reverse_order=True)

    def show_text(self, text):
        show_message(self._device,text,fill="white", font=proportional(CP437_FONT), scroll_delay=0.03)

    def update(self):
        next_pieces: List[Shape] = self._tetris_game.get_bag().get_all_pieces()[:3]
        held_piece: Optional[Shape] = self._tetris_game.get_bag().peek_swap_piece()
        with canvas(self._device) as draw:
            def draw_piece(i, shape: Shape):
                for y, row in enumerate(shape.bit_map):
                    for x, value in enumerate(row):
                        if (value == 1):
                            draw.point((x + (8 * i)+1, y+1), fill="white")
                            
            def draw_held_piece(shape: Shape):
                for y in range(8):
                    for x in range(8):
                        if (x == 0 or x == 7 or y == 0 or y == 7):
                            draw.point((x, y), fill="white")
                        elif shape:
                            b_x = x-1
                            b_y = y-1
                            value = shape.bit_map[b_y][b_x]
                            if value == 1:
                                draw.point((x, y), fill="white")
            draw_held_piece(held_piece)
            for i in range(3):
                shape = next_pieces[i]
                draw_piece(i+1, shape)
            """
            if held_piece is not None:
                text(draw, (0, 0), held_piece.name, font=proportional(CP437_FONT), fill="white")    # Display "1" on the first module
            text(draw, (8, 0), next_pieces[0].name, font=proportional(CP437_FONT), fill="white")    # Display "A" on the second module
            text(draw, (16, 0), next_pieces[1].name, font=proportional(CP437_FONT), fill="white")   # Display "Z" on the third module
            text(draw, (24, 0), next_pieces[2].name, font=proportional(CP437_FONT), fill="white")   # Display "!" on the fourth module
            """
    
    
    def clear(self):
        self._device.clear()
