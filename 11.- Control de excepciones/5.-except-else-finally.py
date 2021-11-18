print("Inicio")

def getNumber():
    print("llamada función")
    try:
        print("try: Inicio")
        i = input("Numero: ")
        number = int(i) #ERROR si i no es un número entero
        print("try: Final")
    except Exception as error:
        print("except: Error!")
        raise error
    else:
        print("else: Todo ha ido bien.")
    finally:
        print("finally: ...")
    print("return función")
    return number



try:
    numero = getNumber()
except:
    print("Ups! Algo va mal. Asignando 0 a numero.")
    numero = 0



print("Número es:", numero)

print("Fin")  