import os
from multiprocessing import Process, current_process


def process_task():
    print(f"{current_process().name} had pid: {os.getpid()} with parent pid: {os.getppid()}")


if __name__ == '__main__':
    process = [0] * 3
    for i in range(3):
        process[i] = Process(target=process_task, name=f"process-{i}")
        process[i].start()

    for i in range(3):
        process[i].join()

    print(f"{current_process().name} has pid: {os.getpid()}")
