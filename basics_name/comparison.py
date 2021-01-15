import time
from queue import Queue
from threading import Thread
import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import BaseManager


class SumUp:
    def __init__(self):
        self.counter = 0

    def add_ints(self, start, end):
        for i in range(start, end + 1):
            self.counter += 1

    def get_counter(self):
        return self.counter


def single_thread():
    obj = SumUp()
    start = time.time()
    obj.add_ints(1, 30_000_000)
    end = time.time() - start
    print(f"Single threaded took: {end} seconds and summed to {obj.counter}")


def multiple_threads():
    start = time.time()
    obj1 = SumUp()
    obj2 = SumUp()

    t1 = Thread(target=obj1.add_ints, args=(1, 15_000_000))
    t2 = Thread(target=obj2.add_ints, args=(15_000_001, 30_000_000))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    combined_sum = obj1.counter + obj2.counter
    end = time.time() - start
    print(f"Multiple threads took: {end} seconds and summed to {combined_sum}")


def single_process(obj1, start, end):
    obj1.add_ints(start, end)


def multiple_processes():
    start = time.time()
    BaseManager.register('SumUp', SumUp)
    manager = BaseManager(address=('127.0.0.1', 63333))
    manager.start()

    obj1 = manager.SumUp()
    obj2 = manager.SumUp()
    start = time.time()

    p1 = Process(target=single_process, args=(obj1, 1, 15000000,))
    p2 = Process(target=single_process, args=(obj2, 15000001, 30000000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    combined_sum = obj1.get_counter() + obj2.get_counter()
    end = time.time() - start
    print(f'Multiple processes took: {end} seconds and summed to {combined_sum}')
    manager.shutdown()


if __name__ == '__main__':
    print(f"System has {multiprocessing.cpu_count()} CPUs")
    single_thread()
    multiple_threads()
    multiple_processes()
