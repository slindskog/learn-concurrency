import time
from threading import Lock, Thread


def thread_one(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.release()


def thread_two(lock1, lock2):
    lock2.acquire()
    time.sleep(1)
    lock1.release()

# Deadlock don't run
# if __name__ == '__main__':
#    lock1 = Lock()
#    lock2 = Lock()
#
#    t1 = Thread(target=thread_one, args=(lock1, lock2))
#    t2 = Thread(target=thread_two, args=(lock1, lock2))
#
#    t1.start()
#    t2.start()
#
#    t1.join()
#    t2.join()
