from Playground import Playground
from Character import Character
from Keyboard import Keyboard

board = Playground(5,5)
keyboard = Keyboard()
character_callbacks = [
    ("up","up"),
    ("right","right"),
    ("down","down"),
    ("left","left"),
]
character = Character(board,keyboard,character_callbacks)
keyboard.key_capture_loop()