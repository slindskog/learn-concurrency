from concurrent.futures import ThreadPoolExecutor


def square(item):
    return item * item


def my_special_callback(ftr):
    res = ftr.result()
    print(f"my_special_callback invoked {res}")


def my_other_callback(ftr):
    res = ftr.result()
    print(f"my_other_callback invoked {res}")


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square, 7)
    future.add_done_callback(my_special_callback)
    future.add_done_callback(my_other_callback)

    executor.shutdown(wait=False)
