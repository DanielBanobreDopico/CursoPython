from typing import Callable
import Playground
import Character
import Keyboard

board = Playground(5,5)
keyboard = Keyboard()
character = Character(board,keyboard,"<UP>","<RIGHT>","<DOWN>","<LEFT>")