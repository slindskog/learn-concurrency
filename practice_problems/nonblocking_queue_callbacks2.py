import time
import random
from concurrent.futures import Future
from threading import Thread, RLock, current_thread


class NonBlockingQueue:

    def __init__(self, max_size: int):
        assert 0 < max_size
        self.max_size = max_size
        self.lock = RLock()
        self.q = []
        self.q_waiting_puts = []
        self.q_waiting_gets = []

    def enqueue(self, item):
        # print(f"Size: {len(self.q_waiting_puts)}")
        future = None
        with self.lock:
            # queue is full so create a future for a put request
            if len(self.q) == self.max_size:
                future = Future()
                self.q_waiting_puts.append(future)
            else:
                self.q.append(item)
                # Remember to resolve a pending future for a get request
                if len(self.q_waiting_gets) != 0:
                    future_get = self.q_waiting_gets.pop(0)
                    future_get.set_result(self.q.pop(0))
        return future

    def dequeue(self):
        result = None
        future = None
        with self.lock:
            if len(self.q) != 0:
                result = self.q.pop(0)
                # Remember to resolve a pending future for a put request
                if len(self.q_waiting_puts) != 0:
                    self.q_waiting_puts.pop(0).set_result(True)
            else:
                # Queue is empty so create a future for a get request
                future = Future()
                self.q_waiting_gets.append(future)
        return result, future


def retry_dequeue(future):
    item = future.result()
    print(f"\nretry_dequeue executed by thread {current_thread().getName()} and {item} consumed on a retry", flush=True)


def consumer_thread(q):
    while True:
        item, future = q.dequeue()
        if item is None:
            future.add_done_callback(retry_dequeue)
        else:
            print(f"\n{current_thread().getName()} consumed item: {item}", flush=True)
        # Slow down consumer
        time.sleep(1)


def retry_enqueue(future):
    print(f"\nCallback invoked by thread {current_thread().getName()}")
    item = future.item
    q = future.q
    new_future = q.enqueue(item)
    if new_future is not None:
        new_future.item = item
        new_future.q = q
        new_future.add_done_callback(retry_enqueue)
    else:
        print(f"\n{item} successfully added on a retry")


def producer_thread(q, val):
    item = val
    while True:
        future = q.enqueue(item)
        if future is not None:
            future.item = item
            future.q = q
            future.add_done_callback(retry_enqueue)
        item += 1
        # Slow down the producer
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    non_blocking_q = NonBlockingQueue(5)

    consumer_thread1 = Thread(target=consumer_thread, name="consumer-1", args=(non_blocking_q,), daemon=True)
    producer_thread1 = Thread(target=producer_thread, name="producer-1", args=(non_blocking_q, 1), daemon=True)

    consumer_thread1.start()
    producer_thread1.start()

    time.sleep(15)
    print("Main thread exiting!")
