from threading import RLock, Thread


def child_task():
    rlock.acquire()
    print("Child task executing")
    rlock.release()


if __name__ == '__main__':
    rlock = RLock()
    rlock.acquire()
    rlock.acquire()

    rlock.release()

    # Uncomment the follow to make the program exit normally
    rlock.release()

    thread = Thread(target=child_task)
    thread.start()
    thread.join()
