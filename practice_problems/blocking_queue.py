import time
import random
from threading import Thread, Condition, current_thread


class BlockingQueue:

    def __init__(self, max_size: int):
        assert 0 < max_size
        self.max_size = max_size
        self.size = 0
        self.cond = Condition()
        self.q = []

    def enqueue(self, item):
        self.cond.acquire()
        while self.size == self.max_size:
            self.cond.wait()

        self.q.append(item)
        self.size += 1

        self.cond.notifyAll()
        self.cond.release()

    def dequeue(self):
        self.cond.acquire()
        while self.size == 0:
            self.cond.wait()

        item = self.q.pop(0)
        self.size -= 1

        self.cond.notifyAll()
        print(f"\nCurrent size of queue: {self.size}", flush=True)
        self.cond.release()

        return item


def consumer_thread(q):
    while True:
        item = q.dequeue()
        print(f"\n{current_thread().getName()} consumed item: {item}", flush=True)
        time.sleep(random.randint(1, 3))


def producer_thread(q, val):
    item = val
    while True:
        q.enqueue(item)
        item += 1
        time.sleep(0.1)


if __name__ == '__main__':
    blocking_q = BlockingQueue(5)

    consumer_thread1 = Thread(target=consumer_thread, name="consumer-1", args=(blocking_q,), daemon=True)
    consumer_thread2 = Thread(target=consumer_thread, name="consumer-2", args=(blocking_q,), daemon=True)
    producer_thread1 = Thread(target=producer_thread, name="producer-1", args=(blocking_q, 1), daemon=True)
    producer_thread2 = Thread(target=producer_thread, name="producer-2", args=(blocking_q, 100), daemon=True)

    consumer_thread1.start()
    consumer_thread2.start()
    producer_thread1.start()
    producer_thread2.start()

    time.sleep(15)
    print("Main thread exiting!")
