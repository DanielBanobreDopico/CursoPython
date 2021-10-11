FILA_REFERENCIA = 4
PRECIO_FILA_REFERENCIA = 6.0
DECREMENTO_FILAS = 0.2
CINE = [[True]*20 for i in range(15)]
caja = 0.0

def precio_butaca(fila):
    return PRECIO_FILA_REFERENCIA - (abs(fila - FILA_REFERENCIA) * DECREMENTO_FILAS)

def filas_libres():
    LIBRES = []
    fila_idx = 0
    for fila in CINE:
        if True in fila:
            LIBRES += [fila_idx]
        fila_idx += 1
    return LIBRES

def precios_filas_libres():
    FILAS = filas_libres()
    PRECIOS = []
    for fila in FILAS:
        PRECIOS += [precio_butaca(fila)]
    return zip(FILAS, PRECIOS)

def butacas_libres(fila):
    if fila in filas_libres():
        LIBRES = []
        butaca_idx = 0
        for butaca in CINE[fila]:
            if butaca:
                LIBRES += [butaca_idx]
            butaca_idx += 1
        PRECIOS = [precio_butaca(fila)] * len(LIBRES)
        return zip(LIBRES, PRECIOS)
    else:
        print("No hay butacas libres en la fila", fila)

def butaca_libre(fila, butaca):
    return CINE[fila][butaca]

def vender_butaca(fila, butaca):
    global caja
    CINE[fila][butaca] = False
    print("Tiene asignada la butaca %s de la fila %s" % (butaca, fila))
    caja += precio_butaca(fila)
    print("Recaudación actual:", caja)

def main():
    print(filas_libres())

    fila = None
    while fila not in filas_libres():
        if fila != None:
            print("La fila %s no tiene butacas disponibles" % fila)
        fila = int(input("Fila: "))
    else:
        print("Seleccionada la fila", fila)

    print(list(butacas_libres(fila)))

    butaca = int(input("Elija una butaca en la fila: "))

    while not butaca_libre(fila,butaca):
        print("La butaca %s no esrá disponibles" % butaca)
        butaca = int(input("Elija otra butaca: "))
    else:
        print("Seleccionada la butaca %s de la fila %s" % (butaca, fila))

    vender_butaca(fila, butaca)

while True:
    main()