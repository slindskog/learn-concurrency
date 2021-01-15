import time
from threading import Timer, current_thread


def say_hi():
    print(f"{current_thread().getName()} says Hi!")


if __name__ == '__main__':
    timer = Timer(1, say_hi)
    timer.start()

    cancel = False
    if cancel:
        timer.cancel()
        print("Canceled!")

    # time.sleep(2)
    print(f"{current_thread().getName()} exiting")
