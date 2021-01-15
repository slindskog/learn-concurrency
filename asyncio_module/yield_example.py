def keep_learning_asynchronous():
    yield "Educative"


def multiple_yeilds_asynchronous():
    yield "Hello"
    yield "World"
    yield "!"


def yield_and_return():
    yield "Hello"
    return "World!"


if __name__ == '__main__':
    s = keep_learning_asynchronous()
    print(s)
    for w in s:
        print(w)

    s = keep_learning_asynchronous()
    print(next(s))

    s = multiple_yeilds_asynchronous()
    for w in s:
        print(w)

    # Cannot invoke next on finished iterator
    # next(s)

    gen = yield_and_return()
    first_string = next(gen)
    print(first_string)

    try:
        next(gen)
    except StopIteration as e:
        second_string = e.value
        print(second_string)
