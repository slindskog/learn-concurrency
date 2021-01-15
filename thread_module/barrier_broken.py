import time
from threading import Barrier, Thread


def thread_task():
    print(f"\nCurrently {barrier.n_waiting} threads blocked on barrier")
    barrier.wait()
    print("Barrier broken")


if __name__ == '__main__':
    num_threads = 5
    barrier = Barrier(num_threads)

    threads = [0] * num_threads
    for i in range(num_threads):
        threads[i - 1] = Thread(target=thread_task)

    for i in range(num_threads):
        threads[i].start()

    time.sleep(3)

    print("Main thread about to invoke abort on barrier")
    barrier.abort()
