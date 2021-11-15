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

    def addHandler(self,keyDescriptor,callback):
        if keyDescriptor in self.handlers:
            self.handlers[keyDescriptor].append(callback)
        else:
            self.handlers[keyDescriptor] = []
            self.addHandler(keyDescriptor,callback)

    def stopListening(self,*arg):
        self.stayListening=False

    def __init__(self):
        self.addHandler('<ESC>', self.stopListening )

if __name__ == '__main__':
    k = Keyboard()
    k.keyCaptureLoop()