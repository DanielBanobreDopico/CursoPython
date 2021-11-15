from curtsies import Input

def no(k):
    k.loop = False

class Keyboard:

    stayListening = True
    handlers = {}

    def keyCaptureLoop(self):
        with Input() as input_generator:
            for key in input_generator:
                print(repr(key))
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