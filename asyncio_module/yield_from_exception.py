def nested_generator():
    for _ in range(5):
        try:
            k = yield
            print(f"Inner generator received = {k}")
        except Exception:
            print("Caught an exception")


def outer_generator():
    nested_gen = nested_generator()
    next(nested_gen)

    for _ in range(5):
        k = yield
        try:
            nested_gen.send(k)
        except StopIteration:
            pass


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
