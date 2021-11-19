from curtsies import Input

class Keyboard:

    stayListening = True
    callbacks = {}

    def keyCaptureLoop(self):
        with Input() as input:
            for key in input:
                if key in self.callbacks:
                    for handler in self.callbacks[key]:
                        handler(key)
                if not self.stayListening: break

    def addCallbacks(self,eventHandlerList):
        # eventHandlerList is a list of tuples event/handler where event is a key representation ans handler a function or method.
        for keyDescriptor, callback in eventHandlerList:
            if not keyDescriptor in self.callbacks: self.callbacks[keyDescriptor] = []
            self.callbacks[keyDescriptor].append(callback)

    def stopListening(self,*arg):
        self.stayListening=False

    def __init__(self):
        self.addCallbacks([('<ESC>', self.stopListening)])

if __name__ == '__main__':
    k = Keyboard()
    k.keyCaptureLoop()