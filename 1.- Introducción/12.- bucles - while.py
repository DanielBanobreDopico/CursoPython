'''
Ejemplo 1
'''
i = 0
while i < 5:
    print(i)
    i += 1

'''
Ejemplo 2
'''
vocales = ["a","e","i","o","u"]
vocales_introducidas = []

vocal = input("""Veamos si conoces el orden de las vocales.
Dime una vocal: """)

while vocal in vocales and vocal not in vocales_introducidas:
    vocales_introducidas += [vocal]
    print(vocales_introducidas)
    if vocales_introducidas == vocales:
        print("Conoces el orden de todas las vocales.")
        break
    vocal = input("Dime otra vocal: ")
else:
    print("Esto no está bien.")
