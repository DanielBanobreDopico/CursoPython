'''
Ejemplo 1:
'''
class Warrior:
    life = 100
    def __init__(thisWarrior, name, enemy = True, strength = 5, speed = 5):
        thisWarrior.name = name
        thisWarrior.enemy = enemy
        thisWarrior.strength = strength
        thisWarrior.speep = speed
    def hurt(thisWarrior, enemy):
        enemy.life -= 1

allies = []
enemies = []

allies.append(Warrior("Ana",False,4,6))
allies.append(Warrior("Manolo",False,6,4))

enemies.append(Warrior("Rodolfo"))
enemies.append(Warrior("Lola"))

print("Allies:",allies)
print("Enemies",enemies)

allies[0].hurt(enemies[0])

print("Vida del enemigo num. 0:", enemies[0].life)

'''
Ejemplo 2:
'''
class Warrior:
    life = 100
    def __init__(thisWarrior, name, enemy = True, strength = 5, speed = 5):
        thisWarrior.name = name
        thisWarrior.enemy = enemy
        thisWarrior.strength = strength
        thisWarrior.speed = speed
    def __str__(thisWarrior):
        return "%s - %s" % (thisWarrior.name, "enemigo" if thisWarrior.enemy else "aliado")
    def __repr__(thisWarrior):
        return "Nam:%s Enemy:%s Life: %s Str:%s Spd:%s" % (thisWarrior.name, "Y" if thisWarrior.enemy else "N", thisWarrior.life, thisWarrior.strength, thisWarrior.speed)

allies = []
enemies = []

allies.append(Warrior("Ana",False,4,6))
allies.append(Warrior("Manolo",False,6,4))

enemies.append(Warrior("Rodolfo"))
enemies.append(Warrior("Lola"))

print("Allies:")
for ally in allies:
    print(ally)

print("Enemies:")
for enemy in enemies:
    print(enemy)

print("Debug:")
for item in allies + enemies:
    print(repr(item))

'''
Ejemplo 3:
'''
class Fellow:
    life = 100
    def __init__(thisFellow, name, strength = 5, speed = 5):
        thisFellow.name = name
        thisFellow.strength = strength
        thisFellow.speed = speed
    def __repr__(thisFellow):
        return "Nam:%s Life: %s Str:%s Spd:%s" % (thisFellow.name, thisFellow.life, thisFellow.strength, thisFellow.speed)

class Ally(Fellow):
    enemy = False
    def __init__(thisAlly, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(thisAlly):
        return "%s - Aliado" % (thisAlly.name)
    def __repr__(thisAlly):
        return super().__repr__() + " Ally"

class Enemy(Fellow):
    enemy = True
    def __init__(thisEnemy, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(thisEnemy):
        return "%s - Enemigo" % (thisEnemy.name)
    def __repr__(thisEnemy):
        return super().__repr__() + " Enemy"

ally = Ally("Ana",4,6)
enemy = Enemy("Pedro")

print(ally)
print(enemy)

print(repr(ally))
print(repr(enemy))

'''
Ejemplo 4:
'''
class Fellow:
    life = 100
    instances = []
    def __init__(self, name, strength = 5, speed = 5):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.__class__.instances.append(self)
    def __repr__(self):
        return "Nam:%s Life: %s Str:%s Spd:%s" % (self.name, self.life, self.strength, self.speed)

class Ally(Fellow):
    enemy = False
    def __init__(self, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(self):
        return "%s - Aliado" % (self.name)
    def __repr__(self):
        return super().__repr__() + " Ally"

class Enemy(Fellow):
    enemy = True
    def __init__(self, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(self):
        return "%s - Enemigo" % (self.name)
    def __repr__(self):
        return super().__repr__() + " Enemy"

allies = ("Ana", "Antonio")
enemies = ("Gabriel", "Lorena")

for name in allies:
    Ally(name)

for name in enemies:
    Enemy(name)

allies_life = 0
enemies_life = 0

print(Fellow.instances)

for guy in Fellow.instances:
    if guy.enemy:
        enemies_life += guy.life
    else:
        allies_life += guy.life

print("Vida aliados:", allies_life, "Vida enemigos:", enemies_life)

'''
Ejemplo 5:
'''
class Fellow:
    life = 100
    instances = []
    def __init__(self, name, strength = 5, speed = 5):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.__class__.instances.append(self)
    def __repr__(self):
        return "Nam:%s Life: %s Str:%s Spd:%s" % (self.name, self.life, self.strength, self.speed)
    def get_allies_life(self):
        life = 0
        for guy in self.instances:
            if guy.enemy == self.enemy:
                life += guy.life
        return life

class Ally(Fellow):
    enemy = False
    def __init__(self, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(self):
        return "%s - Aliado" % (self.name)
    def __repr__(self):
        return super().__repr__() + " Ally"


class Enemy(Fellow):
    enemy = True
    def __init__(self, name, strength = 5, speed = 5):
        super().__init__(name, strength, speed)
    def __str__(self):
        return "%s - Enemigo" % (self.name)
    def __repr__(self):
        return super().__repr__() + " Enemy"

allies = ("Ana", "Antonio")
enemies = ("Gabriel", "Lorena")

for name in allies:
    Ally(name)

for name in enemies:
    Enemy(name)

juana = Ally("Juana")

print("Vida aliados Juana:", juana.get_allies_life())