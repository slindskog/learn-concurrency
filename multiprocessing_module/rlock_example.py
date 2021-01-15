import time
import multiprocessing
from multiprocessing import Process, RLock, current_process


def child_task(rlock):
    for _ in range(5):
        rlock.acquire()
        print(f"I am child process: {current_process().name}")
        time.sleep(0.01)

    for _ in range(5):
        rlock.release()


if __name__ == '__main__':
    # multiprocessing.set_start_method('fork')

    rlock = RLock()
    rlock.acquire()

    process1 = Process(target=child_task, args=(rlock,))
    process1.start()

    process2 = Process(target=child_task, args=(rlock,))
    process2.start()

    # Sleep 3 seconds before releasing the lock
    time.sleep(3)
    rlock.release()

    process1.join()
    process2.join()
