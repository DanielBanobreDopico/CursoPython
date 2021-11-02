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
print(dias[::2])
print(dias[1::2])

'''
Ejemplo 2
'''
dias = ['lunes','miercoles','sábado','domingo']
print(dias)

dias[1] = 'martes'
print(dias)

dias[2:4] = ['miercoles','jueves']
print(dias)

dias[4:6] += ['viernes', 'sabado']
print(dias)

dias[5:7] = ['sabado','domingo']
print(dias)

dias[0:7] = ['Uh','Ah']*3
print(dias)

'''
Ejemplo 3
Aclarar conceptos "referencia" frente a "copia". Puntero.
'''
tablero =[
    [' ','O','X'],
    ['O','X','X'],
    ['O','X','O']
]
print(tablero)

fila1 = tablero[0]
print(fila1)
print(fila1[1])

print(tablero[0][1])

tablero[0][0] = 'O'
print(tablero)

fila1[0] = 'X'
print(tablero)

'''
Ejemplo 4
Ojo con multiplicar listas: paso por referencia.
'''
print("Simple:")
tablero = ["X"]*3
print(tablero)
tablero[1] = "O"
print(tablero)

print("Multiplica filas")
tablero = [["X"]*3]*3
print(tablero)
tablero[1][1] = "O"
print(tablero)

print("Usando \"generador\"")
tablero = [["X"]*3 for idx in range(3)]
print(tablero)
tablero[1][1] = "O"
print(tablero)

'''
Ejemplo 5
'''
t = 1, 2, 3, 4
t = (1, 2, 3, 4)
a, b, c = [1, 2, 3]
a, b, c = (1, 2, 3)
a, b, c = 1, 2, 3
