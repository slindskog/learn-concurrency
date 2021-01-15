def printer():
    item = None
    while True:
        item = yield
        print(item)


if __name__ == '__main__':

    coroutine_object = printer()

    # Priming a coroutine
    next(coroutine_object)

    print(f"Class name: {coroutine_object.__class__.__name__}")

    for i in range(11):
        coroutine_object.send(i)
