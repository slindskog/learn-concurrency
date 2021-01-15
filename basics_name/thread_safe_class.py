import sys

from threading import Thread, Lock


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(1_000_000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()


if __name__ == '__main__':
    # Sets the thread switch interval
    sys.setswitchinterval(0.005)

    numThreads = 5
    counter = Counter()

    threads = [Thread(target=counter.increment) for _ in range(numThreads)]

    for i in range(0, numThreads):
        threads[i].start()

    for i in range(0, numThreads):
        threads[i].join()

    if counter.count != 5_000_000:
        print(f"This should not happen... Count = {counter.count}", flush=True)
    else:
        print("Count = 5_000_000 as expected")
