from threading import Lock, RLock, Thread, current_thread

if __name__ == '__main__':
    # Deadlock
    # ordinary_lock = Lock()
    #
    # ordinary_lock.acquire()
    # ordinary_lock.acquire()
    #
    # print(f"{current_thread().getName()} exiting")
    #
    # ordinary_lock.release()
    # ordinary_lock.release()

    # RLock
    lock = RLock()
    lock.acquire()
    lock.acquire()

    print(f"{current_thread().getName()} exiting")

    lock.release()
    lock.release()
