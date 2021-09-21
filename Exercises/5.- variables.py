'''
Ejemplo 1
'''
alto =  5
ancho = 7
area = alto * ancho
print(area)

'''
Ejemplo 2
'''
alto, ancho = 5, 7
print(alto * ancho)

'''
Ejemplo 3
'''
alto = 5
ancho = alto
print(alto * ancho)

'''
Ejemplo 4
'''
monedas = 0
monedas = monedas + 5
print(monedas)
monedas = monedas - 3
print(monedas)

'''
Ejemplo 5
'''
monedas = 0
monedas += 5
print(monedas)
monedas -= 3
print(monedas)
monedas **= 10
monedas /= 2
print(monedas)

'''
Ejemplo 6
'''
nombre = 'Daniel'
sobrenombre = 'el Magnífico'
live = True
print(nombre, sobrenombre)
print('Con vida:', live)

'''
Ejemplo 7
'''
nombre = input('Introduce tu nombre: ')
sobrenombre = 'The Great'
live = True
print(sobrenombre, nombre)
print('Still alive:', live)