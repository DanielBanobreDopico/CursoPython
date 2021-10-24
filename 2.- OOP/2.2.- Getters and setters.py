class Person:
    _counter = 0
    pocket = []
    def __init__(self, name):
        self.__name = name
        
    @property
    def counter(self):
        return self._counter
    @counter.setter
    def counter(self, value):
        self._counter = value
        
    @property
    def name(self):
        self._counter += 1
        print("Veces que me han preguntado el nombre:",self._counter)
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
        print("Ahora me llamo",self.__name)

persona = Person("Daniel")

print(persona.name)

persona.name = "Pedro"
print(persona.name)
print(persona.name)
print(persona.counter)
persona.counter = 0
print(persona.name)

#print(persona._Person__name)
#print(persona._counter)
#persona._counter = 0