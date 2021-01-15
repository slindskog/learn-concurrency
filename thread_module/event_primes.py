import time
from threading import Event, Thread


def printer_thread_func():
    global prime_holder

    while not exit_prog:
        # Wait for a prime number to become available
        prime_available.wait()

        # Print the prime number
        print(prime_holder)
        prime_holder = None

        # Reset the event to false
        prime_available.clear()

        # Let the finder thread know that printing is done
        prime_printed.set()


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
        prime_available.set()

        # Wait for the printer thread to complete printing
        prime_printed.wait()

        # Reset the flag
        prime_printed.clear()

        i += 1


if __name__ == '__main__':
    prime_available = Event()
    prime_printed = Event()
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
    prime_available.set()
    prime_printed.set()

    printer_thread.join()
    finder_thread.join()
