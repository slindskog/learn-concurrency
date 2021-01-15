from concurrent.futures import ThreadPoolExecutor


def square(item):
    item = None
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square, 7)
    ex = future.exception()
    print(ex)

    executor.shutdown()
