'''
Rangos
'''
print(list(range(10)))
print(list(range(5,10)))
print(list(range(10,100,5)))

'''
Ejemplo 1
'''
for num in range(10):
    print(num+2)

'''
Ejemplo 2
'''
for num in range(1,100,7):
    print(num)
    if num == 15:
        print("I found it!")
        break
else:
    print("I can't found a 15.")

'''
Ejemplo 3
'''
days = ["lunes","martes","miércoles","jueves"]
for day in days:
    print(day)

'''
Ejemplo 4
'''
incomings = {
    "lunes": 100.,
    "martes": 23.50,
    "miercoles": 33.21,
    "jueves": 0.
}
for day in incomings:
    print(day, incomings[day])