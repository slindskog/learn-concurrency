import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

# Port number on which the manager runs on and another can connect at
port_num = 55555


def process_task():
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy = manager.get_my_string()

    print(repr(proxy))
    print(str(proxy))

    print(proxy.isdigit())
    print(proxy.capitalize())


def get_string_callable(s):
    def str_callable():
        return s

    return str_callable


# Doesn't appear to work on Windows
if __name__ == '__main__':
    manager = BaseManager(address=('127.0.0.1', port_num))

    # Register our type
    my_string = 'educative'

    str_func = get_string_callable(my_string)

    manager.register('get_my_string', callable=str_func)
    manager.start()

    p = Process(target=process_task)
    p.start()

    time.sleep(3)
    print('Exiting main process')
    manager.shutdown()
