import time
from threading import Thread, Condition, current_thread


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
        self.cv = Condition()
        self.is_done = False

    def work(self, callback):
        super().work(callback)
        print(f"{current_thread().getName()} thread notifying")
        self.cv.acquire()
        self.cv.notifyAll()
        self.is_done = True
        self.cv.release()

    def execute(self, callback):
        super().execute(callback)

        self.cv.acquire()
        while self.is_done is False:
            self.cv.wait()
        print(f"{current_thread().getName()} thread woken up")
        self.cv.release()


def say_hi():
    print("Hi")


if __name__ == '__main__':
    # Main Thread waits for print message before exiting
    sx = SyncExecutor()
    sx.execute(say_hi)
    print("Main thread exiting")
