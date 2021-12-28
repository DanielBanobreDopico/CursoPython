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
