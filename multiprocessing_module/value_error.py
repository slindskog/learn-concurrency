import multiprocessing
from multiprocessing import Process, Value, Queue


def child_process(var, q):
    print(f"Child process received var={var.value} with id={id(var)} from queue")


if __name__ == '__main__':
    q = Queue()
    print(f"This machine has {multiprocessing.cpu_count()} CPUs")

    var = Value("I", 1, lock=False)

    # Generates an error
    # RuntimeError: c_uint objects should only be shared between processes through inheritance
    q.put(var)

    print(f"Parent process puts item on queue with id {id(var)}")

    process = Process(target=child_process, args=(var, q))
    process.start()
    process.join()
