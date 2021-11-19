from pynput import keyboard

class Keyboard:

    callbacks = {}

    def key_capture_loop(self):
        with keyboard.Listener(
                on_press=self.call_press_callbacks,
                on_release=self.call_release_callbacks) as listener:
            listener.join()

    def call_callbacks(self,key_obj,event):
        key = key_obj.char if hasattr(key_obj,"char") else key_obj.name
        if key in self.callbacks:
            for handler in self.callbacks[key]:
                handler(key,event)

    def call_press_callbacks(self,key):
        self.call_callbacks(key,'press')

    def call_release_callbacks(self,key):
        self.call_callbacks(key,'release')

    def add_callbacks(self,eventHandlerList):
        # eventHandlerList is a list of tuples event/handler where event is a key representation ans handler a function or method.
        for key_descriptor, callback in eventHandlerList:
            if not key_descriptor in self.callbacks: self.callbacks[key_descriptor] = []
            self.callbacks[key_descriptor].append(callback)

    def stop_listening(self,*arg):
        self.stayListening=False

    def __init__(self): pass

if __name__ == '__main__':
    k = Keyboard()
    k.key_capture_loop()