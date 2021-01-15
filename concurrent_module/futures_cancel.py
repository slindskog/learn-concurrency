import time
from concurrent.futures import ThreadPoolExecutor


def square(item):
    time.sleep(5)
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)

    future1 = executor.submit(square, 7)
    future2 = executor.submit(square, 9)

    print(f"Is running: {future2.running()}")
    print(f"Is done: {future2.done()}")
    print(f"Attempt to cancel: {future2.cancel()}")
    print(f"Is cancelled: {future2.cancelled()}")

    executor.shutdown()
