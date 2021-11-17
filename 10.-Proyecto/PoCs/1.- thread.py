from threading import Thread
from time import sleep

counter = {
    'value': 0,
}

def secondary_task(seconds, counter):
    while counter["value"] < 5:
        counter["value"] += 1
        print('Tarea secundaria:', counter["value"])
        sleep(seconds)

secondary_thread = Thread(target=secondary_task, args=(1, counter))
secondary_thread.start()

while counter["value"] < 3:
    print('Tarea primaria:', counter["value"])
    sleep(0.5)