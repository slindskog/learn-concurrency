import inspect


def natural_nums():
    i = 0
    while True:
        i += 1
        yield i


if __name__ == '__main__':
    it = natural_nums()
    print(f"Generator state: {inspect.getgeneratorstate(it)}")
    next(it)
    print(f"Generator state: {inspect.getgeneratorstate(it)}")
    it.close()
    print(f"Generator state: {inspect.getgeneratorstate(it)}")
