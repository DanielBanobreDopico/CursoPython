'''
Ejemplo 1
'''
monedas = 53

def suma(a,b):
    resultado = a + b
    return resultado

r = suma(7,3)

#print(monedas,a,b,resultado,r)

'''
Ejemplo 2
'''
monedas = 53
resultado = None

def suma(a,b):
    global resultado
    resultado = a + b
    return resultado

r = suma(7,3)

print(monedas,resultado,r)

'''
Ejemplo 3
'''
resultado = None

def suma(a,b):
    global resultado
    resultado = a + b

suma(7,3)

print(resultado)

'''
Ejemplo 4
'''
resultado = None

def suma(a,b):
    resultado = a + b

suma(7,3)

print(resultado)

'''
Ejemplo 5
'''
manzanas = 25

def suma(manzanas,b):
    manzanas += b

suma(manzanas,3)

print(manzanas)

'''
Ejemplo 6
'''
manzanas = 25

def suma(manzanas,b):
    manzanas += b
    return manzanas

manzanas = suma(manzanas,3)

print(manzanas)
