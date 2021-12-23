from Playground import Playground
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Bomb import Bomb
from expansions.daniel.BadGuy import BadGuy
from expansions.daniel.AddObjectsLoop import AddObjectsLoop

board = Playground(5,5)
keyboard = Keyboard()

daniel1_callbacks = [
    ("up","up"),
    ("right","right"),
    ("down","down"),
    ("left","left"),
]

board.add_threaded_object(Daniel(board,keyboard,daniel1_callbacks,'😏'))

board.add_threaded_object(AddObjectsLoop(board,Bomb,"💣",10))

# Personaje autónomo
board.add_threaded_object(BadGuy(board,keyboard))
