from threading import RLock, Thread

# def perform_unlock():
#    rlock.release()
#    print("Child task executing")
#    rlock.release()
#
#
# RunTimeError: cannot release un-acquired lock
# if __name__ == '__main__':
#    rlock = RLock()
#
#    # Reentrant lock acquired by main thread
#    rlock.acquire()
#
#    # Let's attempt to unlock using a child thread
#    thread = Thread(target=perform_unlock)
#    thread.start()
#    thread.join()
