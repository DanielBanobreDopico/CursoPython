import basic

print(dir(basic))
print(basic.suma(2,5))
print(basic.PI)

import basic as math

print(math.suma(1,3))

from basic import suma, PI

print(suma(5,PI))

from basic import suma as sum, PI as P

print(sum(3,P))

from basic import *

print(resta(5,PI))