from warnings import warn

print("Inicio")

try:
    counter = 0
    while True:
        if counter == 1000:
            warn("Ya me estoy cansando.")
        if counter > 1000:
            raise Exception('Estoy contanto demasiado...')
        counter += 1
except Exception as error:
    print("Se ha producido un error:", error)

print("Fin")