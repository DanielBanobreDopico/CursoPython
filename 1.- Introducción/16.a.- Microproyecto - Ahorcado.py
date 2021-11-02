"""
Juego del ahorcado.
* El ordenador tiene una PALABRA que el jugardor intentará adivinar.
* Se muestra el dibujo incompleto de un cadalso.
* Bajo el cadalso se muestran las posiciones bacías para cada una de las letras de la palabra.
* El jugador propone letras turno tras turno.
* Las letras propuestas por el jugador que formen parte de la palabra se muestran en las posiciones adecuadas bajo el cadalso.
* El jugador puede intentar adivinar la palabra en cada turno.
* El jugador gana si completa todas las letras de la palabar o la adivina en un intento.
* El jugador pierde si se completa el dibujo del cadalso o falla en un intento de adivinar la palabra.

Indicaciones para el programa
* Crea un bucle que se repita mientras "ganador" sea None.
* En cada iteración (ciclo) del bucle:
  * Imprime el texto de "CADALSO" correspondiente al valor de "errores".
  * Imprime un string de tal modo que, para cada letra de la palabra a adivinar:
    * Si la letra está en LETRAS_ACERTADAS, muestra la letra.
    * Si la letra NO está en la lista LETRAS_ACERTADAS, muestra el caracter "_".
  * Pide una letra al jugador
  * Si el jugador proporciona una letra:
    * Comprueba si la letra forma parte de la palabra.
    * Si forma parte de la palabra, añadela a la lista de LETRAS_ACERTADAS.
    * Si NO forma parte de la palabra, incrementa el contador "errores".
  * Si el jugador NO proporciona una letra:
    * Pide al jugador que intente adivinar la palabra.
    * Si el jugador acierta la palabra, asigna True a "acerto_palabra".
    * Si el jugador NO acierta la palabra, asigna False a "acerto_palabra".
  * Si errores es igual a la longitud de "CADALSO" menos uno, asigna False a "ganador".
  * Si acerto_palabra es False, asigna False a "ganador".
  * Si acerto_palabra es True, asigna True a "ganador".
  * Si todas las letras de PALABRA están en LETRAS_ACERTADAS, asigna True a "ganador".
* Finalizado el bucle:
  * Si ganador es True imprime "Ha ganado".
  * Si ganador es Falso imprime "Has perdido".
"""

PALABRA = "ALMACIGA"

errores = 0

LETRAS_ACERTADAS = []

acerto_palabra = None

ganador = None

CADALSO = [
 """
 
 │
 │
 │
 │
 │
 │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │
 │
 │
 │
 │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │      O
 │
 │
 │
 │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │      O
 │      │
 │      │
 │
 │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │      O
 │     ┌┼┐
 │     │││
 │
 │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │      O
 │     ┌┼┐
 │     │││
 │     ┌┴┐
 │     │ │
 │
 │
 ┴───────────
 """,
 """
 ┌──────┐
 │      │
 │      O
 │     ┌┼┐
 │     │││
 │     ┌┴┐
 │     │ │
 │     ┘ └
 │
 ┴───────────
 """
]

print("El juego del ahorcado")

print(CADALSO[6])

while (ganador == None):
    cadena_a_mostrar = ""
    todas_las_letras_acertadas = True
    print(CADALSO[errores])
    for letra in PALABRA:
        if letra in LETRAS_ACERTADAS:
            cadena_a_mostrar += letra
        else:
            cadena_a_mostrar += "_"
    print(cadena_a_mostrar)
    letra_propuesta = input("Introduce una letra o vacío para adivinar: ")
    
    if letra_propuesta == "":
        intento_adivinar = input("¿Cuál es la palabra?: ")
        acerto_palabra = True if intento_adivinar == PALABRA else False
    elif letra_propuesta in PALABRA:
        LETRAS_ACERTADAS.append(letra_propuesta)
    else:
        errores += 1
    
    for letra in PALABRA:
        if letra not in LETRAS_ACERTADAS:
            todas_las_letras_acertadas = False 

    if errores == len(CADALSO)-1 or acerto_palabra == False:
        ganador = False
    elif todas_las_letras_acertadas == True or acerto_palabra == True:
        ganador = True
        
print("Has ganado" if ganador == True else "Has perdido")
    