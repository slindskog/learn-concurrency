import time
from threading import Thread, Condition, current_thread

flag = False
cond_var = Condition()


def child_task():
    global flag
    name = current_thread().getName()

    cond_var.acquire()
    if not flag:
        cond_var.wait()
        print(f"\n{current_thread().getName()} woken up \n")

    cond_var.release()

    print(f"\n{current_thread().getName()} exiting\n")


if __name__ == '__main__':
    thread1 = Thread(target=child_task, name="thread1")
    thread2 = Thread(target=child_task, name="thread2")
    thread3 = Thread(target=child_task, name="thread3")

    thread1.start()
    thread2.start()
    thread3.start()

    cond_var.acquire()
    cond_var.notifyAll()
    cond_var.release()

    thread1.join()
    thread2.join()
    thread3.join()

    print("\nMain thread exits\n")
