from Playground import Playground
from Character import Character
from Keyboard import Keyboard

board = Playground(5,5)
keyboard = Keyboard()
character = Character(board,keyboard,"<UP>","<RIGHT>","<DOWN>","<LEFT>")
keyboard.keyCaptureLoop()