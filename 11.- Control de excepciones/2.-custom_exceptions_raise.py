class CuentoMucho(Exception):
    pass

print("Inicio")

try:
    counter = 0
    while True:
        if counter > 1000:
            raise CuentoMucho('Estoy contanto demasiado...')
        counter += 1
except CuentoMucho as error:
    print("Se ha producido un error:", error)

print("Fin")    