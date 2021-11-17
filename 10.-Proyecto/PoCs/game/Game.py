from Playground import Playground
from Character import Character
from Keyboard import Keyboard

board = Playground(5,5)
keyboard = Keyboard()
character_callbacks = [
    ("<UP>","up"),
    ("<RIGHT>","right"),
    ("<DOWN>","down"),
    ("<LEFT>","left"),
]
character = Character(board,keyboard,character_callbacks)
keyboard.keyCaptureLoop()