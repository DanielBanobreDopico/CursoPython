'''
Ejemplo 1
'''
dias = ['lunes','miercoles','sábado','domingo']
print(dias[0])
print(dias[0:2])
print(dias[:2])
print(dias[2:])
print(dias[:])
print(dias[0:3:2])

'''
Ejemplo 2
'''
dias[1] = 'martes'
dias[2:4] = ['miercoles','jueves']
dias[4:6] += ['viernes', 'sabado']
dias[5:7] = ['sabado','domingo']
print(dias)

'''
Ejemplo 3
'''
tablero =[
    [' ','O','X'],
    ['O','X','X'],
    ['O','X','O']
]
print(tablero[0])
print(tablero[0][2])
tablero[0][0] = 'O'
print(tablero)