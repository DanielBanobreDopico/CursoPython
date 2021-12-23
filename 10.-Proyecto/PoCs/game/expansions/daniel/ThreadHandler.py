from threading import Thread

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
class ThreadHandler:
    stopThreads = False
    def __init__(self, theClass, threadFunctionName="threadFunction", threadArgs = "threadArgs"):
        def constructor(*args):
            instance = theClass(*args)
            thread = Thread(target=self.runThread(instance[threadFunctionName]), args=instance[threadArgs])
            thread.start()
        return constructor

    def runThread(self,function,args):
        while self.stopThreads:
            function(args)