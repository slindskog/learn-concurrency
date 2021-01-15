import time
from threading import Thread, Condition


def task1():
    cond_var.acquire()
    cond_var.wait()
    cond_var.release()


def task2():
    cond_var.acquire()
    cond_var.notify()
    cond_var.release()


# Do not run. Will hang.
if __name__ == '__main__':
    cond_var = Condition()

    # Start thread 2 first which invokes notify
    thread2 = Thread(target=task2)
    thread2.start()

    # Delay starting thread 1 by three seconds
    time.sleep(3)

    # Start thread 1
    thread1 = Thread(target=task1)
    thread1.start()

    thread1.join()
    thread2.join()
