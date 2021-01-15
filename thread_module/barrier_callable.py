import time
import random
from threading import Barrier, Thread, current_thread


def thread_task():
    time.sleep(random.randint(0, 5))
    print(f"\nCurrently {barrier.n_waiting} threads blocked on barrier")
    barrier.wait()


def when_all_threads_released():
    print(f"All threads released. Reported by: {current_thread().getName()}")


if __name__ == '__main__':
    num_threads = 5
    barrier = Barrier(num_threads, action=when_all_threads_released)

    threads = [0] * num_threads
    for i in range(num_threads):
        threads[i - 1] = Thread(target=thread_task)

    for i in range(num_threads):
        threads[i].start()
