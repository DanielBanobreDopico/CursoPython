from uuid import uuid4

class Thing:
    def __init__(self, name):
        self.id = str(uuid4())
    def __repr__(self):
        return "  💩 "
    def __str__(self):
        return self.__repr__()
