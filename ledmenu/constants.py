LED_FREQ_HZ          = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA              = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS       = 20     # Set to 0 for darkest and 255 for brightest
LED_GHOST_BRIGHTNESS = 5
LED_INVERT           = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL          = 0       # set to '1' for GPIOs 13, 19, 41, 45 or

WIDTH         = 10
HEIGHT        = 20
#used to parse the data from bluetooth controllers (x for axis, y for value)
BLUETOOTH_DIRECTIONS = {
    "LEFT" : {
        'x': 0,
        'y': -1
    },
    "RIGHT" : {
        'x': 0,
        'y': 1
    },
    "UP" : {
        'x': 1,
        'y': -1
    },
    "DOWN" : {
        'x': 1,
        'y': 1
    },
}