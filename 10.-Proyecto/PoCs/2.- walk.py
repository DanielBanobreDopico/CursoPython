from time import sleep

path = ['_']*10

for idx in range(100):
    position = idx % len(path)
    old_position = (idx - 1) % len(path)
    path[old_position] = '_'
    path[position] = "¡"
    print(path)
    sleep(0.1)

'''
for idx in reversed(range(100)):
    position = idx % len(path)
    old_position = (idx + 1) % len(path)
    path[old_position] = '_'
    path[position] = "🚶"
    print(path)
    sleep(0.3)
'''