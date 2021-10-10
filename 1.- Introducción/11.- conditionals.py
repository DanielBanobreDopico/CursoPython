'''
Ejemplo 1
'''
def saldoSuficiente(importe, saldo):
    if saldo >= importe:
        print("Suficiente saldo para pagar %s€." % importe)
        return True

print(saldoSuficiente(100, 150))
print(saldoSuficiente(1000,12))

'''
Ejemplo 2
'''
def saldoSuficiente(importe, saldo):
    if saldo >= importe:
        print("Suficiente saldo para pagar %s€." % importe)
        return True
    else:
        print("No te llega. Sólo tienes %s€." % saldo)
        return False

print(saldoSuficiente(100, 150))
print(saldoSuficiente(1000,12))

'''
Ejemplo 3
'''
def saldoSuficiente(importe, saldo):
    diferencia = saldo - importe
    if (saldo >= importe) & (diferencia >= 100):
        print("Suficiente saldo para pagar %s€." % importe)
        return True
    elif (saldo >= importe) & (diferencia < 100):
        print("Te llega para pagar, pero te quedas con solo %s€." % (saldo - importe))
        return None
    elif importe >= saldo:
        print("No te llega. Sólo tienes %s€." % saldo)
        return False
    else:
        print("No se muy bien que decirte. No estoy programado para esta situación: saldo %s e importe %s" % diferencia)
        return None

print(saldoSuficiente(100, 150))
print(saldoSuficiente(1000,12))
print(saldoSuficiente(10,10000))

'''
Ejemplo 4
'''
numero = 5
es_par = True if 5%2 == 0 else False
print(es_par)

'''
Ejemplo 5
'''
valid_numbers = [1,3,5,6,7]
if 5 in valid_numbers:
    print("Ok")
else:
    print("Ugly number")