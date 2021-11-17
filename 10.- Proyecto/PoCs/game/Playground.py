from random import choice

class Playground:
    characters = {}
    def __init__(self, x, y):
        self.board = [ [None]*x for row in range(y)]
    def move(self, character, x, y):
        if character.id in self.characters:

            current_x = self.characters[character.id]["x"]
            current_y = self.characters[character.id]["y"]
            self.board[current_y][current_x] = None

            next_x = self.reduceDimension("x", current_x + x)
            next_y = self.reduceDimension("y", current_y + y)
            self.characters[character.id]["x"] = next_x
            self.characters[character.id]["y"] = next_y
            self.board[next_y][next_x] = character

            for row in self.board:
                print(row)
            print("\n")

    @property
    def emptyPositions(self):
        '''Return a list of tuplas with choods for all empty positions.'''
        free_positions = []
        for y, row in enumerate(self.board):
            for x, pos in enumerate(row):
                if pos == None: free_positions.append((x,y))
        return free_positions

    def randomFreePosition(self):
        '''Return a dupla with x, y choords for a empty board position.'''
        return choice(self.emptyPositions)

    def addCharacter(self, character, position = None):
        if not character.id in self.characters:
            self.characters[character.id] = {}
            x, y = position if position else self.randomFreePosition()
            self.characters[character.id]["x"] = self.reduceDimension("x",x)
            self.characters[character.id]["y"] = self.reduceDimension("y",y)
            self.board[y][x] = character

    def reduceDimension(self, axis, dimension):
        if axis == "x":
            return dimension % len(self.board)
        elif axis == "y":
            return dimension % len(self.board[0])
