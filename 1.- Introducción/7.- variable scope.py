'''
Ejemplo 1
'''
monedas = 53

def suma(a,b):
    monedas = a + b
    return monedas

r = suma(7,3)

print(monedas,r)
#print(a,b)

'''
Ejemplo 2
'''
resultado = None

def suma(a,b):
    global resultado
    resultado = a + b
    return resultado

r = suma(7,3)

print(resultado,r)

'''
Ejemplo 3
¡A EVITAR!
'''
resultado = None

def suma(a,b):
    global resultado
    resultado = a + b

suma(7,3)

print(resultado)

'''
Ejemplo 4
¿Porqué no funciona?
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
