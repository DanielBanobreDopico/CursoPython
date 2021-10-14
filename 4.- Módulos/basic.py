if __name__ == "__main__":
    import sys
    print("Cosas que hacer si ejecuto el módulo...")
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)

PI = 3.14

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y