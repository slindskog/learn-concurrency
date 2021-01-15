import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

port_num = 5555


def process_task():
    manager = BaseManager(address=('127.0.0.1', port_num), authkey=b"MySecretKey")
    manager.register('get_my_string')
    manager.connect()
    proxy = manager.get_my_string()

    print(repr(proxy))
    print(str(proxy))

    print(proxy.isdigit())
    print(proxy.capitalize())


def get_string():
    return "educative"


if __name__ == '__main__':
    manager = BaseManager(address=('127.0.0.1', port_num), authkey=b'MySecretKey')

    # Register our type
    manager.register('get_my_string', callable=get_string)
    manager.start()

    p = Process(target=process_task)
    p.start()

    time.sleep(3)
    print("Exiting main process")
    manager.shutdown()
