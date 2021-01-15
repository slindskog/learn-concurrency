import os
import random
from multiprocessing import Pool, Queue


def square(arg):
    i = random.randrange(0, 5)
    tmp = arg
    if i % 5 == 0:
        print("Injecting failure", flush=True)
        tmp = None
    try:
        res = None
        res = tmp * tmp
    except:
        square.q.put(arg)
    return res


def init(main_id, q):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}", flush=True)
    square.q = q


def queue_to_list(q):
    i = 0
    items = []
    while not q.empty():
        items.append(q.get())
        i += 1
    return items, i


if __name__ == '__main__':

    q = Queue()
    failures = 0
    done = False
    items = [i for i in range(1, 11)]

    main_process_id = os.getpid()

    pool = Pool(
        processes=5,
        initializer=init,
        initargs=(main_process_id, q),
        maxtasksperchild=50
    )

    final_results = []
    while not done:
        result = pool.map(
            square,
            items,
            chunksize=2
        )
        print(result)
        final_results.append(result)

        if not q.empty():
            items, i = queue_to_list(q)
            failures += 1
        else:
            done = True

    print(f"Failures: {failures}")
    print(f"Final results: {final_results}")
