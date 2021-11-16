class Playground:
    characters = {}
    def __init__(self, x, y):
        self.board = [ [None]*x for row in range(y)]
    def move(self, character, x, y):
        if character.id in self.characters:

            current_x = self.characters[character.id]["x"]
            current_y = self.characters[character.id]["y"]
            self.board[current_x][current_y] = None

            next_x = self.reduceDimension("x", current_x + x)
            next_y = self.reduceDimension("y", current_y + y)
            self.characters[character.id]["x"] = next_x
            self.characters[character.id]["y"] = next_y
            self.board[next_x][next_y] = character

            print(self.characters[character.id])
            for row in self.board:
                print(row)

    def addCharacter(self, character, x, y):
        if not character.id in self.characters: self.characters[character.id] = {}
        self.characters[character.id]["x"] = self.reduceDimension("x",x)
        self.characters[character.id]["y"] = self.reduceDimension("y",y)

    def reduceDimension(self, axis, dimension):
        if axis == "x":
            return dimension % len(self.board[0])
        elif axis == "y":
            return dimension % len(self.board)
