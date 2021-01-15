def get_natural_nums():
    i = 0
    while True:
        yield i
        i += 1


if __name__ == "__main__":
    # The close() method is invoked by the interpreter when the generator object is garbage collected.
    # It can also be invoked manually and doing so would make the generator unavailable for iteration.
    gen = get_natural_nums()

    # Close the generator
    gen.close()

    # Attempt to iterate
    next(gen)
