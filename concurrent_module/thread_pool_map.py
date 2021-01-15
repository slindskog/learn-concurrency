import time
from concurrent.futures import ThreadPoolExecutor


def square(item):
    if item == 5:
        time.sleep(10)
    return item * item


# Timeout example
if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)
    it = executor.map(square, range(1, 10), chunksize=1, timeout=2)

    for sq in it:
        print(sq)

    executor.shutdown()
