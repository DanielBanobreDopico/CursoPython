'''
Proporciona un objeto BadGuy que hereda de Character y supone un contrincante al que enfrentarse.
'''
from random import choice
from threading import Thread
from time import sleep
from Character import Character

class BadGuy(Character):

    movements = ((-1,0),(1,0),(0,-1),(0,-1))
    maxMove = 1

    def __init__(self, playground, keyboard):
        super().__init__(playground, keyboard, [], "🤠")
        self.timer = Thread(target=self.self_move,args=(1,))
        self.timer.start()

    def self_move(self, wait):
        while not self.stop_game:
            sleep(wait)
            movement = choice(self.movements)
            self.move(movement[0],movement[1])

