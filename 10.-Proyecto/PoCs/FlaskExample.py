# For running:
# pip install flask
# FLASK_APP=FlaskExample.py python -m flask run


from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/noticias/<name>/", methods=['GET'])
def hello_you(name):
    return "<h1>Hello, %s.</h1>" % escape(name)

@app.route("/noticias/", methods=['GET'])
def hello_world():
    # ...
    return "<p>Hello, World!</p>"

@app.route("/login/", methods=['POST'])
def login():
    print(request.form['username'])
    print(request.form['password'])
    return ""