from Playground import Playground
from Character import Character
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Thing import Thing

board = Playground(5,5)
keyboard = Keyboard()
daniel1_callbacks = [
    ("up","up"),
    ("right","right"),
    ("down","down"),
    ("left","left"),
]
daniel2_callbacks = [
    ("w","up"),
    ("d","right"),
    ("s","down"),
    ("a","left"),                      
    ("space","shoot"),
    ("x","dress")
]
daniel1 = Daniel(board,keyboard,daniel1_callbacks,'😏')
daniel2 = Daniel(board,keyboard,daniel2_callbacks,'🤓')

# Engadimos unha "cousa" ó taboleiro.
cosa = Thing("Cosa")
board.addCharacter(cosa,(0,0))

keyboard.key_capture_loop()