import time
import random
from multiprocessing import Barrier, Process, current_process


def process_task(barrier):
    time.sleep(random.randint(0, 5))
    print(f"\nCurrently {barrier.n_waiting} processes blocked on barrier", flush=True)
    barrier.wait()


def when_all_processes_released():
    print(f"\nAll processes released, reported by: {current_process().name}", flush=True)


if __name__ == '__main__':
    num_processes = 5
    barrier = Barrier(num_processes, action=when_all_processes_released)
    processes = [0] * num_processes

    for i in range(num_processes):
        processes[i - 1] = Process(target=process_task, args=(barrier,))

    for i in range(num_processes):
        processes[i].start()
