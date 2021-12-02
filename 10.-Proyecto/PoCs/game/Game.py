from Playground import Playground
from Character import Character
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Thing import Thing

board = Playground(5,5)
keyboard = Keyboard()
character_callbacks = [
    ("up","up"),
    ("right","right"),
    ("down","down"),
    ("left","left"),
]
daniel_callbacks = [
    ("w","up"),
    ("d","right"),
    ("s","down"),
    ("a","left"),                      
    ("space","shoot"),
    ("x","dress")
]
character = Character(board,keyboard,character_callbacks)
daniel = Daniel(board,keyboard,daniel_callbacks,'🤓')
cosa = Thing("Cosa")
board.addCharacter(cosa,(0,0))
keyboard.key_capture_loop()