from flask import Flask, Response
from FIFO import FIFO

app = Flask(__name__)

fifo = FIFO()

@app.route("/estado/", methods=['GET'])
def estado():
    return Response(FIFO.messages(), mimetype="text/event-stream")

fifo.sendMessage('Hola!')