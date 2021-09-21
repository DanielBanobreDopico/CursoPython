'''
Ejemplo 1
'''
def suma(a,b):
    resultado = a + b
    return resultado

r = suma(5,7)
print(r)
print(suma(5,7))

'''
Ejemplo 2
'''
def suma(a,b):
    resultado = a + b
    print('%s + %s = %s' % (a, b, resultado))

r = suma(5,7)
print(r)

'''
Ejemplo 3
'''
def suma(a,b):
    return a + b

r = suma(5,7)
print(r)

'''
Ejemplo 4
'''
def iva(subtotal):
    return subtotal * .21

def total(subtotal):
    return subtotal + iva(subtotal)

print(total(50))