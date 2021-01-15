def nested_generator():
    i = 0
    while i < 5:
        i += 1
        yield i
    return 999


def outer_generator():
    nested_gen = nested_generator()
    ret_val = yield from nested_gen
    print(f"Received in outer generator: {ret_val}")


if __name__ == '__main__':
    gen = outer_generator()
    for item in gen:
        print(item)
