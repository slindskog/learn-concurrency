import time
from threading import Condition, Thread, current_thread


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        cond_var.acquire()
        # Check for predicate
        while not found_prime and not exit_prog:
            cond_var.wait()

        if not exit_prog:
            print(f"{current_thread().getName()} prints: {prime_holder}")
            prime_holder = None
            # Make sure to wake up the finder thread
            found_prime = False
            cond_var.notifyAll()
        cond_var.release()
    print(f"Printer {current_thread().getName()} exiting")


def is_prime(num):
    if num == 2 or num == 3:
        return True
    div = 2
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread_func():
    global prime_holder
    global found_prime

    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so we can see the output
            time.sleep(0.01)

        prime_holder = i
        cond_var.acquire()
        found_prime = True
        # cond_var.notifyAll()  # for all 3 printer threads to run
        cond_var.notify()
        cond_var.release()

        cond_var.acquire()
        while found_prime and not exit_prog:
            cond_var.wait()
        cond_var.release()
        i += 1
    print('Finder exiting')


if __name__ == '__main__':
    cond_var = Condition()
    found_prime = False
    prime_holder = None
    exit_prog = False

    printer_thread = Thread(target=printer_thread_func)
    printer_thread.start()

    printer_thread2 = Thread(target=printer_thread_func)
    printer_thread2.start()

    printer_thread3 = Thread(target=printer_thread_func)
    printer_thread3.start()

    finder_thread = Thread(target=finder_thread_func)
    finder_thread.start()

    # Let the threads run for 5 seconds
    time.sleep(3)

    # Let the threads exit
    exit_prog = True

    cond_var.acquire()
    cond_var.notifyAll()
    cond_var.release()

    printer_thread.join()
    printer_thread2.join()
    printer_thread3.join()
    finder_thread.join()
