import time
from threading import Thread, Condition, current_thread


class Barrier:
    def __init__(self, size):
        self.barrier_size = size
        self.reached_count = 0
        self.cond = Condition()

    def arrived(self):
        self.cond.acquire()
        self.reached_count += 1
        if self.reached_count == self.barrier_size:
            self.cond.notifyAll()
            self.reached_count = 0
        else:
            self.cond.wait()
        self.cond.release()


def thread_process(sleep_for):
    time.sleep(sleep_for)
    print(f"Thread {current_thread().getName()} reached the barrier")
    barrier.arrived()

    time.sleep(sleep_for)
    print(f"Thread {current_thread().getName()} reached the barrier")
    barrier.arrived()

    time.sleep(sleep_for)
    print(f"Thread {current_thread().getName()} reached the barrier")
    barrier.arrived()


if __name__ == '__main__':
    # This version has a serious bug.
    # The wait() method should always be used in a while loop that checks for a condition
    # and if found false, should make the thread wait again.
    barrier = Barrier(3)

    t1 = Thread(target=thread_process, args=(0,))
    t2 = Thread(target=thread_process, args=(0.5,))
    t3 = Thread(target=thread_process, args=(1.5,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
