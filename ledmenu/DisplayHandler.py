from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from typing import List, Optional

class DisplayHandler:

    def __init__(self):
        serial = spi(port=0, device=0, gpio_noop=True)
        self._device = max7219(serial, cascaded=4, blocks_arranged_in_reverse_order=True)

    def scroll_text(self, text):
        show_message(self._device,text,fill="white", font=proportional(CP437_FONT), scroll_delay=0.01)

    def write_text(self, text):
        text(draw, (0, 0), text, font=proportional(CP437_FONT), fill="white")

    def clear(self):
        self._device.clear()
