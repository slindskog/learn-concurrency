import time
from threading import Condition, Thread

flag = False
cond_var = Condition()


def child_task():
    cond_var.acquire()
    if flag == False:
        cond_var.wait(1)

    if flag == False:
        print("Child thread times out waiting for notification")

    # Don't forget to release the lock
    cond_var.release()


if __name__ == '__main__':
    thread = Thread(target=child_task)
    thread.start()

    time.sleep(3)
    thread.join()
