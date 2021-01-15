import time
from threading import Thread, current_thread, Lock


def thread_A(lock1, lock2):
    lock1.acquire()
    print(f'{current_thread().getName()} acquired lock1')
    time.sleep(1)
    lock2.acquire()
    print(f'{current_thread().getName()} acquired both locks')


def thread_B(lock1, lock2):
    lock2.acquire()
    print(f'{current_thread().getName()} acquired lock2')
    time.sleep(1)
    lock1.acquire()
    print(f'{current_thread().getName()} acquired both locks')

# Do not run this, will time out
# if __name__ == '__main__':
#    lock1 = Lock()
#    lock2 = Lock()
#
#    Thread(target=thread_A, args=(lock1, lock2)).start()
#    Thread(target=thread_B, args=(lock1, lock2)).start()
