import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import SyncManager


def process1(ns):
    print(ns.item)
    ns.item = 'educative'


def process2(ns):
    print(ns.item)
    ns.item = "Educative is awesome!"


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")

    # Create a namespace
    manager = SyncManager(address=('127.0.0.1', 55555))
    manager.start()
    shared_vars = manager.Namespace()
    shared_vars.item = "empty"
    # shared_vars._item = "empty"  # underscore will create an attribute on the namespace proxy and not on referent

    # Create the first process
    p1 = Process(target=process1, args=(shared_vars,))
    p1.start()
    p1.join()

    # Create the second process
    p2 = Process(target=process2, args=(shared_vars,))
    p2.start()
    p2.join()

    print(shared_vars.item)
