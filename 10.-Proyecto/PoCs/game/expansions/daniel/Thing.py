from uuid import uuid4

class Thing:
    def __init__(self, theme, playground):
        self.id = str(uuid4())
        self.__theme = theme
        self.playground = playground
        self.playground.addCharacter(self)


    def __repr__(self):
        return self.__theme
    def __str__(self):
        return self.__repr__()
    def get_touched(self, character):
        print("%s touched me." % character)
    '''
    def change_strength(self, strength):
        return strength
    def change_health(self, health):
        return health
    def change_damage(self, damage):
        return damage
    def change_recovery(self, recovery):
        return recovery
    '''
