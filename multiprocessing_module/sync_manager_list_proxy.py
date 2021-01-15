from multiprocessing import Process
from multiprocessing.managers import SyncManager

port_num = 5555


def process_task1(sem1, sem2, lst):
    lst[0] = 1
    sem1.release()
    sem2.acquire()
    print(f"Process 1 sees list as: {lst}")
    print("Process 1 exiting")


def process_task2(sem1, sem2, lst):
    sem1.acquire()
    print(f"Process 2 sees list as: {lst}")
    lst[0] = 2
    sem2.release()
    print("Process 2 exiting")


if __name__ == '__main__':
    manager = SyncManager(address=('127.0.0.1', port_num))
    manager.start()

    # Get a proxy for a Semaphore
    sem1 = manager.Semaphore(0)
    sem2 = manager.Semaphore(0)
    lst = manager.list([0, 0, 0])

    # Create the first process
    p1 = Process(target=process_task1, args=(sem1, sem2, lst))
    p1.start()

    # Create the second process
    p2 = Process(target=process_task2, args=(sem1, sem2, lst))
    p2.start()

    p1.join()
    p2.join()

    print("Main process exiting")
