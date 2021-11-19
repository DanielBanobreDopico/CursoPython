from pynput import keyboard

class Keyboard:

    stayListening = True
    callbacks = {}

    def key_laptureLoop(self):
        with keyboard.Listener(
                on_press=self.call_press_callbacks,
                on_release=self.call_release_callbacks) as listener:
            listener.join()

    def call_callbacks(self,key,event):
        print(key,event)
        '''if key in self.callbacks:
            for handler in self.callbacks[key]:
                handler(key)'''

    def call_press_callbacks(self,key):
        self.call_callbacks(key,'press')

    def call_release_callbacks(self,key):
        self.call_callbacks(key,'release')

    def addCallbacks(self,eventHandlerList):
        # eventHandlerList is a list of tuples event/handler where event is a key representation ans handler a function or method.
        for keyDescriptor, callback in eventHandlerList:
            if not keyDescriptor in self.callbacks: self.callbacks[keyDescriptor] = []
            self.callbacks[keyDescriptor].append(callback)

    def stop_listening(self,*arg):
        self.stayListening=False

    def __init__(self): pass
        #self.addCallbacks([('<ESC>', self.stopListening)])

if __name__ == '__main__':
    k = Keyboard()
    k.key_laptureLoop()