from uuid import uuid4

class Character:
    id = str(uuid4())
    def __init__(self, playground, keyboard, upKey, rightKey, downKey, leftKey):
        self.playground = playground
        playground.addCharacter(self,3,2)
        keyboard.addHandlers([
            (upKey,self.up),
            (rightKey,self.right),
            (downKey,self.down),
            (leftKey,self.left),
            ])
    def __str__(self):
        return "🚶"
    def move(self,x,y):
        self.playground.move(self,x,y)
    def up(self, key):
        self.move(0,1)
    def right(self, key):
        self.move(1,0)
    def down(self, key):
        self.move(0,-1)
    def left(self, key):
        self.move(-1,0)