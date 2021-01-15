import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait


def square(item):
    if item != 1:
        time.sleep(1)
    return item * item


if __name__ == '__main__':
    thread_executor = ThreadPoolExecutor(max_workers=10)
    process_executor = ProcessPoolExecutor(max_workers=10)

    items = []
    for i in range(1, 6):
        items.append(thread_executor.submit(square, i))

    for i in range(6, 11):
        items.append(process_executor.submit(square, i))

    # result = wait(items, timeout=None, return_when="ALL_COMPLETED")
    result = wait(items, timeout=0.01, return_when="FIRST_COMPLETED")

    print(f"Competed futures count: {len(result.done)} and uncompleted futures count: {len(result.not_done)}")

    for ftr in result.done:
        print(ftr.result())

    thread_executor.shutdown()
    process_executor.shutdown()
