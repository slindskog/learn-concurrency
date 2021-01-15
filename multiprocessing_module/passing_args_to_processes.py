import os
from multiprocessing import Process, current_process


def process_task(x, y, z, key1, key2):
    print(f"\n{current_process().name} has pid: {os.getpid()} with parent pid: {os.getppid()}")
    print(f"Received arguments: {x}, {y}, {z}, {key1}, {key2}\n")


if __name__ == '__main__':
    process = Process(
        target=process_task,
        args=(1, 2, 3),
        kwargs={
            'key1': 'arg1',
            'key2': 'arg2'
        }
    )

    process.start()
    process.join()
