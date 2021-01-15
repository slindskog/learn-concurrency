import time
from threading import Thread, Semaphore


class AsyncExecutor:

    def work(self, callback):
        # Simulate work
        time.sleep(5)
        # Work is done, invoke callback
        callback()

    def execute(self, callback):
        Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):

    def __init__(self):
        self.sem = Semaphore(0)

    def work(self, callback):
        super().work(callback)
        self.sem.release()

    def execute(self, callback):
        super().execute(callback)
        self.sem.acquire()


def say_hi():
    print("Hi")


if __name__ == '__main__':
    # Main Thread waits for print message before exiting
    sx = SyncExecutor()
    sx.execute(say_hi)
    print("Main thread exiting")
