def nested_generator():
    for _ in range(5):
        try:
            k = yield
            print(f"Inner generator received = {k}")
        except Exception:
            print("Caught an exception")


def outer_generator():
    nested_gen = nested_generator()
    yield from nested_gen


if __name__ == "__main__":

    gen = outer_generator()
    next(gen)

    for i in range(5):
        try:
            if i == 1:
                gen.throw(Exception("Delibrate exception"))
            else:
                gen.send(i)
        except StopIteration:
            pass
