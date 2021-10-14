# https://xkcd.com/353/
# https://docs.python.org/3/py-modindex.html

from random import randint
print(randint(0,10))

from datetime import datetime

now = datetime.now()
xmass = datetime(2021,12,25,23,59,59)

print(xmass - now)

from sys import path

print(path)

from os import name

print(name)

from base64 import b64encode, b64decode

original_text = """Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel augue
nec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,
sit amet cursus ante. In interdum laoreet mi, sit amet ultrices purus
pulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.
Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leo
felis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementum
dolor luctus. Curabitur lacinia mi ornare consectetur vestibulum."""
original_data = original_text.encode()

b64 = b64encode(original_data)
print(b64)
data = b64decode(b64)

text = data.decode()
print(data == original_data and text == original_text)