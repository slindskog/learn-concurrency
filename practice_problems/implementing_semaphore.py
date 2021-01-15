import time
from threading import Thread, Condition


class CountSemaphore:

    def __init__(self, permits):
        self.max_permits = permits
        self.given_out = 0
        self.cond_var = Condition()

    def acquire(self):
        self.cond_var.acquire()
        while self.given_out == self.max_permits:
            self.cond_var.wait()
        self.given_out += 1
        self.cond_var.notifyAll()
        self.cond_var.release()

    def release(self):
        self.cond_var.acquire()
        while self.given_out == 0:
            self.cond_var.wait()
        self.given_out -= 1
        self.cond_var.notifyAll()
        self.cond_var.release()


def task1(sem):
    # Consume the first permit
    sem.acquire()
    print("acquiring")
    sem.acquire()
    print("acquiring")
    sem.acquire()
    print("acquiring")
    sem.acquire()


def task2(sem):
    time.sleep(2)
    print("releasing")
    sem.release()

    time.sleep(2)
    print("releasing")
    sem.release()

    time.sleep(2)
    print("releasing")
    sem.release()


if __name__ == '__main__':
    sem = CountSemaphore(1)

    t1 = Thread(target=task1, args=(sem,))
    t2 = Thread(target=task2, args=(sem,))

    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()
