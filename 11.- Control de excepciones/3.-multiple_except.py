from random import randint

class OdioElSeis(Exception):
    pass
class OdioElUno(Exception):
    pass

print("Inicio")

try:

    while True:
        number = randint(1,6)
        if number == 6:
            raise OdioElSeis('No quiero seises en mi vida.')
        if number == 1:
            raise OdioElUno('No hay nada peor que un uno.')
        else:
            raise Exception('No me gusta este juego.')

except OdioElUno as error:
    print("Se ha producido UN error:", error)
except OdioElSeis:
    print("Ha salido otro seis.")
except Exception as error:
    print("Algo ha pasado:", error)

print("Fin")    