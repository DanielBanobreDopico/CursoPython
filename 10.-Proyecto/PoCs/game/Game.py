from Playground import Playground
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Bomb import Bomb
from expansions.daniel.BadGuy import BadGuy
from expansions.daniel.AddObjectsLoop import AddObjectsLoop

game_elements = []

board = Playground(5,5)
keyboard = Keyboard()

daniel1_callbacks = [
    ("up","up"),
    ("right","right"),
    ("down","down"),
    ("left","left"),
]

game_elements.append(Daniel(board,keyboard,daniel1_callbacks,'😏'))

game_elements.append(AddObjectsLoop(board,Bomb,"💣",10))

# Personaje autónomo
game_elements.append(BadGuy(board,keyboard))

print(game_elements)