from mix import *
print(dir())
print(string.add(1,3))

import mix
print(dir(mix))
print(mix.string.add(1,3))

from mix.string import add

print(add(3,4))