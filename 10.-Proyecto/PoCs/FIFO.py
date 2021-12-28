from singleton import singleton
from time import sleep

@singleton
class FIFO:
    __messages = []
    def sendMessage(self,msg):
        self.__messages.append(msg)
    def messages(self):
        while True:
            sleep(0.2)
            if len(self.__messages) > 0:
                yield self.__messages.pop(0)
