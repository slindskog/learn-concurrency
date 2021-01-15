import multiprocessing
from multiprocessing import Process
from threading import Lock


def process_task(lock):
    print("Child process")


if __name__ == '__main__':
    lock = Lock()
    multiprocessing.set_start_method('spawn')
    process = Process(
        target=process_task,
        args=(lock,)
    )
    process.start()
    process.join()
