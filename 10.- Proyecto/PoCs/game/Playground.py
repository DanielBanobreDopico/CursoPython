class Playground:
    characters = {}
    def __init__(self, x, y):
        self.board = [ [[]*x] for row in range(y)]
    def move(self, character, x, y):
        if character in self.characters:

            current_x = self.characters[character].x
            current_y = self.characters[character].y
            self.board[current_x][current_y] = None

            next_x = self.reduceDimension("x", current_x + x)
            next_y = self.reduceDimension("y", current_y + y)
            self.characters[character].x = next_x
            self.characters[character].y = next_y
            self.board[next_x][next_y] = character

    def addCharacter(self, character, x, y):
        if not character in self.characters:
            self.characters[character].x = self.reduceDimension("x",x)
            self.characters[character].y = self.reduceDimension("y",y)

    @classmethod
    def reduceDimension(self, axis, dimension):
        if axis == "x":
            return dimension % len(self.board[0])
        elif axis == "y":
            return dimension % len(self.board)
