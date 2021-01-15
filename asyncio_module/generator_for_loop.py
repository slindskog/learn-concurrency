def get_item():
    yield 3
    yield 5
    yield 7
    # raise StopIteration


if __name__ == "__main__":

    # no StopIteration is thrown
    for num in get_item():
        print(num)
