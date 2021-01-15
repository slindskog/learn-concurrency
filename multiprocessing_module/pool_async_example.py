import os
import time
from multiprocessing import Pool


def init(main_id):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}")


def square(x):
    return x * x


def on_success(result):
    print(f"Result is: {result}")


def on_error(err):
    print(f"Error is: {err}")


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=1,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=1  # 2 switch to 2 for only 1 init call
    )

    result = pool.apply_async(square, (3,), callback=on_success, error_callback=on_error)

    # Prevent main from exiting before the pool process completes
    time.sleep(2)
