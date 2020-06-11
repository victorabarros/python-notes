from threading import Thread
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(.5)


t = Thread(target=countdown, args=(10,))
t.start()
