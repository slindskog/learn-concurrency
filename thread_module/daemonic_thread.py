import time
from threading import Thread, current_thread


def regular_thread_task():
    for _ in range(20):
        print(f"{current_thread().getName()} executing")
        time.sleep(1)


if __name__ == '__main__':
    regular_thread = Thread(target=regular_thread_task, name="regularThread", daemon=True)
    regular_thread.start()  # Start the regular thread
    time.sleep(3)

    print("Main thread exiting and Python program too")
