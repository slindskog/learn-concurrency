import time
import random
from threading import Thread
from multiprocessing import Process
from multiprocessing.managers import BaseManager


def processA(port_num):
    my_string = "Hello world"
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string', callable=lambda: my_string)
    server = manager.get_server()

    Thread(target=shutdown, args=(server,)).start()

    server.serve_forever()


def processB(port_num):
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy_my_string = manager.get_my_string()

    print(f"In processB repr(proxy_my_string): {repr(proxy_my_string)}")
    print(f"In processB str(proxy_my_string): {str(proxy_my_string)}")

    print(proxy_my_string)
    print(proxy_my_string.capitalize())
    print(proxy_my_string._callmethod("capitalize"))


def shutdown(server):
    time.sleep(3)
    server.stop_event.set()


if __name__ == '__main__':
    port_num = random.randint(10_000, 60_000)

    # Start another process which will access the shared string
    p1 = Process(target=processA, args=(port_num,), name="ProcessA")
    p1.start()

    time.sleep(1)

    p2 = Process(target=processB, args=(port_num,), name="ProcessB")
    p2.start()

    p1.join()
    p2.join()
