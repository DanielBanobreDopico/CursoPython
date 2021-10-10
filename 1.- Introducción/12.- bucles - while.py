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
vocales = []
vocal = input("Dime una vocal: ")
while vocal in ["a","e","i","o","u"] and vocal not in vocales:
    vocales += [vocal]
    if len(vocales) == 5:
        print("Conoces todas las vocales.")
        break
    vocal = input("Dime otra vocal: ")
else:
    print("Esto no está bien.")