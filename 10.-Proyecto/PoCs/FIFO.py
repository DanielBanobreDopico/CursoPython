from singleton import singleton

@singleton
class FIFO:
    __messages = []
    def sendMessage(self,msg):
        self.__messages.append(msg)
    def messages(self):
        while True:
            if len(self.__messages) > 0:
                yield self.messages.pop(0)
