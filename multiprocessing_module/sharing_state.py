import multiprocessing
from multiprocessing import Process, Queue, Semaphore


def child_process(q, sem1, sem2):
    var = q.get()
    print(f"Child process received var = {var} with id {id(var)} from queue")
    sem2.release()
    sem1.acquire()

    print(f"After changes by parent process var = {var}", flush=True)


if __name__ == '__main__':
    q = Queue()
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print(f"This machine has {multiprocessing.cpu_count()} CPUs")

    var = 1
    print(f"Parent process puts item on queue with id {id(var)}")
    q.put(var)

    process = Process(target=child_process, args=(q, sem1, sem2))
    process.start()

    sem2.acquire()

    # Change the var
    var += 2
    print(f"Parent processs changed the enqueded item to {var}", flush=True)
    sem1.release()
    process.join()
