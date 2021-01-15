import os
from multiprocessing import Pool


def init(main_id):
    print(f"Pool process with id: {os.getpid()} received a task from main process with id: {main_id}")


def square(x):
    return x * x


if __name__ == '__main__':
    main_process_id = os.getpid()

    pool = Pool(
        processes=1,
        initializer=init,
        initargs=(main_process_id,),
        maxtasksperchild=1
    )
    result = pool.apply(square, (3,))
    print(result)
