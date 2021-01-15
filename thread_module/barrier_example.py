import time
import random
from threading import Barrier, Thread


def thread_task():
    time.sleep(random.randint(0, 7))
    print(f"Currently {barrier.n_waiting} threads blocked on barrier.")
    barrier.wait()


if __name__ == '__main__':
    num_threads = 5
    barrier = Barrier(num_threads)
    threads = [0] * num_threads
    for i in range(num_threads):
        threads[i - 1] = Thread(target=thread_task)

    for i in range(num_threads):
        threads[i].start()
