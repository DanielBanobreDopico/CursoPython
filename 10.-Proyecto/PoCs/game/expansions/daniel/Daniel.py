from Character import Character

class Daniel(Character):

    __life = 100

    def __init__(self, playground, keyboard, callbacks, aspecto):
        self.aspecto = aspecto
        super().__init__(playground, keyboard, callbacks)
        self.__backpack = []

    def __repr__(self):
        return " %s " % self.aspecto

    def shoot(self,key,event):
        if event == "press": print("Pun!!!",event)

    def dress(self,key,event):
        self.aspecto = "🤠"

    def put_in_backpack(self, object):
        self.__backpack.append(object)
        print("Mochila: %s" % self.__backpack)

    def get_hurted(self,value):
        self.__life -= value