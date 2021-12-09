from expansions.daniel.Thing import Thing

class Bomb(Thing):
    def __init__(self, theme, playground):
        super().__init__(theme, playground)
    def get_touched(self, character):
        character.get_hurted(10)
        del self
        #super().get_touched(character)
