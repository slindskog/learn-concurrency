import time
from threading import Thread


class AsyncExecutor:

    def work(self, callback):
        time.sleep(5)
        callback()

    def execute_async(self, callback):
        Thread(target=self.work, args=(callback,)).start()


def say_hi():
    print("Hi")


if __name__ == '__main__':
    # Message is printed after main thread exits
    ax = AsyncExecutor()
    ax.execute_async(say_hi)

    print("Main thread exiting")
