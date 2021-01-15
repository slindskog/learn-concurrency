def nested_generator():
    i = 0
    while i < 5:
        i += 1
        yield i


def outer_generator_with_yield_from():
    nested_gen = nested_generator()
    yield from nested_gen


def outer_generator():
    nested_gen = nested_generator()
    for item in nested_gen:
        yield item


if __name__ == '__main__':
    gen_using_yield_from = outer_generator_with_yield_from()

    for item in gen_using_yield_from:
        print(item)
