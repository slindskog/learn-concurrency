import multiprocessing
from multiprocessing import Process, Semaphore, Array


def child_process(sem1, sem2, arr):
    print(f"Child process received var = {arr[0]} with id {id(arr)}", flush=True)
    sem2.release()
    sem1.acquire()

    print(f"After changes by parent process var = {arr[0]}", flush=True)


if __name__ == '__main__':
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print(f"This machine has {multiprocessing.cpu_count()} CPUs")

    arr = Array('i', range(5))
    print(f"Parent process puts item on queue with id {id(arr)}")

    process = Process(target=child_process, args=(sem1, sem2, arr))
    process.start()

    sem2.acquire()

    # Change the arr and verify the change is reflected in the child process
    arr[0] += 100
    print(f"Parent processs changed the enqueded item to {arr[0]}", flush=True)
    sem1.release()
    process.join()
