import time
import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import BaseManager

port_num = 5555


def process_task():
    manager = BaseManager(address=('', port_num))
    manager.register('get_pair')
    manager.connect()

    p = manager.get_pair()
    p.set_x(7)
    p.set_y(7)
    print(p.get_x())
    print(p.get_y())


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


# This doesn't seem to work on Windows, but should throw an AttributeError
if __name__ == '__main__':
    p1 = Process(target=process_task)

    manager = BaseManager(address=('', port_num))
    pair = Pair(5, 6)
    # Exposed: only can use the method get_x
    manager.register('get_pair', callable=lambda: pair, exposed=['get_x'])
    manager.start()
    p1.start()

    time.sleep(3)
    manager.shutdown()
