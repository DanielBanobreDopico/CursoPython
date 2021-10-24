text = """Muchas cosas que contar.
Las guardaré en un fichero.
Y luego lo cerraré."""
text_file = open("text.txt","w")
text_file.write(text)
text_file.close()

text_file = open("text.txt","r")
first_line = text_file.readline()
print(first_line)
text_file.close()

text_file = open("text.txt","a")
import base64
from ctypes import sizeof
from datetime import datetime
text_file.write("\n" + str(datetime.now()))
text_file.close()
text_file = open("text.txt","r")
lines = text_file.readlines()
for idx, line in enumerate(lines):
    print(idx + 1, line)
text_file.close()

text_file = open("text.txt","a+") # a+ = a+r, w+ = w+r, r+ = r+w
from datetime import datetime
text_file.write("\n" + str(datetime.now()))
text_file.seek(0,0)
text = text_file.read()
print(text)
text_file.close()

from base64 import b64encode
binary_file = open("photo.jpg","rb")
image = binary_file.read()
binary_file.close()
b64string = b64encode(image).decode()
print(len(b64string))

from os.path import getsize
file_len = getsize("photo.jpg")
binary_file = open("photo.jpg","rb")
start = binary_file.read(10)
print("Position:", binary_file.tell())
binary_file.seek(int(file_len / 2))
print("Position:", binary_file.tell())
middle = binary_file.read(10)
binary_file.seek(file_len-10, 0)
end = binary_file.read()
print(len(start),len(end))
