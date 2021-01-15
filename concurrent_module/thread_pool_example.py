from threading import current_thread
from concurrent.futures import ThreadPoolExecutor


def say_hi(item):
    print(f"\nHi {item} executed in thread id: {current_thread().name}", flush=True)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)
    items = []
    for i in range(1, 10):
        items.append(executor.submit(say_hi, f"guest {i}"))

    for future in items:
        future.result()

    executor.shutdown()
