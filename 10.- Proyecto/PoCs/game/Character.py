class Character:
    def __init__(self, playground, keyboard, upKey, rightKey, downKey, leftKey):
        self.playground = playground
        keyboard.addHandler(upKey,self.up,self.right,self.down,self.left)
    def move(self,x,y):
        self.playground.move(self,x,y)
    def up(self):
        self.move(0,1)
    def right(self):
        self.move(1,0)
    def down(self):
        self.move(0,-1)
    def left(self):
        self.move(-1,0)