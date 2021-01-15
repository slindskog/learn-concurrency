import time
from ctypes import c_bool
import multiprocessing
from multiprocessing import Process, Condition, Value


def printer_process(exit_prog, found_prime, prime, cond_var):
    while not exit_prog.value:
        cond_var.acquire()
        while not found_prime.value and not exit_prog.value:
            cond_var.wait()
        cond_var.release()

        if not exit_prog.value:
            print(prime.value)
            prime.value = 0

            cond_var.acquire()
            found_prime.value = False
            cond_var.notify()
            cond_var.release()


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_process(exit_prog, found_prime, prime, cond_var):
    i = 1

    while not exit_prog.value:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(0.001)

        prime.value = i

        cond_var.acquire()
        found_prime.value = True
        cond_var.notify()
        cond_var.release()

        cond_var.acquire()
        while found_prime.value and not exit_prog.value:
            cond_var.wait()
        cond_var.release()

        i += 1


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')

    cond_var = Condition()
    prime = Value('i', 0)
    found_prime = Value(c_bool, False)
    exit_prog = Value(c_bool, False)

    printer = Process(target=printer_process, args=(exit_prog, found_prime, prime, cond_var))
    printer.start()

    finder = Process(target=finder_process, args=(exit_prog, found_prime, prime, cond_var))
    finder.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog.value = True

    # Let the threads exit
    cond_var.acquire()
    cond_var.notify_all()
    cond_var.release()

    printer.join()
    finder.join()
