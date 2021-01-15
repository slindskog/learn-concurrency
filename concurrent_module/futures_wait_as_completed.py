import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def square(item):
    if item <= 5: time.sleep(5 - item)
    return item * item


if __name__ == '__main__':
    process_executor = ProcessPoolExecutor(max_workers=10)

    items = []
    for i in range(1, 5):
        items.append(process_executor.submit(square, i))

    result = as_completed(items, timeout=None)

    for ftr in result:
        print(ftr.result())

    process_executor.shutdown()
