import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager, BaseProxy

port_num = 5555


class MyProxy(BaseProxy):
    def get_x(self):
        x = self._callmethod('get_x')
        return x * x


def process_task():
    manager = BaseManager(address=('', port_num))
    manager.register('get_pair', proxytype=MyProxy, create_method=False)
    manager.connect()

    p = manager.get_pair()
    print(p.get_x())


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

    manager = BaseManager(address=('', port_num))
    pair = Pair(15, 6)

    # Exposed: only can use the method get_x
    manager.register('get_pair', callable=lambda: pair, exposed=['get_x'])
    manager.start()
    p1.start()

    time.sleep(3)
    manager.shutdown()
