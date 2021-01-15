import random
import multiprocessing
from multiprocessing import Process, Queue, current_process, Lock


def child_process(q, lock):
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False
        lock.release()

    print(f"Child process {current_process().name} processed {count} items from the queue", flush=True)


if __name__ == '__main__':
    # multiprocessing.set_start_method("forkserver")
    q = Queue()
    lock = Lock()

    random.seed(42)
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q, lock))
    p2 = Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
