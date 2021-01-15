import time
import random
import multiprocessing
from multiprocessing import Process, Manager, current_process
from multiprocessing.managers import BaseManager, ListProxy


def top_level_function():
    return (Manager()).list([f"set by {current_process().name}"])


def processA(port_num):
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_items', callable=top_level_function, proxytype=ListProxy)
    manager.start()

    time.sleep(3)


def processB(port_num):
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_items')
    manager.connect()
    proxy_items = manager.get_my_items()
    proxy_items.append("Eductive is Great!")

    print(proxy_items[0])
    print(proxy_items[1])


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    port_num = random.randint(10000, 60000)

    # Start another process which will access the shared string
    p1 = Process(target=processA, args=(port_num,))
    p1.start()

    time.sleep(0.8)

    p2 = Process(target=processB, args=(port_num,))
    p2.start()

    p1.join()
    p2.join()
