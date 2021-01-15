import time
import multiprocessing
from threading import Lock

lock = Lock()


def process_task():
    lock.acquire()
    print("I am a child process")
    lock.release()


# Windows does not support fork
# Do not run. Deadlock example
if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    process = multiprocessing.Process(target=process_task)

    # Acquire the lock just before starting a new process
    lock.acquire()

    process.start()

    # Release the lock after starting the child process
    lock.release()

    # Wait for the child process to be done
    print("Parent process waiting for child process to finish")
    process.join()
    print("done")
