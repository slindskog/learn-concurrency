import time
from threading import Lock, Thread, current_thread

shared_state = [1, 2, 3]
my_lock = Lock()


def thread1_operations():
    with my_lock:
        print(f"{current_thread().getName()} has acquired the lock")

        time.sleep(3)
        shared_state[0] = 777

        print(f"{current_thread().getName()} about to release the lock")

    print(f"{current_thread().getName()} released the lock")


def thread2_operations():
    with my_lock:
        print(f"{current_thread().getName()} has acquired the lock")

        time.sleep(3)
        shared_state[0] = 777

        print(f"{current_thread().getName()} about to release the lock")

    print(f"{current_thread().getName()} released the lock")


if __name__ == '__main__':
    # Create and run the two threads
    thread1 = Thread(target=thread1_operations, name="thread1")
    thread1.start()
    thread2 = Thread(target=thread2_operations, name="thread2")
    thread2.start()

    # Wait for the two threads to complete
    thread1.join()
    thread2.join()
