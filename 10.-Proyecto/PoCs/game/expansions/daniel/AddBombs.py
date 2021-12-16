from threading import Thread
from time import sleep

class AddBombs:
    
    def __init__(self, playground, bomb_class):
        self.playground = playground
        self.timer = Thread(target = self.add_bombs, args=(5,playground,bomb_class))
        self.timer.run()
        
        
    def add_bombs(self,wait_time,playground,bomb_class):
        while True:
            sleep(wait_time)
            bomb_class("💣",playground)
        