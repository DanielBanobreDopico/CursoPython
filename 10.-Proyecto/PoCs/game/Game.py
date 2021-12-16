from Playground import Playground
from Character import Character
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
daniel2_callbacks = [
    ("w","up"),
    ("d","right"),
    ("s","down"),
    ("a","left"),                      
    ("space","shoot"),
    ("x","dress")
]

Daniel(board,keyboard,daniel1_callbacks,'😏')
# Daniel(board,keyboard,daniel2_callbacks,'🤓')

# Engadimos unha "cousa" ó taboleiro.
#Bomb("💣",board)

AddObjectsLoop(board,Bomb,"💣",10)

# Personaje autónomo
BadGuy(board,keyboard)

