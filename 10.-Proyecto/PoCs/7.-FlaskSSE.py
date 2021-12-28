from flask import Flask, Response
from FIFO import FIFO

app = Flask(__name__)

fifo = FIFO()

@app.route("/", methods=['GET'])
def hello_world():
    return Response(FIFO.messages(), mimetype="text/event-stream")