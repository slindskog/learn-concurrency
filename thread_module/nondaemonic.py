import time
from threading import Thread, current_thread


def regular_thread_task():
    while True:
        print(f"{current_thread().getName()} executing")
        time.sleep(1)

# This will time out
# if __name__ == '__main__':
#    regular_thread = Thread(target=regular_thread_task, name="regularThread", daemon=False)
#    regular_thread.start()  # Start the regular thread
#    time.sleep(3)
#
#    print("Main thread exiting but Python program doesn't")
