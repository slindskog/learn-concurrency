import os
from multiprocessing import Pool


def square(arg1, arg2):
    return f"{arg2}-{arg1 * arg1}"


def init(main_id):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}", flush=True)


def on_success(results):
    for result in results:
        print(f"\nResult is: {result}")


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

    result = pool.starmap_async(
        square,
        (
            (1, 'chunk1'),
            (3, 'chunk2'),
            (5, 'chunk3'),
            (7, 'chunk4'),
            (9, 'chunk5'),
        ),
        callback=on_success,
        error_callback=on_error
    )

    pool.close()
    pool.join()
