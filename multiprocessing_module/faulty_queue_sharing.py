import random
import multiprocessing
from multiprocessing import Process, Queue, current_process


def child_process(q):
    count = 0
    while not q.empty():
        print(q.get())
        count += 1

    print(f"Child process {current_process().name} processed {count} items from the queue", flush=True)


if __name__ == '__main__':
    # multiprocessing.set_start_method("forkserver")
    q = Queue()

    random.seed(42)
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
