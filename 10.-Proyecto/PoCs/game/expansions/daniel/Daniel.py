from Character import Character

class Daniel(Character):
    def __init__(self, playground, keyboard, callbacks, aspecto):
        self.aspecto = aspecto
        super().__init__(playground, keyboard, callbacks)

    def __repr__(self):
        return " %s " % self.aspecto

    def shoot(self,key,event):
        if event == "press": print("Pun!!!",event)

    def dress(self,key,event):
        self.aspecto = "🤠"