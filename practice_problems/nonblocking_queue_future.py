import time
import random
from threading import Thread, Lock, current_thread


class NonBlockingQueue:

    def __init__(self, max_size: int):
        assert 0 < max_size
        self.max_size = max_size
        self.lock = Lock()
        self.q = []

    def enqueue(self, item):
        with self.lock:
            if len(self.q) == self.max_size:
                return False
            else:
                self.q.append(item)
                return True

    def dequeue(self):
        with self.lock:
            if len(self.q) != 0:
                return self.q.pop(0)
            else:
                return False


def consumer_thread(q):
    while True:
        item = q.dequeue()
        if item == False:
            print("Consumer couldn't dequeue an item")
        else:
            print(f"\n{current_thread().getName()} consumed item: {item}", flush=True)
        time.sleep(random.randint(1, 3))


def producer_thread(q, val):
    item = val
    while True:
        result = q.enqueue(item)
        if result is True:
            print(f"\n{current_thread().getName()} produced an item")
            item += 1


if __name__ == '__main__':
    non_blocking_q = NonBlockingQueue(5)

    consumer_thread1 = Thread(target=consumer_thread, name="consumer-1", args=(non_blocking_q,), daemon=True)
    producer_thread1 = Thread(target=producer_thread, name="producer-1", args=(non_blocking_q, 1), daemon=True)

    consumer_thread1.start()
    producer_thread1.start()

    time.sleep(15)
    print("Main thread exiting!")
