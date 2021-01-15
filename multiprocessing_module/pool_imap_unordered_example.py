import os
from multiprocessing import Pool


def square(arg):
    return arg * arg


def init(main_id):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}", flush=True)


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=5,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=50
    )

    result = pool.imap_unordered(
        square,
        (range(1, 11)),
        chunksize=2
    )
    for sq in result:
        print(sq)
