import datetime
import threading


def everyFive():
    threading.Timer(5.0, everyFive).start()
    print("hi")


current = datetime.datetime.now().time()
print('You clocked in at ' + str(current))

everyFive()
