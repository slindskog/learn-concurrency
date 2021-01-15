import multiprocessing
from multiprocessing import Process, Semaphore, Value


def child_process(sem1, sem2, var):
    print(f"Child process received var = {var.value} with id {id(var)}")
    sem2.release()
    sem1.acquire()

    print(f"After changes by parent process var = {var.value}", flush=True)


if __name__ == '__main__':
    # multiprocessing.set_start_method('spawn')
    sem1 = Semaphore(0)
    sem2 = Semaphore(0)
    print(f"This machine has {multiprocessing.cpu_count()} CPUs")

    var = Value('I', 1)
    print(f"Parent process puts item on queue with id {id(var)}")

    process = Process(target=child_process, args=(sem1, sem2, var))
    process.start()

    sem2.acquire()

    # Change the var
    var.value += 2
    print(f"Parent processs changed the enqueded item to {var.value}", flush=True)
    sem1.release()
    process.join()
