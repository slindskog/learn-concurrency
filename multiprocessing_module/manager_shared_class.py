import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager, BaseProxy

port_num = 5556


class MyProxy(BaseProxy):
    def get_x(self):
        x = self._callmethod('get_x')
        return x * x


def process_task():
    manager = BaseManager(address=('', port_num))
    manager.register('get_pair')
    manager.connect()

    obj1 = manager.get_pair(1, 3)
    obj2 = manager.get_pair(2, 3)

    # Verify two different objects are created
    print(obj1.get_x())
    print(obj2.get_x())


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


# Doesn't appear to work on Windows...
if __name__ == '__main__':
    p1 = Process(target=process_task)
    manager = BaseManager(address=('127.0.0.1', port_num))

    # Exposed: only can use the method get_x
    manager.register('get_pair', Pair)
    manager.start()
    p1.start()

    time.sleep(3)
    manager.shutdown()
