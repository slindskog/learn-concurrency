import time
from multiprocessing import Process
from multiprocessing.managers import SyncManager

port_num = 5555


def process_task(sem):
    manager = SyncManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy = manager.get_my_string()

    print(repr(proxy))
    print(str(proxy))
    print("Child process exiting in 5 seconds")

    time.sleep(5)
    sem._callmethod("release")

    # Invoking methods on the proxy's referent
    print(proxy._callmethod('isdigit'))
    print(proxy._callmethod('capitalize'))


def get_string():
    return 'educative'


if __name__ == '__main__':
    manager = SyncManager(address=('127.0.0.1', port_num))

    # Register our type
    my_string = 'educative'
    manager.register('get_my_string', callable=get_string)
    manager.start()

    # Get a proxy for a Semaphore
    sem = manager.Semaphore(0)

    # Pass the semaphore to the other process
    p = Process(target=process_task, args=(sem,))
    p.start()

    # Wait for the semaphore to be set
    sem._callmethod('acquire')

    print("Main process exiting")
