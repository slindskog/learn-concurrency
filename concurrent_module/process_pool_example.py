import os
import multiprocessing
from multiprocessing import current_process
from threading import current_thread
from concurrent.futures import ProcessPoolExecutor


def say_hi(item):
    print(f"\nHi {item} executed in thread id: {current_thread().name} in process id: {os.getpid()} with name "
          f"{current_process().name}", flush=True)


if __name__ == '__main__':
    print(f"Main process id: {os.getpid()}")
    multiprocessing.set_start_method("spawn")
    executor = ProcessPoolExecutor(max_workers=10)
    items = []
    for i in range(1, 10):
        items.append(executor.submit(say_hi, f"guest {i}"))

    for future in items:
        future.result()

    executor.shutdown()
