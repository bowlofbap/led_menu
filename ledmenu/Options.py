from enum import Enum

class Options(Enum):
    TETRIS = (
        "Tetris",
        [
            {
                "Name": "1P",
                "AI": False,
            },
            {
                "Name": "AI",
                "AI": True,
            },
        ],
    )
    SNAKE = (
        "Snake",
        [
            {
                "Name": "1P"
                "AI": False,
                "Multiplayer": False,
            },
            {
                "Name": "2P"
                "AI": False,
                "Multiplayer": True,
            },
            {
                "Name": "AI"
                "AI": True,
                "Multiplayer": False,
            },
        ],
    )
    GIFS = 
    (
        "Gifs",
        [
            {
                "Name": "Test1"
                "AI": False,
                "Multiplayer": False,
            },
            {
                "Name": "Test2"
                "AI": False,
                "Multiplayer": False,
            },
        ],
    )

    @property
    def option_name(self):
        return self.value[0]

    @property
    def option_settings(self):
        return self.value[1]