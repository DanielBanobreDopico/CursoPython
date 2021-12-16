from Keyboard import Keyboard

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
         # Creates a new instance for this class only if previous
         # instances doesn't exists.
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_] # Returns the only instance for this class.
    # Returns a function how retunrs the only instance for the class.
    return getinstance

@singleton
class KeyboardSingleton(Keyboard):
    pass

if __name__ == "__init__":
    key1 = KeyboardSingleton() # Decorated class, really a function. Instantiates object.
    key2 = KeyboardSingleton() # Same function. Don't instantiates. Returns same instance.
    print(key1 is key2) # We can verify it's the same instance.
    print(id(key1),id(key2))