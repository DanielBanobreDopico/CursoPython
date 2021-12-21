from random import choice
from Miguel.Utils import clearScreen

from Character import Character



class Playground:

    characters = {}

    def __init__(self, x, y):
        self.board = [ [None]*x for row in range(y)]

    def move(self, character, x, y):
        if character.id in self.characters:

            current_x = self.characters[character.id]["x"]
            current_y = self.characters[character.id]["y"]

            next_x = self.reduceDimension("x", current_x + x)
            next_y = self.reduceDimension("y", current_y + y)
            # Is next character empty?
            if isinstance(self.board[next_y][next_x],(Character)):
                 print("Toc!")
            else:
                if self.board[next_y][next_x] != None:
                    # character.put_in_backpack(self.board[next_y][next_x])
                    self.board[next_y][next_x].get_touched(character)
                    self.removeCharacter(self.board[next_y][next_x])
                self.characters[character.id]["x"] = next_x
                self.characters[character.id]["y"] = next_y
                self.board[next_y][next_x] = character
                self.board[current_y][current_x] = None

                clearScreen()
                for row in range(len(self.board)-1,-1,-1):
                    print(self.board[row])
                print("\n")




    @property
    def emptyPositions(self):
        '''Return a list of tuplas with choods for all empty positions.'''
        free_positions = []
        for y, row in enumerate(self.board):
            for x, pos in enumerate(row):
                if pos == None: free_positions.append((x,y))
        return free_positions

    def adjacent_characters(self,character):
        directions = ((x, y) for x in (-1,0,1) for y in (-1,0,1) if not (x==0 and y==0) )
        character_x = self.characters[character.id]["x"]
        character_y = self.characters[character.id]["y"]
        adjacent_positions = ({"x": self.reduceDimension("x", character_x + x), "y": self.reduceDimension("y", character_y+y)} for x, y in directions)
        return [self.board[pos["x"]][pos["y"]] for pos in adjacent_positions if self.board[pos["x"]][pos["y"]]]

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

    def removeCharacter(self,character):
        character_x = self.characters[character.id]["x"]
        character_y = self.characters[character.id]["y"]
        self.board[character_y][character_x] = None
        del self.characters[character.id]

    def reduceDimension(self, axis, dimension):
        if axis == "x":
            return dimension % len(self.board)
        elif axis == "y":
            return dimension % len(self.board[0])