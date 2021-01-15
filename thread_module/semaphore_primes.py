import time
from threading import Semaphore, Thread


def printer_thread_func():
    global prime_holder

    while not exit_prog:
        # Wait for a prime number to become available
        sem_find.acquire()

        # Print the prime number
        print(prime_holder)
        prime_holder = None

        # Let the finder thread find the next prime
        sem_print.release()


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

    i = 1
    while not exit_prog:
        while not is_prime(i):
            i += 1
        prime_holder = i
        # Let the printer thread know we have a prime to print
        sem_find.release()
        # Wait for the printer thread to complete printing
        sem_print.acquire()
        i += 1


if __name__ == '__main__':
    sem_find = Semaphore(0)
    sem_print = Semaphore(0)
    prime_holder = None
    exit_prog = False

    printer_thread = Thread(target=printer_thread_func)
    printer_thread.start()

    finder_thread = Thread(target=finder_thread_func)
    finder_thread.start()

    # Let the threads run for 5 seconds
    time.sleep(3)

    # Let the threads exit
    exit_prog = True

    printer_thread.join()
    finder_thread.join()
