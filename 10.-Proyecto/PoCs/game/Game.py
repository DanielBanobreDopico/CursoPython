from flask import Flask, Response, send_from_directory

from FIFO import FIFO

from Playground import Playground
from Keyboard import Keyboard

from expansions.daniel.Daniel import Daniel
from expansions.daniel.Bomb import Bomb
from expansions.daniel.BadGuy import BadGuy
from expansions.daniel.AddObjectsLoop import AddObjectsLoop

app = Flask(__name__)
fifo = FIFO()

    
@app.route('/<file>', methods=["GET"])
def public(file):
    if not file: file = "index.html"
    return send_from_directory("./public/",file)

@app.route('/game/', methods=["GET"])
def httpGet():
    return Response(fifo.messages(),mimetype="text/event-stream")

keyboard = Keyboard()
board = Playground(5,5,keyboard,fifo.sendMessage)

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
