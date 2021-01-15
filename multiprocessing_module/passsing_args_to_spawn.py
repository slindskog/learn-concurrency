import os
import multiprocessing
from multiprocessing import Process, current_process

global_arg = "this is a global arg"


def process_task(garg, larg):
    print(f"{garg}-{larg}")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    local_arg = "This is a global arg"
    process = Process(
        target=process_task,
        name='process1',
        args=(global_arg, local_arg),
    )

    process.start()
    process.join()
