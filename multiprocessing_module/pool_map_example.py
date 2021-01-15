import os
from multiprocessing import Pool


def square(arg):
    return arg * arg


def init(main_id):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}", flush=True)


def on_success(result):
    print(f"Result is: {result}")


def on_error(err):
    print(f"Error is: {err}")


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=5,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=50
    )

    # Can use async or regular map
    # result = pool.map_async(
    #    square,
    #    (range(10)),
    #    callback=on_success,
    #    error_callback=on_error
    # )

    result = pool.map(
        square,
        (range(10)),
        chunksize=2
    )
    print(result)

    pool.close()
    pool.join()
