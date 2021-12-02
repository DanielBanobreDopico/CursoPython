# Class implementing a Context Manager.
class ReadableFile:
    def __init__(self,filePath):
        self.__file = open(filePath,"r") # read only
    def __enter__(self):
        print("===> Entering")
        return self.__file # return the object to use inner "with"
    def __exit__(self, type, val, traceback):
        if not self.__file.closed: self.__file.close()
        print("===> Saliendo: self.__file.closed\n\n", type, val, traceback)

# Using 'with' in exception handler
try:
    with ReadableFile('cousa.txt') as cousa:
        print("First line: %s" % cousa.readline())
        cousa.write("New content.") # Error: read only file.
except Exception as err:
    print(err)

print("===> Fin")

