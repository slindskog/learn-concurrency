import time


def natural_nums():
    print("Inside natural_nums function")
    i = 0
    while True:
        i += 1
        yield i  # yield let's Python know to treat the function like an iterator


if __name__ == '__main__':
    # Get the generator object
    it = natural_nums()

    # Print statement not called until next is called
    time.sleep(3)

    # Print the next value from the generator function
    print(next(it))
    # Print the next 2 values
    print(next(it))
    print(next(it))
