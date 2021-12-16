from threading import Thread
from time import sleep

class AddObjectsLoop:
    
    def __init__(self, playground, object_class, aspect="💩", time=0):
        self.playground = playground
        self.timer = Thread(target = self.add_object, args=(time,playground,object_class,aspect))
        self.timer.start()
        
        
    def add_object(self,wait_time,playground,object_class,aspect):
        while True:
            sleep(wait_time)
            object_class(aspect,playground)
        