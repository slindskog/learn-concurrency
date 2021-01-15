import time
from threading import Thread, Semaphore


def task1():
    sem.acquire()


def task2():
    sem.release()


if __name__ == '__main__':
    # Initialize with zero
    sem = Semaphore(0)

    # Start thread 2 first which invokes release
    thread2 = Thread(target=task2)
    thread2.start()

    # Delay starting thread 1 by three seconds
    time.sleep(3)

    # Start thread 1
    thread1 = Thread(target=task1)
    thread1.start()

    thread1.join()
    thread2.join()
