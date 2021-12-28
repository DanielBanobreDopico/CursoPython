from flask import Flask

from Playground import Playground
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Bomb import Bomb
from expansions.daniel.BadGuy import BadGuy
from expansions.daniel.AddObjectsLoop import AddObjectsLoop

app = Flask(__name__)

@app.route('/game/', methods=["GET"])
def httpGet():
    return str(board)

keyboard = Keyboard()
board = Playground(5,5,keyboard)

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
