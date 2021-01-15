import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import SyncManager

port_num = 5555


def process_task1(list_proxy):
    list_proxy[0] = 1
    print(f"Process 1 sees list as: {list_proxy}")
    nested_list = list({})
    list_proxy.append(nested_list)

    nested_list.append(99)
    nested_list.append(98)
    nested_list.append(97)
    print(f"Child process sees list as: {list_proxy}")
    list_proxy[3] = nested_list
    print(f"Child process sees list as: {list_proxy}")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    manager = SyncManager(address=('127.0.0.1', port_num))
    manager.start()
    lst = manager.list([0, 0, 0])

    # Create first process
    p1 = Process(target=process_task1, args=(lst,))
    p1.start()
    p1.join()

    print("Main process exiting")
