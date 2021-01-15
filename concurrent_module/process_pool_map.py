import os
from concurrent.futures import ProcessPoolExecutor


def square(item):
    print(f"Executed in process with id: {os.getpid()}", flush=True)
    return item * item


if __name__ == '__main__':
    print(f"Main process id: {os.getpid()}")
    executor = ProcessPoolExecutor(max_workers=10)

    it = executor.map(square, range(1, 10), chunksize=1)

    for sq in it:
        print(sq)

    executor.shutdown()
