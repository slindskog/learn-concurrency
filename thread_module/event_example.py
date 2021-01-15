import time
from threading import Thread, Event


def task1():
    event.wait()
    event.wait()
    event.wait()
    print("Thread invoked wait() thrice")


def task2():
    time.sleep(1)
    print('Thread2 about to set event')
    event.set()


if __name__ == '__main__':
    event = Event()

    thread1 = Thread(target=task1)
    thread1.start()

    thread2 = Thread(target=task2)
    thread2.start()

    thread1.join()
    thread2.join()
