import time
from concurrent.futures import ThreadPoolExecutor


def square(item):
    # Simulate a computation by sleeping
    time.sleep(5)
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square, 7)

    print(f"Is running: {future.running()}")
    print(f"Is done: {future.done()}")
    print(f"Attempt to cancel: {future.cancel()}")
    print(f"Is cancelled: {future.cancelled()}")

    executor.shutdown()
