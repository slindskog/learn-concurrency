def nested_generator():
    for _ in range(5):
        k = yield
        print(f"Inner generator received = {k}")


def outer_generator():
    nested_gen = nested_generator()
    next(nested_gen)

    for _ in range(5):
        # receive the value from the caller
        k = yield
        try:
            # send the value to the inner generator
            nested_gen.send(k)
        except StopIteration:
            pass


if __name__ == "__main__":

    gen = outer_generator()
    next(gen)

    for i in range(5):
        try:
            gen.send(i)
        except StopIteration:
            pass
