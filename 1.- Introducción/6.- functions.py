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

'''
Ejemplo 4
'''
respuesta = input("¿Cuanto es 2 + 2?:")
print(respuesta)
print(len(respuesta))
print(type(respuesta))
print(respuesta + "4")
intRespuesta = int(respuesta)
print(type(intRespuesta))
print(intRespuesta + 4)
print(str(intRespuesta) + "...")

'''
Ejemplo 5
'''
def iva(importe,tipo=0.21):
    return importe * tipo

'''
Ejemplo 6
'''
def iva(tipo, *importes):
    print(type(importes))
    return tuple(imp * tipo for imp in importes)

subtotales = iva(0.21, 1, 20, 100) #Equivalente a iva(0.21, (1, 20, 100)) o a iva(0.21, tuple(1, 20, 100))
print(subtotales)

'''
Ejemplo 7
'''
def iva(tipo, articulos):
    print(type(articulos))
    for idx, val in articulos.items():
        articulos[idx] += val * tipo
    return articulos

carrito = {
    "leche": 2,
    "pan": 1,
}
subtotales = iva(0.21,carrito)
print(subtotales)

'''
Ejemplo 8
'''
a = lambda x: x*2

def a(x):
    return x*2

'''
Python built-in functions:
https://docs.python.org/3/library/functions.html
'''

print("Hello world")

abs(-5)
divmod(17, 3)

all([5>3, 2>4])
any([5>3, 2>4])
max([1,2,9,4,5])
min([9,8,1,7,6])

bin(255)
hex(255)
oct(255)
float("3")
int("3")
chr(97)
ord("a")
round(1.2)

str("a")
repr("a")

dict(one=1, two=2, three=3)
dict([('two', 2), ('one', 1), ('three', 3)])
list((1, 2, 3, 4))
list("hola")
tuple([1,2,3,4,5])
zip(["a","b","c"],[1,2,3])

enumerate(["a", "b", "c"])
reversed(["a", "b", "c"])
sorted(["b","c","a"])
guys = [
    {'name': "Daniel", 'age': 2},
    {'name': "Pedro", 'age': 13},
    {'name': "Ana", 'age': 5}
]
b = sorted(guys, key=lambda guy: guy['age'], reverse=True)

map(lambda x: x**2, [1,2,3,4])
filter(lambda x: x > 5, [1, 3, 5, 6 ,9])

input("Dime algo: ")

isinstance()
issubclass()
#super()

dir([])
len("cosa")
type(3)
vars()

help()