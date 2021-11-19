from platform import system
from keyboard import on_press_key, on_release_key, unhook
from curtsies import Input

system = system() # 'Linux', 'Darwin', 'Java', 'Windows'

class Cursies:
    pass

class Keyboard:
    #keyboard.on_press_key(key, callback, suppress=False)
    #keyboard.unhook(remove)
    #keyboard.on_press_key(key, lambda ev: print(ev), suppress=False)
    #keyboard.hook(lambda ev: print(ev))
    pass

if system in ('Linux', 'Darwin'):
    class KeyEvents(Cursies):
        pass
elif system in ('Windows'):
    class KeyEvents(Keyboard):
        pass

if __name__ == "__main__":
    print(system)

