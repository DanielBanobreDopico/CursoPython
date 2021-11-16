from curtsies import Input

class Keyboard:

    stayListening = True
    handlers = {}

    def keyCaptureLoop(self):
        with Input() as input:
            for key in input:
                if key in self.handlers:
                    for handler in self.handlers[key]:
                        handler(key)
                if not self.stayListening: break

    def addHandlers(self,eventHandlerList):
        # eventHandlerList is a list of tuples event/handler where event is a key representation ans handler a function or method.
        for keyDescriptor, callback in eventHandlerList:
            if not keyDescriptor in self.handlers: self.handlers[keyDescriptor] = []
            self.handlers[keyDescriptor].append(callback)

    def stopListening(self,*arg):
        self.stayListening=False

    def __init__(self):
        self.addHandlers([('<ESC>', self.stopListening)])

if __name__ == '__main__':
    k = Keyboard()
    k.keyCaptureLoop()