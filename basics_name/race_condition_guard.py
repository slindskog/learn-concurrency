import time
import random
from threading import Thread, Lock

rand_int = 0
lock = Lock()


def updater():
    global rand_int
    global lock
    while 1:
        with lock:
            rand_int = random.randint(1, 9)


def printer():
    global rand_int
    global lock
    while 1:
        with lock:
            # test
            if rand_int % 5 == 0:
                if rand_int % 5 != 0:
                    # and act
                    print(rand_int)


if __name__ == '__main__':
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 5 seconds
    time.sleep(5)
