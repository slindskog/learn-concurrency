import time
from ctypes import c_bool
import multiprocessing
from multiprocessing import Semaphore, Process, Value


def process_A(sem1, sem2, exit):
    while not exit.value:
        print("ping", flush=True)
        sem1.release()
        sem2.acquire()
        time.sleep(0.05)


def process_B(sem1, sem2, exit):
    while not exit.value:
        # Wait for a prime number to become available
        sem1.acquire()
        print("pong", flush=True)
        sem2.release()
        time.sleep(0.05)


if __name__ == '__main__':
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)

    exit_prog = Value(c_bool, False)

    processA = Process(target=process_A, args=(sem1, sem2, exit_prog))
    processA.start()

    processB = Process(target=process_B, args=(sem1, sem2, exit_prog))
    processB.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog.value = True

    processA.join()
    processB.join()
