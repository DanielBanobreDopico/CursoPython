código_unicode = 'U+1F605' # Python 3 soporta unicode incluso en los nombres de variables.
parte_numérica_del_código = código_unicode[2:] # Lo anterior no implica que sea buena idea usarlo.
valor_numérico_del_código = (int(parte_numérica_del_código,16)) #16 porque está en base 16, hexadecimal.
print(código_unicode)
print(parte_numérica_del_código)
print(valor_numérico_del_código)
print(chr(valor_numérico_del_código))
print(chr(int(código_unicode[2:],16))) #En una linea y sin nombres absurdos de variables
print('\U0001F605')