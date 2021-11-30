# context management protocol
with open('file.txt') as ficheiro:
    for i in ficheiro.readlines():
        print(i)


class Cousa:
    def __enter__(self):
        print("Entrando")
        return range(0,5)
    def __exit__(self, type, val, traceback):
        print("Saliendo", type, val, traceback)

with Cousa() as cousa:
    for i in cousa:
        print(i)

